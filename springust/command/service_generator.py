import os
from command.finder import find_package_new
from jinja2 import Template

class ServiceGenerator:
    def __init__(self, config):
        self.config = config

    def generate(self, class_name):
        # project_path = "spring-project"
        project_path = "." # pass it from outside as an argument

        if "Service" not in class_name:
            class_name = "{}{}".format(class_name, "Service")
        
        package_path, package = find_package_new(project_path, class_name, "service")

        with open(class_filename(package_path, class_name), "w") as out:
            out.write(render(package, class_name, self.config))

def render(package, service_name, service_config):
    rendered = ""
    with open(template_path(service_config.templates_folder), "r") as input:
        tm = Template(input.read())
        rendered = tm.render(package_name = package, service_name = service_name, config = service_config)
    return rendered

def template_path(templates_root):
    return os.path.join(templates_folder(templates_root), "service.java.jinja2")

def templates_folder(templates_folder):
    return templates_folder if templates_folder else os.path.join(".", "templates")

def class_filename(package_path, class_name):
    return os.path.join(package_path, class_name + ".java")