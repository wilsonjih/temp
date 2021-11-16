from pypinyin import pinyin
import re
import jieba
# from pygame import mixer
import time


keyword = [
	['打電話給', '撥電話', '打給', 'call'],#call related 
	['查看行事曆', '新增行事曆', '新增提醒'],
]

dec_pinyin = ['líng','yī','èr','sān','sì','wǔ','liù','qī','bā','jiǔ']

def which_language(zh, en):
	for word_list in keyword:
		for word in word_list:
			if(word in zh):
				return zh
			if(word in en):
				return en
	return en
# determine which language to send to text2Function

def text2Function(command):
	command_found = -1
	for word_list in keyword:
		for word in word_list:
			if(word in command):
				# print('THERE IS KEYWORD IN THE STR')
				return keyword.index(word_list)
	print('COMMAND NOT FOUND')
	return -1

def isPhoneNumber(str):
	return re.match(r'\d(-\d)*', str)

def isEnglish(str):
	return re.match(r'[a-zA-z]+', str)

def call_by_name(name):
	print('你要打給聯絡人：' , name)
	return 1

def call_by_number(number):
	print('你要打給號碼：' , number)
	return 1

def call(input_str):
	for word in keyword[which_function]:
		location = input_str.find(word)
		if(location!=-1):
			target = input_str[location+len(word):] 
			#view the string after the keyword as the target
			target = target.lstrip()
			#remove the left space in the target str
			break
		else :
			continue
	if(len(target) == 0):
		print('CALL failed')
		return -1 
		#if there is no left string after the keyword
	if(isPhoneNumber(target)):
		return call_by_number(target) 
		#to see if the target match the re '\d(-\d)*'
	target_pinyin = pinyin(target)
	return call_by_name(target_pinyin)


def calender(input_str):
	#check_calender(date)
	#add_calender(date, target)
	#add_calender_perweek(tm_wday, target)

def ask(input_str):
	print('C')

def dontknow():
	mixer.init()
	mixer.music.load('noCommand.mp3')
	mixer.music.play()
	time.sleep(3)

function_list = [call, calender, ask, dontknow]

def main():
	calender("")
	return
	test_str_zh = "call 小黑"
	test_str_en = "KO Shahi"

	which_function = text2Function(test_str)
	function_list[which_function](test_str)

main()