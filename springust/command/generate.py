import os
from jinja2 import Template
from command.finder import find_package

def execute(class_type, class_name):
    if class_type == "controller":
        # We need to get current dir or provide through arguments
        project_folder = os.path.join(".", "spring-project")
        
        package_path, package = find_package("spring-project", class_type)

        with open(os.path.join(package_path, class_name + ".java"), "w") as out:
            out.write(create_controller(class_type, package, class_name))
    elif class_type == "service":
        print("not implemented for now")
    else:
        print("You have entered unsupported command...")


def create_controller(class_type, package, controller_name):
    rendered = ""
    with open(os.path.join(".", "templates", "controller.java.jinja2"), "r") as input:
        tm = Template(input.read())

        rendered = tm.render(package_name = package, controller_name = controller_name, root_path = create_controller_root_path("MyTestController"))
    return rendered

def create_controller_root_path(controller_name):
    return "/" + controller_name.replace("Controller", "").lower()