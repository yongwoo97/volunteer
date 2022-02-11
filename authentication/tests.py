import re


pat = re.compile('(?P<name1>(tom|pot)ato)')
string = 'tomato potato'


mat = pat.search(string)

print(mat.groupdict())
print(mat.group())
print(mat.group(0))
print(mat.group(1))
print(mat.group(2))