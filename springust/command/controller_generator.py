import os
from command.finder import find_package_new
from command.class_generator import ClassGenerator
from jinja2 import Template

class ControllerGenerator(ClassGenerator):
    def __init__(self, config):
        self.config = config

    def generate(self, class_name):
        project_path = "."

        if "Controller" not in class_name:
            class_name = "{}{}".format(class_name, "Controller")

        package_path, package = find_package_new(project_path, class_name, "controller")

        with open(self.class_filename(package_path, class_name), "w") as out:
            out.write(self.render(package, class_name, self.config))

    def render(self, package, controller_name, controller_config):
        rendered = ""
        with open(self.template_path(controller_config.templates_folder, "controller.java.jinja2"), "r") as input:
            tm = Template(input.read())
            rendered = tm.render(package_name = package, controller_name = controller_name, root_path = create_controller_root_path(controller_name) + "s", options = controller_config)
        return rendered
    
def create_controller_root_path(controller_name):
    return "/" + controller_name.replace("Controller", "").lower()