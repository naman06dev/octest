"""A tiny arithmetic CLI used to exercise the background coding agent."""
import argparse


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


OPS = {
    "add": add,
    "sub": sub,
    "mul": mul,
}


def main(argv=None):
    parser = argparse.ArgumentParser(description="tiny calculator")
    parser.add_argument("op", choices=sorted(OPS), help="operation to run")
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args(argv)
    result = OPS[args.op](args.a, args.b)
    print(result)
    return result


if __name__ == "__main__":
    main()
