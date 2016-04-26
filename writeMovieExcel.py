import xlwt
import getMovieInfo
import parseTime

# this is the title row
titleRow = 0

# constants for columns
MOVIEIDCOL = 0
MOVIETITLECOL = 1
MOVIERELEASEYEARCOL = 2
MOVIEUSERRATINGCOL = 3
MOVIEMPAARATINGCOL = 4
MOVIELENGTHCOL = 5
MOVIEGROSSCOL = 6

# names of the columns
name_MovieID_col = 'MovieID'
name_MovieTitle_col = 'Title'
name_ReleaseYear_col = 'ReleaseYear'
name_UserRating_col = 'UserRating'
name_MPAARating_col = 'MPAARating'
name_MovieLength_col = 'Length'
name_MovieGross_col = 'Gross'

class writeMovie:

    def __init__(self):
        self.book = xlwt.Workbook()
        self.sh = self.book.add_sheet('Movies')

        # keeps track of the current row to be written too
        self.curMovieInTable = 1

        # set up title row
        self.sh.write(titleRow, MOVIEIDCOL, name_MovieID_col)
        self.sh.write(titleRow, MOVIETITLECOL, name_MovieTitle_col)
        self.sh.write(titleRow, MOVIERELEASEYEARCOL, name_ReleaseYear_col)
        self.sh.write(titleRow, MOVIEUSERRATINGCOL, name_UserRating_col)
        self.sh.write(titleRow, MOVIEMPAARATINGCOL, name_MPAARating_col)
        self.sh.write(titleRow, MOVIELENGTHCOL, name_MovieLength_col)
        self.sh.write(titleRow, MOVIEGROSSCOL, name_MovieGross_col)

        # save the workbook
        self.book.save('Movie.xls')

    def addMovie(self, name, numActors):
        # returns the MovieID and actorList in a list
        returnList = []

        movie = getMovieInfo.Movie(name)

        # get MovieID
        movieID = movie.getMovieID()

        self.sh.write(self.curMovieInTable, MOVIEIDCOL, movieID)

        # get Movie title
        movieTitle = movie.getTitle()

        self.sh.write(self.curMovieInTable, MOVIETITLECOL, movieTitle)

        # get movie ReleaseYear
        movieReleaseYear = movie.getReleaseYear()

        self.sh.write(self.curMovieInTable, MOVIERELEASEYEARCOL, movieReleaseYear)

        # get user rating
        movieUserRating = movie.getUserRating()

        self.sh.write(self.curMovieInTable, MOVIEUSERRATINGCOL, movieUserRating)

        # get MPAA rating
        movieMPAARating = movie.getMPAARating()

        self.sh.write(self.curMovieInTable, MOVIEMPAARATINGCOL, movieMPAARating)

        # get movie Length
        movieLength = movie.getRuntime()

        movieLength = parseTime.parseMinutes(movieLength)

        hourMinStyle = xlwt.easyxf(num_format_str='hh:mm')

        self.sh.write(self.curMovieInTable, MOVIELENGTHCOL, movieLength, hourMinStyle)

        # get movie Gross and format
        movieGross = movie.getGross()

        currencyStyle = xlwt.easyxf(num_format_str='"$"#,##0.00_);("$"#,##')
        self.sh.write(self.curMovieInTable, MOVIEGROSSCOL, movieGross, currencyStyle)

        # get the list of actors of length numActors
        actorList = movie.getActors(numActors)

        # get the list of directors
        directorList = movie.getDirectorList()

        # get the list of writers
        writerList = movie.getWriterList()

        # get the list of producer
        producerList = movie.getProducerList()

        # get the list of genres
        genreList = movie.getGenre()

        # fill the list with the return information
        returnList = [movieID, actorList, directorList, writerList, producerList, genreList]

        # save the workbook
        self.book.save('Movie.xls')

        self.curMovieInTable = self.curMovieInTable + 1

        return returnList
