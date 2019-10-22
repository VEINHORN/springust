from command.finder import find_package_new
from command.finder import find_entity
from command.class_generator import ClassGenerator
from jinja2 import Template
from command.entity_generator import EntityGenerator
from command.entity_config import EntityConfig

class RepositoryGenerator(ClassGenerator):
    def __init__(self, config):
        self.config = config

    def generate(self, class_name):
        project_path = "."

        class_name = self.enrich_class_name(class_name, "Repository")

        package_path, package = find_package_new(project_path, class_name, "repository")

        with open(self.class_filename(package_path, class_name), "w") as out:
            out.write(self.render(package, class_name, self.config))

    def render(self, package, repository_name, repository_config):
        rendered = ""
        with open(self.template_path(repository_config.templates_folder, "repository.java.jinja2"), "r") as input:
            entity_package_name, entity_name = None, None
            
            if repository_config.include_entity:
                entity_config = EntityConfig(templates_folder=repository_config.templates_folder)

                entity_generator = EntityGenerator(entity_config)
                entity_package_name, entity_name = entity_generator.generate(repository_name.replace("Repository", ""))
            else:
                # trying to find entity in the project and include it
                project_path = "."
                what_search = repository_name.replace("Repository", "")
                entity_package_name, entity_name = find_entity(what_search)
                print(entity_name)

            tm = Template(input.read())
            rendered = tm.render(package_name = package, repository_name = repository_name, entity_package_name = entity_package_name, entity_name = entity_name)
        return rendered
