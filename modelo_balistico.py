import numpy as np
import scipy.integrate as ode
import matplotlib.pyplot as plt

def modelo(t, Y):

    # parametros
    rho = 0.41
    cd = 0.2
    A = 0.008
    m = 20
    # variables

    h = Y[0]
    v = Y[1]
    
    # derivadas
    dhdt = v
    dvdt = -9.8 -1/2*rho*v*abs(v)*cd*A/m 
    return [dhdt, dvdt]

y0 = [0, 880]
tf = 145
t = np.linspace(0,tf,1000)
y1=ode.solve_ivp(fun=modelo, t_span=[0,tf] ,t_eval=t, y0=y0, method='RK45', atol=1e-7, rtol=1e-8)
ys = y1.y
t = y1.t
yobjetivo = t*0+25000
#plt.plot(t,ys[1]/1000)
plt.plot(t,yobjetivo/1000)
plt.plot(t,ys[0]/1000)
plt.title('Modelo balístico. V0=880 m/s')
plt.xlabel('tiempo [s]')
plt.ylabel('Altura [km]')
plt.show()



