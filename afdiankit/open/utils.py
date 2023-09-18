from hashlib import md5


def sign(token: str, params: str, ts: int, user_id: str) -> str:
    return md5(f"{token}params{params}ts{ts}user_id{user_id}".encode()).hexdigest()
