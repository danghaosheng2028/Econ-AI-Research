import matplotlib.pyplot as plt

# 数据来源：模拟 IMF 关于 Geoeconomic Fragmentation 的预测数据
scenarios = ['Limited Fragmentation', 'Moderate Decoupling', 'Severe Fragmentation']
gdp_loss = [-0.2, -2.5, -7.0]  # 负值代表GDP损失百分比

plt.figure(figsize=(9, 6))
colors = ['#FFCC00', '#FF6600', '#CC0000']
bars = plt.bar(scenarios, gdp_loss, color=colors, width=0.6)

plt.axhline(0, color='black', linewidth=0.8)
plt.ylabel('Potential Long-term GDP Change (%)', fontsize=12)
plt.title('Economic Cost of Global Trade Fragmentation', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加数值标注
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval - 0.5, f'{yval}%', 
             ha='center', va='top', fontweight='bold', color='black')

plt.show()
