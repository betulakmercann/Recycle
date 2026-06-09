import sqlite3
import os
DB_FILE = 'recycling_db.db'

def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS geri_donusum_kayitlari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            atık_turu TEXT NOT NULL,
            yukleme_zamani TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"'{DB_FILE}' veritabanı ve 'geri_donusum_kayitlari' tablosu oluşturuldu (varsa zaten var).")

if __name__ == '__main__':
    create_table()