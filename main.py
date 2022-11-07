
import array as arr
from typing import List


class Agent:
  def __init__(self,size):
    self.size = size
    self.num = []

  def value(self, x):
    return self.num[x]

def isParetoImprovement(agents:List[Agent], option1:int, option2:int)->bool:

    for x in agents:
        if(x.value(option1) < x.value(option2)):
            return False

    return True

def isParetoOptimal(agents:List[Agent], option:int,  allOptions:List[int])->bool:
    for opt in allOptions:
        if option is not opt:
            if isParetoImprovement(agents,option, opt) is False:
                return False
    return True

if __name__ == '__main__':
    a =Agent(2)
    b= Agent(2)
    a.num = [1, 2]
    b.num = [3,1]
    d = [a,b]
    print(bool(isParetoImprovement(d,1,0)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
