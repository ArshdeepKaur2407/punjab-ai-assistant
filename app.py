from deep_translator import GoogleTranslator
from flask import Flask, render_template, request, jsonify
import markdown

from service_database import SERVICES
from government_links import get_fallback_link
from search_service import search_official_websites, extract_context
from service_detector import detect_service
from ranker import rank_results, get_top_links
from gemini_service import generate_answer
from translations import translations

app = Flask(__name__)

conversation_memory = {}


# -----------------------------
# Translation helper
# -----------------------------
def translate_text(text, lang):
    if not text or lang == "en":
        return text

    try:
        return GoogleTranslator(source="auto", target=lang).translate(text)
    except Exception:
        return text


@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Translation API
# -----------------------------
@app.route("/translations/<lang>")
def get_translations(lang):
    return jsonify(translations.get(lang, translations["en"]))


# -----------------------------
# Chat API
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "").strip()
    language = data.get("language", "en")
    session_id = "default"

    if not user_message:
        return jsonify({
            "reply": "<p>Please enter a question.</p>",
            "links": []
        })

    service = detect_service(user_message)

    if service == user_message.title():
        if session_id in conversation_memory:
            service = conversation_memory[session_id]

    conversation_memory[session_id] = service

    search_query = f"""
    {service}
    Punjab Government
    official service
    eligibility
    required documents
    fee
    processing time
    apply online
    """

    try:
        search = search_official_websites(search_query)
        results = search.get("results", [])

        ranked_results = rank_results(results, service)
        context = extract_context(ranked_results[:3])

        language = data.get("language", "en")

        ai_response = generate_answer(
            context=context,
            user_question=user_message,
            language=language
        )

        # ✅ Translate only once (fixed)
        ai_response = translate_text(ai_response, language)

    except Exception as e:
        print(e)
        return jsonify({
            "reply": "<h3>Something went wrong.</h3>",
            "links": []
        })

    reply = markdown.markdown(ai_response, extensions=["extra"])

    links = []

    fallback = get_fallback_link(service)
    if fallback:
        links.append(fallback)

    top_links = get_top_links(ranked_results)

    for link in top_links:
        if link["url"] not in [x["url"] for x in links]:
            links.append(link)

    links = links[:4]

    return jsonify({
        "reply": reply,
        "links": links
    })

# -----------------------------
# Service Info API
# -----------------------------
@app.route("/service-info", methods=["POST"])
def service_info():
    data = request.get_json()

    service = data.get("service", "").strip()
    language = data.get("language", "en")

    if service not in SERVICES:
        return jsonify({
            "success": False,
            "message": "Service not found."
        })

    # -----------------------------
    # Special handling for Scholarships
    # -----------------------------
    if service == "scholarships":
        scholarship = SERVICES["scholarships"]

        if language != "en":
            scholarship = {
                "title": translate_text(scholarship["title"], language),
                "description": translate_text(scholarship["description"], language),
                "items": [
                    {
                        "name": translate_text(item["name"], language),
                        "eligibility": translate_text(item["eligibility"], language),
                        "benefits": translate_text(item["benefits"], language),
                        "how_to_apply": translate_text(item["how_to_apply"], language),
                        "official_link": item["official_link"]
                    }
                    for item in scholarship["items"]
                ]
            }

        return jsonify({
            "success": True,
            "type": "scholarships",
            "title": scholarship["title"],
            "description": scholarship["description"],
            "items": scholarship["items"]
        })

    # -----------------------------
    # Other Services
    # -----------------------------
    info = SERVICES[service]

    if language != "en":
        try:
            info = {
                "purpose": translate_text(info["purpose"], language),
                "documents": [
                    translate_text(doc, language)
                    for doc in info["documents"]
                ],
                "fee": translate_text(info["fee"], language),
                "processing_time": translate_text(
                    info["processing_time"], language
                ),
                "apply_online": translate_text(
                    info["apply_online"], language
                ),
                "apply_offline": translate_text(
                    info["apply_offline"], language
                ),
                "links": info["links"]
            }
        except Exception as e:
            print("Sidebar translation error:", e)

    return jsonify({
        "success": True,
        "service": service,
        "purpose": info["purpose"],
        "documents": info["documents"],
        "fee": info["fee"],
        "processing_time": info["processing_time"],
        "apply_online": info["apply_online"],
        "apply_offline": info["apply_offline"],
        "links": info["links"]
    })

if __name__ == "__main__":
    app.run(debug=True)