import time
start = time.clock()

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Polygon

fig = plt.figure()
ax1 = fig.add_axes([0.2,0.2,0.8,0.8])

#调用Basemap类，创建一个地图
'''
llcrnrlon和llcrnrlat 是左下角的经纬度
urcrnrlon和urcrnrlat 是右上角的经纬度
lat_0和lon_0 是中心点的经纬度
resolution 翻译过来是分辨率，具体指的是什么，还不确定
'''
map = Basemap(llcrnrlon=115.0,
              llcrnrlat=39.2,
              urcrnrlon=118,
              urcrnrlat=41.1,
              resolution='h',
              projection='cass',
              lat_0=40,
              lon_0=116.3,
              ax=ax1)

shp_info = map.readshapefile(r"C:\Users\cz\Desktop\china map\python-code\resources\CHN_adm_shp\CHN_adm1","states",drawbounds=True)
#读取北京市2010-2016年2级以上地震数据，主要是读取经纬度
lon_lat = pd.read_csv(r"C:\Users\cz\Desktop\EQ09_ChinaML2.CSV")
#取出经度列表
lons = list(lon_lat["经度"])
#取出纬度列表
lats = list(lon_lat["纬度"])

for info,shp in zip(map.states_info,map.states):
    proid = info['NAME_1']
    if proid == 'Beijing':
        # poly = Polygon(shp,facecolor='w',edgecolor='c',lw=3)
        # ax1.add_patch(poly)
        # x是经度，y是纬度
        x, y = map(lons, lats)
        map.scatter(x, y, marker='o', color='m')



map.shadedrelief()
map.drawcoastlines() #画出海岸线
end = time.clock()
print(end-start)
plt.show() #打开一个新窗口来显示地图