#🧠Finding the second largest element.
This project presents 2 solutions to find the second largest unique number in a given array(unsorted).
If no such element exists, it returns -1.

##Note:This project was created as a first step towards open source contribution and a practice problem.

#🔧How to use

Run the script
$ python3 second_largest.py

Sample input
Enter your list, separated by comma: 1,2,3,4
Second largest: 3


#Example
Input: [1, 2, 3, 4]
Output: 3

Input: [2, 3, 4, 3, 4, 3, 4, 5]
Output: 4

Input: [5, 5, 5]
Output: -1

#📌Constraints:
0<=arr[i]<=10^5
1<=len(arr)<=10^5

#Description
##Brute force
Given an array [1,2,3,4]

Now , if the array is sorted and has unique elements, the second largest number is always one index left of the max element , that is, the index is always len(arr)-2.

Consider this example arr=[1,2,3,4,4,4]
In case there are  'x' duplicates of max element , the second max element is present at len(arr)-2-x.So here, there is 3 duplicates,and the index of the second largest element is 6-1-3=2. arr[2] is 3 which is indeed the second largest element.

Consider a third example to demonstrate no second largest
arr=[3,3,3]
In this case, all elements are equal. So the value -1 must be returned.

So we perform the following steps to brute force the problem:
- sort the arr
- initialise i to be last element.
- while i points to the value same as last element and i is greater than or equal to zero
    -decrement i
- if i is greater than or equal to zero
    -return i
-else
    -return -1
Note:The sort(arr) used in code uses in place sorting, so no extra space is utilized.But this causes the original arr to change.

##optimal 
-We know that the second largest is always that value which is less than the first but greater than all other elements in the -arr.This is the key point to be focused on.
-We can identify the largest element (max_element) by iterating through the arr.
-Assume the default second_largest to be -1
-We find the second largest by once more iterating the arr, but this time
    -if arr[i]>second_largest and arr[i] < max_element , then second_largest=arr[i]
-We simply return the second_largest


📁File Structure
Harvard_Shahan/
├── second_largest.py   # Main logic and test cases
├── README.md           # Project overview

🤝 Contributing

Feel free to fork the repo and submit PRs!
This project is beginner-friendly and ideal for those starting out with open source.

📜 License

This project is open source and available under the MIT License.
