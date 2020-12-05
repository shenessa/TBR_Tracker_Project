from TBRmodel import TBRModel

class BookView(object):

    def __init__(self):
        self._getFile()
        self._methods = {}
        self._methods["1"] = self._insert
        self._methods["2"] = self._remove
        self._methods["3"] = self._print
        self._methods["4"] = self._quit

    def run(self):

        while True:
            print("Select option from list below:\n")
            print("1 Add a book")
            print("2 Remove a book")
            print("3 Print T.B.R. List")
            print("4 Quit program\n")
            selection = input("Select an option: ")
            theMethod = self._methods.get(selection, None)
            if theMethod is None:
                print("Invalid selection. Try Again")
            else:
                theMethod()
                if self._model is None:
                    break

    def _getFile(self):
        filename = "TBR_List.txt"
        self._model = TBRModel(filename)

    def _insert(self):
        book = input("Enter title to be added: ")
        self._model.insert(book)

    def _remove(self):
        book = input("Enter title to be removed: ")
        self._model.remove(book)

    def _print(self):
        self._model.print()

    def _quit(self):
        self._model = None
        print("Program Ended")

if __name__ == "__main__":
    BookView().run()
