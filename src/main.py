from database import DatabaseManager
import sys

def toon_menu():
    print("\n--- BULK TRACKER MENU ---")
    print("1. Nieuw product toevoegen")
    print("2. Stoppen")
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

def main():
    db = DatabaseManager()
    db.create_tables() 

    while True:
        toon_menu()
        keuze = input("Maak een keuze (1-2): ")

        if keuze == '1':
            nieuw_product_toevoegen(db)
        elif keuze == '2':
            print("Tot ziens en succes met bulken!")
            sys.exit()
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()