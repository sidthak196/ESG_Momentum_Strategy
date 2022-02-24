from itertools import count


def paths(n):
    #size n = mat length - 1
    arr = ['']*(2**n) 
    for i in range(n):
        
        val = 2**i
        count = 0
        temp = 'd'
        for j in range(2**n):
            count= count+1
            if count > val:
                if temp == 'd':
                    temp = 'r'
                else:
                    temp = 'd'
                count = 0
            arr[j] =  arr[j] + temp
    arr = sorted(arr)
    return arr


mat = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
arr = paths(len(mat)-1)
l_mat= len(mat)
dic ={}

for i in range(len(arr)):
    x =0
    y=0
    #UL mat
    p1val = 0
    p1 = ''
    #
    p2val = 0
    p2 = ''
    p3val = 0
    p3 = ''
    p4val = 0
    p4 = ''
    if arr[i].count('d')==2:
        for j in arr[i]:
            if j == 'd':
                x = x+1
                p1 = p1 + j
                p1val = p1val + mat[x][y]
                p2 = p2 + 'u'
                p2val = p2val + mat[l_mat-x-1][y]
                p3 = p3 + j
                p3val = p3val + mat[x][l_mat-y-1]
                p4 = p4 + 'u'
                p4val = p4val + mat[l_mat-x-1][l_mat-y-1]
            else:
                y = y+1
                p1 = p1 + j
                p1val = p1val + mat[x][y]
                p2 = p2 + j
                p2val = p2val + mat[l_mat-x-1][y]
                p3 = p3 + 'l'
                p3val = p3val + mat[x][l_mat-y-1]
                p4 = p4 + 'l'
                p4val = p4val + mat[l_mat-x-1][l_mat-y-1]
        dic[p1] = p1val 
        dic[p2] = p2val
        dic[p3] = p3val
        dic[p4] = p4val    

print(dic)
print(max(dic, key=dic.get))