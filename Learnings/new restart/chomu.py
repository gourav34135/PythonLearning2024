####First Come First Serve Simple Implementation ############################################################################
from operator import itemgetter
# 1st step : decide how to store the processes. process(pid,at,bt,ct,tat,wt)
processList = [[1,1,1,-1,-1,-1],[2,2,5,-1,-1,-1],[3,4,2,-1,-1,-1],[4,6,3,-1,-1,-1],[5,7,1,-1,-1,-1]]
#2nd step : sort processList on arrival time
processListSorted = sorted(processList,key=itemgetter(1))
print(processListSorted)
#3rd step : sort processListSorted on processId
processListSortedID = sorted(processListSorted,key=itemgetter(0))
print(processListSortedID)
################################################################################
c = 0
print("=====================================================================")
availableProcesses = []
while (True):
    
    c += 1
print("=====================================================================")
