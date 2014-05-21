# -*- coding:utf-8 -*-

import re


def load_champions_list():
    context = ''
    with open("ChampionsList.txt", 'r') as file:
        for line in file:
            context += line
    return context


# 找出所有「－」字元後的名字回傳
def find_all_names(context):
    pattern = '－(.*)'
    return re.findall(pattern, context)


context = load_champions_list()
results = find_all_names(context)

count = len(results)
result = '\"' + '\",\"'.join(results) + '\"'

print u'完成：', result.decode('utf-8')
with open("Champions.txt", 'w') as file:
    file.write(result)
print u'此結果將同時輸出到檔案「Champions.txt」。'

if count != 10:
    print u'　　注意！本次共有', count, u'名英雄。'

print u'請按 Enter 鍵終止。'
raw_input('')
