import json
from openai import OpenAI
from tqdm import tqdm
from prompt_tot_fake_character import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key="sk-jccicrulafivqunreohxlikmzyhepazugzufyvejzmkhogdc",  # 替换为你的 API key
    base_url="https://api.siliconflow.cn/v1"  # 自定义 base_url（如使用 deepseek API）
)

# 输入输出文件路径
input_file = "/root/autodl-tmp/shiyan/politifact/test111.jsonl"
output_file = "/root/autodl-tmp/shiyan/politifact/test111_tot_character_output.jsonl"

# 使用的模型名
MODEL_NAME = "Pro/deepseek-ai/DeepSeek-V3"

# 创建/清空输出文件
with open(output_file, "w", encoding="utf-8") as f_out:
    pass

# 逐条处理输入数据
with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "a", encoding="utf-8") as f_out:
    for line in tqdm(f_in, desc="Processing"):
        data = json.loads(line)
        text = data.get("text", "")
        need = data.get("need", "")
        ratio = data.get("ratio", "")
        width = data.get("width", "")
        sw = data.get("sw", "")
        #ef = data.get("ef", "")
        credibility = data.get("credibility", "")

        # 构建消息内容
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(
                text=text,
                need=need,
                ratio=ratio,
                width=width,
                sw = sw,
                #ef = ef,
                credibility = credibility
            )}
        ]

        try:
            # 调用 OpenAI ChatCompletion 新 API
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.0
            )
            reply = response.choices[0].message.content.strip()

        except Exception as e:
            reply = "Error: " + str(e)

        # 保存结果
        data["response_new"] = reply
        f_out.write(json.dumps(data, ensure_ascii=False) + "\n")
