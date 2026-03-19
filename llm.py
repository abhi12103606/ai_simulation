import os
import google.generativeai as genai
import json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_agent_decision(context):
    prompt = f"""
You are an autonomous AI agent.

Context:
{context}

Return ONLY valid JSON:
{{
  "thought": "",
  "action": "move/talk/observe/reflect",
  "target": "",
  "message": "",
  "destination": ""
}}
"""

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        try:
            return json.loads(text)
        except:
            return {"action": "observe"}

    except Exception as e:
        print("LLM ERROR:", e)
        return {"action": "observe"}
