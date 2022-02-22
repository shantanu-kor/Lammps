from turtle import color
import lammps_logfile
import matplotlib.pyplot as plt

log = lammps_logfile.File("./log.lammps")
print(log.get_keywords())
a = log.get_num_partial_logs()
b = list()
c = list()
f = list()
g = list()
h = list()
j = list()
k = list()
print(a)
for i in range(a):
    d = log.get('Temp', i)
    e = log.get('c_ape', i)
    h = log.get('c_ake', i)
    if i%11 == 0:
        b[:] = d
        c[:] = e
        j[:] = h
    else:
        b.append(sum(d)/len(d))
        c.append(sum(e)/len(e))
        j.append(sum(h)/len(h))
    if i%11 == 10:
        f.append(b)
        g.append(c)
        k.append(j)
        b = list()
        c = list()
for i in range(3):
    fig, axes = plt.subplots(2)
    axes[0].plot(f[i], g[i], color='r', label='P/atom (eV)')
    axes[1].plot(f[i], k[i], color='b', label='T/atom (eV)')
    plt.xlabel('Temperature (K)')
    plt.ylabel('E/atom (eV)')
    if i == 0:
        plt.savefig("MedCutoff")
    elif i == 1:
        plt.savefig("LowCutoff")
    else:
        plt.savefig("HighCutoff")
    plt.show()