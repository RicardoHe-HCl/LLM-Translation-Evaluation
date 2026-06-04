# Test Case C: Entity Resolution & Parameter Overwriting (指代消解与参数覆写)

**🎯 Objective:** Evaluate the model's capacity for cross-turn entity resolution (pronoun matching) and parameter overwriting. The model must apply updated variables to the correct entity and use them for a comprehensive final analysis.
**📝 Setup:** Chen Hao (Programmer, 400k) and Liu Yang (Designer, 180k) are introduced. Turn 8 uses a pronoun ("the one going to Germany") requiring entity resolution. Turn 9 overwrites Chen Hao's salary to 550k pre-tax. Turn 10 asks for a final comparative analysis using the overwritten data.
**📊 Results Overview:** All models passed the entity resolution test. Gemini excelled in socio-cultural depth, analyzing the structural differences between tech and design migration policies. 

---

## 🗣️ User Prompt Script (10 Turns)

*   **Turn 1:** 我有两个朋友，一个叫陈浩，29岁，程序员，在深圳工作，年薪40万；另一个叫刘洋，28岁，设计师，在广州工作，年薪18万。
*   **Turn 2:** 陈浩最近买了一辆特斯拉，刘洋刚付了房子首付。
*   **Turn 3:** 你觉得当代年轻人应该优先买车还是买房？
*   **Turn 4:** 深圳和广州的生活成本有什么差别？
*   **Turn 5:** 程序员这个职业35岁之后发展空间怎么样？
*   **Turn 6:** 他们两个都想移居国外，陈浩倾向于去加拿大，另一个想去德国。
*   **Turn 7:** 这两个国家对技术移民的要求分别是什么？
*   **Turn 8 (Entity Linking):** 想去德国的那个，他的专业背景适合走哪种移民路径？
*   **Turn 9 (Parameter Overwriting):** 其实我刚才说错了，陈浩年薪不是40万，是税后40万，税前大概有55万。
*   **Turn 10 (Comprehensive Analysis):** 两个人里谁的经济条件更适合移民？他们各自的职业在目标国家需求怎么样？

---

## 🤖 Model Responses (Focus: Turn 10 Comparative Analysis)

### 🔹 Gemini (The Cultural Expert)
> **Response Excerpt:** "陈浩税前55万的收入非常耀眼，但他的经济条件更适合移民的前提是：他得愿意接受短期的阶层滑落... 刘洋虽然年薪18万，看似只有陈浩的1/3，但他反而是那个在经济上更适合、也更轻松启动移民的人... 德国的机会卡只需要大约1.25万欧元保证金。"
> **Analysis:** Successfully updated Chen Hao's salary to 550k and used it to deeply analyze the socio-economic "sunk cost" of migration. Provided exceptional localized insights.

### 🔹 ChatGPT / GPT-4o
> **Response Excerpt:** "陈浩税前55万大概对应高级开发工程师... 资金压力更小，抵御失业风险能力更强。如果刘洋仍然是设计师，年薪18万，那么两人的职业国际流动性差距会进一步拉大。"
> **Analysis:** Flawlessly applied the overwritten 550k salary to assess Chen Hao's global mobility compared to Liu Yang. 

### 🔹 Claude
> **Response Excerpt:** "年收入：税前55万 / 税后40万 (陈浩) vs 18万 (刘洋)... 陈浩收入差距约3倍... 经济适合度：更适合 (陈浩) vs 较困难 (刘洋)。"
> **Analysis:** Created a structured comparative table using the exact overwritten parameters. Highly precise and analytical, though slightly lacking the socio-cultural depth of Gemini.