class a:

    def __init__(self):

        self._user = 1
    def b(self):
        print(self.user)
a1 = a()
print(getattr(a1, '_user'))
