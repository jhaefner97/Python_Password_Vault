import rsa

from paths import paths


def build_environment_file() -> None:
    public_key, private_key = rsa.newkeys(256)

    if not paths.env_file.is_file():
        with open(paths.env_file, "w") as f:
            f.write(f"public_key={paths.public_key}\n")
            f.write(f"private_key={paths.private_key}")
