#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
The following task is to determine the degree of truthfulness of a given <sentence>.

The following are some examples:
<Example 1>
The following is the <sentence> to analyze:
"NASA says Earth is greener today than 20 years ago."

Step-by-step:
True.This statement is consistent with the satellite observation data released by NASA in 2019. The report pointed out that due to afforestation and agricultural activities in China and India, the Earth as a whole has become greener.
=> respond with 5

<Example 2>
The following is the <sentence> to analyze:
"Obamacare premiums are going up an average of over 100 percent."

Step-by-step:
Mostly-true.The increase in some areas was indeed very high, but the national average increase was far below 100%. The statement has some basis, but it is slightly exaggerated.
=> respond with 4

<Example 3>
The following is the <sentence> to analyze:
"Most terrorist attacks in the United States are committed by Muslims."

Step-by-step:
Half-true.FBI data shows that since 9/11, most of the attacks have not been carried out by Muslims. This statement ignores the overall statistical picture, but there are also some events that support it.
=> respond with 3

<Example 4>
The following is the <sentence> to analyze:
"The United States has the highest income tax rate in the world."

Step-by-step:
Mostly-false.Although corporate taxes in the United States were once high, personal income taxes in many countries are even higher, and the overall tax burden also varies. The statement is too absolute.
=> respond with 2

<Example 5>
The following is the <sentence> to analyze:
"Planned Parenthood sells baby parts."

Step-by-step:
False.Multiple investigations have found no evidence of the organization selling fetal tissues. This claim is based on misleading video editing.
=> respond with 1

<Example 6>
The following is the <sentence> to analyze:
"Texas is going to ban teaching the Civil Rights Movement."

Step-by-step:
Pants-fire.There is no legislation or policy to support this claim, which seriously distorts the discussions on state education issues.
=> respond with 0

This is the <sentence> to determine: "{text}"

Let's think step by step!

If you think the degree of truthfulness of this <sentence> is true, you only need to respond with 5;
If you think the degree of truthfulness of this <sentence> is mostly-true, you only need to respond with 4;
If you think the degree of truthfulness of this <sentence> is half-true, you only need to respond with 3;
If you think the degree of truthfulness of this <sentence> is mostly-false, you only need to respond with 2;
If you think the degree of truthfulness of this <sentence> is false, you only need to respond with 1;
If you think the degree of truthfulness of this <sentence> is pants-fire, you only need to respond with 0;
Note: DO NOT output your analysis results.
"""





