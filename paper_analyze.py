import ollama

# 从PDF提取的样本文本
paper_text = """
放线菌作为一类具有广泛实际用途和巨大经济价值的微生物类群 ，其分子生态学是
微生物分子生态学的重要组成部分 。 放线菌分子生态学的研究内容目前主要是采用分子
生物学技术研究不同自然环境中放线菌的多样性 、分布状况以及它们的数量动态 ；目前的
放线菌分子生态学方法还不能揭示各种群和群落的生态学功能 。 应用于放线菌分子生态
学研究的方法大致可以分成两大类 ，即 rRNA 分析法和 DNA 指纹分析法（DNA finger唱
printing） 。 rRNA 分析法主要包括序列测定和探针检测 。 近年来 DNA 指纹分析法的发
展非常迅速 ，如限制性酶切片段长度多态性（RFLP）分析 、扩增性 rDNA 限制性酶切片段
分析（ARDRA） 、rRNA 基因间区分析（RISA） 、长度异质性分析（LH唱PCR）以及变性梯度
凝胶电泳分析等 。 这些方法以电泳图谱带型或带谱（band profile ，banding pattern）的形式
为结果 ，可比性好 ，是复杂自然微生物群落快速比较研究非常有用的方法 。
"""

prompt = f"将这篇论文总结为100字：{paper_text}"
response = ollama.generate(
    model="mistral",
    prompt=prompt 
)
print(response["response"])