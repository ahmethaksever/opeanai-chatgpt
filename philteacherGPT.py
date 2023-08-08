import openai

openai.api_key = "sk-buraya opeanai key eklenecek"

instruction = "What Socrates was known for?"

# Create a request to the ChatCompletion endpoint
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system",
     "content": "You are a high school philosophy teacher. Explain philosophical questions, consepts, terms and paradoxes in a simple way to understand. Give a short answer. The answer should 3 sentences at most."},
    {"role": "user",
     "content": instruction
    }
  ],
  max_tokens=100
)

print(response['choices'][0]['message']['content'])
