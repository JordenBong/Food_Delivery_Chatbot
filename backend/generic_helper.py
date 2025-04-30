
import re

def extract_session_id(session_str: str):
    match = re.search(r'/sessions/(.*?)/contexts/', session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""

def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])


if __name__ == "__main__":
    # print(extract_session_id("projects/mira-chatbot-for-food-del-ergq/agent/sessions/5994c2de-ca3b-c288-de8b-b3226e3d54b9/contexts/ongoing-order"))
    print(get_str_from_food_dict({"samosa": 2, "pizza": 3}))
