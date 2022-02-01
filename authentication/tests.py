import re

mat = re.search('^$', '13')
if mat:
    print('success')
#지금 여기가 실행이 안됬지
# 흠 여기가 실행이 안되었으니
mat1 = re.search('^(?P<pk>[^/.]\d+)', '1234')
print(mat1)
url=r'^{prefix}{trailing_slash}$'

a = url.format(
    prefix = '',
    rommname = '12',
    trailing_slash = ''
)

print(a)

mat = re.search('^$', '')
if mat:
    print('success')

print(mat.groupdict())
print(mat.groups())