'''
去掉reason部分
'''

'''
将模型txt输出结果转换为json格式
'''
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
# input_filename = 'C:/Users/27433/Downloads/results_snopes_round01.txt'
# output_filename = 'C:/Users/27433/Downloads/results_snopes_round01.json'
# convert_txt_to_json(input_filename, output_filename)

'''
处理id不连贯的现象: 暂不需要
'''

'''
根据原数据条目添加对应id
'''
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
# jsonl_file_path = 'C:/Users/27433/Desktop/test.jsonl'  # JSONL 文件路径
# json_file_path = 'C:/Users/27433/Downloads/results_snopes_round01.json'    # JSON 文件路径
# output_file_path = 'C:/Users/27433/Downloads/results_snopes_round01111.json' # 输出文件路径

# transform_json_keys(jsonl_file_path, json_file_path, output_file_path)

'''
计算ratio和width和depth和新加入的4个指标(新加入的4个指标取平均)
'''
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
#             receiver_count += len(receivers)

#         sharing_values.append(character_data.get("Sharing Willingness", 0))
#         emotional_values.append(character_data.get("Emotional Fluctuation", 0))
#         credibility_values.append(character_data.get("Credibility", 0))

#     depth = 1 if non_none_receivers > 0 else 0
#     ratio_val = non_none_receivers / num_characters
#     ratio = 1 if ratio_val >= 0.5 else 0
#     width_val = receiver_count / num_characters
#     width = 1 if width_val >= 0.5 else 0

#     def average(lst):
#         if not lst:
#             return 0.0
#         return round(sum(lst) / len(lst), 1)

#     return {
#         "id": entry_id,
#         "need": 1,
#         "depth": depth,
#         "ratio": ratio,
#         "width": width,
#         "Sharing Willingness": average(sharing_values),
#         "Emotional Fluctuation": average(emotional_values),
#         "Credibility": average(credibility_values),
#     }

# def main():
#     input_path = "C:/Users/27433/Downloads/results_snopes_round01.json"    # 替换为你的输入文件路径
#     output_path = "C:/Users/27433/Downloads/results_snopes_round01.jsonl" # 输出文件路径

#     with open(input_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     with open(output_path, 'w', encoding='utf-8') as fout:
#         for entry_id, characters in data.items():
#             result = process_entry(entry_id, characters)
#             fout.write(json.dumps(result, ensure_ascii=False) + '\n')

# if __name__ == "__main__":
#     main()

'''
字符串转为整数(pubhealth不需要)
'''
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
# input_filename = 'C:/Users/27433/Downloads/results_snopes_round01.jsonl'  # 替换为你的输入文件名
# output_filename = 'C:/Users/27433/Downloads/results_snopes_round01111.jsonl'  # 替换为你想要的输出文件名
# convert_ids(input_filename, output_filename)

'''
添加指标到原始文件(添加7个)
'''
import json

def merge_jsonl(aaa_path, bbb_path, output_path):
    # 1. 先读取 bbb.jsonl，构建 id 到数据的映射
    id_to_extra = {}
    with open(bbb_path, 'r', encoding='utf-8') as bbb_file:
        for line in bbb_file:
            obj = json.loads(line)
            id_to_extra[obj["id"]] = {
                "need": obj.get("need"),
                "depth": obj.get("depth"),
                "ratio": obj.get("ratio"),
                "width": obj.get("width"),
                "sw": obj.get("sw"),
                "ef": obj.get("ef"),
                "credibility": obj.get("credibility")
            }

    # 2. 处理 aaa.jsonl，合并字段
    with open(aaa_path, 'r', encoding='utf-8') as aaa_file, \
         open(output_path, 'w', encoding='utf-8') as out_file:

        for line in aaa_file:
            obj = json.loads(line)
            match = id_to_extra.get(obj["id"])
            if match:
                obj.update(match)
            out_file.write(json.dumps(obj, ensure_ascii=False) + '\n')

# 替换为你的实际路径
merge_jsonl("C:/Users/27433/Desktop/test.jsonl", 
            "C:/Users/27433/Downloads/results_snopes_round01.jsonl", 
            "C:/Users/27433/Downloads/test111.jsonl")

