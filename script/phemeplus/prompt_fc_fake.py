#System Prompt
SYSTEM_PROMPT = """You are an AI assistant specialized in analyzing sentences to determine the truth status of their content.
"""
#step 1
USER_PROMPT_TEMPLATE ="""
The following task is to determine the degree of truthfulness of a given <sentence>.

The following are some examples:
<Example 1>
The following is the <sentence> to analyze:
Breaking news: Over 1400 paintings worth millions found in Gurlitt's apartment! #art #Munich

Step-by-step:
True. This tweet refers to a real event where German art collector Cornelius Gurlitt was found to have hundreds of valuable artworks in his Munich apartment. This news was verified by multiple trusted sources and widely reported by mainstream media.
=> respond with 2

<Example 2>
The following is the <sentence> to analyze:
Putin hasn’t been seen in public in 10 days... is he sick? dead? removed? Kremlin silent. #PutinMissing

Step-by-step:
Unverified. During a 10-day period in 2015, Vladimir Putin was not seen in public, leading to widespread speculation online. However, there was no official confirmation regarding his status during that time, making this claim unverified.
=> respond with 1

<Example 3>
The following is the <sentence> to analyze:
Michael Essien has tested positive for Ebola, Ghana FA confirms. #EbolaEssien

Step-by-step:
False. This tweet falsely claimed that Ghanaian footballer Michael Essien had Ebola, which was quickly denied by Essien himself and Ghana Football Association. There were no credible reports confirming such diagnosis.
=> respond with 0

This is the <sentence> to determine: "{text}"

Let's think step by step!

If you think the degree of truthfulness of this <sentence> is true, you only need to respond with 2;
If you think the degree of truthfulness of this <sentence> is unverified, you only need to respond with 1;
If you think the degree of truthfulness of this <sentence> is false, you only need to respond with 0;
Note: DO NOT output your analysis results.
"""





