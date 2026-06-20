# gpt

# import json
# from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
# from collections import defaultdict

# # 替换为你的 jsonl 文件路径
# jsonl_file = 'C:/Users/27433/Downloads/politifact_zero_character_output.jsonl'

# # 初始化变量
# true_labels = []
# pred_labels = []

# # 为每个label统计正确和总数
# label_correct = defaultdict(int)
# label_total = defaultdict(int)

# # 读取数据
# with open(jsonl_file, 'r', encoding='utf-8') as f:
#     for line in f:
#         item = json.loads(line)
#         true = item["label"]
#         pred = item["response_new"]

#         true_labels.append(true)
#         pred_labels.append(pred)

#         label_total[true] += 1
#         if true == pred:
#             label_correct[true] += 1

# # 打印每个label的Accuracy
# print("Accuracy per label:")
# for label in range(6):  # 0~5
#     total = label_total[label]
#     correct = label_correct[label]
#     acc = correct / total if total > 0 else 0.0
#     print(f"Label {label}: {acc:.4f} ({correct}/{total})")

# # 计算总体指标
# overall_accuracy = accuracy_score(true_labels, pred_labels)
# precision = precision_score(true_labels, pred_labels, average='macro', zero_division=0)
# recall = recall_score(true_labels, pred_labels, average='macro', zero_division=0)
# f1 = f1_score(true_labels, pred_labels, average='macro', zero_division=0)

# print("\nOverall metrics:")
# print(f"Accuracy : {overall_accuracy:.4f}")
# print(f"Precision: {precision:.4f}")
# print(f"Recall   : {recall:.4f}")
# print(f"F1 Score : {f1:.4f}")

'''
///////////////////////////////////////////////////////////
'''

'''
计算前提取字段(二分类)
'''
# import json
# import re

# def process_response_new(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:

#         for line in infile:
#             data = json.loads(line)

#             # 提取response_new中的1或0
#             if 'response_new' in data:
#                 response_new = str(data['response_new'])
#                 # 使用正则表达式查找第一个出现的1或0
#                 match = re.search(r'[10]', response_new)
#                 if match:
#                     data['response_new'] = int(match.group())
#                 else:
#                     # 如果没有找到1或0，设置为None或默认值
#                     data['response_new'] = None

#             # 写入处理后的数据
#             outfile.write(json.dumps(data) + '\n')

# # 使用示例
# input_file = 'C:/Users/27433/Downloads/politifact_zero_character_output_reason.jsonl'
# output_file = 'C:/Users/27433/Downloads/politifact_zero_character_output.jsonl'

# process_response_new(input_file, output_file)
# print(f"处理完成，结果已保存到 {output_file}")

'''
计算前提取字段(多分类)
'''
# import json
# import re

# def process_response_new(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:

#         for line in infile:
#             data = json.loads(line)

#             # 提取response_new中的1或0
#             if 'response_new' in data:
#                 response_new = str(data['response_new'])
#                 # 使用正则表达式查找第一个出现的1或0
#                 match = re.search(r'[3210]', response_new)
#                 if match:
#                     data['response_new'] = int(match.group())
#                 else:
#                     # 如果没有找到1或0，设置为None或默认值
#                     data['response_new'] = None

#             # 写入处理后的数据
#             outfile.write(json.dumps(data) + '\n')

# # 使用示例
# input_file = 'C:/Users/27433/Downloads/pubhealth_zero_character_output_reason.jsonl'
# output_file = 'C:/Users/27433/Downloads/pubhealth_zero_character_output.jsonl'

# process_response_new(input_file, output_file)
# print(f"处理完成，结果已保存到 {output_file}")

'''
deepseek计算指标
'''
# import json
# from collections import defaultdict
# from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score

# def evaluate_jsonl(file_path):
#     # 初始化统计变量
#     label_counts = defaultdict(int)
#     correct_counts = defaultdict(int)
#     total_correct = 0
#     total_samples = 0

