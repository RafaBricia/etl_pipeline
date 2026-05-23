class LoadError(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
        self.error_type = 'LoadError'
        super().__init__(self.message)
