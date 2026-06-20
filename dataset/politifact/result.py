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
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            label = data['label']
            response = data['response']
            
            # 统计每个label的情况
            label_counts[label] += 1
            if label == response:
                correct_counts[label] += 1
                total_correct += 1
            total_samples += 1
            
            # 收集所有标签用于总体计算
            all_labels.append(label)
            all_responses.append(response)
    
    # 计算每个label的Accuracy
    print("Accuracy for each label:")
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
#evaluate_jsonl('C:/Users/27433/Desktop/Claim Detection/IAG/shiyan/politifact/v3/第一轮传播后_new/1234_old/test111_fc_character_output.jsonl')
evaluate_jsonl(r'C:\Users\27433\Desktop\MID\PAG\shiyan\politifact\v3\无传播\test_zs_output.jsonl')

'''
6分类AUC
'''
# import json
# from collections import defaultdict
# from sklearn.metrics import (
#     precision_score,
#     recall_score,
#     accuracy_score,
#     f1_score,
#     roc_auc_score
# )

# def evaluate_jsonl(file_path):
#     # 初始化统计变量
#     label_counts = defaultdict(int)
#     correct_counts = defaultdict(int)
#     total_correct = 0
#     total_samples = 0

#     # 存储所有预测和真实标签
#     all_labels = []
#     all_responses = []

#     # 存储所有类别概率
#     all_probs = []

#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             data = json.loads(line)

#             label = data['label']
#             response = data['response']
#             probs = data['probs']

#             # 统计每个 label 的情况
#             label_counts[label] += 1

#             if label == response:
#                 correct_counts[label] += 1
#                 total_correct += 1

#             total_samples += 1

#             # 收集所有标签、预测结果和概率
#             all_labels.append(label)
#             all_responses.append(response)
#             all_probs.append(probs)

#     # 计算每个 label 的 Accuracy
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

#     # 计算多分类 AUC
#     try:
#         auc_macro = roc_auc_score(
#             all_labels,
#             all_probs,
#             labels=[0, 1, 2, 3, 4, 5],
#             multi_class='ovr',
#             average='macro'
#         )

#         auc_weighted = roc_auc_score(
#             all_labels,
#             all_probs,
#             labels=[0, 1, 2, 3, 4, 5],
#             multi_class='ovr',
#             average='weighted'
#         )

#         print(f"AUC (macro, OvR): {auc_macro:.4f}")
#         print(f"AUC (weighted, OvR): {auc_weighted:.4f}")

#     except ValueError as e:
#         print(f"AUC cannot be computed: {e}")


# # 使用示例
# evaluate_jsonl(
#     r'C:\Users\27433\Downloads\test_zs_output_auc_politifact_v3.jsonl'
# )

'''
2分类AUC
'''
# import json
# from collections import defaultdict
# from sklearn.metrics import (
#     precision_score,
#     recall_score,
#     accuracy_score,
#     f1_score,
#     roc_auc_score
# )

# def evaluate_jsonl(file_path):
#     # 初始化统计变量
#     label_counts = defaultdict(int)
#     correct_counts = defaultdict(int)
#     total_correct = 0
#     total_samples = 0

#     # 存储所有预测和真实标签
#     all_labels = []
#     all_responses = []

#     # 存储 label=1 的预测概率，用于计算二分类 AUC
#     all_positive_probs = []

#     # 统计有效 probs 数量
#     valid_probs_count = 0

#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue

#             data = json.loads(line)

#             label = data['label']
#             response = data['response']

#             # 二分类 probs 格式：
#             # probs[0] = label=0 / false 的置信度
#             # probs[1] = label=1 / true 的置信度
#             probs = data.get('probs', None)

#             label_counts[label] += 1

#             if label == response:
#                 correct_counts[label] += 1
#                 total_correct += 1

#             total_samples += 1

#             all_labels.append(label)
#             all_responses.append(response)

#             if probs is not None:
#                 if len(probs) != 2:
#                     raise ValueError(
#                         f"Each probs must contain exactly 2 values: [prob_false, prob_true]. "
#                         f"Got {len(probs)} values in data id={data.get('id', 'unknown')}"
#                     )

#                 # AUC 在二分类中需要正类 label=1 的置信度
#                 all_positive_probs.append(probs[1])
#                 valid_probs_count += 1

#     # 计算每个 label 的 Accuracy
#     print("Accuracy for each label:")
#     for label in sorted(label_counts.keys()):
#         accuracy = correct_counts[label] / label_counts[label] if label_counts[label] > 0 else 0

#         label_name = "true" if label == 1 else "false"
#         print(
#             f"Label {label} ({label_name}): "
#             f"{accuracy:.4f} ({correct_counts[label]}/{label_counts[label]})"
#         )

#     # 计算总体指标
#     print("\nOverall metrics:")

#     accuracy = accuracy_score(all_labels, all_responses)
#     precision = precision_score(
#         all_labels,
#         all_responses,
#         average='binary',
#         pos_label=1,
#         zero_division=0
#     )
#     recall = recall_score(
#         all_labels,
#         all_responses,
#         average='binary',
#         pos_label=1,
#         zero_division=0
#     )
#     f1 = f1_score(
#         all_labels,
#         all_responses,
#         average='binary',
#         pos_label=1,
#         zero_division=0
#     )

#     print(f"Accuracy: {accuracy:.4f}")
#     print(f"Precision: {precision:.4f}")
#     print(f"Recall: {recall:.4f}")
#     print(f"F1 Score: {f1:.4f}")

#     # 计算 AUC
#     if valid_probs_count == total_samples:
#         try:
#             auc = roc_auc_score(
#                 all_labels,
#                 all_positive_probs
#             )
#             print(f"AUC: {auc:.4f}")
#         except ValueError as e:
#             print(f"AUC cannot be computed: {e}")
#     else:
#         print(
#             "AUC cannot be computed because the jsonl file does not contain "
#             "valid probability scores for every sample."
#         )


# evaluate_jsonl(
#     r'C:\Users\27433\Downloads\test_zs_output_auc_snopes_v3.jsonl'
# )