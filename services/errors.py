class EmailAlreadyRegisteredError(Exception):
    def __init__(self, message="Email already registered"):
        self.message = message
        super().__init__(self.message)

class ProducAlreadyExistError(Exception):
    def __init__(self, message="Product already in DB"):
        self.message = message
        super().__init__(self.message)
