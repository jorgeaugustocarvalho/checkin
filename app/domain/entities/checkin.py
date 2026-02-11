from datetime import datetime


class CheckIn:
    def __init__(self, name: str, document: str | None = None):
        """
        Represents a check-in record with name, optional document, and creation timestamp.

        Parameters:
        - name (str): Person or entity name; required.
        - document (str | None): Optional document identifier.

        Raises:
        - ValueError: If name is empty.

        Attributes:
        - name (str): Provided name.
        - document (str | None): Provided document identifier.
        - created_at (datetime): UTC timestamp when the instance was created.
        """
        if not name:
            raise ValueError("Name is required")

        self.name = name
        self.document = document
        self.created_at = datetime.utcnow()