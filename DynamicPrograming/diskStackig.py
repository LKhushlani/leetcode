# On2 time , On space
def diskStacking(disks):
    disks.sort(key = lambda disk: disk[2])

    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightIdx = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]

            if checkStrictness(currentDisk, otherDisk):
                if heights[i] <= currentDisk[2]+ heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i]  = j

        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i
    return buildSequence(sequences, maxHeightIdx, disks)

def buildSequence(sequences, currentIdx, disks):
    sequence = []
    print("sequences", sequences, currentIdx)
    while currentIdx is not None:
        sequence.append(disks[currentIdx])
        currentIdx = sequences[currentIdx]
        print("current idx", currentIdx)
	
	print(list(reversed(sequence)))
    return list(reversed(sequence))


def checkStrictness(c, o):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]



