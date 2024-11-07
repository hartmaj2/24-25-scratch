import random
import matplotlib.pyplot as plt

n_of_ifs_limit = 20

no_of_reps = 100_000

ifs= []
ratios = []

for ifs_count in range(2,n_of_ifs_limit):
    successes = 0
    for i in range(no_of_reps):
        triggers = 0
        for j in range(1,ifs_count+1):
            if random.randint(1,ifs_count) == j:
                triggers += 1
        if triggers == 1:
            successes += 1
    ifs.append(ifs_count)
    ratios.append(successes/no_of_reps)
print(f"Ifs: {ifs}")
print(f"Ratios: {ratios}")

plt.scatter(ifs,ratios)

for i in range(len(ratios)):
    plt.text(ifs[i],ratios[i],f"{ratios[i]:.3}",ha="left",va="bottom")


plt.xticks(range(0,n_of_ifs_limit))
plt.yticks([x * 0.1 for x in range(0,10)])
plt.show()