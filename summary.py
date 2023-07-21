openai.api_key = "OPENAI_TOKEN"

prompt="""
          Summarize the following text into two concise bullet points:
        """

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=400,
  temperature=0
)

print(response["choices"][0]["text"])
