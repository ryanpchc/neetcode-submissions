class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # if the capacity = length, array is full
        if self.length == self.capacity:
            self.resize()
        
        # put n to next element
        self.arr[self.length] = n

        # increment length
        self.length += 1

    def popback(self) -> int:
        self.length -= 1 # decrement length to point to final element

        return self.arr[self.length] # return pop element

    def resize(self) -> None:
        # 1. Double the capacity
        self.capacity *= 2 

        # 2. Create new list with new capacity
        new_arr = [0] * self.capacity

        # 3. Copy elements from old arr to new arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]

        # 4. Update reference
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity