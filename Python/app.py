from db import insert_password_hash, insert_new_account, create_database, retrieve_password_hash
from encryption_and_decryption import Encryptor, Decryptor
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

    def add_account_to_db(self, username: str) -> None:
        pass_builder = PasswordBuilder(self.password_requirements)
        raw_password = pass_builder.build_password()
        encryptor = Encryptor(raw_password.encode('utf-8'))
        encryptor.load_public_key()
        password_hash = encryptor.encrypt_password()
        insert_new_account(username)
        insert_password_hash(password_hash, username)

    @staticmethod
    def get_account_password(username: str) -> str:
        decrypt = Decryptor()
        decrypt.load_private_key()
        password_hash = retrieve_password_hash(username)
        return decrypt.decrypt_password(password_hash)


if __name__ == '__main__':
    t = PasswordGenerator()
    # t.determine_password_requirements(10, True, True, True)
    # t.add_account_to_db("Josh_Test")
    print(t.get_account_password("Josh_Test"))
