'''
去掉reason部分
'''
# def process_data(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f_in, \
#          open(output_file, 'w', encoding='utf-8') as f_out:
        
#         for line in f_in:
#             # 保留分隔线
#             if line.strip() == '-------------------':
#                 f_out.write(line)
#                 continue
            
#             # 处理非空行
#             if line.strip():
#                 # 移除reason部分
#                 if '; reason:' in line:
#                     processed_line = line.split('; reason:')[0] + '\n'
#                     f_out.write(processed_line)
#                 else:
#                     f_out.write(line)
#             else:
#                 f_out.write(line)

# # 使用示例
# input_filename = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23_reason.txt'  # 你的输入文件名
# output_filename = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23.txt'  # 输出文件名
# process_data(input_filename, output_filename)


'''
将模型txt输出结果转换为json格式
'''
# import json
# import re

# def convert_txt_to_json(input_file, output_file):
#     # 读取输入文件
#     with open(input_file, 'r', encoding='utf-8') as f:
#         content = f.read()
    
#     # 分割不同的数据块（假设由"-------------------"分隔）
#     data_blocks = content.split('-------------------')
    
#     result = {}
    
#     for block_id, block in enumerate(data_blocks, start=1):
#         block = block.strip()
#         if not block:
#             continue
            
#         block_dict = {}
        
#         # 使用正则表达式匹配每一行
#         for line in block.split('\n'):
#             line = line.strip()
#             if not line:
#                 continue
                
#             # 匹配键和值
#             match = re.match(r'^"(.+?)":\s*"(.+?)"$', line)
#             if not match:
#                 continue
                
#             key = match.group(1)
#             value = match.group(2)
            
#             # 处理"none"和多个character的情况
#             if value == "none":
#                 block_dict[key] = "none"
#             else:
#                 # 分割多个character
#                 characters = [c.strip() for c in value.split('", "')]
#                 # 清理每个character字符串
#                 characters = [c.replace('"', '') for c in characters]
#                 block_dict[key] = characters
        
#         # 添加到结果中，使用"id"作为键
#         result[f"id {block_id}"] = block_dict
    
#     # 写入输出JSON文件
#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump(result, f, indent=2, ensure_ascii=False)

# # 使用示例
# input_filename = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23.txt'  # 替换为你的输入文件名
# output_filename = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23.json'  # 替换为你想要的输出文件名

# convert_txt_to_json(input_filename, output_filename)
# print(f"转换完成，结果已保存到 {output_filename}")

'''
处理id不连贯的现象
'''
# import json
# import re

# def complete_missing_ids(input_file, output_file):
#     # 读取原始JSON文件
#     with open(input_file, 'r', encoding='utf-8') as f:
#         data = json.load(f)
    
#     # 提取所有ID并转换为数字
#     ids = []
#     for key in data.keys():
#         match = re.match(r'id (\d+)', key)
#         if match:
#             ids.append(int(match.group(1)))
    
#     if not ids:
#         return  # 如果没有ID，直接返回
    
#     # 找出最小和最大ID
#     min_id = min(ids)
#     max_id = max(ids)
    
#     # 创建新的完整数据
#     complete_data = {}
#     for i in range(min_id, max_id + 1):
#         key = f'id {i}'
#         complete_data[key] = data.get(key, {})
    
#     # 写入新的JSON文件
#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump(complete_data, f, indent=2, ensure_ascii=False)

# # 使用示例
# input_json = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23.json'  # 替换为你的输入文件路径
# output_json = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23111.json'  # 替换为你想要的输出文件路径

# complete_missing_ids(input_json, output_json)
# print(f"处理完成，结果已保存到 {output_json}")

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
# jsonl_file_path = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/test.jsonl'  # JSONL 文件路径
# json_file_path = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23111.json'    # JSON 文件路径
# output_file_path = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23222.json' # 输出文件路径

# transform_json_keys(jsonl_file_path, json_file_path, output_file_path)

'''
计算ratio和width
'''
# import json

# # 输入和输出文件路径
# input_file = 'C:/Users/27433/Downloads/results_pubhealth.json'
# output_file = 'C:/Users/27433/Downloads/results_pubhealth.jsonl'

# def process_entry(entry_id, entry_data):
#     if not entry_data:
#         return {"id": entry_id, "need": 0}

#     total_characters = len(entry_data)
#     spreaders = 0
#     spread_targets = set()

