class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Assssh..'
            self.hungry = False
        else:
            print 'No, Thank you, sir!'

class SongBird(Bird):
    def __init__(self):
       super(SongBird, self).__init__() 

b = SongBird()
b.eat()
