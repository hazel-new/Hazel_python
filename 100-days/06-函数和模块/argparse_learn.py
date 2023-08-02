import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('--name', default='Great')

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    name = args.name
    names = name.split(',')
    print(names)