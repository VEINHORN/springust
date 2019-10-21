from command.finder import find_package_new
from command.class_generator import ClassGenerator
from jinja2 import Template

class RepositoryGenerator(ClassGenerator):
    def __init__(self, config):
        self.config = config

    def generate(self, class_name):
        project_path = "."

        class_name = self.enrich_class_name(class_name)

        package_path, package = find_package_new(project_path, class_name, "repository")

        with open(self.class_filename(package_path, class_name), "w") as out:
            out.write(self.render(package, class_name, self.config))

    def render(self, package, repository_name, repository_config):
        rendered = ""
        with open(self.template_path(repository_config.templates_folder, "repository.java.jinja2"), "r") as input:
            tm = Template(input.read())
            rendered = tm.render(package_name = package, repository_name = repository_name)
        return rendered

    def enrich_class_name(self, class_name):
        return "{}{}".format(class_name.capitalize(), "Repository") if "Repository" not in class_name else class_name