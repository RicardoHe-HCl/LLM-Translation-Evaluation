import matplotlib.pyplot as plt
import numpy as np
import os

# 确保有 figures 文件夹
if not os.path.exists('figures'):
    os.makedirs('figures')

# 设置中文字体（如果是英文系统，可以去掉或换成 Arial）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False


# ==========================================
# 图1: Track 2 多轮对话五维雷达图
# ==========================================
def plot_dialogue_radar():
    categories = ['Context Tracking', 'Logical Accuracy', 'Interaction Fluency', 'Register Match', 'Socio-Cultural']
    N = len(categories)

    # Track 2 评分数据
    chatgpt = [5.0, 4.5, 4.8, 4.5, 5.0]
    gemini = [5.0, 3.0, 5.0, 4.9, 5.0]
    claude = [5.0, 5.0, 4.5, 4.0, 4.5]

    # 闭合雷达图
    chatgpt += chatgpt[:1]
    gemini += gemini[:1]
    claude += claude[:1]

    # 角度计算
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # 绘制 ChatGPT (蓝色)
    ax.plot(angles, chatgpt, linewidth=2, linestyle='solid', label='ChatGPT (GPT-4o)', color='#1f77b4')
    ax.fill(angles, chatgpt, '#1f77b4', alpha=0.1)

    # 绘制 Gemini (绿色)
    ax.plot(angles, gemini, linewidth=2, linestyle='solid', label='Gemini', color='#2ca02c')
    ax.fill(angles, gemini, '#2ca02c', alpha=0.1)

    # 绘制 Claude (橙色)
    ax.plot(angles, claude, linewidth=2, linestyle='solid', label='Claude', color='#ff7f0e')
    ax.fill(angles, claude, '#ff7f0e', alpha=0.1)

    # 设置刻度与标签
    plt.xticks(angles[:-1], categories, size=12)
    ax.set_rlabel_position(30)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=10)
    plt.ylim(0, 5)

    plt.title('Track 2: Multi-turn Dialogue Capabilities', size=16, y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # 保存图片到 figures 文件夹
    plt.savefig('figures/fig4_dialogue_radar.png', bbox_inches='tight', dpi=300)
    print("生成成功: figures/fig4_dialogue_radar.png")


# ==========================================
# 图2: Track 1 (翻译) vs Track 2 (对话) 总体得分对比柱状图
# ==========================================
def plot_overall_comparison():
    models = ['DeepL', 'ChatGPT', 'Gemini', 'Claude']

    # Track 1 翻译总分 (根据你之前的 README 数据)
    track1_scores = [4.18, 4.71, 4.67, 4.79]

    # Track 2 对话总分 (DeepL 不支持此任务，设为 0 以作区分)
    track2_scores = [0, 4.76, 4.58, 4.60]

    x = np.arange(len(models))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width / 2, track1_scores, width, label='Track 1: Translation', color='#6c757d')
    rects2 = ax.bar(x + width / 2, track2_scores, width, label='Track 2: Multi-turn Dialogue', color='#007bff')

    ax.set_ylabel('Average Score (1-5)', fontsize=12)
    ax.set_title('Overall Performance Comparison by Track', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=12)
    ax.set_ylim(0, 5.5)
    ax.legend(loc='upper left')

    # 在柱子上显示具体分数
    def autolabel(rects, is_track2=False):
        for i, rect in enumerate(rects):
            height = rect.get_height()
            if height == 0 and is_track2:
                ax.annotate('N/A', xy=(rect.get_x() + rect.get_width() / 2, 0.2),
                            xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)
            else:
                ax.annotate(f'{height:.2f}', xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

    autolabel(rects1)
    autolabel(rects2, is_track2=True)

    plt.savefig('figures/fig5_track_comparison.png', bbox_inches='tight', dpi=300)
    print("生成成功: figures/fig5_track_comparison.png")


if __name__ == '__main__':
    plot_dialogue_radar()
    plot_overall_comparison()