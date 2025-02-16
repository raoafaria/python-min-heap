class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) >> 1  # Equivalent to (index - 1) // 2

    def _left_child(self, index):
        return (index << 1) + 1  # Equivalent to 2 * index + 1

    def _right_child(self, index):
        return (index << 1) + 2  # Equivalent to 2 * index + 2

    def build_min_heap(self, elements):
        """Builds a min heap from an unsorted list."""
        self.heap = elements
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify(i)

    def _heapify(self, index):
        """Ensures the heap property for the subtree rooted at index."""
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify(smallest)

    def pop(self):
        """Removes and returns the smallest element from the heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return root

    def insert(self, value):
        """Inserts a new value into the heap, avoiding duplicates."""
        if value in self.heap:
            print(f"Element {value} already exists in the heap.")
            return
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0 and self.heap[self._parent(index)] > self.heap[index]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)
        print(f"Heap after inserting {value}: {self.heap}")  # Debugging step

    def __str__(self):
        return str(self.heap)


def menu():
    heap = MinHeap()
    while True:
        print("\nMin Heap Operations")
        print("1. Build Min Heap")
        print("2. Insert Element")
        print("3. Pop Root Element")
        print("4. View Heap")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            elements = list(map(int, input("Enter the elements separated by space: ").split()))
            heap.build_min_heap(elements)
            print("Heap built successfully.")

        elif choice == "2":
            # Modified insert to handle multiple elements
            elements = list(map(int, input("Enter the elements to insert (separated by spaces): ").split()))
            for element in elements:
                heap.insert(element)
            print(f"Elements {elements} inserted.")

        elif choice == "3":
            popped = heap.pop()
            if popped is not None:
                print(f"Popped element: {popped}")
            else:
                print("Heap is empty.")

        elif choice == "4":
            print("Current heap:", heap)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
