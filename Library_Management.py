class Library:
    def issue_book(self):
        pass


class StudentLibrary(Library):
    def issue_book(self):
        print("Student can issue maximum 2 books.")


class FacultyLibrary(Library):
    def issue_book(self):
        print("Faculty can issue maximum 5 books.")


s = StudentLibrary()
f = FacultyLibrary()

s.issue_book()
f.issue_book()