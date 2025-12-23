import sqlite3
import json
import os

class DatabaseManager:
    def __init__(self, settings_file='settings.json'):
        # Pad bepalen naar settings.json
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(base_dir)
        full_path = os.path.join(project_root, settings_file)
        with open(full_path, 'r') as f:
            config = json.load(f)
            self.db_name = os.path.join(project_root, config['db_name'])
        os.makedirs(os.path.dirname(self.db_name), exist_ok=True)
    def connect(self):
        return sqlite3.connect(self.db_name)
    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS producten (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT NOT NULL,
                kcal_per_100g INTEGER,
                prijs_per_eenheid REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dagboek (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                datum TEXT,
                hoeveelheid REAL,
                FOREIGN KEY(product_id) REFERENCES producten(id)
            )
        ''')
        conn.commit()
        conn.close()
    def voeg_product_toe(self, naam, kcal, prijs):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO producten (naam, kcal_per_100g, prijs_per_eenheid)
            VALUES (?, ?, ?)
        ''', (naam, kcal, prijs))
        conn.commit()
        conn.close()
        print(f"'{naam}' is toegevoegd aan de database.")