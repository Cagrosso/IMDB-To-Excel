import sys
import random

try:
    import imdb
except ImportError:
    print "IMDbPy not found, please install"
    sys.exit(1)

class Movie:

    def __init__(self, submittedTitle):
        # Initializes the Movie object.  'submittedTitle' is the unchecked
        # title given by the user.

        self.submittedTitle = submittedTitle
        # this is the IMDb object to retrieve information
        self.i = imdb.IMDb()

        try:
            # takes the best match of the returned list
            self.result = self.i.search_movie(self.submittedTitle)[0]
        except imdb.IMDbError, e:
            print "Error searching for movie"
            print e
            sys.exit(0)

        if not self.result:
            print "No such movie of '%s' title found" % self.submittedTitle
            sys.exit(0)

        self.i.update(self.result)

    def getKeys(self):
        return sorted(self.result.keys())

    def getTitle(self):
        # Returns the IMDb checked title of the movie
        return self.result.get('title')

    def getReleaseYear(self):
        # Returns the release year of the movie
        return self.result.get('year')

    def getProducerList(self):
        # return the list of producers
        producerList = self.result.get('producer')
        if producerList == 'None':
            return 'None'
        elif len(producerList) < 3:
            return producerList
        else:
            return producerList[:2]

        returnList = []

        for producer in producerList:
            returnList.append('%s' % producer)

        return returnList

    def getDirectorList(self):
        # Returns name of the Director
        directorList = self.result.get('director')

        returnList = []

        for director in directorList:
            returnList.append('%s' % director)

        return returnList

    def getWriterList(self):
        # returns names of the writers
        writerList = self.result.get('writer')
        if len(writerList) > 3:
            writerList = writerList[:2]

        returnList = []

        for writer in writerList:
            returnList.append('%s' % writer)

        return returnList

    def getMovieID(self):
        # Returns IMDB movie ID
        return self.result.movieID

    def getUserRating(self):
        # Returns IMDb user rating
        return self.result.get('user rating')

    def getGenre(self):
        # return the IMDb getGenre
        return self.result.get('genre')

    def getRuntime(self):
        # returns the runtime of the movie
        # some movies may have multiple run lengths, I chose the Theatrical version
        return self.result.get('runtime')[0]

    def getMPAARating(self):
        # return the MPAA Rating for the movie
        ratingList = self.result.get('certificates')
        ratingList = [rating.strip() for rating in ratingList]
        rating = ratingList[len(ratingList) - 1]

        # US MPAA rating seems to mostly be the last value in list
        rating = rating.split(':')[1]

        if rating != 'G':
            if rating != 'PG':
                if rating != 'PG-13':
                    if rating != 'R':
                        # default rating if US rating was not chosen
                        rating = 'PG'

        return rating

    def getGross(self):
        # return the Gross made by the movie
        # random number for now
        Gross = random.randint(100000000, 999999999)
        return Gross

    def getActors(self, n):
        # return 'n' number of actors/actresses in movie
        actorList = self.result.get('cast')[:n]
        returnList = []

        for actor in actorList:
            name = '%s' % actor
            returnList.append(name)

        return returnList
