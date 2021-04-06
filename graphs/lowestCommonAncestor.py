# od time O1 space
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # steps
    '''

    :param topAncestor:
    :param descendantOne:
    :param descendantTwo:
    :return:

    calculate the depths of 2 nodes ,
    subtract both
    align the deeper level to the difference and then move both in tandem
    see if both have same ancestors
    '''

    depthOne = getDepth(descendantOne, topAncestor)
    depthTwo = getDepth(descendantTwo, topAncestor)

    if depthOne > depthTwo:
        return backtrackDescendant(descendantOne, descendantTwo, depthOne - depthTwo)

    else:
        return backtrackDescendant(descendantTwo, descendantOne, depthTwo - depthOne)


def getDepth(descendant, topAncestor):
    '''
    :param descendant:
    :param topAncestor:
    :return:
    steps =    d = 0
    start from descented finf the ancestor , iteratively unitil u meet the top ancestors ancestor is none  and calculate heright on the way
              a
         b          c
     d      e   f      g

    '''
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackDescendant(lowerDescendent, higherDescendant, difference):
    while difference > 0:
        lowerDescendent = lowerDescendent.ancestor
        difference -= 1

    while lowerDescendent != higherDescendant:
        lowerDescendent = lowerDescendent.ancestor
        higherDescendant = higherDescendant.ancestor

    return lowerDescendent
