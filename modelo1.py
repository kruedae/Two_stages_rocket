import numpy as np
import scipy.integrate as ode
import matplotlib.pyplot as plt

def modelo(t, Y):

    # parametros

    rho = 1.25
    cd = 0.1
    A = 0.8
    ve = 720
    mdot1 = 1
    mdot2 = 2
    ml = 2
    ms1 = 4
    ms2 = 4

    # variables

    h = Y[0]
    v = Y[1]
    mp = Y[2]
    m = mp + ms1 + ms2 + ml

    # derivadas

    dhdt = v
    dmpdt = -mdot1
    if mp<10:
        dmpdt = -mdot2
        m = mp + ms2 + ml
    if mp <= 0.0:
        dmpdt = 0
    dvdt = -9.8 -1/2*rho*v*abs(v)*cd*A/m -dmpdt*ve/m
    
    return [dhdt, dvdt, dmpdt]

# condiciones iniciales

y0 = [0, 0.0, 20]

# intervalo de tiempo

t = (0,50)

# metodo de solucion

y1=ode.solve_ivp(fun=modelo, t_span=t, y0=y0, method='RK45', rtol=1e-9)
ys = y1.y
t = y1.t

# graficas
fig, ax = plt.subplots(3)
ax[0].plot(t, ys[0])
ax[0].set_title('Altura')
ax[1].plot(t, ys[1])
ax[1].set_title('Velocidad')
ax[2].plot(t, ys[2])
ax[2].set_title('Masa')

plt.show()


