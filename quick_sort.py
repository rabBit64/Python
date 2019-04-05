#(2)-퀵정렬
def partition(arr, left, right):   
    i_index = left+1 # 왼->오 인덱스
    j_index = right # 오->왼 인덱스
    pivot = arr[left] #pivot은 첫번째 원소
    start = left #pivot 위치
        
    while i_index < j_index:
        if(arr[i_index]<=pivot): #왼쪽에서 오른쪽으로 pivot보다 큰값
            i_index+=1
        if(arr[j_index]>=pivot):#오른쪽에서 왼쪽으로 pivot보다 작은값
            j_index-=1            
        if(i_index<j_index):            
            arr[i_index], arr[j_index] = arr[j_index], arr[i_index] #swap  
        
    if arr[start] > arr[j_index]:
        arr[start], arr[j_index] = arr[j_index], arr[start] #pivot 삽입
    
    print arr, "left:", left, "right", right, "|pivot:", arr[j_index]
    return j_index #pivot위치

def quickSort(arr, left, right):         
    if left <= right:
        mark = partition(arr,left,right) #분할
        quickSort(arr, left, mark-1) #왼쪽 sort   
        quickSort(arr, mark+1, right) #오른쪽 sort
        
        
if __name__=="__main__":
    arr = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
    size = len(arr)

    quickSort(arr, 0, (size-1))   
