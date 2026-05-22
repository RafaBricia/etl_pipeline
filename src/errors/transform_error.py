class TransformError(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
        self.error_type = 'TransformError'
        super().__init__(self.message)
