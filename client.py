from openai import OpenAI

#client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
   api_key=" ", #Enter your API key
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in general task like Alexa and Google cloud."},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message)