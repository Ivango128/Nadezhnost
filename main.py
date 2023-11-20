import matplotlib.pyplot as plt

mas_P0 =[]
mas_P1 = []
mas_P2 = []
mas_P3 = []
mas_P4 = []
mas_t = []
def f(P, t):
    P0, P1, P2, P3, P4 = P
    return [f0(P0, P1, P2, P3, P4), f1(P0, P1, P2, P3, P4), f2(P0, P1, P2, P3, P4), f3(P0, P1, P2, P3, P4), f4(P0, P1, P2, P3, P4)]

def f0(P0, P1, P2, P3, P4):
    return -1.4*P0+0.5*P1+4*P2

def f1(P0, P1, P2, P3, P4):
    return -2.5*P1+0.9*P0+P3

def f2(P0, P1, P2, P3, P4):
    return -6*P2+0.5*P0+P4

def f3(P0, P1, P2, P3, P4):
    return -1*P3+2*P1

def f4(P0, P1, P2, P3, P4):
    return -1*P4+2*P2

def eiler(P0, P1, P2, P3, P4, a, b, h):
    global mas_t, mas_P4, mas_P3, mas_P2, mas_P1, mas_P0
    t = a
    while t < b:
        P0 += (f0(P0, P1, P2, P3, P4)*h)
        P1 += (f1(P0, P1, P2, P3, P4)*h)
        P2 += (f2(P0, P1, P2, P3, P4)*h)
        P3 += (f3(P0, P1, P2, P3, P4)*h)
        P4 += (f4(P0, P1, P2, P3, P4)*h)
        mas_P0.append(P0)
        mas_P1.append(P1)
        mas_P2.append(P2)
        mas_P3.append(P3)
        mas_P4.append(P4)
        mas_t.append(t)
        t += h
    print(P0, P1, P2, P3, P4)
    print(P0+P1+P2+P3+P4)



a = 0
b = 100
h = 0.01
P0 = 1
P1 = 0
P2 = 0
P3 = 0
P4 = 0

eiler(P0, P1, P2, P3, P4, a, b, h)

fig, axs = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(10)

axs.grid(color='black',
                linewidth=1,
                linestyle='--')

axs.axis([mas_t[0], mas_t[-1], 0, 1.1])
axs.plot(mas_t, mas_P0, 'pink', label='P0', linewidth=2)
axs.plot(mas_t, mas_P1, 'grey', label='P1', linewidth=2)
axs.plot(mas_t, mas_P2, 'red', label='P2', linewidth=2)
axs.plot(mas_t, mas_P3, 'yellow', label='P3', linewidth=2)
axs.plot(mas_t, mas_P4, 'purple', label='P4', linewidth=2)
axs.legend(loc='upper right')
plt.show()