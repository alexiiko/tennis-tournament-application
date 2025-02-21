import sqlite3
import data_getter

all_tournaments_with_data = data_getter.return_tournaments_with_data()

conn = sqlite3.connect("tournaments.db")
cursor = conn.cursor()

def create_database_tables():
    for index in range(len(all_tournaments_with_data)):
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {list(all_tournaments_with_data.keys())[index]} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                tournament_date TEXT,
                regis_start_date TEXT,
                regis_end_date TEXT,
                draw_date TEXT,
                street TEXT, 
                plz TEXT
            )
        """)

    conn.commit()


def insert_tournament_data_into_tables():
    pass


def delete_already_passed_tournaments():
    pass

    
def main():
    create_database_tables()
    insert_tournament_data_into_tables()
    delete_already_passed_tournaments()


main()
