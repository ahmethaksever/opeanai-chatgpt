openai.api_key = "OPENAI_TOKEN"

prompt="""
          Summarize the following text into three concise bullet points:
          Artificial intelligence (AI) is the intelligence of machines or software, as opposed to the intelligence of human beings or animals. AI applications include advanced web search engines (e.g., Google Search), recommendation systems (used by YouTube, Amazon, and Netflix), understanding human speech (such as Siri and Alexa), self-driving cars (e.g., Waymo), generative or creative tools (ChatGPT and AI art), and competing at the highest level in strategic games (such as chess and Go).
          Artificial intelligence was founded as an academic discipline in 1956. The field went through multiple cycles of optimism followed by disappointment and loss of funding. After 2012, deep learning surpassed all previous AI techniques, leading to a vast increase in funding and interest.
          The various sub-fields of AI research are centered around particular goals and the use of particular tools. The traditional goals of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception, and support for robotics. General intelligence (the ability to solve an arbitrary problem) is among the field's long-term goals.
          To solve these problems, AI researchers have adapted and integrated a wide range of problem-solving techniques, including search and mathematical optimization, formal logic, artificial neural networks, and methods based on statistics, probability, and economics. AI also draws upon psychology, linguistics, philosophy, neuroscience and many other fields.
        """

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=400,
  temperature=0
)

print(response["choices"][0]["text"])
