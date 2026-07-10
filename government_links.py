government_links = {

    "Income Certificate": {
        "title": "Punjab eSewa Portal",
        "url": "https://esewa.punjab.gov.in"
    },

    "Birth Certificate": {
        "title": "Punjab eSewa Portal",
        "url": "https://esewa.punjab.gov.in"
    },

    "Death Certificate": {
        "title": "Punjab eSewa Portal",
        "url": "https://esewa.punjab.gov.in"
    },

    "Caste Certificate": {
        "title": "Punjab eSewa Portal",
        "url": "https://esewa.punjab.gov.in"
    },

    "Residence Certificate": {
        "title": "Punjab eSewa Portal",
        "url": "https://esewa.punjab.gov.in"
    },

    "Marriage Certificate": {
        "title": "Punjab eSewa Portal",
        "url": "https://esewa.punjab.gov.in"
    },

    "Driving Licence": {
        "title": "Parivahan",
        "url": "https://parivahan.gov.in"
    },

    "Aadhaar": {
        "title": "UIDAI",
        "url": "https://uidai.gov.in"
    },

    "Passport": {
        "title": "Passport Seva",
        "url": "https://www.passportindia.gov.in"
    },

    "Scholarship": {
        "title": "National Scholarship Portal",
        "url": "https://scholarships.gov.in"
    },

    "Seva Kendra": {
        "title": "Punjab eSewa Portal",
        "url": "https://esewa.punjab.gov.in"
    }
}


def get_fallback_link(service_name):
    """
    Returns a guaranteed official link
    for a government service.
    """

    return government_links.get(service_name)