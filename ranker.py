from urllib.parse import urlparse


def calculate_score(result, service_name):
    """
    Assign a relevance score to each search result.
    Higher score = Better result.
    """

    score = 0

    title = result.get("title", "").lower()
    url = result.get("url", "").lower()

    service = service_name.lower()

    # -------------------------
    # Positive Scoring
    # -------------------------

    if service in title:
        score += 120

    if "apply" in title:
        score += 70

    if "certificate" in title:
        score += 40

    if "eligibility" in title:
        score += 20

    if "required documents" in title:
        score += 20

    if "eservices.punjab.gov.in" in url:
        score += 100

    elif "esewa.punjab.gov.in" in url:
        score += 90

    elif "punjab.gov.in" in url:
        score += 80

    elif "india.gov.in" in url:
        score += 50

    # -------------------------
    # Negative Scoring
    # -------------------------

    bad_words = [
        "search",
        "service list",
        "all services",
        "directory",
        "apps",
        "recruitment",
        "tender",
        "notice",
        "circular",
        "advertisement"
    ]

    for word in bad_words:
        if word in title:
            score -= 120

    if ".pdf" in url:
        score -= 100

    if "play.google.com" in url:
        score -= 100

    return score


def rank_results(results, service_name):
    """
    Sort results from best to worst.
    """

    ranked = []

    for result in results:

        result["score"] = calculate_score(
            result,
            service_name
        )

        ranked.append(result)

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked


def get_top_links(results, limit=4):
    """
    Return only the best unique official links.
    """

    links = []

    seen = set()

    for result in results:

        url = result.get("url", "")
        title = result.get("title", "")

        if not url:
            continue

        if url in seen:
            continue

        domain = urlparse(url).netloc.lower()

        if not (
            domain.endswith(".gov.in")
            or domain.endswith(".nic.in")
        ):
            continue

        seen.add(url)

        links.append({
            "title": title,
            "url": url
        })

        if len(links) >= limit:
            break

    return links