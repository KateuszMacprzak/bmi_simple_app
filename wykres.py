import matplotlib.pyplot as plt
import numpy as np

results = [2,39,38,21]
names = ['niedowaga','waga prawidłowa','nadwaga','otyłość']

plt.bar(names,results, width=0.25)
plt.title('BMI - POLSKA')
plt.savefig('poland_bmi')