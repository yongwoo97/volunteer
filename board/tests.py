class MyError(Exception):
    def __str__(self):
        return 'error'


def say_nick(nick):
    if nick == 'a':
        raise MyError

c = 3
try:
    say_nick('a')
except MyError as e:
    if c == 3:
        raise
    print(e)