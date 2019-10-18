import os
from jinja2 import Template
from command.finder import find_package

def execute(class_type, class_name, options):
    # project_path = "spring-project"
    project_path = "."

    if class_type == "controller":
        if "Controller" not in class_name:
            class_name = "{}{}".format(class_name, "Controller")

        package_path, package = find_package(project_path, class_type)

        with open(os.path.join(package_path, class_name + ".java"), "w") as out:
            out.write(create_controller(package, class_name, options))
    elif class_type == "service":
        package_path, package = find_package(project_path, class_type)

        with open(class_filename(package_path, class_name), "w") as out:
            out.write(create_service(package, class_name, options))
    else:
        print("You have entered unsupported command...")

def class_filename(package_path, class_name):
    return os.path.join(package_path, class_name + ".java")

def create_controller(package, controller_name, options):
    rendered = ""
    with open(os.path.join(".", "templates", "controller.java.jinja2"), "r") as input:
        tm = Template(input.read())

        rendered = tm.render(package_name = package, controller_name = controller_name, root_path = create_controller_root_path(controller_name) + "s", options = options)
    return rendered

def create_controller_root_path(controller_name):
    return "/" + controller_name.replace("Controller", "").lower()

def create_service(package, service_name, options):
    return "sdfsdf"