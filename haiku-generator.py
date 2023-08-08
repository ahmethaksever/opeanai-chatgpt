import openai

openai_api_key="sk-openaikey"

theme = input("Hangi konu üzerine haiku şiir yazdırmak istersin? ")

prompt=f"{theme} hakkında haiku şiir yaz."

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=100,
  temperature=0.7
)

print(response["choices"][0]["text"])
