from database import DatabaseManager
from rapportage import RapportGenerator
import sys

def toon_menu():
    print("\n--- BULK TRACKER MENU ---")
    print("1. Nieuw product toevoegen")
    print("2. Lijst met producten tonen")
    print("3. Iets gegeten? (Loggen)")
    print("4. Excel Rapport maken")
    print("5. Stoppen")
    print("-------------------------")

def nieuw_product_toevoegen(db):
    print("\n--- PRODUCT TOEVOEGEN ---")
    try:
        naam = input("Naam van het product (bv. Kipfilet): ")
        kcal = int(input("Kcal per 100g (bv. 110): "))
        prijs = float(input("Prijs (bv. 8.50): ")) 
        db.voeg_product_toe(naam, kcal, prijs)
    except ValueError:
        print("FOUT: Voer aub geldige getallen in voor kcal en prijs!")

def toon_producten_lijst(db):
    print("\n--- PRODUCTENLIJST ---")
    producten = db.haal_producten_op()
    
    if not producten:
        print("Nog geen producten gevonden.")
        return

    print(f"{'ID':<4} | {'Naam':<20} | {'Kcal/100g':<10} | {'Prijs':<10}")
    print("-" * 50)
    for p in producten:
        
        print(f"{p[0]:<4} | {p[1]:<20} | {p[2]:<10} | € {p[3]:<10.2f}")
        
def log_consumptie(db):
    print("\n--- ETEN LOGGEN ---")
    
    toon_producten_lijst(db)
    
    try:
        prod_id = int(input("\nWelk ID heb je gegeten? "))
        gram = float(input("Hoeveel gram? "))
        
        
        db.voeg_consumptie_toe(prod_id, gram)
    except ValueError:
        print("FOUT: Voer geldige getallen in.")   
        
def genereer_rapport(db):
    print("\n--- RAPPORT GENEREREN ---")
    rapport = RapportGenerator(db)
    rapport.maak_excel_rapport()
        
def main():
    db = DatabaseManager()
    db.create_tables() 

    while True:
        toon_menu()
        keuze = input("Maak een keuze (1-5): ")

        if keuze == '1':
            nieuw_product_toevoegen(db)
        elif keuze == '2':
            toon_producten_lijst(db)
        elif keuze == '3':
            log_consumptie(db)
        elif keuze == '4':
            genereer_rapport(db)
        elif keuze == '5':
            print("Tot ziens!")
            sys.exit()
        else:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    main()