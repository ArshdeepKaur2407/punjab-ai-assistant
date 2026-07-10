from google import genai
from config import GEMINI_API_KEY

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


# ==========================================================
# AI Chatbot
# ==========================================================

def generate_answer(context, user_question, language="en"):
    """
    Generate an AI answer using only the official context.
    """

    # Language instruction
    if language == "hi":
        language_instruction = """
Respond ONLY in Hindi.
Use simple and natural Hindi.
Do NOT mix English except for official service names, document names, website names, and URLs.
"""

    elif language == "pa":
        language_instruction = """
Respond ONLY in Punjabi (Gurmukhi script).
Use simple and natural Punjabi.
Do NOT mix English except for official service names, document names, website names, and URLs.
"""

    else:
        language_instruction = """
Respond ONLY in English.
"""

    prompt = f"""
{language_instruction}

You are Punjab AI Citizen Assistant.

Answer ONLY using the official information provided.

Rules:
- Use only the official information provided below.
- Never guess or make up information.
- If information is missing, clearly state that it is not available in the official records.
- Keep the answer well structured using headings and bullet points when appropriate.
- Preserve official names of services, documents, websites, and URLs exactly as they appear.

Official Information:

{context}

User Question:

{user_question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ==========================================================
# Government Service Overview
# ==========================================================

def generate_service_info(service):
    """
    Generate a formatted overview from structured service data.
    """

    reply = f"""# {service.get('name', 'Unknown Service')}

## 📌 Purpose
{service.get('purpose', 'Not Available')}

## ✅ Eligibility
{service.get('eligibility', 'Not Available')}

## 📄 Required Documents
"""

    # Required Documents
    documents = service.get("documents", [])

    if documents:
        for doc in documents:
            reply += f"- {doc}\n"
    else:
        reply += "Not Available\n"

    reply += f"""

## 💵 Government Fee
{service.get('government_fee', 'Not Available')}

## 💰 Facilitation Fee
{service.get('fee', 'Not Available')}

## ⏱ Processing Time
{service.get('processing_time', 'Not Available')}

## 🖥 Apply Online
{service.get('apply_online', 'Not Available')}

## 🏢 Apply Offline
{service.get('apply_offline', 'Not Available')}

## 👤 Issuing Authority
{service.get('issuing_authority', 'Not Available')}

## 🌐 Official Sources
"""

    links = service.get("links", [])

    if links:
        for link in links:
            title = link.get("title", "Official Website")
            url = link.get("url", "")
            reply += f"- {title}: {url}\n"
    else:
        reply += "Not Available\n"

    return reply