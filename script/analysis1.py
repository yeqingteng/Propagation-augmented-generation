# '''
# 将模型txt输出结果转换为json格式
# '''
# import json
# import re

# def convert_txt_to_json(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         content = f.read()

#     # 按块分割，每个 block 是由 ------------------- 分隔的
#     data_blocks = content.split('-------------------')

#     result = {}

#     for block_id, block in enumerate(data_blocks, start=1):  # 你例子从 id 1 开始
#         block = block.strip()
#         block_dict = {}

#         if not block:
#             result[str(block_id)] = block_dict
#             continue

#         lines = block.split('\n')
#         for line in lines:
#             line = line.strip()
#             if not line:
#                 continue

#             # 匹配 "character X": ...; Sharing Willingness: 0.8; Emotional Fluctuation: 0.7; Credibility: 0.9
#             match = re.match(
#                 r'^"character (\d+)":\s*(.+?);\s*Sharing Willingness: ([01](?:\.\d+)?);\s*Emotional Fluctuation: ([01](?:\.\d+)?);\s*Credibility: ([01](?:\.\d+)?)$',
#                 line
#             )

#             if not match:
#                 print(f"跳过无法匹配的行：{line}")
#                 continue  # 跳过格式不匹配的行

#             char_id = f"character {match.group(1)}"
#             receiver_raw = match.group(2).strip()
#             sharing = float(match.group(3))
#             emotion = float(match.group(4))
#             trust = float(match.group(5))

#             # 处理接收者
#             if receiver_raw == '"none"':
#                 receivers = ["none"]
#             else:
#                 receivers = re.findall(r'character \d+\([^)]+\)', receiver_raw)

#             block_dict[char_id] = {
#                 "receiver": receivers,
#                 "Sharing Willingness": sharing,
#                 "Emotional Fluctuation": emotion,
#                 "Credibility": trust
#             }

#         result[str(block_id)] = block_dict

#     # 写入 JSON 文件
#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump(result, f, indent=2, ensure_ascii=False)

#     print(f"转换完成，结果已保存到 {output_file}")

# # 示例用法
# input_filename = 'C:/Users/27433/Downloads/phemeplus_shiyan111_result.txt'
# output_filename = 'C:/Users/27433/Downloads/phemeplus_shiyan111_result.json'
# convert_txt_to_json(input_filename, output_filename)

# '''
# 处理id不连贯的现象: 不需要(weibo21和phemeplus不存在无法传播的情况)
# '''

# '''
# 根据原数据条目添加对应id
# '''
# import json

# def transform_json_keys(jsonl_file_path, json_file_path, output_file_path):
#     # 1. 读取 JSONL 文件的所有行，提取 id
#     jsonl_ids = []
#     with open(jsonl_file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             if line.strip():  # 跳过空行
#                 data = json.loads(line)
#                 jsonl_ids.append(str(data['id']))  # 提取 id 并转为字符串

#     # 2. 读取原始 JSON 文件
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#         original_json = json.load(f)

#     # 3. 取较小的条目数量
#     min_entries = min(len(jsonl_ids), len(original_json))
#     print(len(jsonl_ids), len(original_json))
#     print(f"按较少的条目数处理（共 {min_entries} 条）")

#     # 4. 构建新的 JSON 数据（替换键名）
#     new_json = {}
#     # 只遍历前 min_entries 条数据
#     for old_key, new_id in zip(list(original_json.keys())[:min_entries], jsonl_ids[:min_entries]):
#         new_json[new_id] = original_json[old_key]

#     # 5. 写入新的 JSON 文件
#     with open(output_file_path, 'w', encoding='utf-8') as f:
#         json.dump(new_json, f, indent=2, ensure_ascii=False)

# # 使用示例
# jsonl_file_path = 'C:/Users/27433/Desktop/phemeplus_shiyan111.jsonl'  # JSONL 文件路径
# json_file_path = 'C:/Users/27433/Downloads/phemeplus_shiyan111_result.json'    # JSON 文件路径
# output_file_path = 'C:/Users/27433/Downloads/phemeplus_shiyan111_result111.json' # 输出文件路径

# transform_json_keys(jsonl_file_path, json_file_path, output_file_path)

# '''
# json转换为jsonl
# '''
# import json

# def process_entry(entry_id, characters):
#     if not characters:
#         return {"id": entry_id, "need": 0}

