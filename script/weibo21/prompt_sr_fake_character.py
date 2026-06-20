#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
Your task: Conduct a comprehensive analysis from both the content of the <sentence> and its dissemination status to determine the degree of truthfulness of a given <sentence>.

The fields that reflect the dissemination status of the <sentence> are <need>, <sw>, <cw>, <vw>, <er>, <ratio> and <width>. The following are the definitions of the relevant fields:
<need>: A value of 0 indicates that determining the degree of truthfulness of this <sentence> only requires examining the content of the <sentence> itself; a value of 1 indicates that, in addition to the <sentence> content, the <sw>, <cw>, <vw>, <er>, <ratio> and <width> fields also need to be considered when determining the degree of truthfulness of this <sentence>.
<ratio>: Reflect the dissemination rate of the <sentence> within the group. 1 indicates a higher dissemination rate (>=0.5), 0 indicates a lower dissemination rate (<0.5).
<width>: Indicates whether the <sentence> has been widely disseminated within the group. 1 means yes, 0 means no.
<sw>: Group Sharing Willingness. The value can be 1, 0, or null. When the value is null, <sw> can be omitted.
<cw>: The Commenting Willingness of a group. The value can be 1, 0, or null. When the value is null, <cw> can be omitted.
<vw>: The Verification Willingness of the group. The value can be 1, 0, or null. When the value is null, <vw> can be omitted.
<er>: The group's Emotional Reaction. The value can be 1, 0, or null. When the value is null, <er> can be omitted.

Generally speaking:
Statements that are true or false but contain important facts or are likely to produce significant positive or negative effects are likely to have higher <ratio>, <width>, <sw>, <cw>, <vw> and <er>, 
especially false information.
Statements that are true or false but lack important facts or significant impact may have lower <ratio>, <width>, <sw>, <cw>, <vw> and <er>.

During the analysis, the conclusions drawn from the content of the <sentence> and from its dissemination status may conflict. In such cases, you MUST assess which source of conclusion is likely to be more reliable.

This is the <sentence> to determine:
"{text}"

Related fields:
<need>: "{need}"
<ratio>: "{ratio}"
<width>: "{width}"
<sw>: "{sw}"
<cw>: "{cw}"
<vw>: "{vw}"
<er>: "{er}"

Now proceed in two steps:

Step 1: Initial Assessment
First, make an initial judgment based on your understanding of the sentence and the relevant fields. 
- Assign a preliminary truthfulness rating:
    - 1 = false
    - 0 = true
- Briefly explain your reasoning based on both content and dissemination status.

Step 2: Self-Refinement
Now carefully review your initial answer:
- Re-express your reasoning more clearly or more accurately, if needed.
- If you identify flaws or new insights in your reasoning, update your rating accordingly and explain the change.
- If your original judgment still appears to be correct, reaffirm it and briefly justify why no change is needed.

Final Output:
Only respond with the final rating number (1 to 0) based on your refined judgment.
Note: DO NOT output your analysis results.
"""
