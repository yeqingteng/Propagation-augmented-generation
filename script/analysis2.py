'''
总结reason(txt→txt)
'''
# import re
# from openai import OpenAI
# from tqdm import tqdm

# # 初始化 OpenAI 客户端
# client = OpenAI(
#     api_key="34dde694-1fef-45a3-97ce-b7b601cca48b",  # 替换为你的 API 密钥
#     base_url="https://ark.cn-beijing.volces.com/api/v3"  # 替换为你的 base_url（不带 /v1）
# )

# # 使用的模型名
# model_name = "deepseek-v3-250324"

# # 候选因素
# factors = [
#     "gender", "age", "education", "race", "area", "economic_status",
#     "belief", "political_leaning", "social_activity_level", "big_five_personality",
#     "cognition", "conformity", "curiosity", "occupation", "interests"
# ]

# # 构造提示词
# def make_prompt(reason_text):
#     return (
#         "你是一个内容分析师。请从下面的文本中，提取出最多三个最重要的因素，"
#         "按重要性排序，使用英文小写、用英文分号`;`分隔。\n\n"
#         "候选因素为：\n"
#         "gender, age, education, race, area, economic_status, belief, political_leaning, "
#         "social_activity_level, big_five_personality, cognition, conformity, curiosity, "
#         "occupation, interests\n\n"
#         f"文本如下：\n\"{reason_text}\"\n\n"
#         "只返回提取的因素，用英文分号隔开，不要解释或添加其他内容。"
#     )

# # 解析块中的数据项
# def parse_data_blocks(text):
#     blocks = text.strip().split('-------------------')
#     parsed_blocks = []

#     for block in blocks:
#         block = block.strip()
#         if not block:
#             continue

#         entries = re.findall(r'"character \d+": .*?; reason: ".*?"', block)
#         parsed_blocks.append(entries)

#     return parsed_blocks

# # 提取并浓缩 reason
# def simplify_reason(reason):
#     prompt = make_prompt(reason)
#     try:
#         response = client.chat.completions.create(
#             model=model_name,
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.0,
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"[Error] reason: {reason}\nException: {str(e)}\n")
#         return "error"

# # 处理并逐条写入文件
# def process_and_write(input_path, output_path):
#     with open(input_path, 'r', encoding='utf-8') as f:
#         raw_text = f.read()

#     parsed_blocks = parse_data_blocks(raw_text)

#     # 创建/覆盖输出文件，并开始逐条写入
#     with open(output_path, 'w', encoding='utf-8') as f_out:
#         for block in tqdm(parsed_blocks, desc="Processing blocks"):
#             for entry in block:
#                 match = re.match(r'("character \d+": .*?); reason: "(.*?)"', entry)
#                 if match:
#                     left_part = match.group(1)
#                     original_reason = match.group(2)
#                     new_reason = simplify_reason(original_reason)
#                     new_entry = f'{left_part}; reason: "{new_reason}"'
#                     f_out.write(new_entry + '\n')
#                 else:
#                     f_out.write(entry + '\n')  # 保留原始格式错误的数据
#             f_out.write('-------------------\n')  # 每个 block 之后插入分隔符

# # 执行
# if __name__ == "__main__":
#     process_and_write(
#         "/root/autodl-tmp/shiyan/results_phemeplus_round01_reason.txt",
#         "/root/autodl-tmp/shiyan/phemeplus111.txt"
#     )

'''
txt转换为两类jsonl
'''
# import json

# def process_txt_file(input_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         content = f.read()

#     # 按数据块分割
#     data_blocks = content.strip().split('-------------------')

#     # 创建输出文件并清空
#     with open('C:/Users/27433/Downloads/phemeplus_yes.jsonl', 'w', encoding='utf-8') as yes_file, \
#          open('C:/Users/27433/Downloads/phemeplus_none.jsonl', 'w', encoding='utf-8') as none_file:

#         for block in data_blocks:
#             lines = block.strip().split('\n')
#             for line in lines:
#                 line = line.strip()
#                 if not line:
#                     continue

#                 try:
#                     # 示例："character 105": "character 114(...)", ...; reason: "..."
#                     char_part, reason_part = line.split('; reason:')
#                     reason = reason_part.strip().strip('"')
                    
