'''
You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house. If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores and houses at the same location.

Example 1:

Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation: 
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.

'''

def findClosest(houses, stores):
    stores = sorted(stores)
    result  = []
    ans = None


    for h in houses:
        l = 0
        r = len(stores) -1
        ans = None

        while True:
            print("In")
            m = (l+r) // 2
            if stores[m] == h:
                ans = stores[m]
                break
            elif r-l <=1 and stores[l] != h and stores[r]!= h:
                break

            elif stores[m] < h:
                l = m
            else:
                r = m

        if ans is None:
            if abs(stores[l]-h) <= abs(stores[r]-h):
                ans = stores[l]
            else:
                ans = stores[r]

        result.append(ans)


    return result

print(findClosest([5, 10, 17], [1, 5, 20, 11, 16]))

        