#     # 存储所有预测和真实标签
#     all_labels = []
#     all_responses = []

#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             data = json.loads(line)
#             label = data['label']
#             response = data['response_new']
#             #response = data['response']
#             # 统计每个label的情况
#             label_counts[label] += 1
#             if label == response:
#                 correct_counts[label] += 1
#                 total_correct += 1
#             total_samples += 1

#             # 收集所有标签用于总体计算
#             all_labels.append(label)
#             all_responses.append(response)

#     # 计算每个label的Accuracy
#     print("Accuracy for each label:")
#     for label in sorted(label_counts.keys()):
#         accuracy = correct_counts[label] / label_counts[label] if label_counts[label] > 0 else 0
#         print(f"Label {label}: {accuracy:.4f} ({correct_counts[label]}/{label_counts[label]})")

#     # 计算总体指标
#     print("\nOverall metrics:")
#     accuracy = accuracy_score(all_labels, all_responses)
#     precision = precision_score(all_labels, all_responses, average='macro', zero_division=0)
#     recall = recall_score(all_labels, all_responses, average='macro', zero_division=0)
#     f1 = f1_score(all_labels, all_responses, average='macro', zero_division=0)

#     print(f"Accuracy: {accuracy:.4f}")
#     print(f"Precision (macro): {precision:.4f}")
#     print(f"Recall (macro): {recall:.4f}")
#     print(f"F1 Score (macro): {f1:.4f}")

# # 使用示例
# #evaluate_jsonl('C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/snopes/v3/消融/test222_tot_character_output.jsonl')
# evaluate_jsonl('C:/Users/27433/Downloads/test111_zc_character_output.jsonl')

'''
增强鲁棒性的版本
'''
import json
from collections import defaultdict
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score

def evaluate_jsonl(file_path):
    # 初始化统计变量
    label_counts = defaultdict(int)
    correct_counts = defaultdict(int)
    total_correct = 0
    total_samples = 0

    # 存储所有预测和真实标签
    all_labels = []
    all_responses = []

    skipped_samples = 0  # 统计被跳过的样本数

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            label = data.get('label')
            response = data.get('response')  # 或 data.get('response')

            # ✅ 只允许整数类型（跳过非整数）
            if not isinstance(label, int) or not isinstance(response, int):
                skipped_samples += 1
                continue

            # 统计每个label的情况
            label_counts[label] += 1
            if label == response:
                correct_counts[label] += 1
                total_correct += 1
            total_samples += 1

            # 收集所有标签用于总体计算
            all_labels.append(label)
            all_responses.append(response)

    # ✅ 输出被跳过的样本数
    print(f"Skipped {skipped_samples} invalid samples.")

    # ✅ 处理：如果全被跳过，避免报错
    if total_samples == 0:
        print("No valid samples found!")
        return

    # 计算每个label的Accuracy
    print("\nAccuracy for each label:")
    for label in sorted(label_counts.keys()):
        accuracy = correct_counts[label] / label_counts[label] if label_counts[label] > 0 else 0
        print(f"Label {label}: {accuracy:.4f} ({correct_counts[label]}/{label_counts[label]})")

    # 计算总体指标
    print("\nOverall metrics:")
    accuracy = accuracy_score(all_labels, all_responses)
    precision = precision_score(all_labels, all_responses, average='macro', zero_division=0)
    recall = recall_score(all_labels, all_responses, average='macro', zero_division=0)
    f1 = f1_score(all_labels, all_responses, average='macro', zero_division=0)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision (macro): {precision:.4f}")
    print(f"Recall (macro): {recall:.4f}")
    print(f"F1 Score (macro): {f1:.4f}")

# 使用示例
evaluate_jsonl('C:/Users/27433/Desktop/test_zs_output.jsonl')
#evaluate_jsonl('C:/Users/27433/Downloads/weibo21_shiyan_round1222_output.jsonl')
