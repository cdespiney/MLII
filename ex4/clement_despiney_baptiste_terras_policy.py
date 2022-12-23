from agent import Agent
import random

def new_policy(agent: Agent) -> str:
    """
    Policy of the agent
    return "left", "right", or "none"
    """

    actions = ["left", "right"]
    action = actions[random.randint(0,1)]
    if agent.known_rewards[agent.position] != 0:
        return "none"
    if action == "left" and agent.position == 0:
        action = "right"
    if action == "right" and agent.position == 7:
        action = "left"
    return action
