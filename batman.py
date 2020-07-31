from person_c import Person

class Batman(Person):
    def __init__(self,deposit,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.deposit=deposit

if __name__=="__main__":
    b=Batman(10000,"Bad",100,199)
    b.speak()