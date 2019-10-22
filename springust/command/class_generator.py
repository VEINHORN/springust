import os

class ClassGenerator:
    DEFAULT_TEMPLATES_FOLDER = "templates"

    def template_path(self, templates_root, template_name):
        return os.path.join(self.or_default_templates(templates_root), template_name)

    def or_default_templates(self, templates_folder):
        return templates_folder if templates_folder else os.path.join(".", ClassGenerator.DEFAULT_TEMPLATES_FOLDER)

    def class_filename(self, package_path, class_name):
        return os.path.join(package_path, class_name + ".java")

    def enrich_class_name(self, class_name, what_enrich):
        """Used to enrich controller/service/repository names
        """
        if what_enrich not in class_name:
            class_name = "{}{}".format(class_name.capitalize(), what_enrich)
        return class_name