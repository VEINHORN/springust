import os
from pathlib import Path
from jinja2 import Template
import argparse
from command import generate

def main():
    # print(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(help="commands", dest="command")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate Spring classes", add_help=False)

    args = parser.parse_args()

    if args.command == "generate":
        generate.execute()
    #project_folder = os.path.join(".", "spring-project")
    #print("project folder: {}".format(project_folder))

    #files = [f for f in os.listdir(project_folder)]
    #for f in files:
    #    print(f.title())

    #package_folder = os.path.join(project_folder, "src", "main", "java", "com", "spring")

    # we need to get name from somewhere
    #with open(os.path.join(package_folder, "TestController.java"), "w") as out:
    #    out.write(create_controller())

if __name__ == "__main__":
    main()