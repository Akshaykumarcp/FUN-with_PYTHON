from turtle import color
import colorgram

colors = colorgram.extract('18\image.jpg',30)
print(colors)
""" 
[<colorgram.py Color: Rgb(r=253, g=251, b=248), 74.58622367415028%>, <colorgram.py Color: Rgb(r=254, g=250, b=252), 5.134496420379509%>, <colorgram.py Color: Rgb(r=231, g=251, b=242), 2.3387780635295754%>, <colorgram.py Color: Rgb(r=198, g=12, b=32), 2.120664488774588%>, <colorgram.py Color: Rgb(r=250, g=237, b=17), 1.9085285327031347%>, <colorgram.py Color: Rgb(r=39, g=77, b=189), 1.3044415096962536%>, <colorgram.py Color: Rgb(r=38, g=217, b=67), 1.2251338013484396%>, <colorgram.py Color: Rgb(r=238, g=228, b=5), 1.2149162438312366%>, <colorgram.py Color: Rgb(r=229, g=159, b=46), 1.1185097657607561%>, <colorgram.py Color: Rgb(r=27, g=39, b=158), 1.0582470285674568%>, <colorgram.py Color: Rgb(r=215, g=74, b=12), 0.8731493709598944%>, <colorgram.py Color: Rgb(r=15, g=154, b=16), 0.8096197956488497%>, <colorgram.py Color: Rgb(r=199, g=14, b=10), 0.7785500799332731%>, <colorgram.py Color: Rgb(r=242, g=247, b=252), 0.773962605129631%>, <colorgram.py Color: Rgb(r=244, g=33, b=165), 0.7209286161117675%>, <colorgram.py Color: Rgb(r=229, g=17, b=122), 0.6792938069090151%>, <colorgram.py Color: Rgb(r=73, g=9, b=31), 0.6244526308472927%>, <colorgram.py Color: Rgb(r=60, g=14, b=8), 0.4394244804337249%>, <colorgram.py Color: Rgb(r=224, g=141, b=211), 0.3801348439563495%>, <colorgram.py Color: Rgb(r=222, g=160, b=8), 0.3423229304232988%>, <colorgram.py Color: Rgb(r=10, g=98, b=61), 0.33947313546952107%>, <colorgram.py Color: Rgb(r=17, g=18, b=43), 0.2687843191770348%>, <colorgram.py Color: Rgb(r=47, g=214, b=232), 0.25460485160214086%>, <colorgram.py Color: Rgb(r=11, g=227, b=239), 0.15270730520608883%>, <colorgram.py Color: Rgb(r=79, g=72, b=215), 0.13901438798915688%>, <colorgram.py Color: Rgb(r=237, g=155, b=222), 0.13324529088760687%>, <colorgram.py Color: Rgb(r=73, g=213, b=169), 0.09870021547230137%>, <colorgram.py Color: Rgb(r=78, g=234, b=201), 0.07986376589977062%>, <colorgram.py Color: Rgb(r=50, g=234, b=244), 0.05240842427191215%>, <colorgram.py Color: Rgb(r=3, g=66, b=40), 0.049419614930145274%>] """

rgb_colors = []
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)
""" 
[Rgb(r=253, g=251, b=248), Rgb(r=254, g=250, b=252), Rgb(r=231, g=251, b=242), Rgb(r=198, g=12, b=32), Rgb(r=250, g=237, b=17), Rgb(r=39, g=77, b=189), Rgb(r=38, g=217, b=67), Rgb(r=238, g=228, b=5), Rgb(r=229, g=159, b=46), Rgb(r=27, g=39, b=158), Rgb(r=215, g=74, b=12), Rgb(r=15, g=154, b=16), Rgb(r=199, g=14, b=10), Rgb(r=242, g=247, b=252), Rgb(r=244, g=33, b=165), Rgb(r=229, g=17, b=122), Rgb(r=73, g=9, b=31), Rgb(r=60, g=14, b=8), Rgb(r=224, g=141, b=211), Rgb(r=222, g=160, b=8), Rgb(r=10, g=98, b=61), Rgb(r=17, g=18, b=43), Rgb(r=47, g=214, b=232), Rgb(r=11, g=227, b=239), Rgb(r=79, g=72, b=215), Rgb(r=237, g=155, b=222), Rgb(r=73, g=213, b=169), Rgb(r=78, g=234, b=201), Rgb(r=50, g=234, b=244), Rgb(r=3, g=66, b=40)] """

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    temp_color = (r,g,b)
    rgb_colors.append(temp_color)

print(rgb_colors)
""" 
[(253, 251, 248), (254, 250, 252), (231, 251, 242), (198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61), (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169), (78, 234, 201), (50, 234, 244), (3, 66, 40)] 

"""
