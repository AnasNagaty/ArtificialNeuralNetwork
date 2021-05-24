import matplotlib.pyplot as plt


x = [1, 2, -1, -2, -2, 1.5]
y = [1, -2, -1.5, -1, 1, -0.5]
clas = ['A', 'B', 'B', 'B', 'A', 'A']
col = []

w0 = 0 
w1 = 1
w2 = 0.5

n = 0.2
d = 0

def equ(x, y):
    s = w0 + (w1*x) + (w2*y)
    print("S =", s)    
    return s


for i in range(len(x)):
    print(w0,w1,w2)

    if(equ(x[i], y[i]) > 0):
        if(clas[i] == 'A'):
            col.append('y')
        else:
            d = -1
            col.append('b')
            w0 = w0 + (n*d) * 1
            w1 = w1 + (n*d) * x[i]
            w2 = w2 + (n*d) * y[i]

    else:
        if(clas[i] == 'B'):
            col.append('b')
        else:
            d = 1
            col.append('y')
            w0 = w0 + (n*d) * 1
            w1 = w1 + (n*d) * x[i]
            w2 = w2 + (n*d) * y[i]


print("Final Weight: ", w0, w1, w2)
for i in range(len(x)):
    plt.scatter(x[i], y[i], c=col[i])

plt.xlim(-6, 6)
plt.ylim(-6, 6)

plt.axhline(y=0, linestyle='-', c="black", linewidth=0.5)
plt.axvline(x=0, linestyle='-', c="black", linewidth=0.5)

plt.show()
