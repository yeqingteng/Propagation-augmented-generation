import json
from openai import OpenAI
from tqdm import tqdm
from prompt_sc_fake import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key="sk-LCtKcRnWo9259ra3LGUszdDpgleiKcFyOdzkRaXkwlTeQCxf",  # 替换为你的 API key
    base_url="https://api.kksj.org/v1"  # 自定义 base_url（如使用 deepseek API）
)

# 输入输出文件路径
input_file = "/root/autodl-tmp/shiyan/politifact.jsonl"
output_file = "/root/autodl-tmp/shiyan/politifact_sc_output.jsonl"

# 使用的模型名
MODEL_NAME = "deepseek-v3-0324"

# 创建/清空输出文件
with open(output_file, "w", encoding="utf-8") as f_out:
    pass

# 逐条处理输入数据
with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "a", encoding="utf-8") as f_out:
    for line in tqdm(f_in, desc="Processing"):
        data = json.loads(line)
        text = data.get("text", "")

        # 构建消息内容
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(
                text=text
            )}
        ]

        try:
            # 调用 OpenAI ChatCompletion 新 API
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.7,
                n=5
            )
            replies = [choice.message.content.strip() for choice in response.choices]

        except Exception as e:
            replies = "Error: " + str(e)

        # 保存结果
        data["response"] = replies
        f_out.write(json.dumps(data, ensure_ascii=False) + "\n")
