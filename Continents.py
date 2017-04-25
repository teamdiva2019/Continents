from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

DATA_RESOLUTION = '10m'
BORDER_THICKNESS = 0.01
LONG_INTERVAL = 0.1
LAT_INTERVAL = 0.1
DPI = 3200

# X = longitude -180 -> 180
# Y = latitude  -90 -> 90

wb = load_workbook('../../ne_' + DATA_RESOLUTION +'_coastline.xlsx')

ws = wb.get_active_sheet()

continents = np.ones((int(360/LONG_INTERVAL), int(180/LAT_INTERVAL)))

rows = iter(ws.rows)
next(rows)  # skip first row

x = []
y = []

fig = plt.figure();

for index, row in enumerate(rows):
    print("Processing row " + str(index))
    
    if(int(row[2].value) == 1):
        plt.plot(x, y, 'k', linewidth=BORDER_THICKNESS)
        x = []
        y = []
    
    x.append((float(row[3].value) + 179)/LONG_INTERVAL)
    y.append((float(row[4].value) + 89)/LONG_INTERVAL)

plt.plot(x, y, 'k', linewidth=BORDER_THICKNESS)

plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.savefig(DATA_RESOLUTION + '-' + str(BORDER_THICKNESS) +'.png', dpi=DPI, bbox_inches = 'tight',
    pad_inches = 0)

print('Done')
