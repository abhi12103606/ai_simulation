from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
