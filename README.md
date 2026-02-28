# Econ-AI-Research: Math, Physics, and AI
> **项目定位**：利用统计物理模型与强化学习算法探索复杂经济系统中的非线性演化与博弈均衡。

## 📑 课题目录 (Research Tracks)
1.sim_wealth.py - 财富流动与熵增模型：模拟自由市场中的财富集中现象，探讨税收作为“负熵”对系统平衡的影响。

2.sim_debt.py - 债务违约与相变研究：分析杠杆累积导致的系统性金融风险触发点，捕捉非线性崩溃的临界阈值。

3.sim_market.py - 市场恐慌传染 (Ising Model)：借鉴统计物理磁化模型，研究社交情绪如何驱动智能体行为对齐并引发股市闪崩。

4.sim_pricing.py (重点推进) - AI 个性化定价博弈：研究大数据算法对消费者剩余的提取效率及其在信息不对称条件下的伦理边界。

5.sim_discount.py (重点推进) - 长期环境政策贴现建模：研究气候风险不确定性下的代际公平（Intergenerational Equity）与递减贴现率（DDR）的数学必然性。

## 🛠️ 环境要求与运行 (Setup)

### 硬件支持
* **Windows 10/11** (当前实验环境)
* **macOS (Apple Silicon M4)** (已完成适配，支持 MPS 加速)

### 快速启动
```powershell
# 克隆仓库
git clone [https://github.com/danghaosheng2028/Econ-AI-Research.git](https://github.com/danghaosheng2028/Econ-AI-Research.git)
cd Econ-AI-Research

# 安装依赖
pip install numpy matplotlib pandas

# 运行个性化定价模拟
python sim_pricing.py

1. 财富分配模拟：从“熵”到“动态平衡”
对应文件: sim_wealth.py

实验观察:

左图（蓝）: 展示了自由交易下的“长尾分布”，财富自发流向极少数个体。

右图（绿）: 引入 0.1% 的微量税收后，分布回归到有序的“钟形曲线”，显著抑制了贫富差距。

物理学理解: 模拟了系统的熵增（Entropy）。在无干预状态下，财富倾向于演变为高无序度的极端分布；宏观调控本质上是向系统输入负熵，以维持社会结构的低熵有序态。

I used the Yard-Sale Model to demonstrate how spontaneous wealth concentration can be mitigated by minimal algorithmic intervention, mirroring the concept of negative entropy in thermodynamic systems.

2. 债务危机预警：杠杆引发的“非线性崩溃”
对应文件: sim_debt.py

实验观察: 系统在前半段表现出“虚假的繁荣”，破产数为 0；但在杠杆累积至临界点时，破产人数呈指数级突变。

物理学理解: 这是一个典型的**相变（Phase Transition）**过程。就像过饱和溶液突然结晶，债务累积到 Tipping Point 后，任何微小的随机波动都会引发全局性的连锁反应。

经济学含义: 展示了债务的非线性特征。危机爆发前系统的“欺骗性稳定”往往是导致决策迟缓的根本原因。

My simulation suggests that financial instability is a non-linear process; debt accumulation acts as a phase transition where the system remains deceptively stable until it hits a critical threshold.

3. 市场恐慌传播：多智能体间的“磁性耦合”
对应文件: sim_market.py

实验观察: 外部冲击发生后，恐慌并不是线性增加，而是像野火一样瞬间蔓延，斜率急剧变陡。

物理学理解: 借鉴了伊辛模型（Ising Model）。个体的决策受邻近智能体的“自旋方向”（买入/卖出）强烈影响。这种“磁性耦合”产生了经济学中的羊群效应（Herding Effect）。

AI/算法价值: 证明了“熔断机制”的物理必要性——通过强制中断智能体间的相互作用，阻断恐慌情绪的连锁传染。

Inspired by the Ising Model in statistical mechanics, I modeled market panic as a social contagion, demonstrating how localized interactions can lead to large-scale 'avalanches' in financial sentiment.

4. 个性化定价：AI 精度驱动的福利剥削
对应文件: sim_pricing.py

实验观察: 随着 AI 预测精度（Accuracy）提升，**卖家利润（Blue Line）稳步上升，而消费者剩余（Red Line）**呈渐近式下降。

物理学理解: 这代表了系统内**势能（支付意愿）**的精准定向抽取。AI 算法充当了“麦克斯韦妖（Maxwell's Demon）”，通过筛选并利用个体信息，打破了信息的随机性，将原本属于消费者的福利定向转化为卖家的收益。

经济学含义: 模拟了从完全竞争到**一级价格歧视（First-degree Price Discrimination）**的转变。它揭示了算法效率与社会分配公平之间的根本权衡。

My research quantifies the welfare transfer in algorithmic pricing; as AI minimizes information asymmetry, it effectively captures the entire consumer surplus, transforming market efficiency into unilateral profit maximization.

5. 环境政策贴现：不确定性下的“代际公平”
对应文件: sim_discount.py

实验观察:在考虑气候风险（随机增长率 $g$）的模拟中，有效贴现率（Effective Rate）随时间推移呈明显的非线性下降趋势。相比于传统恒定 5% 的贴现率，随机模型下未来 100 年后的环境资产现值（Present Value）得到了显著提升。

物理学理解: 模拟了随机动力学系统中的“期望值演化”。当未来路径存在极端的负向扰动（气候灾难）时，系统为了对冲崩溃风险，数学上会自动降低对未来的“折价”。这证明了在不确定性场中，低贴现率是维持跨时空平衡的稳定解。

经济学含义: 验证了 Weitzman 效应与**递减贴现率（DDR）**理论。它挑战了短期主义的金融逻辑，证明了为了实现代际公平（Intergenerational Equity），保护远期环境资产在数学上要求我们采用极低的贴现率。

Through Monte Carlo simulations of stochastic growth, I demonstrated the 'Weitzman Effect' in environmental economics: as long-term uncertainty accumulates, the effective discount rate must non-linearly decline to zero to prevent the mathematical erasure of future generations' welfare.

git add README.mdgit add README.md