import os
from jinja2 import Template

def execute():
    # We need to get current dir or provide through arguments
    project_folder = os.path.join(".", "spring-project")
    
    package_folder = os.path.join(project_folder, "src", "main", "java", "com", "spring")

    with open(os.path.join(package_folder, "TestController.java"), "w") as out:
        out.write(create_controller())
    # print("executing generate command...")

def create_controller():
    package_name = "my.package.name"
    controller_name = "MyTestController"
    root_path = "/" + controller_name.replace("Controller", "").lower()


    rendered = ""
    with open(os.path.join(".", "templates", "controller.java.jinja2"), "r") as input:
        tm = Template(input.read())

        rendered = tm.render(package_name = package_name, controller_name = controller_name, root_path = root_path)
    return rendered

def create_controller_name():
    return "MyTestController"

def create_controller_root_path(controller_name):
    return "/" + controller_name.replace("Controller", "").lower()