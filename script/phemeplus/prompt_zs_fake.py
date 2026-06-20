#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
The following task is to determine the degree of truthfulness of a given <sentence>.
This is the <sentence> to determine: "{text}"

If you think the degree of truthfulness of this <sentence> is true, you only need to respond with 2;
If you think the degree of truthfulness of this <sentence> is unverified, you only need to respond with 1;
If you think the degree of truthfulness of this <sentence> is false, you only need to respond with 0;
Note: DO NOT output your analysis results.
"""
