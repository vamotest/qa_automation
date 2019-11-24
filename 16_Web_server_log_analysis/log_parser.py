import argparse


def get_args():
    """
    Parser arguments
    """
    arg_parser = argparse.ArgumentParser(description='Access.log parser')

    arg_parser.add_argument('-f', '--file', dest='filename',
                            help='Enter path to file')
    arg_parser.add_argument('-d', '--directory', dest="directory",
                            help='Enter path to files')
    arg_parser.add_argument('-o', '--output', dest="output_name",
                            help='Enter name of output file')

    return arg_parser.parse_args()
