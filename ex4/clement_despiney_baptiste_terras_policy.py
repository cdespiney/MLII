from agent import Agent
import random

def new_policy(agent: Agent) -> str:
    """
    Policy of the agent
    return "left", "right", or "none"
    """

    gamma = 0.5

    if not hasattr(new_policy, "value_function"):
        new_policy.value_function = [0 for x in agent.known_rewards]
    if not hasattr(new_policy, "timer"):
        new_policy.timer = 0

    new_policy.timer += 1

    if new_policy.timer % 10 == 0:
        new_policy.timer = 0

    for i in range(0, len(new_policy.value_function)):
        new_policy.value_function[i] = agent.known_rewards[i] + max(
            gamma * new_policy.value_function[i-1] if i != 0 else 0,
            gamma * new_policy.value_function[i + 1] if i < 7 else 0
        )

    if new_policy.timer < 5:
        actions = ["left", "right"]
        return actions[random.randint(0, 1)]
    
    if (agent.position != 7 and new_policy.value_function[agent.position] < new_policy.value_function[agent.position + 1]) and (agent.position != 0 and new_policy.value_function[agent.position] <  new_policy.value_function[agent.position -1]):
        return "left" if new_policy.value_function[agent.position - 1] >= new_policy.value_function[agent.position + 1] else "right"
    if agent.position != 0 and new_policy.value_function[agent.position] <  new_policy.value_function[agent.position - 1]:
        return "left"
    if agent.position != 7 and new_policy.value_function[agent.position] <  new_policy.value_function[agent.position + 1]:
        return "right"
    return "none"