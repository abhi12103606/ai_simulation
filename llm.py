import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def get_agent_decision(context):
    prompt = f"""
You are an autonomous AI agent.

Context:
{context}

Return JSON only:
{{
  "thought": "",
  "action": "move/talk/observe/reflect",
  "target": "",
  "message": "",
  "destination": ""
}}
"""

    response = model.generate_content(prompt)
    return response.text
