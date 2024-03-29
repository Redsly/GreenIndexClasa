
import json
import folium, glob

rules = json.load(open("data/biology/recommendations/recomendations.json", encoding="utf8"))


def format_data(data):
    
    title = f"<h1>{data['name']}</h1>"
  #  if data.get('status') is None or len(data['status']) == 0  or data['status'].find("default") != -1:
  #      title = f"<h1>{data['name']}</h1>"
  #   else:
  #      title = f"<h1>{data['name']} - {data['status']}</h1>"
  
    suggestions = ""        
    
    if data.get('type') is not None:
        if data['type'] == "Fish":
            suggestions = rules['fish']
        elif data['type'] == "Plants":
            suggestions = rules['plants']
        else:
            suggestions = rules['animals']

    risc = get_status(data)
    
    if len(risc) > 0:
        risc = f"<img style = \"width:100px; height:100px; \" src = \"{risc}\">" 
    
    
    if len(suggestions) > 0:
        suggestions = f"""
            <br>
            <p align=center style = "font-size:30px;">Sugestii</p>
            <ul>
                <li><p>{suggestions[0]}</p></li>
                <li><p>{suggestions[1]}</p></li>
                <li><p>{suggestions[2]}</p></li>
            </ul>
            <br>
        """
    
    
    html = f'''  
    <div class = "item_second" id = "info">
         <div class="wrapper">
            <div align = right class= "item_first">
                {title}
                {risc}
            </div>
            
            <div class = "item_second">
                 <a href="javascript:void(0)" class="infocbtn prevent-select" onclick="closeInfo()">&times;</a>
            </div>
        </div>

        <p align = left style = "width: 70%">
        {data['description']}
        
        </p>
        
        
        {suggestions}
        
        <div class="slideshow-container">
    
            <div class="mapSlides" width = 50%>
                <img src="{data['images']}" class = "resize">
            </div>
        </div>
        <br>    
    </div>
    </div>
    </div>

    '''
    return html

#
#
#
#
#
#

# BIOLOGY
def read_biology_data(marker_list, animal_group, fish_group, plant_group, reservs_group):
    for j_file in glob.glob("data/biology/protected_species/*.json"):
        if j_file.rfind('template') == -1:
            f = open(j_file, encoding = "utf8")
            js = json.load(f)
            i = 0
            
            spec = None
            
            while i < len(js['location']):
                if js['type'] == 'Animal':
                    spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/pawprint.png',icon_size=(45 , 48)))
                    animal_group.add_child(spec)
                elif js['type'] == 'Fish':
                    spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/acvatic.png',icon_size=(45 , 48)))
                    fish_group.add_child(spec)
                elif js['type'] == 'Plant':
                    spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/frunza.png',icon_size=(45 , 48)))
                    plant_group.add_child(spec)
                i+=1
            
            
            marker_list.append(js)
            
            f.close()
            
    for j_file in glob.glob("data/biology/reservations/*.json"):
        if j_file.rfind('template') == -1:
            f = open(j_file, encoding="utf8")
            js = json.load(f)
            
            poly = folium.Marker(location= js['location'], tooltip=js['name'], name=js['name'],icon = folium.CustomIcon('static/images/frunza.png',icon_size=(45 , 48)))
            reservs_group.add_child(poly)
            marker_list.append(js)
            
            f.close()

# HISTORY   
def read_history_data(marker_list, monument_group, battles_group):
    for j_file in glob.glob("data/history/battles/*.json"):
        if j_file.rfind('template') == -1:
            f = open(j_file, encoding = "utf8")
            js = json.load(f)
            i = 0
            
            spec = None
            
            while i < len(js['location']):
                spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/pawprint.png',icon_size=(45 , 48)))
                battles_group.add_child(spec)
                i+=1
            
            
            marker_list.append(js)
            
            f.close()
            
    for j_file in glob.glob("data/history/monuments/*.json"):
        if j_file.rfind('template') == -1:
            f = open(j_file, encoding = "utf8")
            js = json.load(f)
            i = 0
            
            spec = None
            
            while i < len(js['location']):
                spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/pawprint.png',icon_size=(45 , 48)))
                monument_group.add_child(spec)
                i+=1
            
            
            marker_list.append(js)
            
            f.close()

# RELIGION
def read_religion_data(marker_list, religion_group):
    for j_file in glob.glob("data/religion/*.json"):
        if j_file.rfind('template') == -1:
            f = open(j_file, encoding = "utf8")
            js = json.load(f)
            i = 0
            
            spec = None
            
            while i < len(js['location']):
                spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/pawprint.png',icon_size=(45 , 48)))
                religion_group.add_child(spec)
                i+=1
            
            
            marker_list.append(js)
            
            f.close()


# PHILOSOPHY
def read_philosophy_data(marker_list, philosophy_group):
    for j_file in glob.glob("data/philosophy/*.json"):
        if j_file.rfind('template') == -1:
            f = open(j_file, encoding = "utf8")
            js = json.load(f)
            i = 0
            
            spec = None
            
            while i < len(js['location']):
                spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/pawprint.png',icon_size=(45 , 48)))
                philosophy_group.add_child(spec)
                i+=1
            
            
            marker_list.append(js)
            
            f.close()

# GEOGRAPHY
def read_geography_data(marker_list, geography_group):
    for j_file in glob.glob("data/geography/*.json"):
        if j_file.rfind('template') == -1:
            f = open(j_file, encoding = "utf8")
            js = json.load(f)
            i = 0
            
            spec = None
            
            while i < len(js['location']):
                spec = folium.Marker(location = js['location'][i], tooltip = js['name'], name = js['name'],icon = folium.CustomIcon('static/images/pawprint.png',icon_size=(45 , 48)))
                geography_group.add_child(spec)
                i+=1
            
            
            marker_list.append(js)
            
            f.close()

def format_data_gallery(data):
    
    title = f"<h1>{data['name']}</h1>"


    risc = get_status(data)
   
    
    if len(risc) > 0:
        risc = f"<img style = \"width:100px; height:100px; \" src = \"{risc}\">" 
    
    
    html = f'''  
    <div class = "item_second" id = "info">
         <div class="wrapper">
            <div align = right class= "item_first">
                {title}
                {risc}
            </div>
            
            <div class = "item_second">
                 <a href="javascript:void(0)" class="infocbtn prevent-select" onclick="closeInfo()">&times;</a>
            </div>
        </div>

        <p align = left style = "width: 70%">
        {data['description']}
        
        </p>
        
        <div align=center style = "width: 35%">

            <img src="{data['images']}" style="width:100%; height:300px;">
            
        </div>
        <br>
        
    </div>
        
    </div>
    </div>
    </div>

    '''
    return html


def get_status(data):
    if data.get('status') is not None:
        if data['status'] == "Risc Scazut":
            return "/static/images/Lc.jpg"
        elif data['status'] == "Aproape de pericol":
            return "/static/images/Nt.jpg"
        elif data['status'] == "Vulnerabil":
            return "/static/images/Vu.jpg"
        elif data['status'] == "In pericol":
            return "/static/images/En.jpg"
        elif data['status'] == "Critic":
            return "/static/images/Cr.jpg"
        elif data['status'] == "Extinct in salbaticie":
            return "/static/images/Ew.jpg"
        elif data['status'] == "Extint":
            return "/static/images/Ex.jpg"
    return ""