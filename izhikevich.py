from brian2 import *
from scipy import stats


start_scope()
number = 1 #number of neurons
#a = 0.02/ms

b = 0.2/ms
c = -65 * mV
#d = 6*mV/ms
I = 15*mV/ms


#Neuronal equations of the Izhikevich-neuron
eqs = '''
dv/dt = (0.04/ms/mV)*v**2+(5/ms)*v+140*mV/ms-u+I : volt
du/dt = a*(b*v-u)                                : volt/second
a                                                : 1/second
d                                                : volt/second


'''


reset = '''
v = c
u = u + d
'''


#Set up neuron population
G = NeuronGroup(number,eqs,threshold='v >= 30*mV',reset=reset,method='euler')
G.a = 0.02/ms
G.d = 8*mV/ms
G.v = c
G.u = b * c


M = StateMonitor(G,'v', record=True)


run(100*ms)


figure
plot(M.t/ms, M.v[0])
xlabel('Time (ms)')
ylabel('v');

show()
