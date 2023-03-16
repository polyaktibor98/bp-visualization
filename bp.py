import matplotlib.pyplot as plt
from datetime import datetime

file = open('bp_data.csv')

data_header = []
data_header = next(file)

data_rows = []
for row in file:
    data_rows.append(row.strip())

dates = []
systolic = []
diastolic = []
pulse = []

for row in data_rows:
    splitted_row = row.split(',')
    dates.append(datetime.strptime(splitted_row[0], "%Y.%m.%d.").date())
    systolic.append(int(splitted_row[1]))
    diastolic.append(int(splitted_row[2]))
    pulse.append(int(splitted_row[3]))

plt.title("Blood pressure")
plt.xlabel("Dates")
plt.ylabel("mmHg  &  /min")
plt.plot(dates, systolic, label="SYS", marker="o", color="blue")
plt.plot(dates, diastolic, label="DIA", marker="o", color="green")
plt.plot(dates, pulse, label="PUL", marker="o", color="red", linewidth="2.5", markersize="8")
plt.legend()
plt.grid(True)
plt.show()
