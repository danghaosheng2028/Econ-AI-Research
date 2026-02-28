import numpy as np
import matplotlib.pyplot as plt

def run_discount_simulation():
    # 参数设置
    years = 100         # 模拟时长：100年
    n_paths = 5000      # 蒙特卡洛模拟路径数
    delta = 0.005       # 纯时间偏好率 (Stern倾向于接近0)
    gamma = 2.0         # 边际效用弹性 (社会对不平等的厌恶程度)

    # 1. 模拟不确定的经济增长率 g
    # 假设均值为 2%，但存在 3% 的标准差（模拟气候风险导致的波动）
    g_paths = np.random.normal(0.02, 0.03, (n_paths, years))

    # 2. 计算每条路径下的随机贴现率 r = delta + gamma * g
    r_paths = delta + gamma * g_paths

    # 3. 计算贴现因子 (Discount Factor): DF = exp(-sum(r_t))
    # 这一步体现了复合增长的影响
    discount_factors = np.exp(-np.cumsum(r_paths, axis=1))

    # 4. 计算“确定性等效”贴现率 (Certainty-Equivalent Rate)
    # 这是论文的核心：从期望的贴现因子中反推出来的有效利率
    expected_df = np.mean(discount_factors, axis=0)
    effective_rate = -np.log(expected_df) / np.arange(1, years + 1)

    # --- 绘图分析 ---
    plt.figure(figsize=(12, 6))

    # 子图1：有效贴现率随时间下降 (Weitzman效应)
    plt.subplot(1, 2, 1)
    plt.plot(range(1, years + 1), effective_rate * 100, color='darkgreen', linewidth=2)
    plt.title("Effective Discount Rate Over Time\n(The Weitzman Effect)")
    plt.xlabel("Years into the Future")
    plt.ylabel("Effective Rate (%)")
    plt.grid(True, alpha=0.3)

    # 子图2：未来100年后 $1 的现值对比
    plt.subplot(1, 2, 2)
    plt.plot(range(1, years + 1), expected_df, label="Stochastic (With Risk)", color='blue')
    # 对比项：恒定 5% 贴现率
    constant_df = np.exp(-0.05 * np.arange(1, years + 1))
    plt.plot(range(1, years + 1), constant_df, label="Constant 5% (Traditional)", linestyle='--', color='red')
    
    plt.title("Present Value of $1 in the Future")
    plt.xlabel("Years")
    plt.ylabel("Present Value ($)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_discount_simulation()