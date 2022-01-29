import re

test_string = "tomato potato"
pat = '(?P<grouper>(tom|pot)ato)'

mat = re.findall(pat, test_string)
print(mat)


di = {1 : 3}
print(di[1])