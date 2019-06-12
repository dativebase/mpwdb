import pprint

from mpwdb.getargs import get_args
from mpwdb.french import *


__version__ = '0.1.0'



def main():
    config = get_args()
    globals()[config['subcommand'].replace('-', '_')](config)


if __name__ == '__main__':
    main()
