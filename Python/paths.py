from pathlib import Path


class Paths:
    def __init__(self) -> None:
        self.project_dir = Path.cwd().parent

        """Database Paths"""
        self.db_dir: Path = self.project_dir / "DB"
        self.db_file: Path = self.db_dir / "passwords_db.db"

        """SQL Paths"""
        self.SQL = self.project_dir / "SQL"
        self.create_account_table = self.SQL / "Create_Account_Table.sql"
        self.create_password_table = self.SQL / "Create_Password_Table.sql"
        self.insert_account_procedure = self.SQL / "Insert_Account.sql"
        self.insert_password_hash_procedure = self.SQL / "Insert_Password_Hash.sql"
        self.get_account_id_procedure = self.SQL / "Get_Account_ID.sql"
        self.get_password_hash = self.SQL / "Get_Password_Hash.sql"

        """Encryption Key Paths"""
        self.keys_dir = self.project_dir / "Keys"
        self.private_key = self.keys_dir / "private_key.pem"
        self.public_key = self.keys_dir / "public_key.pem"

        self.build_dirs(self.db_dir, self.keys_dir)

    @staticmethod
    def build_dirs(*args: Path) -> None:
        for arg in args:
            if not arg.is_dir():
                arg.mkdir(exist_ok=False)


paths = Paths()
