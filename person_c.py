class Person:

    def __init__(self, name, weight,height, fat_rate=1):
        self.name = name
        self.weight = weight
        self.rate = fat_rate
        self.height = height

    def eat(self):
        self.weight += self.rate

    def exercise(self):
        self.weight -= self.rate

    def speak(self):
        print('%s, weight: %d,height: %d' % (self.name, self.weight,self.height))
    def Health_check(self):
        return self.weight,self.height
def BMI(weight,height,name):
    print(name,",BMI:",weight/((height/100)**2))
if __name__ == '__main__':
    p1 = Person('Kevin', 60,160)
    p2 = Person("King", 60,170,2)
    p3 = Person("Queen", 60,180,3)
    p1.eat()
    p2.eat()
    p3.eat()
    p1.speak()
    p2.speak()
    p3.speak()