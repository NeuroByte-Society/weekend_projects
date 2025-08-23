'''
PROBLEM: TO FIND THE SECOND LARGEST ITEM IN A GIVEN ARRAY
DESCRIPTION: Given an unsorted array of positive numbers, return the second largest item.If no such item is found, return -1
testcase 1 
input arr=[1,2,3,4]
output:3
testcase 2
input arr=[2,-1,3,4,3,4,3,4,5]
output: 4
CONSTRAINTS
0<=arr[i]<=10^5
1<=len(arr)<=10^5
EXPECTED COMPLEXITIES:
TIME:O(n)
SPACE:O(1)
'''




#Solution 1
from typing import List
def brute_force(arr:List[int])->int:
    #Brute force

    #Use in place sorting algorithm to sort the array , so that extra space is not utilized
    arr.sort()
    #return the first value that is not equal to the value present in the last index(max value)
    max_value=arr[-1] #max value
    i=len(arr)-1 
    while(i>=0 and arr[i]==max_value):#as long as the current index's value is equal to max value and current index is valid(i.e greater than or equal zero)
        i-=1 #move the index towards zero
    if(i>=0):#valid index
        return arr[i]
    else:#invalid , all elements were the max element
        return -1
'''
Analysis
Time complexity: O(nlogn)
Reason:          Performing a sort is O(nlogn) and a search to find the second largest is O(n)
                            => O(nlogn + n)
                            => O(nlogn)
Auxilary space complexity: O(1)
Reason:                    No extra space is used
'''




#solution 2
def optimal_soln(arr:List[int])->int:
    #optimal solution

    #identify the max element of arr
    max_element=max(arr)
    #now let second_max be initialised to be -1 because if we do not find a second max we automatically -1
    second_max=-1
    #traverse the array
    for i in range(len(arr)):
        #if current element is greater than the current second_max element and less than the max element
        if(arr[i]>second_max and arr[i]<max_element):
            #replace second max with the current element
            second_max=arr[i]
    return second_max
'''
Analysis
Time complexity: O(n)
Reason:          Finding max element takes O(n), finding the second max takes another O(n)
                            => O(n + n)
                            => O(n)
Auxilary space complexity: O(1)
Reason:                    No extra space is used
'''




if __name__ == "__main__":
    arr=list(map(int,input("Enter your list,seperated by comma : ").split(",")))
    print(arr)
    print(optimal_soln(arr))
    

    


