import numpy as np
import matplotlib.pyplot as plt

def simulate_personalised_pricing(ai_accuracy=0.5):
    """
    ai_accuracy: 0.0 代表完全随机定价，1.0 代表 AI 完美预测消费者心理价位
    """
    n_customers = 1000
    # 消费者的真实支付意愿 (Willingness to Pay) - 服从正态分布
    wtp = np.random.normal(100, 20, n_customers)
    cost = 50 # 卖家的商品成本

    # AI 尝试预测每个人的 WTP
    # AI 的预测值 = 真实值 + 噪声 (噪声随精度降低而增大)
    noise = (1 - ai_accuracy) * np.random.normal(0, 20, n_customers)
    predicted_wtp = wtp + noise
    
    prices = predicted_wtp # 卖家按预测值报价
    
    # 成交逻辑：只有当 报价 <= 真实支付意愿 时，才会成交
    sales_mask = (prices <= wtp) & (prices > cost)
    
    # 计算经济指标
    # 卖家利润 = 价格 - 成本
    seller_profit = np.sum(prices[sales_mask] - cost)
    # 消费者剩余 = 支付意愿 - 价格
    consumer_surplus = np.sum(wtp[sales_mask] - prices[sales_mask])
    
    return seller_profit, consumer_surplus

# --- 实验分析：随着 AI 精度提升，利润如何变化？ ---
accuracies = np.linspace(0, 1, 50)
profits = []
surpluses = []

for acc in accuracies:
    p, s = simulate_personalised_pricing(acc)
    profits.append(p)
    surpluses.append(s)

# --- 绘图展示 ---
plt.figure(figsize=(10, 6))
plt.plot(accuracies, profits, label="Seller Profit (AI Gain)", color='blue', linewidth=2)
plt.plot(accuracies, surpluses, label="Consumer Surplus (User Loss)", color='red', linewidth=2)
plt.title("Impact of AI Pricing Accuracy on Market Welfare")
plt.xlabel("AI Prediction Accuracy (Big Data Capability)")
plt.ylabel("Total Value")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()