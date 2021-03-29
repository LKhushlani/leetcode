def boggleBoard(board, words):
    # Write your code here.
    trie  = Trie()
    for words in words:
        trie.add(word)

    finalWords = {}
    visited = [[False for char in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            explore(i, j, trie, visited, finalWords)
    return list(finalWords.keys())

def explore(i, j, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], trieNode. visited, finalWords)

    visited[i][j] = False

    
def getNeighbors(i, j , board):
    if i >0 and j > 0:
        neighbors.append([i-1, j-1])
      
    if i >0 and j > 0:
        neighbors.append([i-1, j-1])

    if i >0 and j > 0:
        neighbors.append([i-1, j-1])

class Trie:

    def __init__(self):
        self.root = {}
        self.endSymbol =  "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]

        current[self.endSymbol] = word




