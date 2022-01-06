import re

m = re.match(r'(?P<parameter>[0-9]+) ([0-9]+)', '10 123')
print(m.group(1))
print(m.group(2))
print(m.group(0))
print(m.group())
print(m)
print(m['parameter'])
dict1 = {'a' : 1}
a = [1,2,3]
print(*a)

#이렇게 하면 딕셔너리가 나오네?
prac_dict = {**{'a' : '1'}, **{'b':'2'}}
print(prac_dict)

class hello:
    def __init__(self):
        self.a = 1

    b = 2
    @classmethod
    def view1(self):
        print('k')
        print('시작되었습니다')

    def view2(self):
        print('sfjsg')
t = getattr(hello, 'view2', hello)
hello.view1()
t()