from pathlib import Path
import json

import google.generativeai as genai
import yaml

from app.core.retriever import retrieve_chunks


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
CONFIG_PATH = CONFIG_DIR / "config.yaml"


def load_config():
    """Load engine config safely without depending on the current working directory."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text("{}\n", encoding="utf-8")
        return {}

    with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file) or {}


cfg = load_config()
gemini_api_key = cfg.get("gemini_api_key")

if gemini_api_key:
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None


COT = """
You are a claims evaluation assistant. You are provided with:
- A customer query
- Retrieved policy document clauses

Your job is to:
1. Identify the important fields from the query (e.g., age, procedure, location, policy duration).
2. Think step-by-step to determine if the policy covers this case.
3. Reference specific clauses to justify your reasoning.
4. Give a structured JSON response with:
    - decision ("approved" or "rejected")
    - amount (if any)
    - justification

---

Query:
{query}

Retrieved Clauses:
{clauses}

---

Do not return markdown, explanations, or extra text.
Return valid JSON only.
"""


def evaluate_decision(query, session_id):
    if model is None:
        return json.dumps(
            {
                "error": "Gemini API key is missing. Set gemini_api_key in app/config/config.yaml.",
                "decision": "rejected",
                "amount": None,
                "justification": "The evaluation model is not configured.",
            }
        )

    retrieved_chunks = retrieve_chunks(query, session_id)
    clauses = "\n\n".join(retrieved_chunks)
    prompt = COT.format(query=query, clauses=clauses)
    response = model.generate_content(prompt)
    return response.candidates[0].content.parts[0].text
