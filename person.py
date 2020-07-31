def Eat(person):
    person["weight"]+=1
def Exercise(person):
    person["weight"]-=1
def Speak(person):
    print(person)
if __name__=="__main__":
    person={"name":"Jason","weight":60}
    Exercise(person)
    Speak(person)