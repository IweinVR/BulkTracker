import pandas as pd
import os
from datetime import datetime

class RapportGenerator:
    def __init__(self, db_manager):
        self.db = db_manager

    def maak_excel_rapport(self):
        print("Gegevens ophalen en berekenen...")
        
        data = self.db.haal_alle_consumpties()
        
        if not data:
            print("Er is nog geen data om te rapporteren!")
            return

        kolommen = ['Datum', 'Product', 'Hoeveelheid (gram)', 'Kcal/100g', 'Prijs/kg']
        df = pd.DataFrame(data, columns=kolommen)

        df['Totaal Kcal'] = (df['Hoeveelheid (gram)'] / 100) * df['Kcal/100g']
        
        df['Totaal Prijs (€)'] = (df['Hoeveelheid (gram)'] / 1000) * df['Prijs/kg']

        totaal_kcal = df['Totaal Kcal'].sum()
        totaal_prijs = df['Totaal Prijs (€)'].sum()
        
        bestandsnaam = f"BulkRapport_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
        
        try:
            pad = os.path.join(os.path.dirname(os.path.dirname(__file__)), bestandsnaam)
            
            df.to_excel(pad, index=False)
            print(f"\nSucces! Rapport is opgeslagen als: {bestandsnaam}")
            print(f"Totaal gegeten: {totaal_kcal:.0f} kcal")
            print(f"Totale kosten: € {totaal_prijs:.2f}")
            
        except Exception as e:
            print(f"Er ging iets mis bij het opslaan: {e}")