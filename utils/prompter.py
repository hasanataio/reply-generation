from utils.emailer import generate_message_general, generate_message_personalized

def generate_general_response(ratings, customer_name):
    prompt = generate_message_general(ratings, customer_name)
    return prompt

def generate_personalized_response(review, ratings, length, food_items, cutomer_name, additional_context,previous_replies):
    system_prompt,prompt = generate_message_personalized(review, ratings, length, food_items, cutomer_name,additional_context,previous_replies)
    return system_prompt,prompt

