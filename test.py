import jieba
import time

def final_time(input_str):
	localtime = time.localtime()
	timelist = [localtime[0], localtime[1], localtime[2], localtime[3], localtime[6]]
	print(timelist)

print(jieba.lcut("新增行事歷 每週二12點家庭聚餐"))