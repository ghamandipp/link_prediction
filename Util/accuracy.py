def evaluatePairList(pairL, neighborL):  # nLogn

    iter = 0
    count = 0
    i = 0
    neighborl = len(neighborL)
    pairl = len(pairL)

    while i < pairl:
        if iter >= neighborl:
            break
        if pairL[i] < neighborL[iter]:
            i += 1
        elif pairL[i] == neighborL[iter]:
            count += 1
            iter += 1
            i += 1
        else:
            iter += 1

    return 1.0 * count / len(pairL)
