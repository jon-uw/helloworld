class Test(object):
    def __init__(self):
        self.test2 = 0

    test = property(test2)

t = Test()
print 't.test = ', t.test
t.test = 10
print 't.test = ', t.test