#                     char_id, connections = char_part.split(':', 1)
#                     char_id = char_id.strip().strip('"')
#                     connections = connections.strip().strip('"').lower()

#                     entry = {"id": char_id, "reason": reason}

#                     if connections == "none":
#                         none_file.write(json.dumps(entry, ensure_ascii=False) + "\n")
#                     else:
#                         yes_file.write(json.dumps(entry, ensure_ascii=False) + "\n")

#                 except ValueError:
#                     print(f"Skipping malformed line: {line}")
#                     continue

# # 调用函数，传入你的文件路径
# process_txt_file('C:/Users/27433/Downloads/phemeplus.txt')

'''
统计画图
'''
import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import os
import numpy as np

# 定义我们关心的类别
# CATEGORIES = [
#     "gender", "age", "education", "race", "area", "economic_status",
#     "belief", "political_leaning", "social_activity_level", "big_five_personality",
#     "curiosity", "occupation", "interests"
# ]

CATEGORIES = [
    "gender", "age", "education", "race", "area", "economic_status",
    "belief", "political_leaning", "big_five_personality", "occupation", "interests"
]

# 文件路径配置
JSONL_FILE_PATH = "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/analysis2/phemeplus.jsonl"
OUTPUT_DIR = "C:/Users/27433/Desktop/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_jsonl_file(file_path):
    stats = defaultdict(int)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                reasons = data.get("reason", "").split("; ")
                for reason in reasons:
                    reason = reason.strip().lower()
                    if reason in CATEGORIES:
                        stats[reason] += 1
            except json.JSONDecodeError:
                print(f"Error decoding line: {line}")
    return stats

def plot_pie_chart(top5, others_total):
    labels = [item[0] for item in top5]
    values = [item[1] for item in top5]

    if others_total > 0:
        labels.append("Other")
        values.append(others_total)

    colors = sns.color_palette("Set2", len(labels))

    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        values,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        pctdistance=0.85,
        wedgeprops=dict(width=0.4, edgecolor='w'),
        textprops=dict(size=14, weight='bold')  # 字号更大
    )

    plt.setp(autotexts, size=14, weight="bold", color="white")
    plt.title('Top 5 Categories and Other', fontsize=18, weight='bold', pad=20)
    plt.tight_layout()
    pie_path = os.path.join(OUTPUT_DIR, "phemeplus_pie.pdf")
    plt.savefig(pie_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"饼图已保存至: {pie_path}")

def plot_other_line_chart(others):
    if not others:
        print("没有其他类别，无需绘制折线图。")
        return

    labels = [item[0] for item in others]
    counts = [item[1] for item in others]
    total = sum(counts)
    percentages = [count / total * 100 for count in counts]  # ✅ 计算比例

    plt.figure(figsize=(14, 6))
    sns.set(style="whitegrid")
    sns.lineplot(x=labels, y=percentages, marker='o', linewidth=3.5, color='tab:blue')  # ✅ 更粗线条

    plt.xticks(rotation=45, ha='right', fontsize=12)  # ✅ 字体更大
    plt.yticks(fontsize=12)
    plt.title("Breakdown of 'Other' Categories (Percentage)", fontsize=18, weight='bold', pad=15)
    plt.xlabel("Category", fontsize=14)
    plt.ylabel("Percentage (%)", fontsize=14)

    for i, value in enumerate(percentages):
        plt.text(i, value + 0.5, f"{value:.1f}%", ha='center', fontsize=11, color='black')  # ✅ 百分比 + 字体更大

    plt.tight_layout()
    line_path = os.path.join(OUTPUT_DIR, "phemeplus_line.pdf")
    plt.savefig(line_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"折线图已保存至: {line_path}")

def plot_and_save_stats(stats):
    sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    top5 = sorted_stats[:5]
    others = sorted_stats[5:]
    others_total = sum(item[1] for item in others)

    plot_pie_chart(top5, others_total)
    plot_other_line_chart(others)

def main():
    stats = process_jsonl_file(JSONL_FILE_PATH)

    print("\n统计结果:")
    for category, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{category}: {count}")

    plot_and_save_stats(stats)

if __name__ == "__main__":
    main()