#     num_characters = len(characters)
#     receiver_count = 0
#     non_none_receivers = 0
#     sharing_values = []
#     emotional_values = []
#     credibility_values = []

#     for character_data in characters.values():
#         receivers = character_data.get("receiver", [])
#         if receivers and receivers != ["none"]:
#             non_none_receivers += 1
#             receiver_count += len(receivers)  # 统计所有接收者的总数

#         sharing_values.append(character_data.get("Sharing Willingness", 0))
#         emotional_values.append(character_data.get("Emotional Fluctuation", 0))
#         credibility_values.append(character_data.get("Credibility", 0))

#     depth = 1 if non_none_receivers > 0 else 0
#     ratio_val = non_none_receivers / num_characters
#     width_new_val = receiver_count  # ✅ 直接使用接收者总数

#     def average(lst):
#         if not lst:
#             return 0.0
#         return round(sum(lst) / len(lst), 1)

#     return {
#         "id": entry_id,
#         "need": 1,
#         "depth": depth,
#         "ratio": round(ratio_val, 3),
#         "width_new": width_new_val,  # 直接输出整数或总数
#         "Sharing Willingness": average(sharing_values),
#         "Emotional Fluctuation": average(emotional_values),
#         "Credibility": average(credibility_values),
#     }

# def main():
#     input_path = "C:/Users/27433/Downloads/phemeplus_shiyan111_result.json"
#     output_path = "C:/Users/27433/Downloads/phemeplus_shiyan111_result.jsonl"

#     with open(input_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     with open(output_path, 'w', encoding='utf-8') as fout:
#         for entry_id, characters in data.items():
#             result = process_entry(entry_id, characters)
#             fout.write(json.dumps(result, ensure_ascii=False) + '\n')

# if __name__ == "__main__":
#     main()

# '''
# 将id从字符串转换为整数
# '''
# import json

# def convert_ids(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:

#         for line in infile:
#             try:
#                 data = json.loads(line.strip())
#                 # 将id从字符串转换为整数
#                 data['id'] = int(data['id'])
#                 # 写入新的JSONL文件
#                 outfile.write(json.dumps(data) + '\n')
#             except (json.JSONDecodeError, KeyError, ValueError) as e:
#                 print(f"处理行时出错: {line.strip()}, 错误: {e}")

# # 使用示例
# input_filename = 'C:/Users/27433/Downloads/phemeplus_shiyan111_result.jsonl'  # 替换为你的输入文件名
# output_filename = 'C:/Users/27433/Downloads/phemeplus_shiyan111_result111.jsonl'  # 替换为你想要的输出文件名
# convert_ids(input_filename, output_filename)

# '''
# 合并传播指标
# '''
# import json

# def merge_metrics(aaa_file, bbb_file, output_file):
#     # 需要合并的指标
#     metrics = ["ef", "width_new", "sw", "ratio", "credibility"]

#     # 读取 bbb.jsonl，构建 {id: {metric: value}} 映射
#     bbb_dict = {}
#     with open(bbb_file, 'r', encoding='utf-8') as f:
#         for line in f:
#             if not line.strip():
#                 continue
#             data = json.loads(line)
#             bbb_dict[data["id"]] = {metric: data.get(metric) for metric in metrics}

#     # 读取 aaa.jsonl，添加指标并写入新文件
#     with open(aaa_file, 'r', encoding='utf-8') as f_in, \
#          open(output_file, 'w', encoding='utf-8') as f_out:
#         for line in f_in:
#             if not line.strip():
#                 continue
#             data = json.loads(line)
#             metrics_values = bbb_dict.get(data["id"])
#             if metrics_values:
#                 for metric, value in metrics_values.items():
#                     if value is not None:
#                         data[metric] = value
#             f_out.write(json.dumps(data, ensure_ascii=False) + "\n")

#     print(f"合并完成，结果已保存到 {output_file}")

# # 调用示例
# merge_metrics(
#     "C:/Users/27433/Desktop/phemeplus_shiyan111.jsonl",
#     "C:/Users/27433/Downloads/phemeplus_shiyan111_result.jsonl",
#     "C:/Users/27433/Desktop/phemeplus_shiyan111_round1.jsonl"
# )

'''
计算指标均值
'''
import json

