from core.baseapp import BaseApp
from core.search_helper import SearchHelper
from data_model.author import Author
from data_model.book import Book
from data_model.publication import Publication

class MainApp(BaseApp):
    def __init__(self):
        self.books = []
        self.InputBook = []
        self.ViewBook = []
        BaseApp.__init__(self)



    @property
    def list_book(self):
        return self.list_book
    def add_book(self):
        return self.add_book()
    def search_book(self):
        return self.search_book()
