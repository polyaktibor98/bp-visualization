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

concor_start_date = datetime.strptime("2023.03.24.", "%Y.%m.%d.").date()
concor_stop_date = datetime.strptime("2023.06.16.", "%Y.%m.%d.").date()

plt.title("Blood pressure")
plt.xlabel("Dates")
plt.ylabel("mmHg  &  /min")
plt.plot(dates, systolic, label="SYS", color="blue", linewidth="1")
plt.plot(dates, diastolic, label="DIA", color="green", linewidth="1")
plt.plot(dates, pulse, label="PUL", color="red", linewidth="2")
plt.axvline(x=concor_start_date, color="black", linewidth="2.5")
plt.axvline(x=concor_stop_date, color="black", linewidth="2.5")
plt.legend()
plt.grid(True)
plt.axvspan(concor_start_date, concor_stop_date, facecolor='grey', alpha=0.25)
plt.show()
