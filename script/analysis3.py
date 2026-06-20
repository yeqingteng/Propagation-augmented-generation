'''
step 1(调用LLM得出结果)
'''
# import json
# from openai import OpenAI
# from tqdm import tqdm

# # ========== 用户需要自定义的参数 ==========
# API_KEY = "34dde694-1fef-45a3-97ce-b7b601cca48b"  
# BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"  # 例如 deepseek API
# MODEL_NAME = "deepseek-v3-250324"

# INPUT_FILE = "/root/autodl-tmp/shiyan/test111_fc_character_output.jsonl"         # 输入文件
# OUTPUT_FILE = "/root/autodl-tmp/shiyan/result.txt"  # 输出TXT文件

# # ========== 初始化 OpenAI 客户端 ==========
# client = OpenAI(
#     api_key=API_KEY,
#     base_url=BASE_URL
# )

# # ========== 主程序 ==========
# with open(INPUT_FILE, "r", encoding="utf-8") as f_in, \
#         open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:

#     for line in tqdm(f_in, desc="Processing"):
#         if not line.strip():
#             continue

#         data = json.loads(line)
#         text = data.get("text", "")
#         response_new = data.get("response_new", "")
#         depth = data.get("depth", "")
#         ratio = data.get("ratio", "")
#         width = data.get("width", "")
#         sw = data.get("sw", "")
#         credibility = data.get("credibility", "")
        
#         # ======== 构造 prompt ========
#         system_prompt = "You are a helpful assistant skilled at analyzing information."
#         user_prompt = f"""
#         你是一名负责信息真伪判断的分析员。现有一条信息，其字段如下：
#         - text: {text}
#         - depth（传播深度，1或0）: {depth}
#         - ratio（转发率，1高，0低）: {ratio}
#         - width（传播广度，1高，0低）: {width}
#         - sw（传播意愿，0~1）: {sw}
#         - credibility（可信度，0~1）: {credibility}
#         - 已知真实标签（response_new，1为真，0为假）: {response_new}

#         任务：
#         1. 根据你对这些字段在判断信息真假时的辅助价值的理解，给出这5个字段（depth、ratio、width、sw、credibility）在辅助判断中的重要性排序及其对应占比（从高到低）。
#         2. 同时，考虑这5个字段整体与text字段本身在判断信息真假时的作用占比（总和为1，例如：5个字段0.4，text字段0.6）。
#         3. 严格按照以下格式回答。例如：
#         Sort: ratio(0.3); width(0.25); depth(0.25); sw(0.15); credibility(0.05); Proportion: field(0.4); text(0.6)
#         """

#         try:
#             response = client.chat.completions.create(
#                 model=MODEL_NAME,
#                 messages=[
#                     {"role": "system", "content": system_prompt},
#                     {"role": "user", "content": user_prompt}
#                 ],
#                 temperature=0.0
#             )
#             reply = response.choices[0].message.content.strip()

#         except Exception as e:
#             reply = "Error: " + str(e)

#         # ======== 写入TXT ========
#         #f_out.write(f"ID: {data.get('id')}\n")
#         #f_out.write(f"Text: {text}\n")
#         f_out.write(f"Analysis: {reply}\n")
#         f_out.write("-" * 50 + "\n")

# print(f"✅ 处理完成，结果保存在: {OUTPUT_FILE}")

'''
step 2(转换)
'''
# import json
# import re

# def parse_data_block(block: str) -> dict:
#     """
#     解析每条数据，返回字典
#     """
#     block = block.strip()
#     result = {}

#     # ✅ 修改后的 Sort 正则：只匹配到 Proportion 之前
#     sort_match = re.search(r"Sort:\s*(.*?)(?=\s*Proportion:|$)", block)
#     if sort_match:
#         sort_str = sort_match.group(1)
#         result["Sort"] = [s.strip() for s in sort_str.split(";") if s.strip()]

