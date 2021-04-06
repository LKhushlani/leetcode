'''
values[i][j] = max{

    values[i-1][j], 
    values [i-1][capacity(j)-weight] + v
    }

'''

def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]

    knapsack  = [[0 for i in range(capacity+1)] for item in range(len(items+1))]
    
    for i in range(1,len(items)+1):
        currentValue = items[i-1][0]
        currentWeight = items[i-1][1]
        for c in range(1,capacity+1):

            if currentWeight >c:
                knapsack[i][c] = max(knapsack[i-1][c],  knapsack[i-1][c-currentWeight] + currentValue)

            else:
                knapsack[i][c]  = knapsack[i-1][c] 

        