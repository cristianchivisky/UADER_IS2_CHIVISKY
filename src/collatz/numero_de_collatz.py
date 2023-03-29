import matplotlib.pyplot as plt

def numero_collatz():
    x=[]
    y=[]
    for i in range(1, 10001):
        x.append(i)
        num = i
        cont = 1
        while num != 1:
            cont += 1
            if num %  2 == 0:
                num = num // 2
            else:
                num = num*3 + 1
        y.append(cont)
    return x, y

eje_x, eje_y = numero_collatz()
plt.plot(eje_x, eje_y)
plt.show()