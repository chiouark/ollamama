import ollama
from ollama import chat
stream=chat(model='qwen2.5:14b',messages=[{'role':'user','content':"comment calculer le rwa d une banque"}],stream=True)
for chunk in stream:
    print(chunk['message']['content'],end='',flush=True)
    