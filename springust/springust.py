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
    # print("current dir: " + os.getcwd())

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-tf", "--templates", help = "Absolute path to the templates folder")
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
    controller_parser.add_argument("--crud", action="store_true", help = "Generates GET/POST/PUT/DELETE methods in controller")

    controller_parser.add_argument("controller_name")

    # ----- Service
    service_parser = generate_subparsers.add_parser("service")
    service_parser.add_argument("-c", "--create", action = "store_true", help = "Generate create REST method in service")
    service_parser.add_argument("-r", "--read", action = "store_true", help = "Generate read REST method in service")
    service_parser.add_argument("-u", "--update", action = "store_true", help = "Generate update REST method in service")
    service_parser.add_argument("-d", "--delete", action = "store_true", help = "Generate delete REST method in service")
    service_parser.add_argument("--crud", action = "store_true", help = "Generates all CRUD methods in service")

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
            service_config = sc.ServiceCongig()
            
            # Specifying path to the templates folder
            if args.templates:
                service_config.templates_folder = args.templates

            if args.crud:
                service_config.has_create = True
                service_config.has_read = True
                service_config.has_update = True
                service_config.has_delete = True
            else:
                if args.create:
                    service_config.has_create = args.create # check that property exists
                if args.read:
                    service_config.has_read = args.read
                
                if args.update:
                    service_config.has_update = args.update
                
                if args.delete:
                    service_config.has_delete = args.delete

            generator = ServiceGenerator(service_config)
            generator.generate(args.service_name)
        else:
            print("You need to specify what you want to generate...")

if __name__ == "__main__":
    main()