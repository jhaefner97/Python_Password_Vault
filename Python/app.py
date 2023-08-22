from db import insert_password_hash, insert_new_account, create_database
from encryption_and_decryption import Encryptor
from password_generation import PasswordBuilder, PasswordRequirements
from paths import paths

if not paths.db_file.is_file():
    create_database(paths.db_file)

reqs = PasswordRequirements(
    length=10,
    has_numbers=True,
    has_symbols=True,
    has_alpha_characters=True
)

pass_builder = PasswordBuilder(reqs)
raw_password = pass_builder.build_password()
encryptor = Encryptor(raw_password.encode('utf-8'))
encryptor.load_public_key()
password_hash = encryptor.encrypt_password()

insert_new_account("TEST2")
insert_password_hash(password_hash, "TEST2")
