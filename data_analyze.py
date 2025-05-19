import ollama

prompt = """
为以下数据编写Python脚本，用Matplotlib绘制柱状图：
Gene,Expression
A,5.2
B,3.8
C,7.1
"""
response = ollama.generate(model="mistral", prompt=prompt)
print(response["response"])