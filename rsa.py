#!/usr/bin/env python3
from sympy import factorint
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorint(number)
            prime_factors = [str(k) + "^" + str(v) for k, v in factors.items()]
            print(f"{number}={'*'.join(prime_factors)}")

