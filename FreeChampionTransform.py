# -*- coding:utf-8 -*-

import re

raw_string = u'''raw string =
執法者－凱特琳

牛頭酋長－亞歷斯塔
　

蒂瑪西亞楷模－嘉文四世
　

蒂瑪西亞總管－趙信
　

孤高劍客－菲歐拉
　

暮光之眼－慎
　

遠古魔導－齊勒斯
　

酒桶之王－古拉格斯
　

虛空掠食者－卡力斯
　

暗影之拳－阿卡莉
'''


# 找出所有「－」字元後的名字回傳
def find_all_name(string):
    pattern = u'－(.*)'
    return re.findall(pattern, string)


results = find_all_name(raw_string)
count = len(results)
result = '\"' + '\",\"'.join(results) + '\"'

if count != 10:
    print '數量錯誤，結果有 %d 筆。' % count

print result
print u'請按 Enter 鍵終止。'
raw_input('')
