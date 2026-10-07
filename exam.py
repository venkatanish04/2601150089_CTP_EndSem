def merge(arr, left, mid, right):
    global comparisons, merge_operations
    merge_operations += 1
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        comparisons += 1
        if left_part[i] >= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
n = int(input("Enter number of employees: "))
salaries = list(map(int, input("Enter employee salaries: ").split()))
if len(salaries) != n:
    print("Error: Number of salaries does not match N.")
else:
    merge_sort(salaries, 0, n - 1)
    print("\nSorted salaries in ascending order:")
    print(*salaries)
    print("\nNumber of comparisons:", comparisons)
    print("\nTheoretical Time Complexity:")
    print("Best Case    : O(N log N)")
    print("Average Case : O(N log N)")
    print("Worst Case   : O(N log N)")
    print("Space Complexity: O(N)")