# Econ-AI-Research: Math, Physics, and AI
1. 财富分配模拟：从“熵”到“动态平衡”
对应文件：sim_wealth.png
实验观察：
左图（蓝）：分布更散，甚至出现极高财富的长尾。这模拟了“自然状态”，财富自发地流向少数幸运儿。
右图（绿）：分布更集中，呈现完美的钟形曲线。仅仅 0.1% 的微量调节就极大地压缩了贫富差距。
物理学理解：这反映了系统的熵增（Entropy）。在封闭系统中，无序度会自然增加（贫富差距拉大）；而宏观调控（税收）本质上是向系统输入负熵，从而维持有序的社会结构。

I used the Yard-Sale Model to demonstrate how spontaneous wealth concentration can be mitigated by minimal algorithmic intervention, mirroring the concept of negative entropy in thermodynamic systems.

2. 债务危机预警：杠杆引发的“非线性崩溃”
对应文件：sim_debt.png / image_29b5d9.png
实验观察：曲线在前半段非常平稳（破产数为0），但在第 25 年左右突然发生“突变”，破产人数呈指数级上升。
物理学理解：这是一个典型的**相变（Phase Transition）**过程。就像水加热到 100°C 会突然沸腾一样，系统内的债务（杠杆）累积到一个临界点（Tipping Point）后，微小的波动就会引发全局性的连锁崩溃。
经济学含义：它展示了债务的“非线性”特征。在危机爆发前，系统看起来非常健康，这往往会误导决策者。

My simulation suggests that financial instability is a non-linear process; debt accumulation acts as a phase transition where the system remains deceptively stable until it hits a critical threshold.

3. 市场恐慌传播：多智能体间的“磁性耦合”
对应文件：sim_market.png

实验观察：第 20 步的“外部冲击”只是一个小火星，但随后的恐慌百分比（紫色曲线）却像野火一样蔓延，且斜率越来越陡。

物理学理解：这借鉴了物理学中的 Ising 模型（描述原子磁矩如何因邻居影响而转向一致）。在市场中，这叫羊群效应（Herding Effect）。每个交易者不仅看新闻，更看邻居的操作。

AI/算法价值：这说明了为什么“熔断机制”是必要的——它通过物理隔离来阻断情绪颗粒的“传染链”。

Inspired by the Ising Model in statistical mechanics, I modeled market panic as a social contagion, demonstrating how localized interactions can lead to large-scale 'avalanches' in financial sentiment.