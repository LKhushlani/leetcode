def mergeIntervals(intervals):

    result  = []

    for interval in intervals:

        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)

        else:
            result[-1][1] = max(interval[1], result[-1][1])

    return result