SEED_LENGTH = 12

def generate_seed() -> str:
    import secrets
    import string
    alpha_digits = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(alpha_digits) for i in range(SEED_LENGTH))

def seed_rng(seed: str | None = None, flags: str = "") -> str:
    if seed is None:
        seed = generate_seed()

    import random
    random.seed(seed + flags)
    return seed
