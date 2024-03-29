from pypinyin import pinyin, lazy_pinyin
import re
import time
import time_extract
import volume_extract
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
    classname = 'NOT DEFINE'
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
                classname = func_dict[func_name]["class"]
                return [classname, func_name, keyword]
    return [calssname, func_name, 'None']


def para_extract(input_str, func_key):
    location = input_str.find(func_key[2])
    if(location != -1): # 有這個關鍵字
        target = input_str[location+len(func_key[2]):]
        target = target.lstrip()
    keyword = func_key[1]
    if(keyword == 'call'):#==================================================CALL=======================================V
        if(len(target) == 0):
            return (func_key[0], 'FAILED', ('TARGET NOT FOUND'))
        if(isPhoneNumber(target)):
            return (func_key[0], 'call', (0, target))
        target_pinyin = lazy_pinyin(target)
        return (func_key[0], 'call', (1, target_pinyin))
    elif( keyword == 'add_calender_week'):#==================================ADD_CALENDER_WEEK
        if(len(target) == 0):
            return (func_key[0], 'FAILED', ('TARGET NOT FOUND'))
        if(len(target) <= 1):
            return (func_key[0], 'FAILED', ('TARGET NOT FOUND'))
        if(target[0] in day_dict.keys()):
            para = time_extract.target_time(target[1:], 0)
            print(para)
            return (func_key[0], 'add_calender_week', (day_dict[target[0]], para[0], para[1], para[2]))
        else:
            return (func_key[0], 'FAILED', ('DAY_NOT_DEFINED'))
    elif( keyword == 'add_calender_day'):#====================================ADD_CALENDER_DAY
        if(len(target) == 0):
            return (func_key[0], 'FAILED', ('TARGET NOT FOUND'))
        para = time_extract.target_time(target, 0)
        return (func_key[0], 'add_calender_day', (tuple(para)))
    elif( keyword == 'add_calender'):#========================================ADD_CALENDER
        if(len(target) == 0):
            return (func_key[0], 'FAILED', ('TARGET NOT FOUND'))
        para = time_extract.target_time(target, 0)
        return (func_key[0], 'add_calender', tuple(para))
    elif( keyword == 'next_calender'):#=======================================NEXT_CALENDER
        return('next_calender', (None))
    elif( keyword == 'read_calender'):#=======================================READ_CALENDER
        para = time_extract.target_time(target, 0)
        return('read_calender', tuple([para[0][5:10]]))
    elif( keyword == 'weather_forecast'):#====================================WEATHER_FORECAST
        para = time_extract.target_time(target, 1)
        place = para[-1]
        if(len(place)==0):
            place = 'HERE'
        elif(place[0] == '的'):
            place = place[1:]
        return('weather_forecast', tuple([para[0],place] ))
    elif( keyword == 'open_bluetooth'):#======================================OPEN_BLUETOOTH============================
        return('open_bluetooth',())
    elif( keyword == 'close_bluetooth'):#=====================================CLOSE_BLUETOOTH===========================
        return('close_bluetooth',())
    elif( keyword == 'louder_system_volume'):
        para = volume_extract.target_volume(target)
        print(para)
        return('louder_system_volume',(para))
    elif( keyword == 'quiter_system_volume'):
        para = volume_extract.target_volume(target)
        print(para)
        return('quiter_system_volume',(para))
    elif( keyword == 'set_system_volume'):
        return('set_system_volume')
    else:
        print('I DONT KNOW QQQ')
        return (func_key[0], 'FAILED', ('UNKNOWN KEYWORD'))
        
test_str = 'asd'

def main(input_str):
    print(input_str)
    which = text2func(input_str)
    # if(which[0] == 'UNKNOWN'):
    #     return (func_key[0], 'FAILED', ('UNKNOWN KEYWORD'))
    ret = para_extract(input_str, which)
    return ret

# print(main('新增行事曆十一月30號九點30分到十一點三十分要吃晚餐'))
# print(' ')
# print(main('新增行事曆十一月30號點30分到八點三十分要吃晚餐'))
# print(' ')
# print(main('新增行事曆十一月30號九點要吃晚餐'))
# print(' ')
print(main('新增行事曆每週二九點五十九到十一點三十要吃晚餐'))
print(' ')
# print(main('新增行事曆每週二九點30分到八點三十分要吃晚餐'))
# print(' ')
# print(main('新增行事曆每週二要吃晚餐'))
# print(' ')
# print(main('新增行事曆每周四九點九百分要吃晚餐'))
# print(' ')
# print(main('新增行事曆30分到點三十分要吃晚餐'))
# print(' ')
# print(main('新增行事曆九點要吃晚餐'))
# print(' ')
# print(main('下一個行程'))
# print(' ')
# print(main('查看行事曆'))
# print(' ')
# print(main('查看行事曆十二月25號'))
# print(' ')
# print(main('系統音量調大聲-99'))
# print(' ')
# print(main('系統音量調大聲-999'))
# print(' ')
# print(main('系統音量調大聲兩趴'))
# print(' ')
# print(main('新'))
# print(' ')
