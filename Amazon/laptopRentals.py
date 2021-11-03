'''
[
  [0, 2],
  [1, 4],
  [4, 6],
  [0, 4],
  [7, 8],
  [9, 11],
  [3, 10]
]

starttimes : [0, 0, 1, 3, 4, 7, 9]
endTimes :  [2, 4, 4, 6, 8, 10, 11]
'''
def laptopRentals(times):
    # Write your code here.
    if len(times) == 0:
        return 0

    usedLaptops = 0
    startTimes = sorted([interval[0] for interval in times])
    endTimes = sorted([interval[1] for interval in times])
    print(startTimes)
    print(endTimes)

    startTimeIdx = 0
    endTimeIdx = 0
    while startTimeIdx < len(startTimes):
        if startTimes[startTimeIdx] <= endTimes[endTimeIdx]:
            usedLaptops -=1
            endTimeIdx += 1
        usedLaptops +=1
        startTimeIdx +=1

    print(usedLaptops)
    return usedLaptops
            



laptopRentals([
  [0, 2],
  [1, 4],
  [4, 6],
  [0, 4],
  [7, 8],
  [9, 11],
  [3, 10]
])



