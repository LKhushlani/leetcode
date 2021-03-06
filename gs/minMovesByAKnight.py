class cell:
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist

def isInside(x,y,N):
    if x >0 and x <= N  and y >0 and y <= N:
        return True
    else:
        return False

def minDistanceByAKnight(start, end , N):

    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 

    queue = []

    queue.append(cell(start[0], start[1], 0))
    visited = [[False for i in range(N+1)] for j in range(N+1)]

    visited[start[0]][start[1]]  = True

    while len(queue) >0:

        t = queue[0]
        queue.pop(0)

        if (t.x == end[0] and t.y == end[1]):
            return t.dist

        for i in range(8):

            x = t.x+dx[i]
            y = t.y + dy[i]

            if isInside(x,y,N) and not visited[x][y]:
                visited[x][y] = True
                queue.append(cell(x,y, t.dist+ 1))


if __name__ == '__main__':

    N = 5
    start  = [1,1]
    end = [5,5]
    print(minDistanceByAKnight(start, end, N))


    
    