#     for sender, targets in entry_data.items():
#         if isinstance(targets, list) and targets:
#             spreaders += 1
#             for target in targets:
#                 # 提取 "character xxx" 格式部分
#                 target_id = target.split('(')[0].strip()
#                 spread_targets.add(target_id)

#     spread_rate = spreaders / total_characters if total_characters > 0 else 0
#     spread_width = len(spread_targets) / total_characters if total_characters > 0 else 0

#     return {
#         "id": entry_id,
#         "need": 1,
#         "ratio": 1 if spread_rate >= 0.5 else 0,
#         "width": 1 if spread_width >= 0.5 else 0
#     }

# def main():
#     # 加载 JSON 数据
#     with open(input_file, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     # 处理并写入 jsonl
#     with open(output_file, 'w', encoding='utf-8') as f_out:
#         for entry_id, entry_data in data.items():
#             result = process_entry(entry_id, entry_data)
#             f_out.write(json.dumps(result, ensure_ascii=False) + '\n')

# if __name__ == '__main__':
#     main()

'''
id字段内容格式转换
'''
# import json

# def convert_id_to_int(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:
        
#         for line in infile:
#             try:
#                 # 解析JSON数据
#                 data = json.loads(line.strip())
                
#                 # 将id从字符串转换为整数
#                 if 'id' in data and isinstance(data['id'], str):
#                     data['id'] = int(data['id'])
                
#                 # 写入处理后的数据到新文件
#                 outfile.write(json.dumps(data) + '\n')
#             except json.JSONDecodeError as e:
#                 print(f"解析JSON时出错: {e}, 行内容: {line}")
#             except ValueError as e:
#                 print(f"转换id为整数时出错: {e}, id值: {data.get('id')}")
#             except Exception as e:
#                 print(f"处理时发生意外错误: {e}")

# # 使用示例
# input_filename = 'C:/Users/27433/Downloads/results_pubhealth.jsonl'  # 替换为你的输入文件名
# output_filename = 'C:/Users/27433/Downloads/results_pubhealth111.jsonl'  # 替换为你想要的输出文件名

# convert_id_to_int(input_filename, output_filename)
# print(f"处理完成，结果已保存到 {output_filename}")


'''
添加need,ratio和width
'''
# import json

# def merge_jsonl_files(aaa_file, bbb_file, output_file):
#     # 读取bbb.jsonl文件，建立id到数据的映射
#     bbb_data = {}
#     with open(bbb_file, 'r', encoding='utf-8') as f:
#         for line in f:
#             item = json.loads(line)
#             bbb_data[item['id']] = item
    
#     # 处理aaa.jsonl文件并添加字段
#     merged_data = []
#     with open(aaa_file, 'r', encoding='utf-8') as f:
#         for line in f:
#             item = json.loads(line)
#             item_id = item['id']
            
#             # 从bbb数据中获取对应id的字段
#             if item_id in bbb_data:
#                 bbb_item = bbb_data[item_id]
#                 item['need'] = bbb_item.get('need', None)
#                 item['ratio'] = bbb_item.get('ratio', None)
#                 item['width'] = bbb_item.get('width', None)
#             else:
#                 # 如果没有找到对应id，可以设置默认值或保留原样
#                 item['need'] = None
#                 item['ratio'] = None
#                 item['width'] = None
            
#             merged_data.append(item)
    
#     # 将合并后的数据写入新文件
#     with open(output_file, 'w', encoding='utf-8') as f:
#         for item in merged_data:
#             f.write(json.dumps(item) + '\n')

# # 使用示例
# aaa_file = 'C:/Users/27433/Desktop/politifact_sc_output.jsonl'
# bbb_file = 'C:/Users/27433/Desktop/results_politifact.jsonl'
# output_file = 'C:/Users/27433/Desktop/politifact_sc_character.jsonl'

# merge_jsonl_files(aaa_file, bbb_file, output_file)
# print(f"合并完成，结果已保存到 {output_file}")

'''
//////////////////////////////////////////////////////////////////////////////////////////////
'''

'''
添加社交活跃度
'''
# import json

# def process_round_data(round_data, character_data):
#     processed_data = {}
    
#     for round_id, round_info in round_data.items():
#         processed_round = {}
        
