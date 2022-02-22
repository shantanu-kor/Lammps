import lammps_logfile
import matplotlib.pyplot as plt

x = ['Al_LowCutoff', 'Al_HighCutoff', 'Al_MedCutoff']
for j in x:
    log = lammps_logfile.File('./'+ j + '/log.lammps')
    print(log.get_keywords())
    a = list()
    b = log.get_num_partial_logs()
    print(b)
    c = 3.8
    average = list()
    d = list()
    for i in range(b):
        try: 
            a.append(log.get('TotEng', i))
            d.append(c)
            c += 0.05
        except: break
    for i in a:
        average.append(sum(i)/(len(i)*2048))
    plt.plot(d, average)
    plt.xlabel('Lattice Constant (A)')
    plt.ylabel('Energy per atom (eV)')
    plt.savefig(j)
    plt.show()