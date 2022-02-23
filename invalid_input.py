class InvalidInput(Exception):
    """Indicates an invalid user input."""
    def __init__(self, message):
        """Sets the message to the user."""
        super().__init__(message)
        self.message = message