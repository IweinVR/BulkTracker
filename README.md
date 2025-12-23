# BulkTracker

BulkTracker is een command-line interface (CLI) applicatie geschreven in Python.  
Het project helpt gebruikers tijdens een *bulking phase* om zowel hun **calorie-inname** als **voedingskosten** bij te houden.

De applicatie maakt gebruik van een SQLite-database waarin producten en dagelijkse consumptie worden opgeslagen.

## Features

- **Productbeheer**
  - Voeg voedingsproducten toe met calorieën en prijs
- **Dagboek**
  - Log dagelijkse consumptie
- **Database**
  - SQLite voor persistente opslag
- **Configuratie**
  - Database-instellingen gescheiden via een `settings.json` bestand
- **CLI-gebaseerd**
  - Eenvoudig te gebruiken vanuit de terminal

## Installatie & Setup

Volg deze stappen om het project lokaal te draaien.

#1 Repository clonen

git clone <URL_TO_YOUR_REPO>
cd BulkTracker

#2 Virtuele omgeving aanmaken (aanbevolen)

python -m venv venv
venv\Scripts\activate

#3 Dependencies installeren

pip install -r requirements.txt

#4 Configuratie instellen (BELANGRIJK)

De applicatie verwacht een settings.json bestand.

Zoek settings_example.json in de hoofdmap

Kopieer dit bestand

Hernoem de kopie naar settings.json

Inhoud van settings.json:

{
    "db_name": "data/bulk_data.db"
}

#5 Database initialiseren

Bij de eerste run moet je de database en tabellen aanmaken:

python src/database.py

##Auteur

Iwein Vander Roost
r0999297
Student Toegepaste Informatica – VIVES