#     # Proportion 部分保持不变
#     proportion_match = re.search(r"Proportion:\s*(.+)", block)
#     if proportion_match:
#         proportion_str = proportion_match.group(1)
#         proportions = {}
#         for item in proportion_str.split(";"):
#             item = item.strip()
#             if "(" in item and ")" in item:
#                 key = item.split("(")[0].strip()
#                 value = float(item[item.find("(")+1:item.find(")")])
#                 proportions[key] = value
#         result["Proportion"] = proportions

#     return result


# def txt_to_jsonl(txt_file: str, jsonl_file: str):
#     """
#     将txt中的数据转换为jsonl格式
#     """
#     with open(txt_file, "r", encoding="utf-8") as f:
#         content = f.read()

#     blocks = [b.strip() for b in content.split("--------------------------------------------------") if b.strip()]

#     with open(jsonl_file, "w", encoding="utf-8") as f:
#         for block in blocks:
#             data = parse_data_block(block)
#             f.write(json.dumps(data, ensure_ascii=False) + "\n")

#     print(f"已成功将 {txt_file} 转换为 {jsonl_file}")


# if __name__ == "__main__":
#     txt_to_jsonl(
#         "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/analysis3/result.txt",
#         "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/analysis3/result.jsonl"
#     )

'''
step 3(合并——为的是只看预测正确的结果)
'''
# import json

# def merge_jsonl(aaa_file: str, bbb_file: str, output_file: str):
#     with open(aaa_file, "r", encoding="utf-8") as f1, \
#          open(bbb_file, "r", encoding="utf-8") as f2, \
#          open(output_file, "w", encoding="utf-8") as out:

#         aaa_lines = f1.readlines()
#         bbb_lines = f2.readlines()

#         if len(aaa_lines) != len(bbb_lines):
#             print("警告：两个文件的行数不一致，将只合并最短的行数！")
        
#         for a_line, b_line in zip(aaa_lines, bbb_lines):
#             a_data = json.loads(a_line.strip())
#             b_data = json.loads(b_line.strip())
            
#             # 合并字典（bbb数据添加到aaa数据后面）
#             a_data.update(b_data)

#             out.write(json.dumps(a_data, ensure_ascii=False) + "\n")

#     print(f"合并完成，结果已保存到 {output_file}")


# if __name__ == "__main__":
#     merge_jsonl("C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/analysis3/test111_fc_character_output.jsonl", 
#                 "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/analysis3/result.jsonl", 
#                 "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/analysis3/combine_result.jsonl")


'''
step 4(计算两类占比)
'''
import re

def parse_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 用 "--------------------------------------------------" 分割每条数据
    entries = [e.strip() for e in content.split("--------------------------------------------------") if e.strip()]

    sort_sums = {"credibility": 0, "depth": 0, "ratio": 0, "width": 0, "sw": 0}
    proportion_sums = {"field": 0, "text": 0}

    sort_counts = 0
    proportion_counts = 0

    for entry in entries:
        # 解析 Sort 部分
        sort_match = re.search(r"Sort:\s*([^;]+(?:;\s*[^;]+)*)", entry)
        if sort_match:
            sort_str = sort_match.group(1)
            for key in sort_sums.keys():
                m = re.search(rf"{key}\(([\d.]+)\)", sort_str)
                if m:
                    sort_sums[key] += float(m.group(1))
            sort_counts += 1

        # 解析 Proportion 部分
        proportion_match = re.search(r"Proportion:\s*([^;]+(?:;\s*[^;]+)*)", entry)
        if proportion_match:
            proportion_str = proportion_match.group(1)
            for key in proportion_sums.keys():
                m = re.search(rf"{key}\(([\d.]+)\)", proportion_str)
                if m:
                    proportion_sums[key] += float(m.group(1))
            proportion_counts += 1

    # 计算平均值
    sort_avg = {k: v / sort_counts for k, v in sort_sums.items()}
    proportion_avg = {k: v / proportion_counts for k, v in proportion_sums.items()}

    # Sort 排名
    sort_ranking = sorted(sort_avg.items(), key=lambda x: x[1], reverse=True)

    return sort_avg, sort_ranking, proportion_avg


