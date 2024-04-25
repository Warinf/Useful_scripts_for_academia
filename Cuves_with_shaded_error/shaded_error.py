import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Your_data.xlsx')

def plot_curve(xdata, ydata, error_bars, curve_num):
    plt.plot(xdata, ydata, label=f'Curve {curve_num} - Average')
    plt.fill_between(xdata, ydata - error_bars, ydata + error_bars, alpha=0.2)

num_curves = len(df.columns) // 2

for curve_num in range(num_curves):
    y_column = f'Average_{curve_num + 1}'
    error_column = f'stdev_{curve_num + 1}'
    
    ydata = df[y_column]
    error_bars = df[error_column]
    xdata = df['Time']

    plot_curve(xdata, ydata, error_bars, curve_num + 1)

plt.title('Data with Shaded Error Bars for Each Curve')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend(loc='best')
plt.savefig('Your_data.pdf')
plt.show()
