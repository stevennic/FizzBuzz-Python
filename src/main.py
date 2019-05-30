import sys

from FizzBuzz import FizzBuzz


def main():
    limit = 100
    if len(sys.argv) == 2:
        try:
            limit = int(sys.argv[1])
        except ValueError:
            print(f'Unrecognized command line parameter: {sys.argv[1]}')
            sys.exit(-1)
    elif len(sys.argv) > 2:
        print('At most one parameter can be specified')
        sys.exit(-1)

    fb = FizzBuzz({3: 'Fizz', 5: 'Buzz', 7: 'Taco'})
    for token in fb.get_fizz_buzz(limit):
        print(token)


if __name__ == '__main__':
    main()
