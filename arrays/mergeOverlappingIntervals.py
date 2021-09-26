def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key = lambda x:x[0])
    result = [intervals[0]]
    for i in range(1,len(intervals)):
        current_interval = result[-1]
        new_interval = intervals[i]
        if current_interval[1] >= new_interval[0]:
            result[-1][1] = max(new_interval[1], current_interval[1])
        else:
            result.append(new_interval)

    return result