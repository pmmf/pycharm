import os
import sys
import argparse

def power(a):
    return a**2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=2)

    args = parser.parse_args()
    n = args.n

    print(power(n))