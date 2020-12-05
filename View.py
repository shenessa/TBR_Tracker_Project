from Model import Model

class View(object):

    def __init__(self):
        self._getFile()
        self._methods = {}
        self._methods["1"] = self._insert
        self._methods["2"] = self._remove
        self._methods["3"] = self._print
        self._methods["4"] = self._quit

    def run(self):
        """A menu-driven command processor for a user."""
        while True:
            print("1 Insert a book title: ")
            print("2 Remove a book title: ")
            print("3 Print TBR List")
            print("4 Quit\n")
            number = input("Select an option: ")
            theMethod = self._methods.get(number, None)
            if theMethod is None:
                print("Unrecognized number")
            else:
                theMethod()
                if self._model is None:
                    break

    def _getFile(self):
        self._model = Model("TBR_List.txt")

    def _insert(self):
        title = input("Enter a book title: ")
        self._model.insert(title)

    def _remove(self):
        title = input("Enter a book title: ")
        if self._model.canModify():
            self._model.remove(title)
        else:
            print("No position established: try moving to next or previous\n")

    def _print(self):
        self._model.print()

    def _quit(self):
        self._model = None
        print("Program ended!")


# Launch the application
if __name__ == "__main__":
    View().run()
