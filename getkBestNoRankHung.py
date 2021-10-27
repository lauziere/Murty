
import numpy as np
from InsertInfStrike import *
from parseClueOutput import *
from reconstructInitialPartition import *

def getkBestNoRankHung(matNR, k_bestNR):
        
    n = matNR.shape[0]
    matNRcols = np.arange(n)
    
    nextMat = matNR.copy()
    nextMatcols = matNRcols.copy()

    origMatrix = matNR.copy()
    origMatrixcols = matNRcols.copy()
    
    proxy_InfNR = 1e6
    
    i = 0
    
    all_solutions = []
    all_colnames = []
    all_objectives = []
    
    fullMats = []
    fullcols = []
    fullObjs = []
    
    partialSols = []
    partitionsAll = []
    partitionsAllcols = []
    
    colsToAddAll = []
    colsToAdd = []
    
    n_possible = np.math.factorial(n)
    
    solution, objval = parseClueOutput(matNR)
    
    all_solutions.append(solution)
    all_objectives.append(objval)
    
    curr_solution = solution
    full_solution = curr_solution
    
    while i < k_bestNR-1:

        idx = np.vstack([np.arange(curr_solution.shape[0]), np.argmax(curr_solution>0,axis=1)]).T
        idx = np.delete(idx, idx.shape[0]-1, axis=0)

        if idx.shape[0] != 0:
            
            idxStrike = [idx[:z+1, :] for z in range(idx.shape[0]-1)]
            idxmaxSubs = [idx[z, :] for z in range(idx.shape[0])]
            
        else:
            
            idxStrike = np.inf
            idxmaxSubs = idx

        matSub = PartitionAndInsertInf(idx, nextMat, idxmaxSubs)
        matSubcols = [nextMatcols for z in range(idx.shape[0])]

        matSub, matSubcols = strikeRwsCols(matSub, matSubcols, idxStrike)

        matCheck1 = [z for z in range(len(matSub)) if np.any(((matSub[z]==1e6).sum(axis=1))==matSub[z].shape[1])]
        matCheck2 = [z for z in range(len(matSub)) if np.any(((matSub[z]==1e6).sum(axis=0))==matSub[z].shape[0])]
        matCheck = matCheck1 + matCheck2

        if len(matCheck) > 0:
            
            matSub = [matSub[z] for z in range(len(matSub)) if z not in matCheck]
            matSubcols = [matSubcols[z] for z in range(len(matSubcols)) if z not in matCheck]

        if len(matSub) > 0:
            
            partitionsAll = partitionsAll + matSub
            partitionsAllcols = partitionsAllcols + matSubcols

            algoList = [parseClueOutputInf(matSub[z]) for z in range(len(matSub))]

            partialSols = partialSols + [algoList[z][0] for z in range(len(algoList))]
            colsToAddAll = colsToAddAll + [list(set(np.arange(n)) - set(matSubcols[z])) for z in range(len(matSub))]

            reconstructedPartition = reconstructPartition(algoList, idx, idxStrike, curr_solution, nextMat)

            if reconstructedPartition[0].shape[0] != origMatrix.shape[0]:

                reconstructedPartition = reconstructInitial(reconstructedPartition, colsToAdd, full_solution)

            fullObjsTmp = [origMatrix[np.argwhere(reconstructedPartition[z]==1)[:,0],np.argwhere(reconstructedPartition[z]==1)[:,1]].sum() for z in range(len(reconstructedPartition))]

            fullMats.extend(reconstructedPartition)
            fullObjs.extend(fullObjsTmp)


        idxOpt = np.argmin(fullObjs)

        i += 1

        full_solution = fullMats[idxOpt]
        curr_solution = partialSols[idxOpt]
        nextMat = partitionsAll[idxOpt]
        nextMatcols = partitionsAllcols[idxOpt]
        colsToAdd = colsToAddAll[idxOpt]

        all_solutions.append(fullMats[idxOpt])
        all_colnames.append(partitionsAllcols[idxOpt])

        all_objectives.append(fullObjs[idxOpt])

        del fullMats[idxOpt]
        del fullObjs[idxOpt]
        del partialSols[idxOpt]
        del partitionsAll[idxOpt]
        del partitionsAllcols[idxOpt]
        del colsToAddAll[idxOpt]

        if (len(all_solutions) == n_possible) and (k_bestNR > n_possible):

            break

    return np.array(all_solutions), np.array(all_objectives)
