from ml_methods.algorithms import LinReg, Predict
from ml_methods.utils import GetData
from ml_methods.matrix import matx
from ml_methods.data import data, datautils
from ml_methods.functions import poly, Poly
import lammps_logfile
import matplotlib.pyplot as plt

r = dict()
x = ['Al_LowCutoff', 'Al_HighCutoff', 'Al_MedCutoff']
for j in x:
    log = lammps_logfile.File('./'+ j + '/log.lammps')
    print(log.get_keywords())
    a = list()
    b = log.get_num_partial_logs()
    c = float(3.8)
    average = list()
    d = list()
    for i in range(b):
        try: 
            a.append(log.get('TotEng', i))
            d.append(float(c))
            c += float(0.05)
        except: break
    for i in a:
        average.append(sum(i)/(len(i)*2048))
    l = GetData.regdata([float(i) for i in average], d)
    l = datautils.powlx(l, [0, ], 2)
    r[j] = LinReg.matrix(l)
    y = Predict.ylinreg(l, r[j]["parameters"])
    p = poly([r[j]["parameters"] , [0, 1, 2]])
    p = Poly.polytoan(Poly.ndpoly(p, 1))
    p = Poly.rootrre(p[0], p[1], 1, [3 + (i / 5) for i in range(10)], 1000, 0.001)
    for i in p.values():
        if i[0] != float('nan'):
            p = i[0]
            break
    ym = Predict.linreg(r[j]["parameters"], [p, p**2])
    plt.plot(d, [i[0] for i in y.matx], '^')
    plt.plot(d, [i[1] for i in y.matx], '--')
    plt.plot([p, ], [ym, ], 'D')
    plt.xlabel('Lattice Constant (A)')
    plt.ylabel('Energy per atom (eV)')
    plt.title(str(r[j])+" minima: "+str(p)+" "+str(ym))
    plt.show()

