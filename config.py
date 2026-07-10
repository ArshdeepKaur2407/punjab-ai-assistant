import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Tavily API Key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Official Government Websites
OFFICIAL_DOMAINS = [
    "eservices.punjab.gov.in",
    "sewa.punjab.gov.in",
    "punjab.gov.in",
    "india.gov.in",
    "uidai.gov.in",
    "parivahan.gov.in",
    "passportindia.gov.in",
    "scholarships.gov.in"
]

# Search Settings
MAX_SEARCH_RESULTS = 8
MAX_OFFICIAL_LINKS = 4
MAX_CONTENT_LENGTH = 3000