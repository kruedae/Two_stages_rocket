import numpy as np
import scipy.integrate as ode
import matplotlib.pyplot as plt

def modelo(t, Y):

    # parametros

    rho = 0.41
    cd = 0.2
    A = 0.008
    ve = 1342
    mdd = 0.5
    mdot1 = mdd
    mdot2 = mdd
    ml = 5
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
    if mp<6:
        dmpdt = -mdot2
        m = mp + ms2 + ml
    if mp <= 0.0:
        dmpdt = 0
    dvdt = -9.8 -1/2*rho*v*abs(v)*cd*A/m -dmpdt*ve/m
    
    return [dhdt, dvdt, dmpdt]

# condiciones iniciales

y0 = [0, 0.0, 12]

# intervalo de tiempo
ti = 0
tf = 90
t_eval = np.linspace(ti,tf,1000)

# metodo de solucion


y1=ode.solve_ivp(fun=modelo, t_span=[ti,tf],t_eval = t_eval , y0=y0, method='RK45', rtol=1e-9)
ys = y1.y
t = y1.t

# graficas
fig, ax = plt.subplots(3)
ax[0].plot(t, ys[0]/1000)
ax[0].set_ylabel('Altura[km]')
ax[0].set_title('Cohete de dos etapas')
ax[1].plot(t, ys[1])
ax[1].set_ylabel('Velocidad[m/s]')
vec_masa = ys[2]
#impresion de la masa
ms2 = 4
for i in range(len(vec_masa)):
    if vec_masa[i]<5:
        vec_masa[i] = vec_masa[i]-ms2
ms1 = 4
ml = 5
vec_masa = vec_masa + ms2 + ms1 + ml
ax[2].plot(t, vec_masa)
ax[2].set_ylabel('Masa[kg]')

plt.show()


