class MyError(Exception):
    def __str__(self):
        return 'error'


def say_nick(nick):
    if nick == 'a':
        raise MyError

#예외처리시 raise하면 파이썬실행이 멈춘다.
c = 3
try:
    say_nick('a')
except MyError as e:
    print(e)


import re

raw_string = 'woo2!2661@naver.com'
pat = '(?P<first>.+)(?P<last>@[a-z]+[^.][a-z]{3})'

result = re.search(pat, raw_string)
print(result.group())


print(callable(MyError))
