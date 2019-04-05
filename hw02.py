#-*-coding: utf-8-*-

def partition(list, start, end):
    i_index = start #왼쪽부터 pivot보다 큰 원소 찾는 인덱스
    j_index = end #오른쪽부터 pivot보다 작은 원소 찾는 인덱스
    pivot = list[start] #첫번째 원소를 pivot으로

    while(i_index<=j_index):
        if(list[i_index]<=pivot): #pivot보다 큰 원소 나타날 때까지 i_index 증가
            i_index+=1
        if(list[j_index]>=pivot): #pivot보다 작은 원소 나타날 때까지 j_index 감소
            j_index-=1
        list[i_index], list[j_index] = list[j_index], list[i_index]
    #i 인덱스가 j 인덱스보다 커지면 i 인덱스 원소와 pivot 원소 교환
        
    

#def quick_sort(list, start, end)
#    if(start<end)
        
        

if __name__=="__main__":
    list = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
    partition(list, 0, len(list)-1)
    for i in range (len(list)):
        print list[i],
    #quick_sort(list, 0, len(list))
