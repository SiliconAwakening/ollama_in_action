import ollama

prompt = "用赛博朋克风格，写一个200字的科幻小说开头，场景是霓虹灯城市。"
response = ollama.generate(model="mistral", prompt=prompt)
print(response["response"])