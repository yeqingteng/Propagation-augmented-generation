# step 1: 挑选无关系的10个match
import json
import random

def load_characters_data(characters_file):
    """加载 characters.json 数据"""
    with open(characters_file, 'r') as f:
        return json.load(f)

def has_relationship(char_data, other_char_id):
    """检查 character 是否与 other_char_id 有社会关系"""
    relationships = char_data.get("relationships", {})
    for tie_level in ["Strong Ties", "Moderate Ties", "Weak Ties"]:
        if tie_level in relationships and other_char_id in relationships[tie_level]:
            return True
    return False

def select_independent_characters(matched_chars, characters_data):
    """从 matched_characters 中选择最多 10 个无社会关系的 characters"""
    if not matched_chars:
        return []
    
    # 随机打乱顺序以避免固定选择
    shuffled_chars = random.sample(matched_chars, len(matched_chars))
    
    selected = []
    remaining_chars = shuffled_chars.copy()
    
    # 选择过程最多进行10次
    max_selections = 10
    
    while len(selected) < max_selections and remaining_chars:
        # 尝试选择下一个character（与所有已选character都无关系）
        # 只在最开始打乱一次顺序，而不是每次选择前都打乱顺序!!!
        next_char_candidates = [
            char for char in remaining_chars
            if all(not has_relationship(characters_data.get(char, {}), s) for s in selected)
        ]
        
        if not next_char_candidates:
            break  # 没有符合条件的character了
            
        # 选择第一个符合条件的character
        next_char = next_char_candidates[0]
        selected.append(next_char)
        remaining_chars.remove(next_char)
    
    return selected

def process_jsonl(input_jsonl, output_jsonl, characters_data):
    """处理输入 JSONL 并生成输出 JSONL"""
    with open(input_jsonl, 'r') as f_in, open(output_jsonl, 'w') as f_out:
        for line in f_in:
            data = json.loads(line)
            matched_chars = data.get("matched_characters", [])
            
            # 选择无社会关系的 characters（最多 10 个）
            selected_chars = select_independent_characters(matched_chars, characters_data)
            
            # 写入输出 JSONL
            result = {"selected_characters": selected_chars}
            f_out.write(json.dumps(result) + "\n")

if __name__ == "__main__":
    # 文件路径
    input_jsonl = "C:/Users/27433/Desktop/test_match.jsonl"          # 输入 JSONL 文件
    output_jsonl = "C:/Users/27433/Desktop/test_match_10.jsonl"      # 输出 JSONL 文件
    characters_file = "C:/Users/27433/Desktop/characters_weibo21.json"  # characters.json 文件
    
    # 加载数据并处理
    characters_data = load_characters_data(characters_file)
    process_jsonl(input_jsonl, output_jsonl, characters_data)
    
    print(f"处理完成！结果已保存至 {output_jsonl}")


# task（5人无关系）
# import json
# import random

# def load_characters_data(characters_file):
#     """加载 characters.json 数据"""
#     with open(characters_file, 'r') as f:
#         return json.load(f)

# def has_relationship(char_data, other_char_id):
#     """检查 character 是否与 other_char_id 有社会关系"""
#     relationships = char_data.get("relationships", {})
#     for tie_level in ["Strong Ties", "Moderate Ties", "Weak Ties"]:
#         if tie_level in relationships and other_char_id in relationships[tie_level]:
#             return True
#     return False

# def select_independent_characters(matched_chars, characters_data):
#     """从 matched_characters 中选择最多 5 个无社会关系的 characters"""
#     if not matched_chars:
#         return []
    
#     # 随机打乱顺序以避免固定选择
#     shuffled_chars = random.sample(matched_chars, len(matched_chars))
    
#     selected = []
#     remaining_chars = shuffled_chars.copy()
    
#     # 任选第一个 character A
#     if remaining_chars:
#         char_a = remaining_chars.pop(0)
#         selected.append(char_a)
    
