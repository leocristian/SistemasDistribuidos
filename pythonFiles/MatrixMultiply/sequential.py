import time
import random

class Matrix:
    def __init__(self, matLen):
        self.mat = []
        # Preencher matriz 100X100 com valores aleatórios
        for i in range(0, matLen):
            arrLin = []
            for j in range(0, matLen):
                arrLin.append(random.randint(0, 10000000))
            self.mat.append(arrLin)

        # self.qtLin = len(self.mat)
        # self.qtCol = len(self.mat[0])
    
    def show(self, msg):
        print(msg)
        for i in self.mat:
            print(i)

    def getLine(self, n):
        return [i for i in self.mat[n]]

    def getColumn(self, n):
        return [i[n] for i in self.mat]

    def __mul__(self, mat2):
        matRes = []

        for i in range(self.qtLin):           
            matRes.append([])

            for j in range(mat2.qtCol):
                listMult = [x*y for x, y in zip(self.getLine(i), mat2.getColu(j))]
                matRes[i].append(sum(listMult))

        return matRes

len = int(input("Informe o tamanho da matriz (NXN): "))

mat1 = Matrix(len)
mat2 = Matrix(len)

print(mat1.show('Matriz 1'))
print(mat2.show('Matriz 2'))

# print('Result')
# print(mat1*mat2)