# Min-Vaer_App

Jeg brukt python for backend og HTML/CSS for frontend og bruker Ubuntu for kjøring. 

På forhånd kan det være lurt å laste ned Python3, rammeverket Flask samt pip(for å enkelt hente andre pakker om nødvendig). 

For å skape mitt virtuelle miljø brukte jeg følgende kommandoer:

pip3 install virtualenvwrapper-win
pip3 install virtualenv

Jeg lagde en requirements.txt for å holde orden på hvilke biblioteker jeg brukte, som blant annet Flask med versjon.
API-nøkkelen hentet jeg på OpenWeatherMap.com

koden kjøres med:

python3 main.py i designert mappe. 

På kjøring vil man få opp main-siden samt resultat-siden etter endt kjøring. Weather.hmtl og result.html er sidene som populerer det visuelle. 
Ved kjøring vil man også få opp følgende data:

Ved valget 'Drammen' hentes været fra openweathermap og viser det visuelt fram som navn, land samt temperatur. Ved kjøring i Ubuntu får vi en hel der mer data. 

http://api.openweathermap.org/data/2.5/weather?q=Drammen&mode=json&units=metric&appid=3d0207bf25d9c175e45bb63a4b03d0c9
{'base': 'stations',
 'clouds': {'all': 90},
 'cod': 200,
 'coord': {'lat': 59.74, 'lon': 10.2},
 'dt': 1551917145,
 'id': 3159016,
 'main': {'humidity': 92,
          'pressure': 991,
          'temp': -0.33,
          'temp_max': 1.11,
          'temp_min': -2.22},
 'name': 'Drammen',
 'rain': {'1h': 0.25},
 'snow': {'1h': 0.04},
 'sys': {'country': 'NO',
         'id': 1679,
         'message': 0.0041,
         'sunrise': 1551938444,
         'sunset': 1551978062,
         'type': 1},
 'visibility': 4000,
 'weather': [{'description': 'light rain',
              'icon': '10n',
              'id': 500,
              'main': 'Rain'},
             {'description': 'light snow',
              'icon': '13n',
              'id': 600,
              'main': 'Snow'},
             {'description': 'light intensity drizzle',
              'icon': '09n',
              'id': 300,
              'main': 'Drizzle'}],
 'wind': {'deg': 50, 'speed': 2.1}}