if __name__ == "__main__":
    file_path = "C:/Users/27433/Downloads/result.txt"  # 替换成你的txt文件路径
    sort_avg, sort_ranking, proportion_avg = parse_txt(file_path)

    print("=== Sort 平均占比 ===")
    for k, v in sort_avg.items():
        print(f"{k}: {v:.3f}")

    print("\n=== Sort 平均占比排名 ===")
    for i, (k, v) in enumerate(sort_ranking, 1):
        print(f"{i}. {k}: {v:.3f}")

    print("\n=== Proportion 平均占比 ===")
    for k, v in proportion_avg.items():
        print(f"{k}: {v:.3f}")

'''
单栏两个环形图(6个指标)
'''
# import matplotlib.pyplot as plt
# import numpy as np

# # 设置输出 PDF 路径
# output_path = 'C:/Users/27433/Desktop/contribution.pdf'

# # -----------------------
# # 数据设置
# # -----------------------
# # 左边环：Text vs Field
# text_ratio = 56
# field_ratio = 44

# # 右边环：Field 内部 6 个子字段占比
# fields = ['Credibility', 'Ratio', 'Breadth', 'Depth', 'Willingness', 'Emotion']
# field_ratios = [33, 19, 17, 13, 10, 8]

# # 配色
# left_colors = ['#6495ED', '#F98E52']  # Text蓝色，Field橙色
# right_colors = ['#E8603C', '#F98E52', '#FDBF6F', '#FEE499', '#FFF7BC', '#D0E6A5']  # 为 Emotion 添加颜色

# # -----------------------
# # 画布与子图布局
# # -----------------------
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.2))  # 单栏合适大小

# # -----------------------
# # 左边环：Text vs Field
# # -----------------------
# wedges1, _ = ax1.pie(
#     [text_ratio, field_ratio],
#     colors=left_colors,
#     startangle=90,
#     counterclock=False,
#     radius=1,
#     wedgeprops=dict(width=0.4, edgecolor='white')
# )

# # 在环形图上显示百分比
# for i, wedge in enumerate(wedges1):
#     ang = (wedge.theta2 + wedge.theta1) / 2
#     x = 0.7 * np.cos(np.deg2rad(ang))
#     y = 0.7 * np.sin(np.deg2rad(ang))
#     ax1.text(x, y, f'{[text_ratio, field_ratio][i]}%', ha='center', va='center',
#              color='black', fontsize=11, weight='bold')

# ax1.set_title('(a)Text vs Indicator', fontsize=13, weight='bold')
# ax1.axis('equal')

# # 图例放环形图中间
# ax1.legend(
#     wedges1, ['Text', 'Field'],
#     loc="center",
#     bbox_to_anchor=(0, 0, 1, 1),
#     fontsize=12
# )

# # -----------------------
# # 右边环：Field 内部 6 个子字段
# # -----------------------
# wedges2, _ = ax2.pie(
#     field_ratios,
#     colors=right_colors,
#     startangle=90,
#     counterclock=False,
#     radius=1,
#     wedgeprops=dict(width=0.4, edgecolor='white')
# )

# # 在环形图上显示百分比
# for i, wedge in enumerate(wedges2):
#     ang = (wedge.theta2 + wedge.theta1) / 2
#     x = 0.7 * np.cos(np.deg2rad(ang))
#     y = 0.7 * np.sin(np.deg2rad(ang))
#     ax2.text(x, y, f'{field_ratios[i]}%', ha='center', va='center',
#              color='black', fontsize=11, weight='bold')

# ax2.set_title('(b)Indicator Components', fontsize=13, weight='bold')
# ax2.axis('equal')

# # 图例放环形图中间
# ax2.legend(
#     wedges2, fields,
#     loc="center",
#     bbox_to_anchor=(0, 0, 1, 1),
#     # fontsize=8.5
#     fontsize=7
# )

# plt.tight_layout()
# plt.savefig(output_path, format='pdf', bbox_inches='tight')
# plt.show()