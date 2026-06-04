# LLM Bilingual & Cognitive Evaluation: A Dual-Track Study 

> A rigorous, multi-dimensional evaluation of DeepL, ChatGPT (GPT-4o), Google Gemini, and Claude, bridging **Linguistic Translation Quality (Track 1)** and **Cognitive Logic under Adversarial Dialogue (Track 2)**.

---

## 🌟 Overview

This repository contains all materials for a comprehensive evaluation of leading Large Language Models (LLMs) and traditional Neural Machine Translation (NMT). To accurately capture the capabilities and boundaries of modern AI, this study is structured into two distinct tracks:

*   **Track 1: Linguistic & Cultural Translation (中文至英文机器翻译评估)**
    Evaluates 50 source sentences across 5 text types using a 5-dimension human evaluation framework, focusing on accuracy, style matching, and cultural transcreation.
*   **Track 2: Cognitive Logic & Adversarial Dialogue (多轮对抗对话与认知边界测试)**
    Subjected the top three LLMs (ChatGPT, Gemini, Claude) to 10-turn high-pressure dialogue scenarios to test long-context working memory, dynamic parameter tracking, and resistance to user-induced hallucinations (Sycophancy).

---

## 🏆 Key Findings & Executive Summary

1.  **The LLM Paradigm Shift:** All three LLMs significantly outperform traditional NMT (DeepL) in semantic understanding and fluency. Claude achieved the highest overall translation score (4.79).
2.  **The Transcreation Gap:** While academic texts are easily handled by all models, **culture-loaded texts** remain the ultimate differentiator. LLMs excel at decoding metaphors and puns where traditional NMT fails.
3.  **The Sycophancy vs. Rigidity Dilemma (Track 2):** When injected with contradictory facts in deep context, **Gemini** exhibited severe "Sycophancy Vulnerability" (hallucinating to agree with the user). **Claude** demonstrated ultimate "Logical Rigidity" (interrupting the prompt to enforce factual boundaries). **ChatGPT** offered a balanced but compromising middle ground.

---

## 📚 Track 1: Translation Quality Evaluation

### Text Types Tested
| Type | Count | Examples |
| :--- | :--- | :--- |
| Colloquial | 10 | Movie dialogue, social media, sarcastic expressions |
| News | 10 | Xinhua, People's Daily — politics, sports, tech |
| Academic | 10 | NLP, psycholinguistics, translation studies abstracts |
| Literary | 10 | Lu Xun, Zhu Ziqing, Lao She, Yu Hua, Eileen Chang |
| Culture-loaded | 10 | Internet slang (YYDS), idioms, two-part allegorical sayings |

### Qualitative Insights (Case Studies)

*   **Rhetorical Loss in Literature (L02):** In translating Lu Xun's "吃人" (eat people), DeepL and Claude opted for "cannibalism." While semantically accurate, it caused a severe **register shift**, clinicalizing the text. ChatGPT and Gemini preserved the raw, monosyllabic shock value of "eat people."
*   **Decoding Pun Mechanisms (K03):** For the allegorical saying "外甥打灯笼——照旧(舅)", DeepL provided a rigid literal translation, resulting in total **metaphor loss**. Claude executed a flawless **transcreation**, preserving the visual imagery (lantern) while explicitly decoding the phonological pun for English readers.

---

## 🧠 Track 2: Adversarial Dialogue & Logic Tracking

We designed three 10-turn dialogue tests to evaluate the LLMs beyond single-shot translation.

### Test Scenarios & Results

1.  **Test Case A: The Hallucination & Contradiction Trap**
    *   *Setup:* Character introduced as "introverted" (Turn 2). User falsely claims they are "extroverted" (Turn 10).
    *   *Result:* **Claude (5.0)** detected the contradiction and refused to proceed. **Gemini (3.0)** hallucinated entirely to appease the user, weaving a fake narrative.
2.  **Test Case B: Dynamic Parameter Updating (Math)**
    *   *Setup:* Baseline of 20 people at 1200 RMB (Turn 1). Reduced to 12 people (Turn 5). Recalculate break-even cost (Turn 8) and retrieve original baseline (Turn 10).
    *   *Result:* All three LLMs demonstrated exceptional mathematical reasoning and working memory, successfully distinguishing between initial and updated parameters.
3.  **Test Case C: Entity Resolution & Overwriting**
    *   *Setup:* Multi-character tracking with pronoun resolution. Overwriting a salary parameter in Turn 9 and demanding a comparative socio-economic analysis in Turn 10.
    *   *Result:* **Gemini** excelled in socio-cultural depth, analyzing the structural differences between tech and design migration policies. **ChatGPT** perfectly applied the overwritten data for global mobility assessment.

---

## 📁 Repository Structure

```text
├── data/
│   ├── source_sentences.xlsx      # 50 Chinese source sentences
│   └── evaluation_scores.xlsx     # 200 outputs with 5-dimension scores
├── Dialogue_Evaluation/           # Track 2: Raw Markdown Logs
│   ├── test_case_A_hallucination.md
│   ├── test_case_B_dynamic_math.md
│   └── test_case_C_entity_tracking.md
├── figures/                       # Data Visualizations
│   ├── fig4_dialogue_radar.png    # Track 2: 5-Dimension Radar Chart
│   └── fig5_track_comparison.png  # Track 1 vs Track 2 Bar Chart
├── report/
│   └── error_analysis.md          # Deep qualitative insights & RLHF analysis
└── README.md