#         for character_key, value in round_info.items():
#             if value == "none":
#                 processed_round[character_key] = "none"
#             else:
#                 # Process the list of relationships
#                 processed_relationships = []
#                 for relationship_str in value:
#                     # Extract character ID and relationship info
#                     char_id = relationship_str.split('(')[0]
#                     relationship_info = relationship_str.split('(')[1].rstrip(')')
                    
#                     # Get social activity level from character data
#                     if char_id in character_data:
#                         social_activity = character_data[char_id]["social_activity_level"]
#                         new_relationship_str = f"{char_id}({relationship_info}; social_activity_level: {social_activity})"
#                         processed_relationships.append(new_relationship_str)
#                     else:
#                         # If character not found, keep original
#                         processed_relationships.append(relationship_str)
                
#                 processed_round[character_key] = processed_relationships
        
#         processed_data[round_id] = processed_round
    
#     return processed_data

# def main():
#     # Load the round.json file
#     with open('C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23.json', 'r') as f:
#         round_data = json.load(f)
    
#     # Load the character.json file
#     with open('C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/characters_weibo21.json', 'r') as f:
#         character_data = json.load(f)
    
#     # Process the data
#     processed_data = process_round_data(round_data, character_data)
    
#     # Save the processed data to a new file
#     with open('C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23111.json', 'w') as f:
#         json.dump(processed_data, f, indent=2)
    
#     print("Processing complete")

# if __name__ == "__main__":
#     main()

'''
先去除不合理的情况再进行筛选: round2_3传完后, 主持人要去除对round1的回传现象和对round2的横传现象
代码实现:
根据 jsonl 文件中每条消息的 match 字典, 清理原始 JSON 文件中的“传播对象”列表
移除其中已经出现在 match 字典中的角色, 保留未出现在 match 字典中的传播对象
'''
# 去除对round1的回传现象和对round2的横传现象
# import json

# def process_files(json_file_path, jsonl_file_path, output_json_file_path):
#     # 读取 JSON 文件
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
    
#     # 创建 ID 到 match 字典的映射
#     id_to_match = {}
#     with open(jsonl_file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             entry = json.loads(line)
#             id_to_match[entry['id']] = entry.get('match', {})  # match 是字典
    
#     # 遍历每条数据
#     for id_key in data:
#         match_dict = id_to_match.get(id_key, {})  # match_dict 是 dict: {"character XXX": value}
        
#         for character_key in data[id_key]:
#             propagation_targets = data[id_key][character_key]

#             if propagation_targets == "none":
#                 continue
            
#             new_targets = []
#             for target in propagation_targets:
#                 target_character = target.split('(')[0].strip()  # e.g., "character 101"
                
#                 if target_character not in match_dict:
#                     new_targets.append(target)
            
#             if new_targets:
#                 data[id_key][character_key] = new_targets
#             else:
#                 data[id_key][character_key] = "none"
    
#     # 写入处理后的 JSON 文件
#     with open(output_json_file_path, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=2)

# # 使用示例
# json_file_path = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23.json'         # 原始 JSON 数据
# jsonl_file_path = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/test_round2_num.jsonl'       # 改为字典形式 match 的 JSONL 数据
# output_json_file_path = 'C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23111.json' # 处理后的输出文件

# process_files(json_file_path, jsonl_file_path, output_json_file_path)


'''
Step 1: 对于传播对象> 3个的情况: 先按传播概率公式进行筛选 (倾向性 + 活跃度 + 衰减); 然后增强传播概率=原始传播概率×(1+α⋅log(接收次数))
其中 α 是调节因子(例如 0.3 或 0.5), log 有助于在次数增长时平滑增长
这样可以兼顾: 传播次数的正相关性; 概率模型的细粒度调整; 避免全保留(全部通过Step1)造成的噪声扩散

Step 2: (针对筛选后仍 > 3个传播对象的情况)每人最多保留 3 个传播对象, 按以下剪枝规则执行

若没有 weak ties: 随机剪掉 Strong/Moderate ties, 直到总数 ≤ 3
若只有 1 个 weak ties 传播对象: 保留该 weak tie; 随机剪掉 Strong/Moderate ties, 直到总数 ≤ 3
若有多个 weak ties: 随机保留 1 个 weak tie, 剪掉其余 weak ties; 若剪掉其余 weak ties后总数仍 > 3, 再随机剪 Strong/Moderate ties, 直到总数 ≤ 3
'''
import json
import math
import random

