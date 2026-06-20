#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
Your task: Conduct a comprehensive analysis from both the content of the <sentence> and its dissemination status to determine the degree of truthfulness of a given <sentence>.

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

The fields that reflect the dissemination status of the <sentence> are <need>, <sw>, <credibility>, <ratio> and <width>. The following are the definitions of the relevant fields:
<need>: A value of 0 indicates that determining the degree of truthfulness of this <sentence> only requires examining the content of the <sentence> itself; a value of 1 indicates that, in addition to the <sentence> content, the <sw>, <credibility>, <ratio> and <width> fields also need to be considered when determining the degree of truthfulness of this <sentence>.
<ratio>: Reflect the dissemination rate of the <sentence> within the group. 1 indicates a higher dissemination rate (>=0.5), 0 indicates a lower dissemination rate (<0.5).
<width>: Indicates whether the <sentence> has been widely disseminated within the group. 1 means yes, 0 means no.
<sw>: Group Sharing Willingness.
<credibility>: The higher the score, the greater the likelihood that the <text content> is definitely true.

Generally speaking:
Statements that are partially true and partially false, or whose truth or falsehood is difficult to fully determine, are more likely to have higher <sw>, <ratio> and <width>.
Statements that are clearly true or false but contain important facts or are likely to produce significant positive or negative effects are likely to have higher <sw>, <ratio> and <width>.
Statements that are clearly true or false but lack important facts or significant impact may have lower <sw>, <ratio> and <width>.
Statements that are extremely absurd, or possibly intended to deceive, are clearly less likely to have lower <sw>, <ratio> and <width>.

During the analysis, the conclusions drawn from the content of the <sentence> and from its dissemination status may conflict. In such cases, you MUST to assess which source of conclusion is likely to be more reliable!!!

This is the <sentence> to determine: "{text}"
Related field:
<need>: "{need}"
<ratio>: "{ratio}"
<width>: "{width}"
<sw>: "{sw}"
<credibility>: "{credibility}"

Let's think step by step!

Based on the above analysis:
If you think the degree of truthfulness of this <sentence> is true, you only need to respond with 5;
If you think the degree of truthfulness of this <sentence> is mostly-true, you only need to respond with 4;
If you think the degree of truthfulness of this <sentence> is half-true, you only need to respond with 3;
If you think the degree of truthfulness of this <sentence> is mostly-false, you only need to respond with 2;
If you think the degree of truthfulness of this <sentence> is false, you only need to respond with 1;
If you think the degree of truthfulness of this <sentence> is pants-fire, you only need to respond with 0;
Note: DO NOT output your analysis results.
"""
