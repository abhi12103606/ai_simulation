def decide(self, context):
    decision = get_agent_decision(context)

    if not isinstance(decision, dict):
        return {"action": "observe"}

    return decision
