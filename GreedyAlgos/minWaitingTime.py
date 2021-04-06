# [3, 2, 1, 2, 6]  ans = 17
#  approach -> 
#  sort the array 
#  calculate the min waiting time 
#  O nlogn , O1 space 

def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()

    totalWaitingTime = 0 
    for idx, duration in enumerate(queries):
        remaininhQueries = len(queries) -(idx +1)
        totalWaitingTime += remaininhQueries * duration



    return totalWaitingTime
