import rsa

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey
from paths import paths


def build_pem_files() -> None:
    public_key, private_key = rsa.newkeys(2048)
    with open(paths.private_key, "wb") as f:
        f.write(private_key.save_pkcs1())
    with open(paths.public_key, "wb") as f:
        f.write(public_key.save_pkcs1())


class Encryptor:
    def __init__(self, password_string: bytes):
        if not paths.public_key.is_file():
            build_pem_files()
        self.public_key: RSAPublicKey | None = None
        self.password_str: bytes = password_string

    def load_public_key(self) -> None:
        with open(paths.public_key, "rb") as f:
            self.public_key = serialization.load_pem_public_key(f.read())

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


class Decryptor:
    def __init__(self):
        self.private_key: RSAPrivateKey | None = None

    def load_private_key(self) -> None:
        with open(paths.private_key, "rb") as f:
            self.private_key = serialization.load_pem_private_key(f.read(), password=None)

    def decrypt_password(self, password_hash: bytes) -> str:
        password = self.private_key.decrypt(
            password_hash,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return password.decode("utf-8")
