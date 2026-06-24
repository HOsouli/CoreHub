import os
from uuid import uuid4


class FileUpload:
    def __init__(self, directory: str, prefix: str):
        self.directory = directory
        self.prefix = prefix  # پوشه ای که مربوط به برند prefix

    def upload_to(self, instance, filename: str) -> str:
        filename, ext = os.path.splitext(filename)

        # security: allow only safe extensions
        allowed_ext = {'.jpg', '.jpeg', '.png', '.webp'}

        if ext.lower() not in allowed_ext:
            raise ValueError("Invalid file type")

        return f"{self.directory}/{self.prefix}/{uuid4()}{ext}"