# ========= 配置 =========
input_json_filename  = "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23.json"  # 改成你的路径
input_jsonl_filename = "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/test_round2_num.jsonl"  # 改成你的路径
output_filename      = "C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/weibo21/v3/第三轮传播后/results_weibo21_round23111.json" # 改成你的路径

decay_k = 0.25
depth   = 3
alpha   = 0.3  # 增强调节因子

# ========= 参数 =========
base_relation_bias = {'Strong': 1.00, 'Moderate': 0.85, 'Weak': 0.65}
activity_bias = {'high': 1.00, 'medium': 0.85, 'low': 0.65}

# ========= 工具函数 =========

def decay(d, k=decay_k):
    return math.exp(-k * d)

def add_perturbation(value, epsilon=0.02):
    return max(0.0, min(1.0, value + random.uniform(-epsilon, epsilon)))

def compute_probability(relation, activity, depth=3):
    relation_val = add_perturbation(base_relation_bias[relation])
    activity_val = activity_bias[activity]
    decay_val    = decay(depth)
    return relation_val * activity_val * decay_val

def compute_boosted_probability(relation, activity, depth, receive_count, alpha=0.3):
    base_prob = compute_probability(relation, activity, depth)
    boost = 1 + alpha * math.log(receive_count) if receive_count > 0 else 1
    return min(base_prob * boost, 1.0)

def extract_relation_type(target_string):
    if 'Strong Ties' in target_string: return 'Strong'
    if 'Moderate Ties' in target_string: return 'Moderate'
    if 'Weak Ties' in target_string: return 'Weak'
    return 'Weak'

def extract_activity_level(target_string):
    if 'social_activity_level: high' in target_string: return 'high'
    if 'social_activity_level: medium' in target_string: return 'medium'
    if 'social_activity_level: low' in target_string: return 'low'
    return 'medium'

# ========= Step 1（仅对传播对象 >3 的角色做筛选）=========

def process_spread_with_boost_limited(raw_data, receive_counts, depth=3, alpha=0.3):
    result = {}
    for claim_id, characters in raw_data.items():
        result[claim_id] = {}
        for char_id, targets in characters.items():
            if targets == "none":
                result[claim_id][char_id] = []
                continue

            if len(targets) <= 3:
                result[claim_id][char_id] = targets[:]
                continue

            char_receive_count = receive_counts.get(claim_id, {}).get(char_id, 1)
            selected_targets = []
            for target in targets:
                relation = extract_relation_type(target)
                activity = extract_activity_level(target)
                prob = compute_boosted_probability(relation, activity, depth, char_receive_count, alpha)
                if random.random() < prob:
                    selected_targets.append(target)

            result[claim_id][char_id] = selected_targets
    return result

# ========= Step 2：剪枝规则 =========

def prune_targets(targets, max_targets=3):
    if len(targets) <= max_targets:
        return targets[:]

    weak_ties = [t for t in targets if 'Weak Ties' in t]
    strong_mod_ties = [t for t in targets if 'Strong Ties' in t or 'Moderate Ties' in t]
    final_targets = []

    if len(weak_ties) == 0:
        final_targets.extend(random.sample(strong_mod_ties, min(max_targets, len(strong_mod_ties))))
    elif len(weak_ties) == 1:
        final_targets.append(weak_ties[0])
        remaining = max_targets - 1
        final_targets.extend(random.sample(strong_mod_ties, min(remaining, len(strong_mod_ties))))
    else:
        keep_weak = random.choice(weak_ties)
        final_targets.append(keep_weak)
        remaining = max_targets - 1
        final_targets.extend(random.sample(strong_mod_ties, min(remaining, len(strong_mod_ties))))

    return final_targets

def apply_pruning(filtered_data, max_targets=3):
    for claim_id, characters in filtered_data.items():
        for char_id, targets in characters.items():
            if len(targets) > max_targets:
                filtered_data[claim_id][char_id] = prune_targets(targets, max_targets)
    return filtered_data

# ========= 提取每个角色的接收次数 =========

