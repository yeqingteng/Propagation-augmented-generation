#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
The following task is to determine the degree of truthfulness of a given <sentence>.

The following are some examples:
<Example 1>
The following is the <sentence> to analyze:
【太暖了!】杭州一位外卖小哥在送餐途中救下落水儿童, 耽误了订单还被顾客怒骂, 但网友都说: 你做得对!

Step-by-step:
True. This matches typical real-life "positive energy" content often seen on Weibo. Such stories are common in local news and tend to be true unless clearly exaggerated.
=> respond with 0

<Example 2>
The following is the <sentence> to analyze:
#健康提醒# 每天早上喝一杯84消毒液稀释水, 能彻底清除体内毒素, 预防癌症! 家人一定要试试!

Step-by-step:
False. This is clearly false and dangerous medical misinformation. 84 disinfectant is toxic when ingested and not supported by any medical evidence.
=> respond with 1

This is the <sentence> to determine: "{text}"

Let's think step by step!

If you think the degree of truthfulness of this <sentence> is true, you only need to respond with 0;
If you think the degree of truthfulness of this <sentence> is false, you only need to respond with 1;
Note: DO NOT output your analysis results.
"""





