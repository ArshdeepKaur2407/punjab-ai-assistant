from tavily import TavilyClient
from urllib.parse import urlparse

from service_pages import SERVICE_PAGES

from config import (
    TAVILY_API_KEY,
    OFFICIAL_DOMAINS,
    MAX_SEARCH_RESULTS,
    MAX_CONTENT_LENGTH
)

tavily = TavilyClient(api_key=TAVILY_API_KEY)


def search_official_websites(query):
    """
    Search official Punjab Government websites.
    """

    search_query = query.lower()

    final_query = query

    # Find the first matching service only
    for service in SERVICE_PAGES.values():

        matched = False

        for keyword in service["keywords"]:

            if keyword.lower() in search_query:
                final_query = service["query"]
                matched = True
                break

        if matched:
            break

    print("\n========== SEARCH QUERY ==========")
    print(final_query)
    print("==================================\n")

    return tavily.search(
        query=final_query,
        search_depth="advanced",
        max_results=MAX_SEARCH_RESULTS,
        include_answer=True,
        include_raw_content=True,
        include_domains=OFFICIAL_DOMAINS
    )


def extract_context(search_results):
    """
    Build context only from official government pages.
    """

    context = ""

    for result in search_results:

        url = result.get("url", "")
        title = result.get("title", "")

        if not url:
            continue

        domain = urlparse(url).netloc.lower()

        if not (
            domain.endswith(".gov.in")
            or domain.endswith(".nic.in")
        ):
            continue

        content = (
            result.get("raw_content")
            or result.get("content")
            or ""
        )

        if not content.strip():
            continue

        context += f"""
TITLE:
{title}

URL:
{url}

CONTENT:
{content[:MAX_CONTENT_LENGTH]}

==================================================

"""

    return context