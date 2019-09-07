import folium as fm
import pandas as pd

#pandas 를 이용한 맵에 csv파일로 맵에 데이터 찍기


df = pd.read_csv('data1.csv', encoding='euc-kr')
df.head()

df1 = df.groupby('다발지명').sum().sort_values('발생건수', ascending = False)

m = fm.Map(location = [37,120], zoom_start=15)

for i in range(1, len(df1)):
    fm.Marker([  float(df1['위도'][i]), float(df1['경도'][i]) ], popup=df1.index[i] + i + "등" ).add_to(m)


m.save('test1.html')



