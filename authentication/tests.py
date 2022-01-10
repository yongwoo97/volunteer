class MyError(Exception):
    def __str__(self):
        return 'error'

def a(b):
    if b == 1:
        raise MyError

try:
    a(1)
except MyError as e:
    print(e)
    print('hello')