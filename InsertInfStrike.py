import numpy as np

def PartitionAndInsertInf(idx, nextMat, idxmaxSubs):
    
    if idx.shape[0] != 0:
        
        matSub = [nextMat.copy() for i in range(idx.shape[0])]

        for x in range(len(matSub)):

            tmpMat = matSub[x]
            tmpidxMax = idxmaxSubs[x]
            tmpMat[tmpidxMax[0], tmpidxMax[1]] = 1e6

            matSub[x] = tmpMat
        
    else:
        
        matSub = nextMat
        tmpidxMax = idxmaxSubs
        
        matSub[tmpidxMax[0],tmpidxMax[1]] = 1e6
    
    return matSub

def strikeRwsCols(matSub, matSubcolnames, idxStrike):

    if type(matSub) == list:

        for x in range(len(matSub)):

            if x >= 2:

                tmpMat = matSub[x]
                tmpMatcolnames = matSubcolnames[x]

                rowsToRem = idxStrike[x - 1][:, 0]
                colsToRem = idxStrike[x - 1][:, 1]

                tmpMat = np.delete(tmpMat, rowsToRem, axis=0)
                tmpMat = np.delete(tmpMat, colsToRem, axis=1)
                tmpMatcolnames = np.delete(tmpMatcolnames, colsToRem, axis=0)

                matSub[x] = tmpMat
                matSubcolnames[x] = tmpMatcolnames

            elif x == 1:

                tmpMat = matSub[x]
                tmpMatcolnames = matSubcolnames[x]

                rowsToRem = idxStrike[x - 1][0, 0]
                colsToRem = idxStrike[x - 1][0, 1]

                tmpMat = np.delete(tmpMat, rowsToRem, axis=0)
                tmpMat = np.delete(tmpMat, colsToRem, axis=1)
                tmpMatcolnames = np.delete(tmpMatcolnames, colsToRem, axis=0)

                matSub[x] = tmpMat
                matSubcolnames[x] = tmpMatcolnames

            else:

                pass
        
    else:

        matSub = [matSub]
        matSubcolnames = [matSubcolnames]

    return matSub, matSubcolnames