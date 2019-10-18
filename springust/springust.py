#!/usr/bin/env python3

import os
from pathlib import Path
from jinja2 import Template
import argparse
from command import generate
import sys
from command import controller_option as co
from command import service_config as sc
from command.service_generator import *

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
    service_parser = generate_subparsers.add_parser("service")
    service_parser.add_argument("-c", "--create", action = "store_true", help = "Generate create REST method")
    service_parser.add_argument("-r", "--read", action = "store_true", help = "Generate save REST method")

    service_parser.add_argument("service_name")

    # ----- Repository
    gr_parser = generate_subparsers.add_parser("repository")
    
    args = parser.parse_args()

    if args.command == "generate":
        generator = None

        if args.gen_type == "controller":
            options = None
            
            if hasattr(args, "crud") and args.crud:
                options = co.ControllerOption(True, True, True, True)
            else: # trying to set separate get/post/put/delete options
                options = co.ControllerOption()
            
            generate.execute(args.gen_type, args.controller_name, options)
        elif args.gen_type == "service":
            service_config = sc.ServiceCongig(args.create)
            # service_config.has_create = args.create # check that property exists
            
            generator = ServiceGenerator(service_config)
            print(args.service_name)
            generator.generate(args.service_name)
            # generate.execute(args.gen_type, args.controller_name, options)
        else:
            print("You need to specify what you want to generate...")
        # print(args.gen_type)



        #if args.gen_type:
        #    if hasattr(args, "crud") and args.crud:
        #        options = co.ControllerOption(True, True, True, True)
        #    else:
        #        options = co.ControllerOption(has_get = args.get, has_post = args.post, has_put = args.put, has_delete= args.delete)
        #
        #    generate.execute(args.gen_type, args.controller_name, options)
        #else:
        #    print("You need to specify what you want to generate...")

if __name__ == "__main__":
    main()