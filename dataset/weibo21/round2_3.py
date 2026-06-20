import json
from openai import OpenAI
from tqdm import tqdm
from typing import Dict, List, Any

# # 配置OpenAI API
# client = OpenAI(
#     api_key="sk-LCtKcRnWo9259ra3LGUszdDpgleiKcFyOdzkRaXkwlTeQCxf",  # 替换为你的API密钥
#     base_url="https://api.kksj.org/v1"  # 或你的自定义base_url
# )
# model = "gpt-4o-2024-11-20"  # 或你选择的模型

client = OpenAI(
    api_key="34dde694-1fef-45a3-97ce-b7b601cca48b",  # 替换为你的API密钥
    base_url="https://ark.cn-beijing.volces.com/api/v3"  # 或你的自定义base_url
)
model = "deepseek-v3-250324"  # 或你选择的模型

# 输入文件路径
jsonl_file_path = "/root/autodl-tmp/shiyan/politifact_round0.jsonl"
characters_file_path = "/root/autodl-tmp/shiyan/characters_new.json"
output_txt_path = "/root/autodl-tmp/shiyan/results_politifact.txt"  # 改为txt输出文件

# 加载characters数据
with open(characters_file_path, 'r', encoding='utf-8') as f:
    characters_data = json.load(f)

def get_character_info(character_id: str) -> Dict[str, Any]:
    """获取指定character的完整信息"""
    return characters_data.get(character_id, {})

def get_relationships_info(character_id: str) -> Dict[str, Dict[str, List[str]]]:
    """获取指定character的所有社会关系及其信息"""
    character_info = get_character_info(character_id)
    if not character_info:
        return {}
    
    relationships = character_info.get("relationships", {})
    result = {}
    
    # 遍历所有关系类型和关系人
    for rel_type, rel_chars in relationships.items():
        for rel_char, rel_names in rel_chars.items():
            rel_char_info = get_character_info(rel_char)
            if rel_char_info:
                # 存储关系信息和关系人信息
                result[rel_char] = {
                    "relationship_type": rel_type,   #强中弱关系
                    "relationship_names": rel_names,   #具体是什么关系
                    "character_info": rel_char_info
                }
    
    return result

def query_gpt4o(character_info: Dict[str, Any], 
                relationships_info: Dict[str, Dict[str, Any]], 
                text: str) -> str:
    """调用GPT-4o判断文本应该传递给哪些社会关系，直接返回格式化字符串"""
    # 构建提示词
    prompt = f"""
    From a U.S. perspective, Chinese platforms like Weibo are fast-moving spaces where news, rumors, and opinions spread rapidly.
    Topics like politics, health, disasters, and entertainment often trigger emotional reactions and wide engagement, reflecting how diverse users interact with and circulate information in real time.
    NOTE: 
    (1) The timeline years you are in is the year 2021. 
    (2) The area you are in won't affect your analysis of this information.

    main character information (this is YOU):
    {json.dumps(character_info, indent=2, ensure_ascii=False)}
    
    <text content>:
    {text}
    
    --- Step 1: Analyze this <text content> thoroughly from main character's perspective ---

    The following common sense can help you in your analysis: 
    In our virtual society, partial false information on Chinese social media platforms such as Weibo more easily triggers emotional resonance, 
    and therefore tends to spread more widely and deeply.
    
    Based on the above common sense (MUST be considered) and combined with your own attributes (the attributes of the main character), do you think this <text content> is worth spreading?
    If the answer is positive, you should enter Step2.
    If the answer is negative, you should skip Step2 and go directly to Step3.

    --- Step 2: Review your social relationship characters ---

    Your social relationship characters information:
    {json.dumps(relationships_info, indent=2, ensure_ascii=False)}

    According to the result of Step 1(Analyze this <text content> thoroughly from main character's perspective), consider:
    which social relationship characters should receive this <text content>?
    
    Pay attention to the following two points:
    - The social relationship characters in Weak Ties should also be appropriately considered.
    - If you are not sure whether this social relationship character should receive this <text content>, there is a high probability that you should not send this <text content> to him/her.
    
    --- Step 3: Return your result ---

    You should return your result in the following EXACT format:
    If no social relationship characters should receive <text content>: "none"; reason: "..."(Within 30 words)
    
    If some social relationship characters should receive <text content>, for example:
    "character 178(Moderate Ties: Colleague)", "character 199(Moderate Ties: Online friends)", ...; reason: "..."(Within 30 words)
    
    DO NOT include any additional text or explanations. ONLY return the formatted string as specified above.
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an AI assistant that specializes in role-playing specific characters and analyzing information dissemination from their perspective."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
            #extra_body={"enable_thinking": False} 
        )
        
        # 直接返回模型生成的格式化字符串
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"API调用出错: {e}")
        return "none"

def process_single_entry(entry: Dict[str, Any]) -> str:
    """处理单个jsonl条目，返回格式化字符串"""
    text = entry["text"]
    result_lines = []
    
    for character_id in entry["match"]:
        # 获取主角色信息
        main_character_info = get_character_info(character_id)
        if not main_character_info:
            result_lines.append(f'"{character_id}": none')
            continue
            
        # 获取所有社会关系信息
        relationships_info = get_relationships_info(character_id)
        if not relationships_info:
            result_lines.append(f'"{character_id}": none')
            continue
            
        # 调用GPT-4o获取格式化结果
        formatted_result = query_gpt4o(main_character_info, relationships_info, text)
        
        # 确保返回的格式正确
        if formatted_result.lower() == "none":
            result_lines.append(f'"{character_id}": none')
        else:
            result_lines.append(f'"{character_id}": {formatted_result}')
    
    return "\n".join(result_lines)

def main():
    # 初始化输出文件
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write("")  # 清空或创建文件
    
    # 处理jsonl文件
    with open(jsonl_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        for i, line in enumerate(tqdm(lines, desc="Processing entries")):
            try:
                entry = json.loads(line.strip())
                result = process_single_entry(entry)
                
                # 写入结果到输出文件
                with open(output_txt_path, 'a', encoding='utf-8') as out_f:
                    if i > 0:  # 如果不是第一条记录，先添加分隔线
                        out_f.write("\n-------------------\n")
                    out_f.write(result)
                    
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")
                continue

if __name__ == "__main__":
    main()