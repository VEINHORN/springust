from command.finder import find_package_new
from command.class_generator import ClassGenerator
from jinja2 import Template

class EntityGenerator(ClassGenerator):
    def __init__(self, config):
        self.config = config

    def generate(self, class_name):
        project_path = "."
        class_name = class_name.capitalize()

        package_path, package = find_package_new(project_path, class_name, "Entity")

        with open(self.class_filename(package_path, class_name), "w") as out:
            out.write(self.render(package, class_name, self.config))
        
        return package, class_name

    def render(self, package, entity_name, entity_config):
        rendered = ""
        with open(self.template_path(entity_config.templates_folder, "entity.java.jinja2"), "r") as input:
            tm = Template(input.read())
            rendered = tm.render(package_name = package, entity_name = entity_name)
        return rendered