#!/usr/bin/env python3

import os
from pathlib import Path
from jinja2 import Template
import argparse
from command import generate
import sys

def main():
    # print(os.path.abspath(__file__))
    print(sys.version)

    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(help="commands", dest="command")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate Spring classes", add_help=False)
    generate_subparsers = generate_parser.add_subparsers(help="type of gen file", dest="gen_type")

    gc_parser = generate_subparsers.add_parser("controller")
    gs_parser = generate_subparsers.add_parser("service")
    gr_parser = generate_subparsers.add_parser("repository")
    

    args = parser.parse_args()


    if args.command == "generate":
        # print("gen type = " + args.gen_type)
        if args.gen_type:
            generate.execute(args.gen_type)
        else:
            print("You need to specify what you want to generate...")

if __name__ == "__main__":
    main()