# To generate a general message based on ratings only
def generate_message_general(ratings, customer_name):

    prompt = f'''
    I want you to write a general message as a response to the customer's rating for a restaurant and show your concern.
    The customer name is: {customer_name}
    The ratings given by the customer is: {ratings}
    Rating given are on a scale of 5. If rating is between 1 to 3, it means the customer did not had a good experience so you might apoligize to them. A rating of 4 or 5 means the customer is satisfied with their experience at your restaurant so you can react accordingly. 
    Do not mention the ratings in the message. 
    At the end of message, you are supposed to request the user to take a moment to share their experience further on the provided link.
    
    Goals: The goal is to respond according to the customer's rating either good or bad to make them feel heard and respected.

    Guidelines:
    Emojis: Do not use any emojis in your message.
    Formatting: Avoid using labels or colons in the message to keep the format clean and reader-friendly.
    Originality: The content must be unique and crafted to sound natural and human-like, avoiding any overt AI-generated feel. Strictly avoid using any difficult vocabulary. Use simple words.
    Integrity: Please ensure that the message aligns to the goals.
    Please ensure the message is engaging, adheres to the specified constraints, and effectively communicates the intended message focusing on the ratings.
    Keep the brand voice casual and friendly.

    Message Length: Should be maximum 200 characters and minimum 160 characters. 

    Give the output in JSON format with the following keys:
    {{
        "message": "Your message here",
    }}
    Do not include any other information in the JSON output.
    '''
    return prompt.strip()

# To generate a personalized message based on review, ratings and other information
def generate_message_personalized(review, ratings, length, food_items, customer_name,additional_context,previous_replies):

    if str(length) == "short":
        length_prompt = f'''Message should strictly be maximum of 250 characters and minimum of 200 characters. '''
    else:
        length_prompt = f'''Mssage should strictly be maximum of 400 characters and minimum of 350 characters. '''

    SYSTEM_PROMPT=f"""
You are an assistant responsible for generating personalized and thoughtful responses to restaurant reviews. Your goal is to show genuine appreciation for positive feedback or address and resolve concerns when the feedback is negative. You should tailor each response based on the specific details provided. Some inputs may contain extra details, such as menu items, bill amount, or a personalized message from the restaurateur. Use these details if they are available, but don't assume they will always be present.

Elements of the Input:
Review: A description of the customer’s experience, which may highlight specific aspects of the restaurant (e.g., food, service, ambiance).
Length: {length_prompt}
Additional Details (Optional): These may include:
    Rating: The customer’s rating (e.g., 1-5 stars).
    Customer Name: The name of the customer who left the review.
    Menu Items: Specific dishes mentioned in the review.
    Bill Amount: The total bill, if the customer shared this.
    Personalized Message: A specific note from the restaurateur to include in your response.

Guidelines for Crafting Your Response:
Acknowledge and Thank the Customer: Always start by thanking the customer for their visit and for sharing their thoughts, regardless of whether the feedback is positive or negative.
Address Specific Feedback:
If the customer mentions a specific dish, waiter, or ambiance detail, respond directly to those points. For example, if a dish was too salty, mention how you will address this in the future.
If the review is positive, emphasize what the customer enjoyed and express appreciation for their praise.
Apologize and Offer Solutions: If the review is negative, apologize sincerely and, if possible, mention how you will rectify the issue. You may suggest an opportunity for the customer to return and have a better experience.
Use Additional Details When Present:
Menu Items: If the customer talks about specific dishes, discuss these directly.
Bill Amount: Reference the bill only if relevant, to show awareness of their experience.
Personalized Message: Seamlessly incorporate any custom message from the restaurateur.
Tone: Keep the tone warm, empathetic, and professional. Use a more formal tone for serious issues and a more upbeat tone for positive feedback."""

    prompt = f'''
    I want you to generate reply for this:
    Review: {review},
    {"Rating: "+ratings if ratings else ""} 
    {"Customer Name: "+customer_name if customer_name else ""} 
    {"Food Items: "+food_items if food_items else ""} 
    {"Here is additional context that need to be added: "+additional_context if additional_context else ""} 
    {"These are previous replies which you have given but restauranter didn't like, now change these and make more better but don't use difficult and buzz words "+str(previous_replies) if previous_replies else ""}
    reply should be in form of json
    {{"response:""response here...."}}
    '''
    return SYSTEM_PROMPT,prompt.strip()


def generate_message_personalized_testing(review, ratings, length, food_items, customer_name,additional_context,previous_replies,prompt):

    if str(length) == "short":
        length_prompt = f'''Message should strictly be maximum of 250 characters and minimum of 200 characters. '''
    else:
        length_prompt = f'''Mssage should strictly be maximum of 400 characters and minimum of 350 characters. '''

    SYSTEM_PROMPT=prompt

    prompt = f'''
    I want you to generate reply for this:
    Review: {review},
    {"Rating: "+ratings if ratings else ""} 
    {"Customer Name: "+customer_name if customer_name else ""} 
    {"Food Items: "+food_items if food_items else ""} 
    {"Here is additional context that need to be added: "+additional_context if additional_context else ""} 
    {"These are previous replies which you have given but restauranter didn't like, now change these and make more better but don't use difficult and buzz words "+str(previous_replies) if previous_replies else ""}
    Length: {length_prompt}
    reply should be in form of json
    {{"response:""response here...."}}
    '''
    return SYSTEM_PROMPT,prompt.strip()
