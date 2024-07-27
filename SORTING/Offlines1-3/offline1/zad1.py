from zad1testy import Node, runtests


def create_list(head):
    mylist = []
    index = 0
    current = head.next
    while current is not None:
        mylist.append((index, current.val))
        current = current.next
        index += 1
    return mylist


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def SortH(p, k):
    # Create list of (index, value) tuples
    mylist = create_list(p)
    
    # Sort the list based on values
    #mylist.sort(key=lambda x: x[1])
    merge_sort(mylist)
    # Extract the original indices in the new sorted order
    sorted_indices = [x[0] for x in mylist]
    
    # Calculate the differences between the original and new indices
    differences = [abs(original_index - i) for i, original_index in enumerate(sorted_indices)]
    
    # Return the maximum difference
    return max(differences)

    

    
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
