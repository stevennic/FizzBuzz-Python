class FizzBuzz:
    def __init__(self, custom_pairings=None):
        if custom_pairings is None:
            # Zero pairings essentially makes it an integer generator.
            self.pairings = {}
        else:
            if isinstance(custom_pairings, dict):
                invalid_keys = [key for key in custom_pairings if key < 1]
                if len(invalid_keys):
                    first_invalid_key = invalid_keys[0]
                    raise ValueError(f'Pairing keys must be positive integers. Found: {first_invalid_key}')
                self.pairings = {key: value for key, value in sorted(custom_pairings.items())}  # Sort the pairings dictionary by key
            else:
                raise TypeError(f'custom_pairings must be of type dictionary. Found: {type(custom_pairings)}')

    def get_fizz_buzz(self, limit=100):
        if limit < 1:
            raise ValueError(f'Limit must be >= 1. Found: {limit}')
        for i in range(1, limit + 1):
            token = ''
            for key, value in self.pairings.items():
                if i % key == 0:
                    token += value
            if len(token) == 0:
                token = str(i)
            yield token
