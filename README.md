**Min Heap Python Program**

This Python program implements a Min Heap data structure and provides the following functionalities:

**Build Min Heap:** Build a min heap from a list of unsorted elements.
**Insert Element:** Insert new elements into the min heap, avoiding duplicates.
**Pop Root Element:** Remove and return the smallest element (root) from the heap, followed by re-heapification.
**View Heap:** View the current state of the heap.

**How to Run**
Clone the repository or download the heap.py file.
Navigate to the directory where heap.py is located using your terminal or command prompt.

**Run the program:**

*python heap.py*

**Menu Options**

Once you run the program, the following menu will be displayed:

**Build Min Heap**

When you select option 1, you will be asked to input a list of elements separated by spaces to build a min heap.

**Insert Element**

When you select option 2, you will be prompted to enter the elements (separated by spaces) that you want to insert into the heap.
The program will check for duplicates before inserting.

**Pop Root Element**

When you select option 3, the smallest element (root) of the heap will be removed and displayed. The heap will be re-heapified after the pop operation.

**View Heap**

When you select option 4, the current state of the heap will be displayed.

**Exit**

Select option 5 to exit the program.

**Notes**
The program supports input with spaces between elements for building the heap and inserting elements.

The insert method ensures that duplicate values are not added to the heap.

The heap uses bit manipulation for calculating parent and child nodes.

The heap can store elements of various data types (e.g., integers, floats, etc.).
