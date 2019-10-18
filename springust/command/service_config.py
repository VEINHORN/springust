class ServiceCongig:
    def __init__(self, templates_folder = None, has_create = None, has_read = None, has_update = None, has_delete = None):
        self.templates_folder = templates_folder
        self.has_create = has_create
        self.has_read = has_read
        self.has_update = has_update
        self.has_delete = has_delete