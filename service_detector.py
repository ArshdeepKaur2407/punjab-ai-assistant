import re

SERVICES = {

    "Income Certificate": [
        "income",
        "income certificate",
        "salary certificate",
        "income proof"
    ],

    "Birth Certificate": [
        "birth",
        "birth certificate"
    ],

    "Death Certificate": [
        "death",
        "death certificate"
    ],

    "Caste Certificate": [
        "caste",
        "sc",
        "st",
        "obc",
        "category certificate"
    ],

    "Residence Certificate": [
        "residence",
        "resident",
        "domicile",
        "residence certificate"
    ],

    "Marriage Certificate": [
        "marriage",
        "marriage certificate"
    ],

    "Driving Licence": [
        "driving licence",
        "driving license",
        "dl",
        "license",
        "licence"
    ],

    "Passport": [
        "passport"
    ],

    "Aadhaar": [
        "aadhaar",
        "aadhar",
        "uidai"
    ],

    "Scholarship": [
        "scholarship",
        "scholarships",
        "student scholarship"
    ],

    "Seva Kendra": [
        "seva kendra",
        "sewa kendra",
        "service center"
    ]
}


def detect_service(user_query):

    query = user_query.lower()

    query = re.sub(r"[^\w\s]", "", query)

    for service, keywords in SERVICES.items():

        for keyword in keywords:

            if keyword in query:
                return service

    return user_query.title()