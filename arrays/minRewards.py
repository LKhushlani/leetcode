def minRewards(scores):
    # Write your code here.
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] +1
    
    for i in reversed(range(len(scores)-1)):
        print(i)
        print("s", scores[i], 's i+1',scores[i+1])
        if scores[i] > scores[i+1]:
            rewards[i]= max(rewards[i], rewards[i+1]+1) 

    return sum(rewards)

print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))


    
