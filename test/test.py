import random
import sys

import pytest

from FizzBuzz import FizzBuzz

# Canonical 3 Fizz / 5 Buzz instance for testing convenience
fizz_buzz_example = {3: 'Fizz', 5: 'Buzz'}


def generate_random_word(size):
    #  Generates a random sequence of lowercase characters
    return ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(size)])


def print_pairings(pairings):
    for key, value in pairings.items():
        print(f'{key:5} : {value}')


def generate_random_pairings(number_of_pairings_min=1, number_of_pairings_max=20, denominator_min=1, denominator_max=100):
    # Generates random pairings
    # Numbers are not guaranteed to be unique, so final number will be <= numberOfPairingsMax
    max_word_size = 10
    number_of_pairings = random.randint(number_of_pairings_min, number_of_pairings_max)
    pairings = {}

    for i in range(number_of_pairings):
        number = random.randint(denominator_min, denominator_max)
        word = generate_random_word(max_word_size)
        pairings[number] = word

    print("Testing with the following pairings:")
    print_pairings(pairings)

    return pairings


def test_number_of_items():
    # Test expected number of items returned for all list sizes between 1 and 1000
    fb = FizzBuzz()
    for i in range(1, 1001):
        fb_list = list(fb.get_fizz_buzz(limit=i))
        assert len(fb_list) == i, f'Expected {i} items. Got {len(fb_list)}.'


def test_pure_int():
    # Test that when no pairings are supplied, all returned values are integers
    fb = FizzBuzz()
    index = 1
    for token in fb.get_fizz_buzz():
        assert token.isdecimal(), f'Expected integer for #{index}. Found {token} instead.'
        assert int(token) == index, f'Expected {index}. Found "{token}" instead.'
        index += 1


def test_pairings():
    # Test with generated pairings
    pairings = generate_random_pairings()
    fb = FizzBuzz(pairings)
    limit = 10000
    index = 1
    for output in fb.get_fizz_buzz(limit):
        pairing_match = False
        for key, value in pairings.items():
            if index % key == 0:
                pairing_match = True
                assert value in output, f'{index} is divisible by {key} and should contain {value} but does not. Found {output} instead.'

        # If no pairing matched, test that output is a number and the correct one
        if not pairing_match:
            assert output.isdecimal(), f'Expected integer for #{index}. Found {output} instead.'
            assert int(output) == index, f'Expected {index}. Found {output} instead.'

        index += 1


def test_15():
    # Test #15
    ntest = 15
    fb = FizzBuzz(fizz_buzz_example)
    fb1 = list(fb.get_fizz_buzz(ntest))
    value = fb1[ntest - 1]
    assert value == 'FizzBuzz', f'#{ntest} does not contain FizzBuzz. Found {value}.'


def test_large_list():
    # Test requesting a large list
    fb = FizzBuzz(fizz_buzz_example)
    fb1 = iter(fb.get_fizz_buzz(sys.maxsize))
    next(fb1)


def test_invalid_pairing_key():
    # Test pairing key < 1
    with_invalid_key = fizz_buzz_example.copy()
    with_invalid_key[-5] = 'Taco'

    # Assert that ValueError exception is properly raised here
    with pytest.raises(ValueError):
        FizzBuzz(with_invalid_key)
