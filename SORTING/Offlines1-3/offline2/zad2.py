"""
Rephrased : Find sum of k-biggest elements in all subarrays of T of length p

"""
from zad2testy import runtests


import bisect

def sum_of_k_biggest_in_subarrays(T, p, k):
    n = len(T)
    result = 0
    
    # Initialize the first window and sort it
    window = sorted(T[:p])
    
    # Add the k-th largest element from the first window to the result
    result += window[-k]
    
    for i in range(p, n):
        # Remove the element that is sliding out of the window
        outgoing_element = T[i - p]
        incoming_element = T[i]
        
        # Find and remove the outgoing element from the sorted window
        idx = bisect.bisect_left(window, outgoing_element)
        window.pop(idx)
        
        # Insert the incoming element to the sorted window
        bisect.insort(window, incoming_element)
        
        # Add the k-th largest element from the current window to the result
        result += window[-k]
    
    return result




def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
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

# Efficient for small values of p
def insertion_sort(arr):
    """Sorts the array using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search_insert(sorted_list, value):

    left, right = 0, len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    sorted_list.insert(left, value)

# Remove the first occurrence of value from the sorted_list
def binary_search_delete(sorted_list, value):
    
    left, right = 0, len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    if left < len(sorted_list) and sorted_list[left] == value:
        sorted_list.pop(left)

def sum_of_k_biggest_in_subarrays1(T, p, k):
    n = len(T)
    result = 0
    
    window = T[:p]
    merge_sort(window)
    
    result += window[-k] # merge sort sorts ascending thats why -k
    
    for i in range(p, n):
        # Remove the element that is sliding out of the window
        outgoing_element = T[i - p]
        incoming_element = T[i]
        
        # Remove the outgoing element from the sorted window
        binary_search_delete(window, outgoing_element)
        
        # Insert the incoming element to the sorted window
        binary_search_insert(window, incoming_element)
        
        # Add the k-th largest element from the current window to the result
        result += window[-k]
    
    return result



def ksum(T, k, p):
   # using built-in bin-search, sort
   # return sum_of_k_biggest_in_subarrays(T, p, k)

   return sum_of_k_biggest_in_subarrays1(T, p, k)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
