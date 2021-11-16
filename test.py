import time

def final_time(input_str):
	localtime = time.localtime()
	timelist = [localtime[0], localtime[1], localtime[2], localtime[3], localtime[6]]
	if "點" in input_str:
		print(input_str.index("點"))
	return timelist

final_time("明天十點")