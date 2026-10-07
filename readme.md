Enter number of employees: 2
Enter employee salaries: -20 50

Sorted salaries in ascending order:
50 -20

Number of comparisons: 31

Theoretical Time Complexity:
Best Case    : O(N log N)
Average Case : O(N log N)
Worst Case   : O(N log N)
Space Complexity: O(N)


VIVA QUESTIONS :

What is Merge Sort?
Merge Sort is a divide-and-conquer sorting algorithm that divides an array into smaller parts, sorts them, and then merges them.

What is the time complexity of Merge Sort?
The best, average, and worst-case time complexity is O(N log N).

What is the space complexity of Merge Sort?
Merge Sort requires O(N) auxiliary space because temporary arrays are used during merging.

How many merge operations are performed for N elements?
For N elements, Merge Sort generally performs N − 1 merge operations when N is a power of 2.

Why is Merge Sort better than Bubble Sort for large data?
Merge Sort has O(N log N) time complexity, while Bubble Sort has O(N²) average and worst-case complexity, making Merge Sort more efficient for large datasets.