def compute_avg_by_label(jsonl_file):
    # 初始化数据结构
    labels = [5, 4, 3, 2, 1, 0]
    stats = {label: {"ef": [], "ratio": [], "width_new": [], "sw": [], "credibility": []} for label in labels}

    # 读取jsonl文件并分类存储
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            label = data.get("label")
            if label not in stats:
                continue  # 只统计0-5的标签

            # 只添加非空且非None的值
            for key in ["ef", "ratio", "width_new", "sw", "credibility"]:
                val = data.get(key)
                if val is not None:
                    stats[label][key].append(val)

    # 计算平均值
    avg_result = {}
    for label, values in stats.items():
        avg_result[label] = {
            key: (sum(v) / len(v) if v else 0)
            for key, v in values.items()
        }

    return avg_result

# ✅ 调用示例
if __name__ == "__main__":
    result = compute_avg_by_label(
        "C:/Users/27433/Desktop/analysis4/weibo21/第一轮/weibo21_shiyan_round1.jsonl")
    for label in sorted(result.keys(), reverse=True):
        avg = result[label]
        print(
            f"Label={label}: "
            f"ef={avg['ef']:.3f}, ratio={avg['ratio']:.3f}, "
            f"width_new={avg['width_new']:.3f}, sw={avg['sw']:.3f}, credibility={avg['credibility']:.3f}"
        )

# '''
# 为下一次传播做准备
# '''
# import json
# import re

# # 输入文件
# jsonl_file = "C:/Users/27433/Desktop/phemeplus_48.jsonl"       # 你的原始jsonl文件
# json_file = "C:/Users/27433/Desktop/phemeplus_shiyan_result.json"         # 你的json文件
# output_file = "C:/Users/27433/Desktop/phemeplus_shiyan.jsonl"     # 输出新jsonl文件

# # 读取json文件
# with open(json_file, "r", encoding="utf-8") as f:
#     json_data = json.load(f)

# # 定义一个正则表达式提取 "character 数字"
# receiver_pattern = re.compile(r"(character\s\d+)")

# def extract_receivers(data):
#     """从一个id的json数据中提取去重后的receiver编号列表"""
#     receivers_set = set()
#     for char_info in data.values():
#         receivers = char_info.get("receiver", [])
#         for r in receivers:
#             if r != "none":
#                 match = receiver_pattern.match(r)
#                 if match:
#                     receivers_set.add(match.group(1))
#     return sorted(receivers_set, key=lambda x: int(x.split()[1]))  # 按数字排序

# # 处理jsonl文件
# with open(jsonl_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
#     for line in fin:
#         if not line.strip():
#             continue
#         item = json.loads(line)
#         str_id = str(item["id"])

#         if str_id in json_data:
#             item["match"] = extract_receivers(json_data[str_id])
#         else:
#             item["match"] = []

#         fout.write(json.dumps(item, ensure_ascii=False) + "\n")

# print(f"处理完成！结果已保存至 {output_file}")

# '''
# 建立 {id: (sw, credibility)} 映射
# '''
# import json

# aaa_file = "C:/Users/27433/Desktop/phemeplus_shiyan.jsonl"
# bbb_file = "C:/Users/27433/Desktop/analysis4/phemeplus/第二轮/phemeplus_shiyan_result.jsonl"
# output_file = "C:/Users/27433/Desktop/phemeplus_shiyan111.jsonl"

# # 1. 读取 bbb.jsonl，建立 {id: (sw, credibility)} 映射
# bbb_data = {}
# with open(bbb_file, "r", encoding="utf-8") as f:
#     for line in f:
#         if not line.strip():
#             continue
#         data = json.loads(line)
#         bbb_data[data["id"]] = (data.get("sw"), data.get("credibility"))

# # 2. 读取 aaa.jsonl，修改 text 字段
# new_lines = []
# with open(aaa_file, "r", encoding="utf-8") as f:
#     for line in f:
#         if not line.strip():
#             continue
#         data = json.loads(line)
#         _id = data["id"]

#         if _id in bbb_data:
#             sw, credibility = bbb_data[_id]
#             original_text = data["text"]
#             data["text"] = f'{original_text}(sw: {sw}; credibility: {credibility})'

#         new_lines.append(data)

# # 3. 写入新的 jsonl 文件
# with open(output_file, "w", encoding="utf-8") as f:
#     for item in new_lines:
#         f.write(json.dumps(item, ensure_ascii=False) + "\n")

# print(f"处理完成，结果已保存到 {output_file}")