from Spiderman import Spiderman
from batman import  Batman
class Superman(Spiderman,Batman):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def stronger(self):
        self.muscle+=3
        print("肌力值:",self.muscle)
if __name__=="__main__":
    superman=Superman(200,300000000,"super",90,180)
    for i in range(100):
        superman.climb()
    superman.speak()
    superman.stronger()