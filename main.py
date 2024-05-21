from Jumplist import JumpList
from SortedSLL import SortedSLL
import random
import numpy as np

def main():
    s = SortedSLL()
    nums_to_insert = [10, 34, 345, 72, 123]
    random_array = []
    for _ in range(25):
        rand = random.randint(1, 100)
        if rand not in nums_to_insert:
            random_array.append(rand)
    random_array = np.unique(random_array)
    # for i in random_array:
    #     s.insert(i)
    # s.display()
    
    # for i in nums_to_insert:
    #     s.insert(i)
    # j = JumpList(s)
    j = JumpList()
    # for i in random_array:
    #     j.insert(i)
    # j.display()
    # j.create_visualization('build_1 JL')
    # j.insert(0)
    j.create_visualization('initial')
    # for i in range(0, len(nums_to_insert)):
    #     print('\nInserting:', nums_to_insert[i])
    #     j.insert(nums_to_insert[i])
    #     j.display()
    #     j.create_visualization('{}'.format(i))
    for i in random_array:
        print('\nInserting:', i)
        j.insert(i)
    j.display()
    j.create_visualization('random_inserts')
    # j.delete(72)
    # j.display()
    # j.create_visualization('build_2 JL')
    
    # j = JumpList()
    # j.insert(10)
    # j.insert(20)
    # j.insert(30)
    # j.insert(40)
    # j.insert(3)
    # j.insert(5)
    # j.insert(43)
    # j.insert(45)
    # j.display()
    # i = 1
    # while i < 150:
    #     i = i+random.randint(1, 10)
    #     j.insert(i)
        

    # j.create_visualization('before_insert_50')
    # j.insert(50)
    # j.display()
    # j.create_visualization('after_insert_50')
    # j.delete(50)
    # j.display()
    # j.create_visualization('after_delete_50')
    
    
if __name__ == "__main__":
    main()