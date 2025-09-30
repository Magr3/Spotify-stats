from spotify import dataset
from matplotlib import pyplot as plt # type: ignore

skip_rate_data = []

for record in dataset:
    skip_rate = float(record["skip_rate"])
    skip_rate_data.append(skip_rate)

plt.hist(skip_rate_data, bins=20, alpha=0.7, edgecolor='black')
plt.title('Histogram of Skip Rate')
plt.ylabel('Number of Users')
plt.xlabel('Skip Rate')

plt.show()