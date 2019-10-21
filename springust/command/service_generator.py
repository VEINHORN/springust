import os
from command.finder import find_package_new
from jinja2 import Template
from command.class_generator import ClassGenerator

class ServiceGenerator(ClassGenerator):
    def __init__(self, config):
        self.config = config

    def generate(self, class_name):
        # project_path = "spring-project"
        project_path = "." # pass it from outside as an argument

        if "Service" not in class_name:
            class_name = "{}{}".format(class_name, "Service")
        
        package_path, package = find_package_new(project_path, class_name, "service")

        with open(self.class_filename(package_path, class_name), "w") as out:
            out.write(render(self, package, class_name, self.config))

def render(self, package, service_name, service_config):
    rendered = ""
    with open(self.template_path(service_config.templates_folder, "service.java.jinja2"), "r") as input:
        tm = Template(input.read())
        rendered = tm.render(package_name = package, service_name = service_name, config = service_config)
    return rendered
