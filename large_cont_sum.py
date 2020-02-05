"""
Given an array of integers (positive and negative) find the largest continuous sum.

Problem: Find the largest continuous sum
Example: large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) == 29
          large_cont_sum([1,2,-1,3,4,-1]) == 9
          large_cont_sum([-1,1]) == 1
Algorthim:
Loop through array 
Create two var to keep track of sum


"""


def large_cont_sum(lst):
    largest_sum = lst[0]
    for start in range(len(lst)):
      for stop in range(start,len(lst)):
        current_sum = sum(lst[start: stop + 1]) 
        if current_sum > largest_sum:
          largest_sum = current_sum
    return largest_sum
