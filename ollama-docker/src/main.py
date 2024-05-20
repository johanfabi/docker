import ollama

response = ollama.chat(model='qwen:0.5b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
    'language': 'en'
  },
])

print(response['message']['content'])