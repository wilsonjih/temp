import re

percent = re.compile(r'((\d+)|((一百)|(二|三|四|五|六|七|八|九)?((十?(一|二|三|四|五|六|七|八|九))|十)))(趴|%)')

input_str = '系統音量調大九十九趴'

print(percent.search(input_str).group())