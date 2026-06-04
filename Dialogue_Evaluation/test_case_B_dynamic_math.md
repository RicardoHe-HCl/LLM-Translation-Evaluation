# Test Case B: Dynamic Parameter Updating (动态变量追踪与多跳计算)

**🎯 Objective:** Evaluate the model's ability to track numerical variables over a long context, dynamically update them when conditions change, and retrieve the original baseline parameters without confusion.
**📝 Setup:** Turn 1-2 establish a baseline: 20 people, 1200 RMB rent, 50 RMB/person. Turn 5 introduces a change: 8 people drop out (12 left). Turn 8 asks to recalculate the break-even point. Turn 10 asks the model to retrieve the initial baseline data hidden behind layers of distractor text.
**📊 Results Overview:** 
All three models demonstrated exceptional mathematical reasoning and working memory, successfully distinguishing between initial and updated parameters.

---

## 🗣️ User Prompt Script (10 Turns)

*   **Turn 1:** 我最近在筹备一个小型读书会，计划3月15日在北京朝阳区举办，预计来20个人，场地租金一共1200元。
*   **Turn 2:** 我们打算读的第一本书是余华的《活着》，每人收50块钱场地费。
*   **Turn 3:** 你觉得读书会一般怎么组织比较好，流程上有什么建议？
*   **Turn 4:** 线上读书会和线下读书会各有什么优缺点？
*   **Turn 5 (Parameter Update):** 对了，后来有8个人临时说来不了，所以人数变成12个人了。
*   **Turn 6:** 《活着》这本书你怎么评价？
*   **Turn 7:** 余华还有哪些值得读的作品？
*   **Turn 8 (Dynamic Math):** 现在场地费应该每人收多少才能刚好覆盖成本？
*   **Turn 9:** 如果我想把这个读书会做成长期活动，每个月办一次，有什么需要注意的？
*   **Turn 10 (Original Memory Retrieval):** 你还记得我们这次活动定在哪一天、哪个区吗？场地费最开始定的是多少？

---

## 🤖 Model Responses (Focus: Turn 8 & Turn 10)

### 🔹 ChatGPT / GPT-4o
> **Turn 8 Excerpt:** "这意味着场地成本实际上变成了：1200 ÷ 12 = 100元/人。而目前只收了 50 元/人。"
> **Turn 10 Excerpt:** "活动时间：3月15日。活动地点：北京的朝阳区。最开始确定的场地费：1200元（场地总租金），每人原计划收取50元场地费。"
> **Analysis:** Perfect extraction and calculation.

### 🔹 Gemini
> **Turn 8 Excerpt:** "因为活动人数从20人变成了12人，在总租金1200元不变的前提下...每人需要收取的费用为：100元。"
> **Turn 10 Excerpt:** "当然记得。这次读书会计划在3月15日举办，地点定在北京的朝阳区。至于场地费，最开始定的是每人50元。"
> **Analysis:** Perfect memory retrieval, paired with highly empathetic advice on how to communicate the price hike to participants.

### 🔹 Claude
> **Turn 8 Excerpt:** "计算很简单：场地租金 ÷ 参与人数 = 每人费用。1200元 ÷ 12人 = 100元/人。所以应该每人收100元，才能刚好覆盖1200元的场地成本。"
> **Turn 10 Excerpt:** "记得清楚：日期：3月15日。地点：北京朝阳区。场地费：1200元...每人原计划收50元。"
> **Analysis:** Direct, flawless logical tracking.