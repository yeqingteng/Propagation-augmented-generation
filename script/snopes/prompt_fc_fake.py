#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
The following task is to determine the degree of truthfulness of a given <sentence>.

The following are some examples:
<Example 1>
The following is the <sentence> to analyze:
The Affordable Care Act prohibits insurance companies from denying coverage due to pre-existing conditions.

Step-by-step:
True. One of the key provisions of the Affordable Care Act is that insurers cannot refuse coverage or charge higher premiums due to pre-existing medical conditions.
=> respond with 1

<Example 2>
The following is the <sentence> to analyze:
Drinking adequate water daily helps prevent kidney stones.

Step-by-step:
False. This claim is extremely dangerous and has been discredited by medical experts and health authorities worldwide. 
Ingesting bleach is toxic and offers no protection against COVID-19.
=> respond with 0

This is the <sentence> to determine: "{text}"

Let's think step by step!

If you think the degree of truthfulness of this <sentence> is true, you only need to respond with 1;
If you think the degree of truthfulness of this <sentence> is false, you only need to respond with 0;
Note: DO NOT output your analysis results.
"""





