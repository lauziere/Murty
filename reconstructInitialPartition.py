import numpy as np

def reconstructPartition(algoList, idx, idxStrike, curr_solution, nextMat):

	matMemory = [curr_solution[:z+1] for z in range(idx.shape[0]-1)]

	reconstructedPartition = []

	for x in range(len(algoList)):

		assignmSol = algoList[x][0]

		if assignmSol.shape[0] == nextMat.shape[0]:

			assignmFull = assignmSol

			reconstructedPartition.append(assignmFull)

		else:

			if assignmSol.shape[0] == nextMat.shape[0] - 1:

				colsToAddPartition = idxStrike[nextMat.shape[1] - assignmSol.shape[1]-1][:,1]

			else:

				colsToAddPartition = idxStrike[nextMat.shape[1] - assignmSol.shape[1]-1][:,1]

			emptyMat = np.zeros((assignmSol.shape[0], len(colsToAddPartition)), 'int')
			assignmFull = np.concatenate([assignmSol, emptyMat],axis=1)

			colOrder = np.argsort(np.concatenate([np.arange(assignmSol.shape[1]), np.sort(colsToAddPartition)-np.arange(colsToAddPartition.shape[0])-1]), kind='mergesort')

			assignmFull = assignmFull[:, colOrder]

			assignmFull = np.concatenate([matMemory[nextMat.shape[1] - assignmSol.shape[1]-1], assignmFull], axis=0)

			reconstructedPartition.append(assignmFull)

	return reconstructedPartition

def reconstructInitial(reconstructedPartition, colsToAdd, full_solution):

	reconstructedInitial = []

	if len(colsToAdd) > 1:

		matMemory = full_solution[:len(colsToAdd), :]

		for x in range(len(reconstructedPartition)):

			assignmSol = reconstructedPartition[x]

			emptyMat = np.zeros((assignmSol.shape[0], len(colsToAdd)), 'int')

			assignmFull = np.concatenate([assignmSol, emptyMat],axis=1)
			colOrder = np.argsort(np.concatenate([np.arange(1,assignmSol.shape[1]+1), np.sort(colsToAdd)-np.arange(len(colsToAdd))]), kind='mergesort')

			assignmFull = assignmFull[:, colOrder]

			assignmFull = np.concatenate([matMemory, assignmFull], axis=0)

			reconstructedInitial.append(assignmFull)

	else:

		matMemory = full_solution[0,:]

		reconstructedInitial = []

		for x in range(len(reconstructedPartition)):

			assignmSol = reconstructedPartition[x]

			emptyMat = np.zeros((assignmSol.shape[0], len(colsToAdd)), 'int')

			assignmFull = np.concatenate([assignmSol, emptyMat],axis=1)

			col = np.concatenate([np.arange(1, assignmSol.shape[1]+1), np.sort(colsToAdd)-np.arange(len(colsToAdd))])
			colOrder = np.argsort(col, kind='mergesort')
			assignmFull = assignmFull[:,colOrder]
			assignmFull = np.vstack([matMemory, assignmFull])

			reconstructedInitial.append(assignmFull)

	return reconstructedInitial

	

