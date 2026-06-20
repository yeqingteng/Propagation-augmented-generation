#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
The following task is to determine the degree of truthfulness of a given <sentence>.
This is the <sentence> to determine: "{text}"

Now start your Tree of Thought: 

Step 1: Interpretation
- What is the main claim in this <sentence>? Paraphrase it in your own words.

Step 2: Fact-Checking Paths (Think step by step)
- Consider at least 3 different aspects (branches) of the main claim:
    - A: Is this consistent with publicly known facts or verified data?
    - B: Does the main claim show signs of exaggeration or distortion?
    - C: Does the main claim use emotionally charged or misleading language?
- For each aspect, provide a short justification (1–2 sentences).

Step 3: Results Aggregation: 
- Based on the above branches, summarize the overall reliability of the <sentence>. Choose ONE of the following numerical labels:
    - 2 = True
    - 1 = unverified
    - 0 = False

Final Output:
Only respond with the final numerical labels (2 to 0) based on your judgment!
Note: DO NOT output your analysis results!
"""