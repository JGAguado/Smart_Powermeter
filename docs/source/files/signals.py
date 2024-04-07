from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import numpy as np


host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)

host.set_xlim(0, 15)
host.set_ylim(-100, 110)

host.set_xlabel("Time")
host.set_ylabel("Current [A]")
par1.set_ylabel("Current [mA]")
par2.set_ylabel("Voltage [V]")

x = np.linspace(0, 5 * np.pi, 1000)
y1 = 100 * np.sin(x)
y2 = 50 * np.sin(x)
y3 = 1.65 + 1.1 * np.sin(x)

rms = np.sqrt(np.mean(y3**2))
print(rms)

p1, = host.plot(x, y1, label="Input CT")
p2, = par1.plot(x, y2, label="Output CT")
p3, = par2.plot(x, y3, label="Measured ADC")

par2.axhline(y=rms, color='g', linestyle='--', label='RMS computed')

par1.set_ylim(-60, 60)
par2.set_ylim(0, 3.3)

host.legend(loc='upper right')

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

plt.draw()
plt.show()