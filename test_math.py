import numpy as np
import matplotlib.pyplot as plt

# 1. 实验设置：1000个个体，每人初始财富 100
n_agents = 1000
agents = np.full(n_agents, 100.0)

# 2. 财富流动模拟：进行 50,000 次随机博弈交易
for _ in range(50000):
    # 随机选择两个博弈者
    i, j = np.random.choice(n_agents, 2, replace=False)
    
    # 交易额：双方中较穷者财富的 1% (风险控制模型)
    trade_amount = min(agents[i], agents[j]) * 0.01
    
    # 50/50 胜负机会 (模拟随机市场博弈)
    if np.random.rand() > 0.5:
        agents[i] += trade_amount
        agents[j] -= trade_amount
    else:
        agents[i] -= trade_amount
        agents[j] += trade_amount

# 3. 计算经济指标：基尼系数 (衡量财富不平等的关键指标)
def get_gini(arr):
    arr = np.sort(arr)
    n = len(arr)
    index = np.arange(1, n + 1)
    return (np.sum((2 * index - n - 1) * arr)) / (n * np.sum(arr))

print(f"模拟完成！当前系统的基尼系数为: {get_gini(agents):.4f}")

# 4. 可视化财富分布 (这就是物理学中的“玻尔兹曼-吉布斯”分布)
plt.figure(figsize=(10, 6))
plt.hist(agents, bins=50, color='royalblue', edgecolor='white')
plt.title("Wealth Distribution after 50,000 Market Exchanges")
plt.xlabel("Wealth Amount")
plt.ylabel("Number of People")
plt.show()



