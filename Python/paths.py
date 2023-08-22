from pathlib import Path


class Paths:
    def __init__(self) -> None:
        self.project_dir = Path.cwd().parent
        self.env_dir: Path = self.project_dir / "ENV"
        self.env_file: Path = self.env_dir / "encryption_keys.env"

        self.db_dir: Path = self.project_dir / "DB"
        self.db_file: Path = self.db_dir / "passwords_db.db"

        self.stored_procedures = self.db_dir / "Stored_Procedures"
        self.insert_account_procedure = self.stored_procedures / "Insert_Account_Procedure.sql"
        self.insert_password_hash_procedure = self.stored_procedures / "Insert_Password_Hash_Procedure.sql"
        self.get_account_id_procedure = self.stored_procedures / "Get_Account_ID.sql"

        self.keys_dir = self.env_dir / "Keys"
        self.private_key = self.keys_dir / "private_key.pem"
        self.public_key = self.keys_dir / "public_key.pem"

        self.build_dirs(self.env_dir, self.db_dir, self.keys_dir)

    @staticmethod
    def build_dirs(*args: Path) -> None:
        for arg in args:
            if not arg.is_dir():
                arg.mkdir(exist_ok=False)


paths = Paths()
