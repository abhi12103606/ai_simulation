import time
from agent import Agent
from environment import Environment
from config import SIMULATION_SPEED

env = Environment()

agents = [
    Agent("NewsAgent", "News Analyst", env),
    Agent("FinanceAgent", "Finance Expert", env)
]

def simulation_loop():
    while True:
        for agent in agents:
            context = agent.perceive(agents)
            decision = agent.decide(context)
            agent.act(decision, agents)

        time.sleep(SIMULATION_SPEED)

if __name__ == "__main__":
    simulation_loop()
