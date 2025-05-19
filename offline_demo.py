import ollama

prompt = """
分析这个样本描述：'灰色岩石，石英含量高，位于北纬35度。'
预测矿物成分。
"""
response = ollama.generate(model="mistral", prompt=prompt)
print(response["response"])