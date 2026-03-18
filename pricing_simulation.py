import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# 确保脚本在当前目录下运行
print("正在启动经济模型模拟程序...")

# 设置随机种子保证结果可复现
np.random.seed(42)

# 1. 模拟 1000 名消费者的支付意愿 (WTP)
num_consumers = 1000
wtp = np.random.uniform(10, 100, num_consumers)
marginal_cost = 20  # 边际成本

# 2. 场景一：统一定价 (Uniform Pricing)
possible_prices = np.linspace(10, 100, 100)
profits = [(p - marginal_cost) * np.sum(wtp >= p) for p in possible_prices]
optimal_uniform_price = possible_prices[np.argmax(profits)]

uniform_profit = np.max(profits)
uniform_cs = np.sum(wtp[wtp >= optimal_uniform_price] - optimal_uniform_price)
uniform_dwl = np.sum(wtp[(wtp >= marginal_cost) & (wtp < optimal_uniform_price)] - marginal_cost)

# 3. 场景二：完美个性化定价 (Perfect PP)
perfect_pp_profit = np.sum(wtp[wtp >= marginal_cost] - marginal_cost)
perfect_pp_cs = 0 
perfect_pp_dwl = 0 

# 4. 场景三：现实算法定价 (Realistic AI Pricing)
algorithm_efficiency = 0.85
biased_price = np.where(wtp >= marginal_cost, wtp * algorithm_efficiency, 0) 
imperfect_profit = np.sum(np.maximum(0, biased_price - marginal_cost))
imperfect_cs = np.sum(np.maximum(0, wtp[wtp >= marginal_cost] - biased_price[wtp >= marginal_cost]))

# 5. 打印结果到终端 (确保即使没图也能看到数据)
data = {
    "Scenario": ["Uniform", "Perfect PP", "Realistic AI"],
    "Producer_Surplus": [uniform_profit, perfect_pp_profit, imperfect_profit],
    "Consumer_Surplus": [uniform_cs, perfect_pp_cs, imperfect_cs],
    "Total_Welfare": [uniform_profit + uniform_cs, perfect_pp_profit + perfect_pp_cs, imperfect_profit + imperfect_cs]
}

df = pd.DataFrame(data)
print("\n" + "="*50)
print("经济模型模拟结果对比 (用于论文引用)")
print("="*50)
print(df.to_string(index=False))
print("="*50)

# 自动保存数据到 CSV
df.to_csv("simulation_results.csv", index=False)
print("数据已保存至: simulation_results.csv")

# 6. 绘图
try:
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 6))

    labels = ['Uniform', 'Perfect PD', 'Realistic AI']
    profits_list = [uniform_profit, perfect_pp_profit, imperfect_profit]
    cs_list = [uniform_cs, perfect_pp_cs, imperfect_cs]

    plt.bar(labels, profits_list, label='Producer Surplus (Profit)', color='#2E5A88')
    plt.bar(labels, cs_list, bottom=profits_list, label='Consumer Surplus', color='#D98850')

    plt.title('Economic Welfare Distribution: Efficiency vs. Equity')
    plt.ylabel('Value')
    plt.legend()

    # 自动保存图表
    plt.savefig("welfare_distribution.png", dpi=300)
    print("图表已自动保存为: welfare_distribution.png")
    
    # 尝试显示
    print("正在尝试弹出图表窗口...")
    plt.show()
except Exception as e:
    print(f"绘图显示遇到一点小问题 (可能是环境缺少UI支持)，但图片已保存。错误信息: {e}")

print("\n程序运行完毕！")
