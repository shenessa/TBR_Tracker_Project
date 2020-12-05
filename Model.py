from linkedlist import LinkedList

class Model(object):

    def __init__(self, filename):
        # New instance variable _canModify permits or
        # disallows removals and replacements
        # New instance variable _filename needed to save
        # modifications to the file
        file = open(filename, 'r')
        self._list = LinkedList().listIterator()
        for line in file:
            self._list.insert(line)
        file.close()
        self._canModify = True
        self._filename = filename

    def canModify(self):
        # Returns True if a line can be removed or replaced
        # or False otherwise.
        if self._canModify:
            return True
        else:
            return False

    def first(self):
        # Navigate to the first line.
        # Return the next line.
        self._list.first()
        return self._list.next()

    def last(self):
        # Navigate to the last line.
        # Return the previous line.
        self._list.last()
        return self._list.previous()


    def next(self):
        # If there is a next line, set self._canModify to True
        # and return the next line. Otherwise, return None.
        if self._list.hasNext():
            self._canModify = True
            return self._list.next()
        else:
            return None


    def previous(self):
        # If there is a previous line, set self._canModify to True
        # and return the previous line. Otherwise, return None.
        if self._list.hasPrevious():
            self._canModify = True
            return self._list.previous()
        else:
            return None


    def insert(self, book):
        self._list.last()
        self._list.insert(book)
        file = open("TBR_List.txt", 'w')
        cursor = self.first()
        while cursor != None:
            file.write(cursor)
            file.write("\n")
            cursor = self.next()
        file.close()

    def remove(self, book):
        cursor = self.first()
        while cursor.strip() != book:
            cursor = self.next()
        self._list.remove()
        file = open("TBR_List.txt", 'w')
        cursor = self.first()
        while cursor != None:
            if cursor != "":
                file.write(cursor)
                file.write("\n")
            cursor = self.next()
        file.close()

    def print(self):
        file = open("TBR_List.txt", 'r')
        print("\n")
        print(file.read())
        print("\n")
        file.close()
