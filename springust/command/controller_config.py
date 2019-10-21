class ControllerConfig:
    def __init__(self, templates_folder = None, has_get = None, has_post = None, has_put = None, has_delete = None):
        self.templates_folder = templates_folder
        self.has_get = has_get
        self.has_post = has_post
        self.has_put = has_put
        self.has_delete = has_delete