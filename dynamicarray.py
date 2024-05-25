# Implement the following functions for a dynamic array : 

# que1 : Inserts an element at the specified index.

class dynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.resize_factor = resize_factor
    
    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bound")
        self.array.insert(index, element)
        self.size += 1


# que 2 : - Deletes the element at the specified index.

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        del self.array[index]
        self.size-=1


 #que3:- Returns the size of the dynamic array.

    def get_size(self):
        return self.size
    
 #que 4 : - 

    def is_empty(self):
        return self.size == 0
    
#Que 5 : - rotate 

    def rotate(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]


#Que 6 :- 

    def reverse(self):
        self.array.reverse()

#Que 7:- append 

    def append(self, ele):
        self.array.append(ele)
        self.size += 1

#que 8 :- prepend 
    
    def prepend(self, ele):
        self.array.insert(0, ele)
        self.size += 1
        

#Que 9 :-  merge 

    def merge(self, other_array):
        self.array.extend(other_array.array)
        self.size += other_array.size



#que 10 :- find middle 

    def find_middle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]
    
#que 11 :- index of specific value 


    def index_of(self, ele):
        for i in range(self.size):
            if self.array[i] == ele:
                return i
        return -1
    

#Que 14 :-  resize 


    def resize(self, new_resize_factor):
        self.resize_factor = new_resize_factor




    
    


