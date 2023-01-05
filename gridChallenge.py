def gridChallenge(grid):
    newgrid=[]
    if len(grid)==1:
        return('yes')
    for x in grid:
        x=(sorted(x))
        newgrid.append(x)

    index = 0
    gridindex1=0
    gridindex2=1
    grid1 = newgrid[gridindex1]
    grid2 = newgrid[gridindex2]
    while index<len(grid1):
        val1 = grid1[index]
        val2 = grid2[index]
        if ord(val1)>ord(val2):
            return("no")
        else:
            gridindex1+=1
            gridindex2+=1
        if gridindex2>len(newgrid)-1:
            index+=1
            gridindex1=0
            gridindex2=1
        else:
            grid1=newgrid[gridindex1]
            grid2=newgrid[gridindex2]
    return("yes")

print(gridChallenge(grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
grid3 = ['abc','hjk', 'mpq', 'rtv']
print(gridChallenge(grid3))