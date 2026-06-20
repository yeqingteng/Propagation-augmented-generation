# 3个类别的匹配
import json

# 1. 加载 final_characters.json
with open("C:/Users/27433/Desktop/characters_new.json", "r") as f:
    characters_data = json.load(f)

# 2. 构建一个字典：{ "classifier": ["character 1", "character 2", ...] }
classifier_to_characters = {}

for char_id, char_data in characters_data.items():
    if "interests" in char_data and "politifact" in char_data["interests"]:
        for classifier in char_data["interests"]["politifact"]:
            if classifier not in classifier_to_characters:
                classifier_to_characters[classifier] = []
            classifier_to_characters[classifier].append(char_id)

# 3. 处理输入 JSONL 文件，并输出匹配结果
input_jsonl_path = "C:/Users/27433/Desktop/politifact_classifier.jsonl"
output_jsonl_path = "C:/Users/27433/Desktop/politifact_match.jsonl"

with open(input_jsonl_path, "r", encoding="utf-8") as f_in, open(output_jsonl_path, "w", encoding="utf-8") as f_out:
    for line in f_in:
        data = json.loads(line)
        classifier_str = data.get("classifier", "")
        
        # 分割classifier字符串为多个类别，并去除前后空格
        classifiers = [c.strip() for c in classifier_str.split(",")] if classifier_str else []
        
        # 查找所有匹配的characters（去重!!!）
        matched_characters = []
        for classifier in classifiers:
            matched_characters.extend(classifier_to_characters.get(classifier, []))
        matched_characters = list(set(matched_characters))  # 去重
        
        # 写入输出 JSONL（仅包含 matched_characters）
        result = {"matched_characters": matched_characters}
        f_out.write(json.dumps(result) + "\n")

print(f"匹配完成！结果已保存至 {output_jsonl_path}")


# 1个类别的匹配
# import json

# # 1. 加载 final_characters.json
# with open("C:/Users/27433/Desktop/Claim Detection/my_paper/step2/characters.json", "r") as f:
#     characters_data = json.load(f)

# # 2. 构建一个字典：{ "classifier": ["character 1", "character 2", ...] }
# classifier_to_characters = {}

# for char_id, char_data in characters_data.items():
#     if "interests" in char_data and "covid19" in char_data["interests"]:
#         for classifier in char_data["interests"]["covid19"]:
#             if classifier not in classifier_to_characters:
#                 classifier_to_characters[classifier] = []
#             classifier_to_characters[classifier].append(char_id)

# # 3. 处理输入 JSONL 文件，并输出匹配结果
# input_jsonl_path = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/covid19_classifier.jsonl"
# output_jsonl_path = "C:/Users/27433/Desktop/Claim Detection/my_paper/step2/covid19match.jsonl"

# with open(input_jsonl_path, "r", encoding="utf-8") as f_in, open(output_jsonl_path, "w", encoding="utf-8") as f_out:
#     for line in f_in:
#         data = json.loads(line)
#         classifier = data.get("classifier", "")
        
#         # 查找匹配的 characters
#         matched_characters = classifier_to_characters.get(classifier, [])
        
#         # 写入输出 JSONL（仅包含 matched_characters）
#         result = {"matched_characters": matched_characters}
#         f_out.write(json.dumps(result) + "\n")

# print(f"匹配完成！结果已保存至 {output_jsonl_path}")