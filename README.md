# Punjab AI Citizen Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
An AI-powered web application that helps citizens access Punjab Government services through natural language queries in English and Punjabi.

## Features

- AI-powered citizen assistance
- Supports English and Punjabi
- Intelligent government service detection
- Official Punjab Government links
- AI-generated responses using Google Gemini
- Web search integration using Tavily
- Mobile-friendly responsive interface
- Fast Flask backend

---

## Technologies Used

- Python
- Flask
- Google Gemini API
- Tavily Search API
- HTML5
- CSS3
- JavaScript
- Markdown

---

## Project Structure

```
Punjab-AI-Citizen-Assistant/
│
├── app.py
├── config.py
├── gemini_service.py
├── search_service.py
├── service_database.py
├── service_detector.py
├── government_links.py
├── translations.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    ├── script.js
    ├── logo.png
    └── favicon files
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/ArshdeepKaur2407/punjab-ai-assistant.git
```

Move into the project

```bash
cd punjab-ai-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=xxxxx...
TAVILY_API_KEY=xxxxxx...
```

Run the application

```bash
python app.py
```

---

## Deployment

The application is deployed using **Render**.

Live Demo:

https://punjab-ai-assistant.onrender.com

---

## Future Improvements

- Voice Assistant
- Speech-to-Text
- OCR for Government Documents
- More Punjab Government Services
- User Authentication
- Conversation History

---

## Disclaimer

This project is developed for educational purposes.

The application provides AI-assisted guidance and official government links. Users should always verify important information through the respective Punjab Government departments.

---

## Author

**Arshdeep Kaur**

B.Tech Computer Engineering

Thapar Institute of Engineering & Technology

GitHub:
https://github.com/ArshdeepKaur2407

---

## Copyright

© 2026 Arshdeep Kaur. All Rights Reserved.

This project and its source code are the intellectual property of Arshdeep Kaur.

No part of this repository may be copied, modified, distributed, reproduced, or used for commercial or non-commercial purposes without prior written permission from the author.
