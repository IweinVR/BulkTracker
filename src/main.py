from database import DatabaseManager
from rapportage import RapportGenerator
import sys

def toon_menu():
    """Toont het hoofdmenu met alle opties in de terminal."""
    print("\n--- BULK TRACKER MENU ---")
    print("1. Nieuw product toevoegen")
    print("2. Lijst met producten tonen")
    print("3. Iets gegeten? (Loggen)")
    print("4. Excel Rapport maken")
    print("5. Product prijs wijzigen")
    print("6. Product verwijderen")     
    print("7. Stoppen")
    print("-------------------------")

def nieuw_product_toevoegen(db):
    """Vraagt de gebruiker om input en maakt een nieuw product aan."""
    print("\n--- PRODUCT TOEVOEGEN ---")
    try:
        naam = input("Naam van het product (bv. Kipfilet): ")
        kcal = int(input("Kcal per 100g (bv. 110): "))
        prijs = float(input("Prijs (bv. 8.50): ")) 
        db.voeg_product_toe(naam, kcal, prijs)
    except ValueError:
        print("FOUT: Voer aub geldige getallen in voor kcal en prijs!")

def toon_producten_lijst(db):
    """
    Haalt alle producten op en print ze in een tabel.
    Returns:
        True als er producten zijn, False als de lijst leeg is.
    """
    print("\n--- PRODUCTENLIJST ---")
    producten = db.haal_producten_op()
    
    if not producten:
        print("Nog geen producten gevonden.")
        return False

    print(f"{'ID':<4} | {'Naam':<20} | {'Kcal/100g':<10} | {'Prijs':<10}")
    print("-" * 50)
    for p in producten:
        print(f"{p[0]:<4} | {p[1]:<20} | {p[2]:<10} | € {p[3]:<10.2f}")
    return True    
        
def log_consumptie(db):
    """Voegt een entry toe aan het dagboek (wat heb je gegeten)."""
    print("\n--- ETEN LOGGEN ---")
    
    toon_producten_lijst(db)
    
    try:
        prod_id = int(input("\nWelk ID heb je gegeten? "))
        gram = float(input("Hoeveel gram? "))
        
        
        db.voeg_consumptie_toe(prod_id, gram)
    except ValueError:
        print("FOUT: Voer geldige getallen in.")   
        
def genereer_rapport(db):
    """Start de rapportage module om een Excel te maken."""
    print("\n--- RAPPORT GENEREREN ---")
    rapport = RapportGenerator(db)
    rapport.maak_excel_rapport()
    
def wijzig_product_prijs(db):
    """Past de prijs van een bestaand product aan."""
    print("\n--- PRIJS WIJZIGEN ---")
    if toon_producten_lijst(db):
        try:
            prod_id = int(input("\nWelk ID wil je aanpassen? "))
            nieuwe_prijs = float(input("Wat is de nieuwe prijs? "))
            db.update_prijs(prod_id, nieuwe_prijs)
        except ValueError:
            print("FOUT: Ongeldige invoer.") 
            
def verwijder_een_product(db):
    """Verwijderd een product uit de database op basis van ID."""
    print("\n--- PRODUCT VERWIJDEREN ---")
    if toon_producten_lijst(db):
        try:
            prod_id = int(input("\nWelk ID wil je verwijderen? "))
            bevestiging = input(f"Weet je zeker dat je ID {prod_id} wilt wissen? (j/n): ")
            if bevestiging.lower() == 'j':
                db.verwijder_product(prod_id)
            else:
                print("Geannuleerd.")
        except ValueError:
            print("FOUT: Ongeldige invoer.")
        
def main():
    """De hoofdfunctie die de applicatie start."""
    db = DatabaseManager()
    db.create_tables() 

    while True:
        toon_menu()
        keuze = input("Maak een keuze (1-7): ")

        if keuze == '1':
            nieuw_product_toevoegen(db)
        elif keuze == '2':
            toon_producten_lijst(db)
        elif keuze == '3':
            log_consumptie(db)
        elif keuze == '4':
            genereer_rapport(db)
        elif keuze == '5':
            wijzig_product_prijs(db)
        elif keuze == '6':
            verwijder_een_product(db)
        elif keuze == '7':
            print("Tot ziens!")
            sys.exit()
        else:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    main()