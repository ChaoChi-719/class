from person_c import Person


class Spiderman(Person):
    def __init__(self, muscle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.muscle = muscle

    def climb(self):
        if self.muscle >= 100:
            print('sucess')
            self.muscle -= 1
        else:
            print('false')
            self.muscle -= 2
            if (self.muscle<10) & (self.muscle>0):
                print("You need to be stronger,or you will die.")
            if self.muscle<0:
                print("you're dead")
                exit(0)
        print('剩餘肌力值:', self.muscle)

    def stronger(self):
        self.muscle += 1
        print('肌力值:', self.muscle)


if __name__ == "__main__":
    spiderman = Spiderman(102, "calwer", 60, 180)
    for i in range(200):
        spiderman.climb()

