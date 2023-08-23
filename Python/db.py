import sqlite3

from paths import paths


def db_op(func):
    def wrapper(*args, **kwargs):
        con = sqlite3.connect(paths.db_file)
        cursor = con.cursor()
        result = func(cursor, *args, **kwargs)
        con.commit()
        con.close()
        return result
    return wrapper


@db_op
def create_database(cursor: sqlite3.Cursor):
    account_table = paths.create_account_table.open()
    password_table = paths.create_password_table.open()
    cursor.execute(account_table.read())
    cursor.execute(password_table.read())


@db_op
def insert_new_account(cursor: sqlite3.Cursor, account: str) -> None:
    sql = paths.insert_account_procedure.open()
    cursor.execute(sql.read(), (account,))


@db_op
def get_account_id(cursor: sqlite3.Cursor, username: str) -> int:
    sql = paths.get_account_id_procedure.open()
    account_id = cursor.execute(sql.read(), (username,)).fetchone()
    return int(account_id[0])


@db_op
def insert_password_hash(cursor: sqlite3.Cursor, password_hash: bytes, username: str) -> None:
    sql = paths.insert_password_hash_procedure.open()
    cursor.execute(sql.read(), (get_account_id(username), password_hash))


@db_op
def retrieve_password_hash(cursor: sqlite3.Cursor, username: str) -> bytes:
    sql = paths.get_password_hash.open()
    result = cursor.execute(sql.read(), (get_account_id(username),)).fetchone()
    return result[0]
