import xlwt
import getMovieInfo

# this is the title row
titleRow = 0

# constants for columns
MOVIEID = 0
GENRE = 1

# names of the columns
name_MovieID_col = 'MovieID'
name_Genre_col = 'Genre'

class writeGenre:

    def __init__(self):
        self.book = xlwt.Workbook()
        self.sh = self.book.add_sheet('Movies')

        # keeps track of the current row to be written too
        self.curGenreInTable = 1

        # set up titleRow
        self.sh.write(titleRow, MOVIEID, name_MovieID_col)
        self.sh.write(titleRow, GENRE, name_Genre_col)

        # save the workbook
        self.book.save('Genre.xls')

    def addGenre(self, movieID, genre):
        self.sh.write(self.curGenreInTable, MOVIEID, movieID)
        self.sh.write(self.curGenreInTable, GENRE, genre)

        self.book.save('Genre.xls')

        self.curGenreInTable = self.curGenreInTable + 1
