from pypinyin import pinyin, lazy_pinyin
import re
import time
import time_extract
import jieba
import json

# 目前還不支援 明/後 天 時間
with open('./keyword.json', encoding="utf-8") as f :
    func_dict = json.load(f) 

day_dict = {'一': 1, '1': 1 , '二': 2, '2': 2 , '三': 3, '3': 3 , '四': 4, '4': 4 , 
            '五': 5, '5': 5 , '六': 6, '6': 6 , '末': 6 ,'天': 7, '日': 7}

def isPhoneNumber(str):
    return re.match(r'\d(-\d)*', str)

def text2func(input_str):
    key_found = 0
    keyword_index = -1
    smallest_index = 999999999
    keyword_str = 'NOT FOUND'
    allfunc_list = []
    for func_name in list(func_dict):
        for keyword in list(func_dict[func_name]["keywords"]):
            allfunc_list.append(keyword)
    for keyword in allfunc_list:
        keyword_index = input_str.find(keyword)
        if (keyword_index!=-1):
            if(keyword_index < smallest_index):
                smallest_index = keyword_index
                keyword_str = keyword
    for func_name in list(func_dict):
        for keyword in list(func_dict[func_name]["keywords"]):
            if( keyword == keyword_str):
                keyword_str = keyword
                return [func_name, keyword]


def para_extract(input_str, func_key):
    location = input_str.find(func_key[1])
    if(location != -1): # 有這個關鍵字
        target = input_str[location+len(func_key[1]):]
        target = target.lstrip()
    keyword = func_key[0]
    if(keyword == 'call'):#==================================================CALL=======================================V
        if(len(target) == 0):
            return ('FAILED', ('TARGET NOT FOUND'))
        if(isPhoneNumber(target)):
            return ('call', (0, target))
        target_pinyin = lazy_pinyin(target)
        return ('call', (1, target_pinyin))
    elif( keyword == 'add_calender_week'):#==================================ADD_CALENDER_WEEK
        if(len(target) == 0):
            return ('FAILED', ('TARGET NOT FOUND'))
        if(len(target) <= 1):
            return ('FAILED', ('TARGET NOT FOUND'))
        if(target[0] in day_dict.keys()):
            para = time_extract.target_time(target[1:], 0)
            return ('add_calender_week', (day_dict[target[0]], para[0], para[1], para[2]))
        else:
            return ('FAILED', ('DAY_NOT_DEFINED'))
    elif( keyword == 'add_calender_day'):#====================================ADD_CALENDER_DAY
        if(len(target) == 0):
            return ('FAILED', ('TARGET NOT FOUND'))
        para = time_extract.target_time(target, 0)
        return ('add_calender_day', (tuple(para)))
    elif( keyword == 'add_calender'):#========================================ADD_CALENDER
        if(len(target) == 0):
            return ('FAILED', ('TARGET NOT FOUND'))
        para = time_extract.target_time(target, 0)
        return ('add_calender', tuple(para))
    elif( keyword == 'next_calender'):#=======================================NEXT_CALENDER
        return('next_calender', (None))
    elif( keyword == 'read_calender'):#=======================================READ_CALENDER
        para = time_extract.target_time(target, 0)
        return('read_calender', tuple([para[0][5:10]]))
    elif( keyword == 'weather_forecast'):
        target = input_str
        para = time_extract.target_time(target, 1)
        place = para[-1][0:-1*len(func_key[1])]
        if(len(place)==0):
            place = 'HERE'
        return('weather_forecast', tuple([para[0],place] ))
    elif( keyword == 'open_bluetooth'):#======================================OPEN_BLUETOOTH============================
        return('open_bluetooth',())
    elif( keyword == 'close_bluetooth'):#=====================================CLOSE_BLUETOOTH===========================
        return('close_bluetooth',())
    elif( keyword == 'louder_system_value'):
        return('louder_system_value',())
    elif( keyword == 'quiter_system_value'):
        return('quiter_system_value',())
    elif( keyword == 'set_system_value'):
        return('set_system_value')
    else:
        return ('FAILED', ('UNKNOWN KEYWORD'))
        
test_str = 'asd'

def main(input_str):
    print(input_str)
    which = text2func(input_str)
    # if(which[0] == 'UNKNOWN'):
    #     return ('FAILED', ('UNKNOWN KEYWORD'))
    ret = para_extract(input_str, which)
    return ret

print(main('打電話給新增行事曆'))
# print(main('新增行事曆每週二十點都要到學校'))
# print(' ')
# print(main('新增行事曆每天十點十分到十一點都要去上課'))
# print(' ')
# print(main('查詢行事曆十二月十八號'))
# print(' ')
# print(main('天氣怎麼樣'))
# print(' ')
# print(main('台北天氣怎麼樣'))
# print(' ')
# print(main('十一月二十八號天氣怎麼樣'))
# print(' ')
# print(main('明天八點天氣怎麼樣'))
# print(' ')
# print(main('十月十號八點台北天氣怎麼樣'))
# print(' ')
# print(main('窩不知道'))
# print(' ')