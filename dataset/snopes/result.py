# gpt
# import json
# from collections import defaultdict
# from sklearn.metrics import classification_report, accuracy_score

# # 修改为你的文件路径
# file_path = 'C:/Users/27433/Downloads/pubhealth_zero_character_output.jsonl'

# # 存储标签和预测值
# true_labels = []
# pred_labels = []

# # 按类别统计
# label_counts = defaultdict(int)
# correct_counts = defaultdict(int)

# # 读取文件
# with open(file_path, 'r', encoding='utf-8') as f:
#     for line in f:
#         data = json.loads(line)
#         label = data['label']
#         response = data['response_new']
        
#         true_labels.append(label)
#         pred_labels.append(response)
        
#         label_counts[label] += 1
#         if label == response:
#             correct_counts[label] += 1

# # 计算每个label的Accuracy
# print("Per-label Accuracy:")
# for lbl in sorted(label_counts):
#     acc = correct_counts[lbl] / label_counts[lbl] if label_counts[lbl] else 0.0
#     print(f"Label {lbl}: Accuracy = {acc:.4f}")

# # 总体评估指标
# print("\nOverall Classification Report:")
# report = classification_report(true_labels, pred_labels, digits=4)
# print(report)

# # 总体准确率
# overall_accuracy = accuracy_score(true_labels, pred_labels)
# print(f"Overall Accuracy: {overall_accuracy:.4f}")

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
#evaluate_jsonl('C:/Users/27433/Desktop/Claim Detection/my_paper/shiyan/politifact/传播后/politifact_zero_character_output.jsonl')
evaluate_jsonl('C:/Users/27433/Desktop/test_sc_output.jsonl')