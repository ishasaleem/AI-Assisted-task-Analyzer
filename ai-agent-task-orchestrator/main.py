from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Keyword-based task templates
BACKEND_TASKS = {
    "login": [
        "Create REST API for login",
        "Implement login validation logic",
        "Add JWT authentication",
        "Write unit tests for login endpoint"
    ],
    "signup": [
        "Create REST API for signup",
        "Implement password hashing",
        "Send verification email",
        "Write unit tests for signup endpoint"
    ],
    "dashboard": [
        "Create dashboard API endpoint",
        "Fetch user data for dashboard",
        "Implement caching for dashboard data",
        "Write unit tests for dashboard API"
    ],
    "task": [
        "Create REST API for tasks",
        "Implement task CRUD operations",
        "Add task validation",
        "Write unit tests for task endpoints"
    ],
    "sharing": [
        "Implement task sharing logic",
        "Create API to share tasks with users",
        "Handle permission checks for shared tasks",
        "Write tests for sharing functionality"
    ]
}

FRONTEND_TASKS = {
    "login": [
        "Build React Login component",
        "Style login page with TailwindCSS",
        "Add form validation",
        "Connect login form to API"
    ],
    "signup": [
        "Build React Signup component",
        "Style signup page with TailwindCSS",
        "Add form validation",
        "Connect signup form to API"
    ],
    "dashboard": [
        "Build React Dashboard component",
        "Display user data",
        "Add charts and stats",
        "Connect dashboard to API"
    ],
    "task": [
        "Build Task component in React",
        "Add task creation form",
        "Display tasks list",
        "Connect tasks to backend API"
    ],
    "sharing": [
        "Add sharing button in Task component",
        "Create sharing modal",
        "Handle shared task display",
        "Connect sharing functionality to backend"
    ]
}

# NLP-based brief parsing
def parse_brief(brief):
    doc = nlp(brief.lower())
    keywords = set()
    for token in doc:
        if token.pos_ in ["NOUN", "VERB"]:
            keywords.add(token.lemma_)
    return keywords

# Generate tasks based on keywords
def generate_tasks(keywords):
    backend = []
    frontend = []

    # Match keywords to task templates
    for kw in keywords:
        if kw in BACKEND_TASKS:
            backend += BACKEND_TASKS[kw]  # Include all backend tasks
        if kw in FRONTEND_TASKS:
            frontend += FRONTEND_TASKS[kw]  # Include all frontend tasks

    # Fallback if nothing matched
    if not backend and not frontend:
        backend = ["No backend tasks matched. Consider using common keywords like login, signup, dashboard, task, sharing."]
        frontend = ["No frontend tasks matched. Consider using common keywords like login, signup, dashboard, task, sharing."]

    return {"backend": backend, "frontend": frontend}

# API endpoint
@app.route("/analyze", methods=["POST"])
def analyze_brief():
    data = request.get_json()
    brief = data.get("brief", "")
    if not brief:
        return jsonify({"error": "No brief provided"}), 400

    keywords = parse_brief(brief)
    tasks = generate_tasks(keywords)

    return jsonify(tasks)

# Run server
if __name__ == "__main__":
    app.run(port=5001, debug=True)
