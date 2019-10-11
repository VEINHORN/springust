class ControllerOption:
    def __init__(self, has_get, has_post, has_put, has_delete):
        self.has_get = has_get
        self.has_post = has_post
        self.has_put = has_put
        self.has_delete = has_delete