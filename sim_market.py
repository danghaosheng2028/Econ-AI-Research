import numpy as np
import matplotlib.pyplot as plt

def simulate_market_panic():
    n_agents = 50  # 模拟一个 50x50 的交易者网格
    # 状态：1 代表买入/持有（乐观），-1 代表卖出（恐慌）
    market_sentiment = np.ones((n_agents, n_agents))
    
    panic_levels = []
    
    # 模拟 100 个时间步
    for t in range(100):
        # 外部冲击：在第 20 步时，突然发生一个负面经济新闻
        external_shock = -0.5 if t > 20 else 0.1
        
        # 随机选择交易者更新情绪
        for _ in range(500):
            i, j = np.random.randint(0, n_agents, 2)
            
            # 邻居影响：观察四周 4 个交易者的情绪
            neighbors = (market_sentiment[(i-1)%n_agents, j] + 
                         market_sentiment[(i+1)%n_agents, j] + 
                         market_sentiment[i, (j-1)%n_agents] + 
                         market_sentiment[i, (j+1)%n_agents])
            
            # 决策逻辑：外部冲击 + 羊群效应
            score = external_shock + 0.5 * neighbors
            market_sentiment[i, j] = 1 if score + np.random.randn()*0.5 > 0 else -1
            
        # 记录全市场恐慌程度（卖出者的比例）
        panic_level = np.sum(market_sentiment == -1) / (n_agents**2)
        panic_levels.append(panic_level)

    # 绘制恐慌演变图
    plt.figure(figsize=(10, 5))
    plt.plot(panic_levels, color='purple', linewidth=2)
    plt.axvline(x=20, color='gray', linestyle='--', label='Market Shock')
    plt.title("Market Panic Propagation (Agent-Based Model)")
    plt.xlabel("Time Step")
    plt.ylabel("Percentage of Panic Sellers")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    simulate_market_panic()