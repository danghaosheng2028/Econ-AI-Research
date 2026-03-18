import matplotlib.pyplot as plt

# 数据设定
labels_gpu = ['NVIDIA (US)', 'AMD (US)', 'Others']
sizes_gpu = [80, 10, 10]
labels_cloud = ['AWS (US)', 'Azure (US)', 'Google (US)', 'Others']
sizes_cloud = [31, 24, 11, 34]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# AI芯片市场
ax1.pie(sizes_gpu, labels=labels_gpu, autopct='%1.1f%%', startangle=90, 
        colors=['#4B0082', '#9370DB', '#DCDCDC'], pctdistance=0.85)
ax1.set_title("AI Accelerator Market Share (2024)")

# 云计算市场
ax2.pie(sizes_cloud, labels=labels_cloud, autopct='%1.1f%%', startangle=90, 
        colors=['#003366', '#336699', '#6699CC', '#DCDCDC'], pctdistance=0.85)
ax2.set_title("Global Cloud Infrastructure Services (2024)")

# 画圆心使之成为环形图
for ax in [ax1, ax2]:
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    ax.add_artist(centre_circle)

plt.tight_layout()
plt.show()
