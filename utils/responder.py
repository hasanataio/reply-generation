import json
import openai
import os 
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# function to generate gpt response
def responder_JSON(system_prompt,prompt):
    # Make a request to the ChatGPT API
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content.strip())