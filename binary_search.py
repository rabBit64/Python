#(1)-이진탐색 함수
def binary_search(list, target):
    first_index = 0
    last_index = len(list)-1
    
    while(first_index<=last_index):
        middle = int(round((first_index+last_index)/2)) #중간값 반올림, 정수
        if(list[middle]<target): #중간값보다 찾는값이 크면 우측
            first_index = middle+1
        elif(list[middle]>target): #중간값보다 찾는값이 작으면 좌측
            last_index = middle-1
        elif(list[middle]==target): #값이 같으면 인덱스 반환
            return middle
    return None
    
if __name__=="__main__":
    list = [1, 11, 15, 19, 37, 48, 59, 61] #오름차순 정렬된 배열
    s = input('Input number : ')
    target = int(s)
    result = binary_search(list, target)
    print("Order : %s" % result)
