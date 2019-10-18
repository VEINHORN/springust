import os
from command.finder import find_package_new

class ServiceGenerator:
    def __init__(self, config):
        self.config = config

    def generate(self, class_name):
        project_path = "spring-project" # pass it from outside

        if "Service" not in class_name:
            class_name = "{}{}".format(class_name, "Service")
        
        package_path, package = find_package_new(project_path, class_name, "service")

        with open(class_filename(package_path, class_name), "w") as out:
            out.write(create_service())

def create_service():
    return "some content"

def class_filename(package_path, class_name):
    return os.path.join(package_path, class_name + ".java")