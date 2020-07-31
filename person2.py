def Eat(weight):
    weight+=1
    return weight
def Exercise(weight):
    weight -= 1
    return weight
def Speak(name,weight):
    print(name,":",weight,"kg")
name="Jason"
weight=60
weight=Exercise(weight)
Speak(name,weight)