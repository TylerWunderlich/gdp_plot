import matplotlib.pyplot as plt
import matplotlib.patches as mplp
import pandas as pd

gdp_data = pd.read_csv('us.csv')
plt.figure(figsize=[16,9])
sorted_gdp_data = gdp_data.sort_values(by=['GDP'], ascending=True)
sorted_gdp_data.set_index(sorted_gdp_data['Region'], inplace=True)

dic = sorted_gdp_data['GDP'].to_dict()
data = list(dic.items())

c = ['red' if i[0].startswith('New York') or i[0].startswith('Mississippi') or i[0].startswith('United States') 
or i[0].startswith('Puerto Rico') else 'blue' for i in data]

plt.barh(sorted_gdp_data['Region'], sorted_gdp_data['GDP'], color = c)
plt.title(label='GDP Per Capita Of Various Countries Versus US Territories', fontdict={'size': 20})
plt.ylabel(ylabel='Region', fontdict={'size': 16})
plt.xlabel(xlabel='GDP Per Capita (US Dollars)', fontdict={'size': 16})
plt.yticks(size=7.5)
blue_patch = mplp.Patch(color = 'blue', label = 'Other Territories')
red_patch = mplp.Patch(color = 'red', label = 'US Territories')
plt.legend(loc = 'center right', handles = [red_patch, blue_patch], fontsize = 12)
plt.show()