def extract_receive_counts_from_jsonl(jsonl_filename):
    receive_counts = {}
    with open(jsonl_filename, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            claim_id = data["id"]
            receive_counts.setdefault(claim_id, {})
            for char, count in data.get("match", {}).items():
                receive_counts[claim_id][char.replace("character ", "")] = count
    return receive_counts

# ========= 主流程 =========

def main():
    with open(input_json_filename, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    receive_counts = extract_receive_counts_from_jsonl(input_jsonl_filename)

    # Step 1：增强概率筛选，仅限传播对象 >3 的角色
    step1_result = process_spread_with_boost_limited(raw_data, receive_counts, depth, alpha)

    # Step 2：剪枝规则
    final_result = apply_pruning(step1_result, max_targets=3)

    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(final_result, f, indent=2, ensure_ascii=False)

    print(f"处理完成，结果已保存至：{output_filename}")

if __name__ == "__main__":
    main()

'''
开始准备下一次传播
'''
'''
根据某条信息的传播结果考虑以下情况:
如果某个人被传了多次(同一个人接收到来自多个好友的消息是可能的), 则可能会增加对这条消息的重视, 下一轮这个人对自身关系的传播倾向会上升
'''
# import json
# from collections import defaultdict

# def find_frequent_recommendations_per_id(json_file_path, output_file_path):
#     # 读取JSON文件
#     with open(json_file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
    
#     # 创建结果字典 {id: {被推荐≥2次的character: 次数}}
#     results = {}
    
#     # 遍历每个ID及其数据
#     for id_key, id_data in data.items():
#         # 为当前ID创建统计字典
#         char_counts = defaultdict(int)
        
#         # 统计当前ID下的所有推荐
#         for value in id_data.values():
#             if isinstance(value, list):  # 处理列表类型的推荐
#                 for recommendation in value:
#                     char_id = recommendation.split('(')[0].split(' ')[1]
#                     char_counts[char_id] += 1
#             elif isinstance(value, str) and value != "none":  # 处理单个推荐
#                 char_id = value.split('(')[0].split(' ')[1]
#                 char_counts[char_id] += 1
        
#         # 筛选当前ID下被推荐≥2次的character及其次数
#         frequent_chars = {char: count for char, count in char_counts.items() if count >= 2}
#         if frequent_chars:
#             results[id_key] = frequent_chars
    
#     # 将结果写入txt文件
#     with open(output_file_path, 'w', encoding='utf-8') as file:
#         if results:
#             file.write("各ID中被多次推荐的character及重复次数：\n\n")
#             for id_key, chars in results.items():
#                 file.write(f"{id_key}:\n")
#                 for char, count in chars.items():
#                     file.write(f"  character {char}: {count}\n")
#                 file.write("\n")
#         else:
#             file.write("没有找到任何被多次推荐的character。\n")
    
#     print(f"分析完成，结果已保存到 {output_file_path}")

# # 使用示例
# find_frequent_recommendations_per_id('C:/Users/27433/Desktop/2016_3_round3.json', 
#                                      'C:/Users/27433/Desktop/many2016_3.txt')

# # -------------------------------------------
# import json
# # 然后将txt转化为jsonl
# def txt_to_jsonl(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f_in, \
#          open(output_file, 'w', encoding='utf-8') as f_out:
        
#         current_id = None
#         character_dict = {}
        
#         for line in f_in:
#             line = line.strip()
#             if not line:
#                 continue
            
#             if line.endswith(':'):  # 这是ID行
#                 # 先写入前一个记录（如果有）
#                 if current_id is not None:
#                     json.dump({"id": current_id, "character": character_dict}, f_out)
#                     f_out.write('\n')
                
#                 # 开始新记录
#                 current_id = line[:-1]  # 去掉冒号
#                 character_dict = {}
#             else:  # 这是character行
#                 parts = line.split(':')
#                 if len(parts) == 2:
#                     char_num = parts[0].replace('character', '').strip()
#                     value = int(parts[1].strip())
#                     character_dict[char_num] = value
        
#         # 写入最后一个记录
#         if current_id is not None:
#             json.dump({"id": current_id, "character": character_dict}, f_out)
#             f_out.write('\n')

# # 使用示例
# input_filename = 'C:/Users/27433/Desktop/many2016_3.txt'  # 你的输入文件名
# output_filename = 'C:/Users/27433/Desktop/many2016_3.jsonl'  # 输出文件名
# txt_to_jsonl(input_filename, output_filename)

'''
先将match字段转换为列表格式
'''
# import json

# def transform_match_field(input_file, output_file):
#     """
#     将输入JSONL文件中的match字段从字典转换为列表，并保存到输出文件
    
#     参数:
#         input_file: 输入JSONL文件路径
#         output_file: 输出JSONL文件路径
#     """
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:
        
#         for line in infile:
#             # 解析JSON行
#             data = json.loads(line.strip())
            
#             # 转换match字段
#             if 'match' in data and isinstance(data['match'], dict):
#                 # 获取字典的键作为列表
#                 data['match'] = list(data['match'].keys())
            
#             # 写入新的JSON行
#             outfile.write(json.dumps(data) + '\n')

# # 使用示例
# input_jsonl = 'C:/Users/27433/Desktop/2016_3.jsonl'  # 替换为你的输入文件路径
# output_jsonl = 'C:/Users/27433/Desktop/2016_3_list.jsonl'  # 替换为你想要的输出文件路径

# transform_match_field(input_jsonl, output_jsonl)
# print(f"转换完成，结果已保存到 {output_jsonl}")


'''
替换原数据条目中的match字段内容
'''
# import json

# # 文件路径（根据你的实际路径修改）
# jsonl_input_path = 'C:/Users/27433/Desktop/2016_3_list.jsonl'
# json_dict_path = 'C:/Users/27433/Desktop/2016_3_round3.json'
# jsonl_output_path = 'C:/Users/27433/Desktop/2016_3_list1111.jsonl'

# # 加载 JSON 文件（字典数据）
# with open(json_dict_path, 'r', encoding='utf-8') as f:
#     character_data = json.load(f)

# # 处理 JSONL 文件
# with open(jsonl_input_path, 'r', encoding='utf-8') as infile, \
#      open(jsonl_output_path, 'w', encoding='utf-8') as outfile:

#     for line in infile:
#         item = json.loads(line)
#         item_id = str(item['id'])  # 确保是字符串以匹配字典中的键

#         # 提取匹配项对应的条目
#         if item_id in character_data:
#             matched_values = character_data[item_id]
#             result_set = set()

#             for value in matched_values.values():
#                 # 如果是字符串类型且不是 "none"
#                 if isinstance(value, str):
#                     if value != 'none':
#                         char_id = value.split('(')[0].strip()
#                         result_set.add(char_id)

#                 # 如果是列表类型
#                 elif isinstance(value, list):
#                     for val in value:
#                         if val != 'none':
#                             char_id = val.split('(')[0].strip()
#                             result_set.add(char_id)

#             # 更新 match 字段
#             item['match'] = sorted(result_set)  # 可选：排序方便阅读

#         else:
#             # 若 id 不存在于 JSON 中，设置为空列表或保留原值（可按需调整）
#             item['match'] = []

#         # 写入处理后的条目
#         outfile.write(json.dumps(item, ensure_ascii=False) + '\n')


'''
在match字段中建立次数映射
'''
# import json

# # 输入输出文件路径
# original_file = "C:/Users/27433/Desktop/2016_3_list1111.jsonl"       # 原始含 match 列表的文件
# count_file = "C:/Users/27433/Desktop/many2016_3.jsonl"  # 含接收次数的文件
# output_file = "C:/Users/27433/Desktop/2016_3_list1111many.jsonl"        # 输出文件

# # 1. 加载接收次数数据为字典: {id -> {character_id: count, ...}}
# id_to_char_counts = {}
# with open(count_file, "r", encoding="utf-8") as f:
#     for line in f:
#         data = json.loads(line)
#         post_id = data["id"]
#         char_counts = data.get("character", {})
#         # 转为统一格式：'character {id}' 为 key
#         char_counts_formatted = {f"character {k}": v for k, v in char_counts.items()}
#         id_to_char_counts[post_id] = char_counts_formatted

# # 2. 处理原始数据并重写 match 字段为字典格式
# with open(original_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
#     for line in fin:
#         data = json.loads(line)
#         post_id = data["id"]
#         original_matches = data.get("match", [])

#         # 获取当前 ID 的角色接收次数
#         char_count_dict = id_to_char_counts.get(post_id, {})

#         # 构建新的 match 字典
#         match_dict = {}
#         for char in original_matches:
#             match_dict[char] = char_count_dict.get(char, 1)  # 默认为 1

#         # 替换 match 字段
#         data["match"] = match_dict

#         # 写入新文件
#         fout.write(json.dumps(data, ensure_ascii=False) + "\n")
