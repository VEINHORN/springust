#!/usr/bin/env python3

import os
from pathlib import Path
from jinja2 import Template
import argparse
import sys
from command import service_config as sc
from command import controller_config as cc
from command import repository_config as rc
from command.service_generator import *
from command.controller_generator import *
from command.repository_generator import *

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
    gr_parser.add_argument("repository_name")
    
    args = parser.parse_args()

    if args.command == "generate":
        generator = None

        if args.gen_type == "controller":
            controller_config = cc.ControllerConfig()
            
            if args.templates:
                controller_config.templates_folder = args.templates

            if args.crud:
                controller_config.has_get = True
                controller_config.has_post = True
                controller_config.has_put = True
                controller_config.has_delete = True
            
            generator = ControllerGenerator(controller_config)
            generator.generate(args.controller_name)
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
        elif args.gen_type == "repository":
            repository_config = rc.RepositoryConfig()

            # Specifying path to the templates folder
            if args.templates:
                repository_config.templates_folder = args.templates

            generator = RepositoryGenerator(repository_config)
            generator.generate(args.repository_name)

        else:
            print("You need to specify what you want to generate...")

if __name__ == "__main__":
    main()