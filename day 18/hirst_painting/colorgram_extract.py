import colorgram

colors = colorgram.colorgram.extract('hirst_spot_painting.jpeg', 30)
set_rgb = []
for i in range(len(colors)):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    set_color = (r, g, b)
    set_rgb.append(set_color)

print(set_rgb)