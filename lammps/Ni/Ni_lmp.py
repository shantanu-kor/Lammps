import lammps_logfile
import matplotlib.pyplot as plt

log = lammps_logfile.File("./log.lammps")
print(log.get_keywords())
a = log.get_num_partial_logs()
b = {"HighCutoff": [], "LowCutoff": [], "MedCutoff": []}
for i in range(a):
    if i%3 == 0:
        b["HighCutoff"].append([log.get('c_ape', i), log.get('Temp', i), log.get('c_ake', i)])
    elif i%3 == 1:
        b["LowCutoff"].append([log.get('c_ape', i), log.get('Temp', i), log.get('c_ake', i)])
    else:
        b["MedCutoff"].append([log.get('c_ape', i), log.get('Temp', i), log.get('c_ake', i)])
c = [[], [], []]
d = [[], [], []]
e = [[], [], []]
for i, j in b.items():
    for k in j:
        if i == "MedCutoff":
            c[0].append(sum(k[0])/len(k[0]))
            d[0].append(sum(k[1])/len(k[0]))
            e[0].append(sum(k[2])/len(k[0]))
        elif i == "LowCutoff":
            c[1].append(sum(k[0])/len(k[0]))
            d[1].append(sum(k[1])/len(k[0]))
            e[1].append(sum(k[2])/len(k[0]))
        else:
            c[2].append(sum(k[0])/len(k[0]))
            d[2].append(sum(k[1])/len(k[0]))
            e[2].append(sum(k[2])/len(k[0]))
for i in range(3):
    fig, axes = plt.subplots(2)
    axes[0].plot(d[i], c[i])
    axes[1].plot(d[i], e[i])
    plt.xlabel('Temperature (K)')
    plt.ylabel('E/atom (eV)')
    if i == 0:
        plt.savefig("MedCutoff")
    elif i == 1:
        plt.savefig("LowCutoff")
    else:
        plt.savefig("HighCutoff")
    plt.show()