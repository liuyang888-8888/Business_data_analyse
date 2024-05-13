# 定义一个函数，用于处理每个值
import re


def process_data(value):
    # 匹配双斜杠后面存在单斜杠的情况
    if '//' in value and '/' in value.split('//')[1]:
        return value.split('//')[0] + '//' + value.split('//')[1].split('/')[0]
    elif '//' in value and '/' not in value.split('//')[1]:
        return value.split('//')[0] + '//' + value.split('//')[1]
    # 匹配只包含单斜杠的情况
    elif '/' in value:
        return value.split('/')[0]
    else:
        return value

import dashscope
dashscope.api_key="	sk-DZCckbAtMG"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/3/26 12:42
# @Author : 桐
# @QQ:1041264242
# 注意事项：
from http import HTTPStatus
import dashscope
from dashscope import MultiModalConversation
import json

import os
dashscope.api_key="sk-DZCckbAtMG"
def qwen_api(query,image_path='',type='text',prompt='随便回答'):
    """
    :param query: 用户问题
    :param image_path: 如果是多模态提问，需要传入图片路径
    :param type: 纯文本提问用'text',图文对话用'image'
    :param prompt: 用于输入系统提示词
    :return: 返回大模型回答结果
    """
    if type=='text':
        messages = [{'role': 'system', 'content': prompt},
                    {'role': 'user', 'content': query}]
        response = dashscope.Generation.call(
            'qwen1.5-110b-chat',
            messages=messages,
            result_format='message',  # set the result is message format.
        )
        if response.status_code == HTTPStatus.OK:
            # print(response)
            return response.output['choices'][0]['message']['content']
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    elif type=='image':
        """Sample of use local file.
           linux&mac file schema: file:///home/images/test.png
           windows file schema: file://D:/images/abc.png
        """
        messages = [{
            'role': 'system',
            'content': [{'text': prompt}]},
            {'role':'user',
            'content': [
                {
                    'image': 'file://'+image_path
                },
                {
                    'text': query
                },
            ]
        }]
        response = MultiModalConversation.call(model='qwen-vl-plus', messages=messages)
        return response.output['choices'][0]['message']['content'][0]['text']


def is_json(my_str):
    try:
        json_object = json.loads(my_str)
    except ValueError as e:
        return False
    return True
def get_category(key):
    # category = bing_search.search_bing_qwen(key)
    query="总结"+key+"是属于什么类别的网站或者应用"
    category = qwen_api(query=query,type='text',prompt='''请你分析以下软件或者网址是干嘛的，不是要你访问网址或者应用，只需分析网址或者应用中的关键词就行。例如：http://www.taobao.com，这个网址包含'taobao'关键词语，因此这个网址是关于购物的。给出一个网址或软件的归类，归类规则如下：包括，不仅限于以下，如果不满足以下的类，请结合你自己的理解进行分类(一段网页的描述可以有多个类别)：1.如果是和游戏相关的，请输出“游戏类”。2.如果是和视频相关的，请输出“视频类”。3.如果是和看病相关的，请输出“看病类”。4.如果是和购物相关的，请输出“购物类”。4.如果是和买房相关的，请输出“买房类”。5.如果是和社交相关的，请输出“社交类”等等。如果无法做出判断，则归类为其他。
    
    输出一个字符出,格式为：==**==。 将其中的**部分替换成类别信息，严格遵循这个格式，不要输出无关内容。''')
    pattern = r'==(.*?)=='
    try:
        matches = re.findall(pattern, category)[0]
    except Exception as e:
        print("--"*20)
        print(e)
        print(key)
        print(category)
        raise
    return matches

# print(qwen_api("你是谁？"))