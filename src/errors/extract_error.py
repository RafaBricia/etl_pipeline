class ExtractError(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
        self.error_type = 'ExtractError'
        super().__init__(self.message)
