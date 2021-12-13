import folium
import base64
from folium import IFrame
from data import countcat

'''python file to create the interactive map'''
m = folium.Map(location=[1.357421, 103.817244], zoom_start=12)

tooltip = "Click me!"
cats = countcat()
areas = ["Block 329B Anchorvale Link", "Block 215 Yishun Ave 2", "Block 122 Potong Pasir Ave 1", "Block 575 Pasir Ris Street 52", "Block 182 Stirling Rd" ]
locations = [[1.395591, 103.889387], [1.431540, 103.835421], [1.334867, 103.866453], [1.373606, 103.945900], [1.295049, 103.805330]]

'''for loop to create the interactive marked icons on the map'''

for i in range(len(areas)):
    encoded = base64.b64encode(open('placesimg/' + areas[i] + '.jpg', 'rb').read())
    html = ('<h1>' + areas[i] + '</h1> <img src="data:image/png;base64,{}" width = 200> <p>cats in the area: ' + str(cats[i]) +'</p>').format
    iframe = IFrame(html(encoded.decode('UTF-8')), width=300, height=400)
    popup = folium.Popup(iframe, max_width=300)

    folium.Marker(location= locations[i], tooltip=html, popup = popup, 
    icon=folium.Icon(color = 'gray')).add_to(m)

m.save("map.html")

