# create array customized   
import random                                                                            

class Array:

    def __init__(self, capacity, fill_value=None):
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self,index,new_item):
        self.items[index] = new_item
        
    def __randNumb__(self):
        for i in range(self.capacity):
            self.__setitem__(i,random.randint(0,9))
        return self.items

    def __sum__(self):
        count = 0
        for i in range(self.capacity):
            count += self.items[i]
            return count

if __name__ == "__main__":
    menu = Array(5)
    menu.__setitem__(0,5)
    print(menu.__str__())
    print(menu.__randNumb__())
    print(menu.__sum__())




