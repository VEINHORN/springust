import os
from pathlib import Path
from jinja2 import Template

def main():
    print(os.path.abspath(__file__))

    # project_folder = Path("../spring-project")
    # print(project_folder)

    project_folder = os.path.join(".", "spring-project")
    print("project folder: {}".format(project_folder))

    files = [f for f in os.listdir(project_folder)]
    for f in files:
        print(f.title())

    package_folder = os.path.join(project_folder, "src", "main", "java", "com", "spring")

    # we need to get name from somewhere
    with open(os.path.join(package_folder, "TestController.java"), "w") as out:
        out.write(create_controller())

def create_controller():
    package_name = "my.package.name"
    controller_name = "MyTestController"
    root_path = "/" + controller_name.replace("Controller", "").lower()


    rendered = ""
    with open(os.path.join(".", "templates", "controller.java.jinja2"), "r") as input:
        tm = Template(input.read())

        rendered = tm.render(package_name = package_name, controller_name = controller_name, root_path = root_path)
    return rendered

if __name__ == "__main__":
    main()