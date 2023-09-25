import uuid


def generate_random_url() -> str:
    return "https://" + str(uuid.uuid4()) + ".com"
