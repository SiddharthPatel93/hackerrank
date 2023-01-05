import math
def flippingMatrix(matrix):
    runningsum =0
    m_index1=0
    m_index2=len(matrix)-1
    index1=0
    index2=len(matrix)-1
    while m_index1 <m_index2 :
        if index1>index2:
            m_index1+=1
            m_index2-=1
            index1=0
            index2=len(matrix)-1
        if m_index1>m_index2:
            break
        matrix1 =(matrix[m_index1])
        val1= matrix1[index1]
        val2 = matrix1[index2]
        matrix2 =matrix[m_index2]
        val3 = matrix2[index1]
        val4 = matrix2[index2]
        runningsum += max(val1,val3,val2,val4)
        index1 +=1
        index2-=1
    return runningsum



matrix = [[112, 42, 83, 119], [56, 125, 56, 49],[15, 78, 101, 43], [62, 98, 114, 108]]
print(flippingMatrix(matrix))