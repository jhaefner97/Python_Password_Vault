import os
import rsa

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from environment_variables import build_environment_file
from paths import paths


def build_pem_files() -> None:
    public_key, private_key = rsa.newkeys(2048)
    with open(paths.private_key, "wb") as f:
        f.write(private_key.save_pkcs1())
    with open(paths.public_key, "wb") as f:
        f.write(public_key.save_pkcs1())

build_pem_files()

class Encryptor:
    def __init__(self, password_string: bytes):
        if not paths.env_file.is_file():
            build_pem_files()
        self.public_key: RSAPublicKey | None = None
        self.password_str: bytes = password_string

    def load_public_key(self) -> None:
        with open(paths.public_key, "rb") as pem_file:
            self.public_key = serialization.load_pem_public_key(pem_file.read())

    def encrypt_password(self) -> bytes:
        password_hash = self.public_key.encrypt(
            self.password_str,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return password_hash
