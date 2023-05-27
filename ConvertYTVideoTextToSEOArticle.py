import os
import openai

with open('key.txt', 'r') as file:
  first_line = file.readline()
os.environ["OPENAI_API_KEY"] = first_line


with open('transcript.txt', 'r') as file:
  text = file.read()

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
  model="gpt-4",
  temperature=0,
  messages=[
      {"role": "system", "content":"Create a SEO article for given text, adding good formatting tags (h1, h1, p, quotes,bold, italics, etc) return a formatted article with html tags"},
      {"role": "user", "content": text}

  ]
)

print(completion.choices[0].message.content)
print(completion.choices[0].message)
print(completion.tokens)
with open('seoArticle.txt', 'w') as f:
    f.write(completion.choices[0].message.content)


