import folium
centre = [38.80549621582031,-77.04344177246094]

macarte = folium.Map(location = centre,
                     tiles = "OpenStreetMap",
                     zoom_start = 7.5,
                    )

folium.Marker([38.80549621582031,-77.04344177246094],
              icon = folium.Icon(icon = "glyphicon", 
                                 prefix = "glyphicon",
                                 color = "red"),
              popup = "Alexendria"
             ).add_to(macarte)

folium.Marker([33.765991,-84.509751],
              icon = folium.Icon(icon = "glyphicon", 
                                 prefix = "glyphicon",
                                 color = "red"),
              popup = "l'Hopital"
             ).add_to(macarte)

folium.Marker([33.3145415,-84.5425594],
              icon = folium.Icon(icon = "glyphicon", 
                                 prefix = "glyphicon",
                                 color = "red"),
              popup = "ferme d'Hershel"
             ).add_to(macarte)

folium.Marker([33.3806716,-84.7996573],
              icon = folium.Icon(icon = "glyphicon", 
                                 prefix = "glyphicon",
                                 color = "red"),
              popup = "La prison"
             ).add_to(macarte)

folium.Marker([33.72450256347656,-84.3984375],
              icon = folium.Icon(icon = "glyphicon", 
                                 prefix = "glyphicon",
                                 color = "red"),
              popup = "le terminus"
             ).add_to(macarte)

folium.Marker([38.89678,-77.07248],
              icon = folium.Icon(icon = "glyphicon", 
                                 prefix = "glyphicon",
                                 color = "red"),
              popup = "le Royaume"
             ).add_to(macarte)


macarte.save('turbo.js')
