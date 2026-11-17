import matplotlib.pyplot as plt
import numpy as np

# load csv
data = np.genfromtxt("June-2021-Provo-River-Streamflow-Rates.csv",
                     delimiter=",", skip_header=1, dtype=str)

# Slice out the columns
x = data[:, 0].astype("datetime64[s]")   # Date/time
y_1 = data[:, 1].astype(float)           # Site 10163000
y_2 = data[:, 2].astype(float)           # Site 10155200
y_3 = data[:, 3].astype(float)           # Site 10155500
y_4 = data[:, 4].astype(float)           # Site 10154200
y_5 = data[:, 5].astype(float)           # Site 10155000

# plot data
# plot site lines
plt.plot(x, y_1, label="Site 10163000")
plt.plot(x, y_2, label="Site 10155200")
plt.plot(x, y_3, label="Site 10155500")
plt.plot(x, y_4, label="Site 10154200")
plt.plot(x, y_5, label="Site 10155000")

# plot title
plt.title("Provo River Streamflow, June 2021")

# plot axis labels
plt.xlabel("Date")
plt.ylabel("Streamflow (cfs)")

# add legend and grid
plt.legend()
plt.grid(True)

plt.show()
