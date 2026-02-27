import numpy as np

# 生成 100 万个随机财富值（正态分布：均值 100，标准差 20）
wealth_data = np.random.normal(100, 20, 1000000)

print(f"--- 财富分布模拟测试 ---")
print(f"总样本量: {len(wealth_data)}")
print(f"平均财富值: {np.mean(wealth_data):.2f}")
print(f"最富有的人财富: {np.max(wealth_data):.2f}")