#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
The following task is to determine the degree of truthfulness of a given <sentence>.
This is the <sentence> to determine: "{text}"

Step 1: Initial Assessment
First, make an initial judgment about the sentence's truthfulness.
- Choose one of the following levels:
    - 2 = true
    - 1 = unverified
    - 0 = false
- Briefly explain your reasoning.

Step 2: Self-Refinement
Now, carefully review your initial answer.
- Re-express your reasoning in a clearer or more accurate way, if needed.
- If you find any flaws, update your rating and explain why.
- If your original rating still seems best, confirm it with justification.

Final Output:
Only respond with the final rating number (2 to 0) based on your refined judgment.
Note: DO NOT output your analysis results.
"""





