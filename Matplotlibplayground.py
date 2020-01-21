#remember to import matplotlib into the terminal before running code 
#python -m pip install -U matplotlib

import matplotlib.pyplot as plt
import numpy as np

week_days = ("Mon", "Tues", "Wed", "Thur")
index = np.arange(len(week_days))
Number_of_items = (14, 18, 19, 14)
plt.bar(week_days, Number_of_items)
plt.xlabel('Days of the Week')
plt.ylabel('Number of Items on To Do List')
plt.title('To Do List Amounts as of January 13-16')
plt.xticks(index,week_days)
plt.show()
#How to change decimals to whole numbers on y-axis