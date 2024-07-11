from core.imp import *


class Pdf():
    def __init__(self, path: str, password: str = None) -> None:
        reader = PdfReader(path)
        if password:
            reader.decrypt(password)

        writer = PdfWriter(clone_from=reader)
        self._pdf = writer
        self._password = password

        self.add_object = self._pdf._add_object
        self.add_annotation = self._pdf.add_annotation
        self.close = self._pdf.close
        self.pages = self._pdf.pages
        self.objects = self._pdf._objects
        self.add_uri = self._pdf.add_uri

    def merge(self, page: PageObject, n: int = 0):
        self._pdf.pages[n].merge_page(page)

    def change_password(self, password: str):
        self._password = password

    def store(self, path: str):
        if self._password:
            self._pdf.encrypt(self._password)
        self._pdf.write(path)
