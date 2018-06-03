def validate_request_params(data, expected_params):
    for param in expected_params:
        if not data[param]:
            return False
    return True

def create_random_id(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
