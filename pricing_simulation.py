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
# 假设 WTP 在 10 到 100 之间均匀分布
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
# 模拟现实中的算法：假设能捕捉到 85% 的剩余
algorithm_efficiency = 0.85
biased_price = np.where(wtp >= marginal_cost, wtp * algorithm_efficiency, 0) 
imperfect_profit = np.sum(np.maximum(0, biased_price - marginal_cost))
imperfect_cs = np.sum(np.maximum(0, wtp[wtp >= marginal_cost] - biased_price[wtp >= marginal_cost]))

# 5. 打印结果到终端
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

# 6. 绘图（加入学术规范微调）
try:
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12, 8))

    labels = ['Uniform', 'Perfect PD', 'Realistic AI']
    profits_list = [uniform_profit, perfect_pp_profit, imperfect_profit]
    cs_list = [uniform_cs, perfect_pp_cs, imperfect_cs]

    # 绘制堆叠柱状图
    ax.bar(labels, profits_list, label='Producer Surplus (Profit)', color='#2E5A88')
    ax.bar(labels, cs_list, bottom=profits_list, label='Consumer Surplus', color='#D98850')

    # 修订点 1：明确纵轴单位
    ax.set_title('Economic Welfare Distribution: Efficiency vs. Equity', fontsize=16, pad=20)
    ax.set_ylabel('Welfare Units', fontsize=12)
    ax.set_xlabel('Pricing Scenarios', fontsize=12)
    ax.legend(loc='upper left', fontsize=11)

    # 在柱状图上添加具体数值标注，增加可读性
    for i in range(len(labels)):
        total_val = profits_list[i] + cs_list[i]
        ax.text(i, profits_list[i]/2, f'{int(profits_list[i])}', ha='center', va='center', color='white', fontweight='bold')
        if cs_list[i] > 0:
            ax.text(i, profits_list[i] + cs_list[i]/2, f'{int(cs_list[i])}', ha='center', va='center', color='white', fontweight='bold')
        # 在顶部显示总福利
        ax.text(i, total_val + 500, f'Total: {int(total_val)}', ha='center', va='bottom', fontweight='bold')

    # 修订点 2：添加学术引用脚注 (Source Note)
    source_text = "Source: Simulated by the author using a Monte Carlo model based on 1,000 heterogeneous consumers."
    plt.figtext(0.5, 0.01, source_text, ha="center", fontsize=10, style='italic', color='gray')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # 为脚注留出空间

    # 自动保存图表
    plt.savefig("welfare_distribution_professional.png", dpi=300)
    print("专业版图表已自动保存为: welfare_distribution_professional.png")
    
    # 尝试显示
    print("正在尝试弹出图表窗口...")
    plt.show()
except Exception as e:
    print(f"绘图显示遇到问题，但图片已保存。错误信息: {e}")

print("\n程序运行完毕！")

