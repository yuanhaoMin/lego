def print_action_agent_human_message(message_content: str):
    print(f"\033[37m****输入给构造代理的信息****\n{message_content}\033[0m")


def print_action_agent_ai_message(message_content: str):
    print(f"\033[34m****来自构造代理的AI输出****\n{message_content}\033[0m")


def print_critic_agent_human_message(message_content: str):
    print(f"\033[37m****输入给判别代理的信息****\n{message_content}\033[0m")


def print_critic_agent_ai_message(message_content: str):
    print(f"\033[33m****来自判别代理的AI输出****\n{message_content}\033[0m")


def print_error_message(message_content: str):
    print(f"\033[31m****发生错误****\n{message_content}\033[0m")


def print_skill_agent_message(message_content: str):
    print(f"\033[32m****来自技能代理的信息****\n{message_content}\033[0m")