#     # 尝试选择 character B（与 A 无关系）
#     char_b_candidates = [
#         char for char in remaining_chars
#         if not has_relationship(characters_data.get(char, {}), char_a)
#     ]
#     if char_b_candidates:
#         char_b = char_b_candidates[0]  # 选第一个符合条件的
#         selected.append(char_b)
#         remaining_chars.remove(char_b)
    
#     # 尝试选择 character C（与 A 和 B 都无关系）
#     char_c_candidates = [
#         char for char in remaining_chars
#         if (not has_relationship(characters_data.get(char, {}), char_a) and
#             not has_relationship(characters_data.get(char, {}), char_b))
#     ]
#     if char_c_candidates:
#         char_c = char_c_candidates[0]  # 选第一个符合条件的
#         selected.append(char_c)
#         remaining_chars.remove(char_c)
    
#     # 尝试选择 character D（与 A、B、C 都无关系）
#     if len(selected) >= 3:
#         char_d_candidates = [
#             char for char in remaining_chars
#             if (not has_relationship(characters_data.get(char, {}), char_a) and
#                 not has_relationship(characters_data.get(char, {}), char_b) and
#                 not has_relationship(characters_data.get(char, {}), char_c))
#         ]
#         if char_d_candidates:
#             char_d = char_d_candidates[0]
#             selected.append(char_d)
#             remaining_chars.remove(char_d)
    
#     # 尝试选择 character E（与 A、B、C、D 都无关系）
#     if len(selected) >= 4:
#         char_e_candidates = [
#             char for char in remaining_chars
#             if (not has_relationship(characters_data.get(char, {}), char_a) and
#                 not has_relationship(characters_data.get(char, {}), char_b) and
#                 not has_relationship(characters_data.get(char, {}), char_c) and
#                 not has_relationship(characters_data.get(char, {}), char_d))
#         ]
#         if char_e_candidates:
#             char_e = char_e_candidates[0]
#             selected.append(char_e)
    
#     return selected

# def process_jsonl(input_jsonl, output_jsonl, characters_data):
#     """处理输入 JSONL 并生成输出 JSONL"""
#     with open(input_jsonl, 'r') as f_in, open(output_jsonl, 'w') as f_out:
#         for line in f_in:
#             data = json.loads(line)
#             matched_chars = data.get("matched_characters", [])
            
#             # 选择无社会关系的 characters（最多 5 个）
#             selected_chars = select_independent_characters(matched_chars, characters_data)
            
#             # 写入输出 JSONL
#             result = {"selected_characters": selected_chars}
#             f_out.write(json.dumps(result) + "\n")

# if __name__ == "__main__":
#     # 文件路径
#     input_jsonl = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/politifactmatch.jsonl"          # 输入 JSONL 文件
#     output_jsonl = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/politifactselect_5.jsonl"        # 输出 JSONL 文件
#     characters_file = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/characters.json"  # characters.json 文件
    
#     # 加载数据并处理
#     characters_data = load_characters_data(characters_file)
#     process_jsonl(input_jsonl, output_jsonl, characters_data)
    
#     print(f"处理完成！结果已保存至 {output_jsonl}")


# task（3人无关系）
# import json
# import random

# def load_characters_data(characters_file):
#     """加载 characters.json 数据"""
#     with open(characters_file, 'r') as f:
#         return json.load(f)

# def has_relationship(char_data, other_char_id):
#     """检查 character 是否与 other_char_id 有社会关系"""
#     relationships = char_data.get("relationships", {})
#     for tie_level in ["Strong Ties", "Moderate Ties", "Weak Ties"]:
#         if tie_level in relationships and other_char_id in relationships[tie_level]:
#             return True
#     return False

# def select_independent_characters(matched_chars, characters_data):
#     """从 matched_characters 中选择最多 3 个无社会关系的 characters"""
#     if not matched_chars:
#         return []
    
