from db import insert_password_hash, insert_new_account, create_database, retrieve_password_hash
from encryption_and_decryption import Encryption, Decryption
from password_generation import PasswordBuilder, PasswordRequirements


class PasswordGenerator:
    def __init__(self):
        create_database()
        self.password_requirements: PasswordRequirements | None = None

    def determine_password_requirements(self,
                                        length: int,
                                        has_num: bool,
                                        has_symbols: bool,
                                        has_alpha_chars: bool) -> None:
        self.password_requirements = PasswordRequirements(
            length=length,
            has_numbers=has_num,
            has_symbols=has_symbols,
            has_alpha_characters=has_alpha_chars
        )

    def build_password(self) -> str:
        pass_builder = PasswordBuilder(self.password_requirements)
        return pass_builder.build_password()

    @staticmethod
    def encrypt_password(raw_password: str) -> bytes:
        encryptor = Encryption(raw_password.encode('utf-8'))
        return encryptor.encrypt_password()

    @staticmethod
    def decrypt_password(username: str) -> str:
        decrypt = Decryption()
        password_hash = retrieve_password_hash(username)
        return decrypt.decrypt_password(password_hash)

    def add_account_to_db(self, username: str) -> None:
        raw_password = self.build_password()
        password_hash = self.encrypt_password(raw_password)
        insert_new_account(username)
        insert_password_hash(password_hash, username)

    def get_account_password(self, username: str) -> str:
        return self.decrypt_password(username)


if __name__ == '__main__':
    t = PasswordGenerator()
    # t.determine_password_requirements(50, True, True, True)
    # t.add_account_to_db("Josh_50")
    print(t.get_account_password("Josh_50"))
