from llm import get_agent_decision
from memory import Memory
from logger import log_event


class Agent:
    def __init__(self, name, role, environment):
        self.name = name
        self.role = role
        self.env = environment
        self.location = self.env.get_random_room()
        self.memory = Memory()

    def perceive(self, agents):
        nearby = [
            a.name for a in agents
            if a.location == self.location and a != self
        ]

        return {
            "name": self.name,
            "role": self.role,
            "location": self.location,
            "nearby_agents": nearby,
            "memory": self.memory.get_summary()
        }

    def decide(self, context):
        decision = get_agent_decision(context)

        if not isinstance(decision, dict):
            return {"action": "observe"}

        return decision

    def act(self, decision, agents):
        action = decision.get("action", "observe")

        if action == "move":
            new_location = decision.get("destination", self.env.get_random_room())
            old_location = self.location
            self.location = new_location

            log_event({
                "type": "movement",
                "agent": self.name,
                "from": old_location,
                "to": new_location
            })

        elif action == "talk":
            message = decision.get("message", "")
            target = decision.get("target")

            log_event({
                "type": "conversation",
                "agent": self.name,
                "target": target,
                "message": message
            })

            self.memory.add(message)

        elif action == "reflect":
            thought = decision.get("thought", "")
            self.memory.add(thought)

            log_event({
                "type": "thought",
                "agent": self.name,
                "content": thought
            })

        else:
            log_event({
                "type": "idle",
                "agent": self.name
            })
