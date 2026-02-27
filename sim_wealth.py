import numpy as np
import matplotlib.pyplot as plt

def simulate_economy(tax_rate=0.0):
    n_agents = 1000
    agents = np.full(n_agents, 100.0)
    
    for _ in range(50000):
        i, j = np.random.choice(n_agents, 2, replace=False)
        trade_amount = min(agents[i], agents[j]) * 0.01
        
        # 模拟博弈
        if np.random.rand() > 0.5:
            agents[i] += trade_amount
            agents[j] -= trade_amount
        else:
            agents[i] -= trade_amount
            agents[j] += trade_amount
        
        # 模拟简单的税收再分配 (宏观调控)
        if tax_rate > 0 and _ % 100 == 0:
            # 这里的逻辑：从所有人身上收一小部分，平均分给所有人
            tax_pool = np.sum(agents * tax_rate)
            agents = agents * (1 - tax_rate) + (tax_pool / n_agents)
            
    return agents

# 实验 1：完全自由放任的市场
result_free = simulate_economy(tax_rate=0.0)
# 实验 2：带微量再分配的市场 (0.1% 的调节)
result_regulated = simulate_economy(tax_rate=0.001)

# 可视化对比
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(result_free, bins=50, color='royalblue', alpha=0.7)
plt.title("Free Market (High Inequality)")

plt.subplot(1, 2, 2)
plt.hist(result_regulated, bins=50, color='seagreen', alpha=0.7)
plt.title("Regulated Market (More Balanced)")

plt.tight_layout()
plt.show()