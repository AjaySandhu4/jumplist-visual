from Jumplist import JumpList
from SortedSLL import SortedSLL
import random
import numpy as np

def main():
    # s = SortedSLL()
    # random_array = []
    # for _ in range(25):
    #     random_array.append(random.randint(1, 100))
    # random_array = np.unique(random_array)
    # for i in random_array:
    #     s.insert(i)
    # s.display()
    # j = JumpList(s)
    j = JumpList()
    # j.insert(10)
    # j.insert(20)
    # j.insert(30)
    # j.insert(40)
    # j.insert(3)
    # j.insert(5)
    # j.insert(43)
    # j.insert(45)
    # j.display()
    i = 1
    while i < 150:
        i = i+random.randint(1, 10)
        j.insert(i)
        

    j.create_visualization('before_insert_50')
    j.insert(50)
    j.display()
    j.create_visualization('after_insert_50')
    j.delete(50)
    j.display()
    j.create_visualization('after_delete_50')
    
    
if __name__ == "__main__":
    main()