#     # 随机打乱顺序以避免固定选择
#     shuffled_chars = random.sample(matched_chars, len(matched_chars))
    
#     selected = []
#     remaining_chars = shuffled_chars.copy()
    
#     # 任选第一个 character A
#     if remaining_chars:
#         char_a = remaining_chars.pop(0)
#         selected.append(char_a)
    
#     # 尝试选择 character B（与 A 无关系）
#     char_b_candidates = [
#         char for char in remaining_chars
#         if not has_relationship(characters_data.get(char, {}), char_a)
#     ]
#     if char_b_candidates:
#         char_b = char_b_candidates[0]  # 选第一个符合条件的
#         selected.append(char_b)
#         remaining_chars.remove(char_b)
    
#     # 尝试选择 character C（与 A 和 B 都无关系）
#     char_c_candidates = [
#         char for char in remaining_chars
#         if (not has_relationship(characters_data.get(char, {}), char_a) and
#             not has_relationship(characters_data.get(char, {}), char_b))
#     ]
#     if char_c_candidates:
#         char_c = char_c_candidates[0]  # 选第一个符合条件的
#         selected.append(char_c)
    
#     return selected

# def process_jsonl(input_jsonl, output_jsonl, characters_data):
#     """处理输入 JSONL 并生成输出 JSONL"""
#     with open(input_jsonl, 'r') as f_in, open(output_jsonl, 'w') as f_out:
#         for line in f_in:
#             data = json.loads(line)
#             matched_chars = data.get("matched_characters", [])
            
#             # 选择无社会关系的 characters（最多 3 个）
#             selected_chars = select_independent_characters(matched_chars, characters_data)
            
#             # 写入输出 JSONL
#             result = {"selected_characters": selected_chars}
#             f_out.write(json.dumps(result) + "\n")

# if __name__ == "__main__":
#     # 文件路径
#     input_jsonl = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/politifactmatch.jsonl"          # 输入 JSONL 文件
#     output_jsonl = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/politifactselect.jsonl"        # 输出 JSONL 文件
#     characters_file = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/characters.json"  # characters.json 文件
    
#     # 加载数据并处理
#     characters_data = load_characters_data(characters_file)
#     process_jsonl(input_jsonl, output_jsonl, characters_data)
    
#     print(f"处理完成！结果已保存至 {output_jsonl}")


# step 2: 拼接到分类文件中
import json

def add_match_field(classifier_file, select_file, output_file):
    # 读取 politifactselect.jsonl 文件，提取 selected_characters
    selected_chars_list = []
    with open(select_file, 'r', encoding='utf-8') as f_select:  # 添加 encoding='utf-8'
        for line in f_select:
            data = json.loads(line)
            selected_chars_list.append(data.get("selected_characters", []))
    
    # 读取 politifact_classifier.jsonl 并添加 match 字段
    with open(classifier_file, 'r', encoding='utf-8') as f_classifier, open(output_file, 'w', encoding='utf-8') as f_out:  # 均添加 encoding='utf-8'
        for i, line in enumerate(f_classifier):
            data = json.loads(line)
            # 确保 selected_chars_list 有对应的数据
            if i < len(selected_chars_list):
                data["match"] = selected_chars_list[i]
            else:
                data["match"] = []  # 如果没有对应的 selected_characters，设为空列表
            f_out.write(json.dumps(data, ensure_ascii=False) + "\n")  # ensure_ascii=False 避免中文被转义

if __name__ == "__main__":
    # 文件路径
    classifier_file = "C:/Users/27433/Desktop/test.jsonl"  # 输入文件（原始数据）
    select_file = "C:/Users/27433/Desktop/test_match_10.jsonl"           # 输入文件（selected_characters）
    output_file = "C:/Users/27433/Desktop/test_round0.jsonl"  # 输出文件

    add_match_field(classifier_file, select_file, output_file)
    print(f"处理完成！结果已保存至 {output_file}")