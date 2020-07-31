def Eat1(person1):
    person1["weight"]+=1
def Eat2(person2):
    person2["weight"] += 2
def Eat3(person3):
    person3["weight"] += 3
def Exercise1(person1):
    person1["weight"]-=1
def Exercise2(person2):
    person2["weight"]-=2
def Exercise3(person3):
    person3["weight"]-=3
def Speak(person):
    print(person)
if __name__=="__main__":
    person1={"name":"Jason","weight":60}
    person2 = {"name": "King", "weight": 60}
    person3 = {"name": "Queen", "weight": 60}
    Speak(person1)
    Speak(person2)
    Speak(person3)