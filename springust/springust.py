#!/usr/bin/env python3

import os
from pathlib import Path
from jinja2 import Template
import argparse
from command import generate
import sys
from command import controller_option as co

def main():
    parser = argparse.ArgumentParser(add_help=True)
    subparsers = parser.add_subparsers(help="commands", dest="command")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate Spring classes", add_help=True)
    generate_subparsers = generate_parser.add_subparsers(help="type of gen file", dest="gen_type")

    # ----- Controller
    controller_parser = generate_subparsers.add_parser("controller")
    controller_parser.add_argument("-g", "--get", action = "store_true", help = "Generate GET methods in controller")
    controller_parser.add_argument("-p", "--post", action = "store_true", help = "Generate POST method in controller")
    controller_parser.add_argument("--put", action="store_true", help = "Generate PUT method in controller")
    controller_parser.add_argument("-d", "--delete", action="store_true", help = "Generate DELETE method in controller")
    controller_parser.add_argument("--crud", action="store_true", help = "Generates all CRUD methods in controller")

    controller_parser.add_argument("controller_name")

    # ----- Service
    gs_parser = generate_subparsers.add_parser("service")

    # ----- Repository
    gr_parser = generate_subparsers.add_parser("repository")
    
    args = parser.parse_args()

    if args.command == "generate":
        if args.gen_type:
            if args.crud:
                options = co.ControllerOption(True, True, True, True)
            else:
                options = co.ControllerOption(has_get = args.get, has_post = args.post, has_put = args.put, has_delete= args.delete)

            generate.execute(args.gen_type, args.controller_name, options)
        else:
            print("You need to specify what you want to generate...")

if __name__ == "__main__":
    main()