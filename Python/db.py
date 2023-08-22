import sqlite3

from pathlib import Path
from paths import paths


def create_database(db_path: Path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Account table
    cursor.execute('''
        CREATE TABLE Account (
            AccountID INTEGER PRIMARY KEY,
            UserName TEXT
        )
    ''')

    # Create Password table with foreign key reference to Account table
    cursor.execute('''
        CREATE TABLE Password (
            PasswordID INTEGER PRIMARY KEY,
            AccountID_FK INTEGER,
            PasswordHash BLOB,
            FOREIGN KEY (AccountID_FK) REFERENCES Account (AccountID)
        )
    ''')

    conn.commit()
    conn.close()


def insert_new_account(account: str) -> None:
    con = sqlite3.connect(paths.db_file)
    cursor = con.cursor()
    sql = paths.insert_account_procedure.open()
    cursor.execute(sql.read(), (account,))
    con.commit()
    con.close()


def get_account_id(username: str) -> int:
    con = sqlite3.connect(paths.db_file)
    cursor = con.cursor()
    sql = paths.get_account_id_procedure.open()
    account_id = cursor.execute(sql.read(), (username,)).fetchone()
    con.close()
    return int(account_id[0])


def insert_password_hash(password_hash: bytes, username: str) -> None:
    con = sqlite3.connect(paths.db_file)
    cursor = con.cursor()
    sql = paths.insert_password_hash_procedure.open()
    cursor.execute(sql.read(), (get_account_id(username), password_hash))
    con.commit()
    con.close()
