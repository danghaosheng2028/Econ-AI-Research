import numpy as np
import matplotlib.pyplot as plt

def simulate_debt_crisis():
    n_agents = 1000
    # 初始财富 100，初始债务 0
    wealth = np.full(n_agents, 100.0)
    debt = np.zeros(n_agents)
    
    crisis_history = []

    for year in range(50): # 模拟 50 年
        for _ in range(1000): # 每年 1000 次交易
            i, j = np.random.choice(n_agents, 2, replace=False)
            trade_amount = 5.0
            
            # 模拟借贷：如果钱不够，允许欠债（杠杆）
            if wealth[i] < trade_amount:
                debt[i] += (trade_amount - wealth[i])
                wealth[i] = 0
            else:
                wealth[i] -= trade_amount
            wealth[j] += trade_amount
        
        # 计算违约人数（债务超过财富 2 倍的人）
        bankrupt_count = np.sum(debt > wealth * 2)
        crisis_history.append(bankrupt_count)

    plt.plot(crisis_history, color='red')
    plt.title("Financial Risk: Number of Bankrupt Agents Over Time")
    plt.xlabel("Year")
    plt.ylabel("Insolvent Agents")
    plt.show()

if __name__ == "__main__":
    simulate_debt_crisis()