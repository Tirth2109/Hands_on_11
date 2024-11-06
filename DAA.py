class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [0] * self.capacity

    def resize(self, new_capacity):
        new_array = [0] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def push_back(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def pop_back(self):
        if self.size > 0:
            self.size -= 1
            if self.size <= self.capacity // 4:
                self.resize(self.capacity // 2)

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of range")

    def set(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def print(self):
        print([self.array[i] for i in range(self.size)])

if __name__ == "__main__":
    dyn_arr = DynamicArray()

    dyn_arr.push_back(1)
    dyn_arr.push_back(2)
    dyn_arr.push_back(3)
    dyn_arr.push_back(4)

    print("Array elements:", end=" ")
    dyn_arr.print()

    print("Element at index 2:", dyn_arr.get(2))

    dyn_arr.set(1, 10)
    print("Array elements after setting index 1 to 10:", end=" ")
    dyn_arr.print()

    dyn_arr.pop_back()
    print("Array elements after pop_back:", end=" ")
    dyn_arr.print()

    print("Size:", dyn_arr.get_size(), ", Capacity:", dyn_arr.get_capacity())
    