# A common mistakes that students do in Scratch is, that when they want to pick uniformly at random from n possibilities they:
# Create n if blocks and put into each (pick random (1) to (n))
# Then they hope that this does what it should
# But some cases, this will not trigger any if or trigger more than one!

# The program below shows you the ratio, how many times the program will correctly select exactly one possibility out of 1,...,n ifs

import random
import matplotlib.pyplot as plt

n = 20

trials = 100_000

ifs = []
success_ratio = []

for ifs_count in range(2,n):
    successes = 0
    for i in range(trials):
        triggers = 0
        for j in range(1,ifs_count+1):
            if random.randint(1,ifs_count) == j:
                triggers += 1
        if triggers == 1: # check if exactly one if was triggered 
            successes += 1
    ifs.append(ifs_count)
    success_ratio.append(successes/trials)
print(f"Ifs: {ifs}")
print(f"Ratios: {success_ratio}")

plt.scatter(ifs,success_ratio)

for i in range(len(success_ratio)):
    plt.text(ifs[i],success_ratio[i],f"{success_ratio[i]:.3}",ha="left",va="bottom")


plt.xticks(range(0,n))
plt.yticks([x * 0.1 for x in range(0,10)])
plt.show()