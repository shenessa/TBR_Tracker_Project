from linkedlist import LinkedList


class TBRModel(object):

    def __init__(self, filename):
        file = open(filename, 'r')
        self._list = LinkedList().listIterator()
        for book in file:
            self._list.insert(book)
        file.close()
        self._filename = filename

    def insert(self, book):
        self._list.insert(book)

    def remove(self, book):
        self._list.remove(book)

    def print(self):
        print("\n")
        file = open(self._filename, 'r')
        for book in file:
            print(book)
        file.close()
