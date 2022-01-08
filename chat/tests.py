from django.test import TestCase


class hello:
    def __call__(self, *args, **kwargs):
        print('hi')
        return 3

a = hello()()
print(a)
# Create your tests here.
