class TestIterator:
    def __init__(self):
        self.value = 0

    def next(self):
        if self.value > 10: raise StopIteration
        result = self.value
        self.value += 1
        print 'result is:', result
        return result

    def __iter__(self):
        return self


ti = TestIterator()
list(ti)
