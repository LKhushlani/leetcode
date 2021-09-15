def tournamentWinner(competitions, results):
    # Write your code here.
    hashmap = {}
    for idx , team in enumerate(competitions):
        winner = results[idx]
        if winner == 0:
            if competitions[1] not in hashmap:
                hashmap[competitions[1]] = 3
            else:
                hashmap[competitions[1]] +=3
        else:
            if competitions[0] not in hashmap:
                hashmap[competitions[0]] = 3
            else:
                hashmap[competitions[0]] +=3
    print(hashmap)


    return max(hashmap, key = lambda x: hashmap[x])



    
