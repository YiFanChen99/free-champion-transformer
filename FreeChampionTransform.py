# -*- coding:utf-8 -*-

import re
import os

input_file = 'TempChampionsList.txt'
output_file = 'Champions.txt'


def load_champions_list():
    context = ''
    with open(input_file, 'r') as file:
        for line in file:
            context += line
    return context


# 找出所有「－」字元後的名字回傳
def find_all_names(context):
    pattern = '－(.*)'
    return re.findall(pattern, context)


# 記錄原始列表
open(input_file, 'a').close()
os.startfile(input_file)
print u'請在該文件中貼上原始的英雄列表。\n並於儲存後按 Enter 繼續。'
raw_input('')

# 讀取並收集所有的英雄名稱
context = load_champions_list()
os.remove(input_file)
results = find_all_names(context)

# 將英雄名稱轉換成特定格式的字串，並輸出到檔案，最後開啟其檔案
count = len(results)
result = '\"' + '\",\"'.join(results) + '\"\n'

with open(output_file, 'w') as file:
    file.write('已完成，以下為此次結果：\n')
    file.write(result)
    if count != 10:
        file.write('　　注意！！本次的英雄數目為： ' + str(count) + '。\n')

os.startfile(output_file)
