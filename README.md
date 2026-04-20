# A Comparative Study of Chinese-to-English Machine Translation Quality Based on Multi-Dimensional Human Evaluation

## 🎯 Project Summary
A human-evaluated benchmark comparing translation performance of major LLMs across multiple text types.

> Taking DeepL, ChatGPT (GPT-4o), Google Gemini, and Claude as Examples

---

## Overview

This repository contains all materials for a study that compares the Chinese-to-English translation quality of four machine translation systems: **DeepL**, **ChatGPT (GPT-4o)**, **Google Gemini**, and **Claude**.

We collected 50 Chinese source sentences across five text types, translated them with each system, and manually scored all 200 outputs using a five-dimension evaluation framework. The goal is to figure out which system works best for what kind of text, and where the real quality gaps are.

---

## Key Findings

- All three LLM-based systems outperform the traditional NMT system DeepL. Claude scores the highest overall (4.79), followed by GPT (4.71) and Gemini (4.67). DeepL comes in at 4.18.
- Text type matters a lot. Academic texts are easy for everyone -- scores are high and close. Culture-loaded texts are where the biggest gaps show up (DeepL 3.52 vs. Claude 4.86).
- Fluency is no longer the differentiator. All systems can write smooth English now. What really separates them is cultural adaptation and terminology accuracy.
- No single system wins across all text types. GPT is strongest on academic texts, Gemini on colloquial, and Claude on news and culture-loaded content.

---

## Text Types Tested

| Type           | Count | Examples                                                       |
| -------------- | ----- | -------------------------------------------------------------- |
| Colloquial     | 10    | Movie dialogue, social media, sarcastic expressions            |
| News           | 10    | Xinhua, People's Daily -- politics, sports, tech               |
| Academic       | 10    | NLP, psycholinguistics, translation studies abstracts           |
| Literary       | 10    | Lu Xun, Zhu Ziqing, Lao She, Yu Hua, Eileen Chang             |
| Culture-loaded | 10    | Internet slang, idioms, two-part allegorical sayings, proverbs |

---

## Evaluation Dimensions

Each translation was scored on a 1--5 Likert scale across five dimensions:

| Dimension            | What It Measures                                                            |
| -------------------- | --------------------------------------------------------------------------- |
| Accuracy             | Whether the translation faithfully conveys the source meaning               |
| Fluency              | Whether the English reads naturally and smoothly                            |
| Style Matching       | Whether the translation matches the register and tone of the source         |
| Terminology Accuracy | Whether specialized terms and fixed expressions are translated correctly    |
| Cultural Adaptation  | How well culture-loaded content (idioms, slang, allusions) is handled       |

---

## Results at a Glance

### Overall Scores

| Rank | System | Avg Score |
| ---- | ------ | --------- |
| 1    | Claude | 4.788     |
| 2    | GPT    | 4.708     |
| 3    | Gemini | 4.672     |
| 4    | DeepL  | 4.176     |

### Scores by Text Type

| Text Type  | DeepL | GPT  | Gemini | Claude | Best   |
| ---------- | ----- | ---- | ------ | ------ | ------ |
| Colloquial | 4.34  | 4.56 | 4.66   | 4.62   | Gemini |
| News       | 4.22  | 4.80 | 4.34   | 4.86   | Claude |
| Academic   | 4.38  | 5.00 | 4.98   | 4.92   | GPT    |
| Literary   | 4.42  | 4.78 | 4.68   | 4.68   | GPT    |
| Cultural   | 3.52  | 4.40 | 4.70   | 4.86   | Claude |

### Scores by Dimension

| Dimension           | DeepL | GPT  | Gemini | Claude |
| ------------------- | ----- | ---- | ------ | ------ |
| Accuracy            | 4.00  | 4.56 | 4.62   | 4.74   |
| Fluency             | 4.76  | 4.84 | 4.96   | 4.94   |
| Style               | 4.08  | 4.50 | 4.46   | 4.68   |
| Terminology         | 3.92  | 4.72 | 4.50   | 4.64   |
| Cultural Adaptation | 3.82  | 4.42 | 4.34   | 4.58   |

---

## Repository Structure

    report/
        paper_chinese.pdf          -- Full paper in Chinese
        paper_english.pdf          -- Full paper in English

    data/
        source_sentences.xlsx      -- 50 Chinese source sentences with metadata
        evaluation_scores.xlsx     -- 200 translation outputs with scores

    figures/
        fig1_overall.png           -- Overall performance comparison (bar chart)
        fig2_by_type.png           -- Performance by text type (grouped bar chart)
        fig3_radar.png             -- Five-dimension radar chart
        fig4_heatmap.png           -- 50 x 4 translation quality heatmap

    README.md

---

## Methodology

1. **Source material**: 50 Chinese sentences selected from real-world sources (news articles, literary works, academic abstracts, movie dialogue, internet expressions), 10 per text type.
2. **Translation**: All four systems were run on the same day (April 18, 2025) using default settings with no extra prompts -- just the raw Chinese text with a request to translate into English.
3. **Evaluation**: Each of the 200 outputs was manually scored on five dimensions (1--5 scale). Scores were recorded with reasoning and reviewed for consistency.

---

## Some Interesting Cases

### "YYDS" (K06) -- DeepL gets it wrong

