#(3)-merge sort
def merge(left_arr, right_arr):
    result = []
    left_length = len(left_arr)
    right_length = len(right_arr)
    
    left_idx = 0
    right_idx = 0
    while left_length > left_idx and right_length > right_idx:
        if left_arr[left_idx] < right_arr[right_idx]:
            result.append(left_arr[left_idx])
            left_idx += 1
        else:
            result.append(right_arr[right_idx])
            right_idx += 1
            
    if left_length != left_idx:
        while left_length != left_idx:
            result.append(left_arr[left_idx])
            left_idx += 1

    if right_length != right_idx:
        while right_length != right_idx:
            result.append(right_arr[right_idx])
            right_idx += 1
    
    return result
            
def merge_sort(arr, left, right):
    if left == right:
        return [ arr[left] ]
    if left < right:
        mid = (left + right) // 2
    
        left_arr = merge_sort(arr, left, mid)
        right_arr = merge_sort(arr, mid+1, right)
            
        return merge(left_arr, right_arr)
    
if __name__ =="__main__":
    arr = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
    sorted_arr = merge_sort(arr, 0, (len(arr)-1))

for i in range(len(arr)): 
    print sorted_arr[i], 
