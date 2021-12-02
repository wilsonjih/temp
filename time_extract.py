import jieba
import datetime
import re
import number_tran as numt


def set_time(newtime):# newtime=[year, month, hour, minute]
	a = datetime.datetime.now()
	time = [a.month, a.day, a.hour, a.minute]
	for i in range(4):
		if (newtime[i] != -1):
			time[i] = newtime[i]
	return ("%04d-%02d-%02d %02d:%02d" %(int(a.year), int(time[0]), int(time[1]), int(time[2]), int(time[3])))

def shift_time(day, hour, minute):
	return (datetime.datetime.now()+datetime.timedelta(days=day, hours=hour, minutes=minute)).strftime("%Y-%m-%d %H:%M")

def target_time(input_str, mode): #return the target time and the place to look later
	date = re.compile(r'((\d+)|(二|三|四|五|六|七|八|九)?十?(一|二|三|四|五|六|七|八|九)?)月((\d+)|(二|三|四|五|六|七|八|九)?十?(一|二|三|四|五|六|七|八|九)?)(日|號)')
	time = re.compile(r'((\d+)|(二|三|四|五|六|七|八|九)?十?(一|二|兩|三|四|五|六|七|八|九)?)(\.|點|時)(((\d+)|(二|三|四|五|六|七|八|九)?十?(一|二|三|四|五|六|七|八|九)?))?')
	later = re.compile(r'((明|後|大後)天)|(((\d+)|(二|三|四|五|六|七|八|九)?十?(一|二|三|四|五|六|七|八|九)?)(週|天|個?小時|分鐘)後)|下週(一|二|三|四|五|六|日|天)?')
	one_99 = re.compile(r'(\d+)|((二|三|四|五|六|七|八|九)?十?(一|二|兩|三|四|五|六|七|八|九)?)')
	target_obj = -1
	# target_str = ''
	time_inter = 0
	time_str = 'NOW'
	month = int(-1)
	day = int(-1)
	hour = int(-1)
	minute = int(-1)
	endhour = int(-1)
	endminute = int(-1)
	time_inter = 0
	result = []
	if(later.search(input_str)):
		target_obj = later.search(input_str)
		target_str = target_obj.group()
		time_str = "1970-01-01 00:00"
		if (target_str=='明天'):
			time_str = shift_time(1, 0, 0)
		elif (target_str=='後天'):
			time_str = shift_time(2, 0, 0)
		elif (target_str=='大後天'):
			time_str = shift_time(3, 0, 0)
		input_str = input_str[target_obj.end():]
		if(time.search(input_str)):
			ntarget_obj = time.search(input_str)
			ntarget_str = ntarget_obj.group()
			minute = 0
			if(ntarget_str.find('點')):
				hour = numt._trans(ntarget_str[:ntarget_str.index('點')])
				if('分' in ntarget_str):
						minute = numt._trans(ntarget_str[ntarget_str.index('點')+1:ntarget_str.index('分')])
			elif(ntarget_str.find('時')):
				hour = numt._trans(ntarget_str[:ntarget_str.index('時')])
				if('分' in ntarget_str):
						minute = numt._trans(ntarget_str[ntarget_str.index('點')+1:ntarget_str.index('分')])
			time_str = time_str[0:11]+("%02d:%02d" %(hour, minute))
			result.append(time_str)
			input_str = input_str[ntarget_obj.end():]
		else:
			if(mode == 0):
				result.append(time_str[0:11]+'00:00')
			else:
				result.append(time_str[0:11]+'06:00')
		if(input_str[0]=='到' and time.search(input_str) and mode == 0):
			if(time.search(input_str)):
				ntarget_obj = time.search(input_str)
				ntarget_str = ntarget_obj.group()
				minute = 0
				if(ntarget_str.find('點')):
					hour = numt._trans(ntarget_str[:ntarget_str.index('點')])
					if('分' in ntarget_str):
						minute = numt._trans(ntarget_str[ntarget_str.index('點')+1:ntarget_str.index('分')])
				elif(ntarget_str.find('時')):
					hour = numt._trans(ntarget_str[:ntarget_str.index('時')])
					if('分' in ntarget_str):
							minute = numt._trans(ntarget_str[ntarget_str.index('點')+1:ntarget_str.index('分')])
				result.append(time_str)
				time_str = time_str[0:11]+("%02d:%02d" %(hour, minute))
				input_str = input_str[ntarget_obj.end():]
		elif(mode == 0):
			result.append(None)
		result.append(input_str)
		return result
		############################################################################ABSOLUTE##############################################
	if(date.search(input_str)):
		target_obj = date.search(input_str)
		month = numt._trans(input_str[target_obj.start():input_str.index('月')])
		# print(month)
		# print(target_obj.group())
		if('日' in target_obj.group()):
			day = numt._trans(input_str[input_str.index('月')+1:input_str.index('日')])
			# print(day)
		elif('號' in target_obj.group()):
			day = numt._trans(input_str[input_str.index('月')+1:input_str.index('號')])
			# print(day)
		input_str = input_str[target_obj.end():]
	if(time.search(input_str)):
		target_obj = time.search(input_str)
		target_str = target_obj.group()
		print(target_str)
		if('點' in target_obj.group() and target_obj.group()[:target_obj.group().index('點')].isnumeric() ):
			hour = numt._trans(input_str[target_obj.start():input_str.index('點')])
			input_str = input_str[input_str.index('點')+1:]
			if( one_99.search(input_str)):
				# print(one_99.search(input_str).group())
				minute = numt._trans(one_99.search(input_str).group())
				input_str = input_str[one_99.search(input_str).end():]
			# if('分' in target_str):
			# 	minute = numt._trans(input_str[:input_str.index('分')])
			# input_str = input_str[input_str.index('分')+1:]
			# print(minute)
			else:
				minute = 0
			# print(hour)
		elif('時' in target_obj.group() and target_obj.group()[:target_obj.group().index('時')].isnumeric()):
			hour = numt._trans(input_str[target_obj.start():input_str.index('時')])
			input_str = input_str[input_str.index('時')+1:]
			if('分' in target_str):
				minute = numt._trans(input_str[:input_str.index('分')])
				input_str = input_str[input_str.index('分')+1:]
				# print(minute)
			else:
				minute = 0
			# print(hour)
		result.append(set_time([month, day, hour, minute]))
	else:
		result.append(shift_time(0, 0, 0))
	if(mode==0 and ('到' or ' 到')in input_str):
		if(time.search(input_str)):
			time_inter = 1
			target_obj = time.search(input_str)
			# print("======TO======")
			if('點' in target_obj.group()):
				endhour = numt._trans(input_str[target_obj.start():input_str.index('點')])
				input_str = input_str[input_str.index('點')+1:]
				# print(endhour)
			elif('時' in target_obj.group()):
				endhour = numt._trans(input_str[target_obj.start():input_str.index('時')])
				input_str = input_str[input_str.index('時')+1:]
				# print(endhour)
			if( one_99.search(input_str)):
				# print(one_99.search(input_str).group())
				endminute = numt._trans(one_99.search(input_str).group())
				input_str = input_str[one_99.search(input_str).end():]
			else:
				endminute = 0
			result.append(set_time([month, day, endhour, endminute]))
		else:
			time_inter = 0
			result.append(None)
	else:
		time_inter = 0
		result.append(None)
	result.append(input_str.lstrip())
	return result