| System | Translation                                                                       | Score |
| ------ | --------------------------------------------------------------------------------- | ----- |
| DeepL  | "which stands for 'You're the God'"                                               | 2.0   |
| GPT    | "meaning 'the GOAT' (the greatest of all time)"                                  | 5.0   |
| Gemini | "which means 'the GOAT'"                                                          | 5.0   |
| Claude | "which stands for 'yong yuan de shen' -- meaning 'the GOAT' or 'a legend forever'" | 5.0   |

DeepL translates "YYDS" as "You're the God", which is factually incorrect. "YYDS" comes from the pinyin initials of "yong yuan de shen" (forever the god). All three LLMs correctly identify it and map it to "GOAT" (greatest of all time). Claude even keeps the original Chinese and adds an explanation.

### Irrelevant Speech Effect (A03) -- Terminology matters

| System | Key Term                      | Score |
| ------ | ----------------------------- | ----- |
| DeepL  | "non-verbal effects" (wrong)  | 3.0   |
| GPT    | "irrelevant speech effect"    | 5.0   |
| Gemini | "irrelevant speech effect"    | 5.0   |
| Claude | "irrelevant speech effect"    | 5.0   |

DeepL translates "wu guan yan yu xiao ying" (irrelevant speech effect) as "non-verbal effects" -- wrong term, wrong meaning. All three LLMs correctly produce "irrelevant speech effect", the standard term in psycholinguistics.

### Two-part Allegorical Saying (K03) -- Layers of meaning

| System | Translation                                                                                          | Score |
| ------ | ---------------------------------------------------------------------------------------------------- | ----- |
| DeepL  | "A nephew holding a lantern -- it still shines on his uncle."                                        | 2.4   |
| GPT    | "A nephew carrying a lantern -- just like before (a pun on 'uncle')."                                | 4.0   |
| Gemini | "Like a nephew carrying a lantern -- everything remains the same as always."                         | 3.2   |
| Claude | "A nephew carrying a lantern -- same as before (lighting the way for his uncle / business as usual)." | 5.0   |

"Wai sheng da deng long -- zhao jiu (jiu)" is a pun where "zhao jiu" (as before) sounds like "zhao jiu" (shining on the uncle). DeepL gives a literal translation that misses the point. Claude manages to preserve the literal image, the pun mechanism, and the actual meaning all at once.

### "Eat People" (L02) -- Style choices

| System | Key Word      | Score |
| ------ | ------------- | ----- |
| DeepL  | "cannibalism" | 4.0   |
| GPT    | "eat people"  | 5.0   |
| Gemini | "Eat people"  | 5.0   |
| Claude | "cannibalism" | 4.0   |

In Lu Xun's *A Madman's Diary*, "chi ren" (eat people) carries raw, direct shock value. GPT and Gemini use "eat people", which keeps that punch. DeepL and Claude use "cannibalism" -- semantically fine, but it sounds too clinical and loses the emotional impact.

### Rhetorical Parallelism (K09) -- Claude's restructuring

| System | Translation                                         | Score |
| ------ | --------------------------------------------------- | ----- |
| DeepL  | "Not very hurtful, but extremely insulting."        | 3.8   |
| GPT    | "Not very harmful, but extremely insulting."        | 3.8   |
| Gemini | "It's not that harmful, but it's highly insulting." | 3.8   |
| Claude | "The damage is minimal; the insult is devastating." | 5.0   |

"Shang hai xing bu gao, wu ru xing ji qiang" has a strong rhythmic and parallel structure. The first three systems roughly get the meaning across but the sentence feels flat. Claude restructures the expression to build contrast and punch in English, which better preserves the rhetorical effect.

---

## Error Type Distribution

| Error Type          | Count | Mainly From          | Typical Case                                              |
| ------------------- | ----- | -------------------- | --------------------------------------------------------- |
| Terminology Error   | 6     | Mostly DeepL         | A03: "irrelevant speech effect" mistranslated             |
| Cultural Loss       | 12    | DeepL > GPT > Gemini | K03: Pun mechanism lost in allegorical saying             |
| Register Shift      | 5     | All systems          | L02: "eat people" rendered as "cannibalism"               |
| Semantic Distortion | 3     | GPT / Claude         | Occasional over-interpretation in some sentences          |
| Metaphor Loss       | 3     | Mostly DeepL         | N06: "lang hua" (wave/splash) metaphor lost               |
| Information Add/Drop | 2    | Sporadic             | Minor additions or omissions in individual sentences      |

---

## Limitations

- Single evaluator -- future work should involve multiple raters and report inter-rater reliability.
- Small corpus (50 sentences) -- each text type only has 10 items.
- Chinese-to-English only -- other language pairs may show different patterns.
- System versions update constantly -- results reflect a snapshot from April 2025.
- Zero-prompt setup -- prompt engineering could change LLM performance significantly.

---

## Citation

If you use this data or reference this study, please cite:

   He chonglin. (2025). A Comparative Study of Chinese-to-English Machine Translation Quality
    Based on Multi-Dimensional Human Evaluation -- Taking DeepL, ChatGPT, Gemini, and Claude
    as Examples.University of Macau.

---

## License

This repository is for academic and research purposes. Please contact the author for any commercial use.
