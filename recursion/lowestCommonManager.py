On time Od space
 
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports  = 0
	for directReport in manager.directReports:
		print("dir", directReport.name)
        orgInfo =  getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
		print("manager:", manager.name)

    if manager == reportOne or manager == reportTwo:
            numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numImportantReports)

class OrgInfo:
	def __init__(self, lowestCommonManager, numImportantReports):
		self.lowestCommonManager = lowestCommonManager
		self.numImportantReports = numImportantReports

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []



		
# 		A
#    B          c

# D     E     F   G 


# H   I
		
	
# A [ b c]

# B  [ D E]
# D  [H I]
# H
# []


# I
# []
# E
# []
# LCM = none





