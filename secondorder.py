def nvalue(a0, a1, a2, n):
    row1 =  vectordefinition(a0, 1)
    row2 =  vectordefinition(a1, 2)
    row3 =  vectordefinition(a2, 3)
    LU = systemsolver(row1, row2, row3)
    return LU[0]*(n**2) + LU[1]*n + LU[2]

def vectordefinition(an, n):
    vector = [n**2, n, 1, an]
    return vector

def systemsolver(row1, row2, row3):
    #find 1s, row 3
    row1 = vectorsubtracter(row1, vectormodifier(row3, 2), 2)
    row2 = vectorsubtracter(row2, vectormodifier(row3, 2), 2)
    row3 = vectormodifier(row3, 2)
    #row2
    row1 = vectorsubtracter(row1, vectormodifier(row2,1),1)
    row2 = vectormodifier(row2,1)
    #row1
    row1 = vectormodifier(row1,0)

    #find zeros, 1s column
    row3 = vectorsubtracter(row3, row1, 0)
    row2 = vectorsubtracter(row2, row1, 0)
    #2 column
    row3 = vectorsubtracter(row3, row2, 1)

    print(row1)
    print(row2)
    print(row3)
    return [row1[3], row2[3], row3[3]]

def vectormodifier(row, n):
    len_vector = len(row)
    if(len_vector > n):
        aux_vector = [0,0,0,0]
        for i in range(len_vector):
            aux_vector[i] = row[i] / row[n]
        return aux_vector
    else:
        return None

def vectorsubtracter(rowx, rowy, n):
    aux_vector = [0,0,0,0]
    for i in range(len(rowx)):
        aux_vector[i] = rowx[i] - (rowx[n] * rowy[i])
    return aux_vector

print(nvalue(1,3,7,1))
print(nvalue(1,3,7,2))
print(nvalue(1,3,7,3))
print(nvalue(1,3,7,4))
