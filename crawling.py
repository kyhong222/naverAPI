import folium

map_osm = folium.Map(location=[37.566345, 126.977893])
map_osm.save('d:/temp/chicken_data/map1.html') #파일이 저장될 위치
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
map_osm.save('d:/temp/chicken_data/map2.html')