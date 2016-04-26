import writePersonExcel
import writeMovieExcel
import writeRoleExcel
import writeGenreExcel

import getMovieInfo

# movie returnList indexs
MOVIEID = 0
ACTORLIST = 1
DIRECTORLIST = 2
WRITERLIST = 3
PRODUCERLIST = 4
GENRELIST = 5

moviesToSearch = ['Star Wars']

# initialize all tables
genreTable = writeGenreExcel.writeGenre()
movieTable = writeMovieExcel.writeMovie()
personTable = writePersonExcel.writePerson()
roleTable = writeRoleExcel.writeRole()

for movieTitle in moviesToSearch:
    print movieTitle
    returnList = movieTable.addMovie(movieTitle, 3)

    actorList = returnList[ACTORLIST]
    directorList = returnList[DIRECTORLIST]
    writerList = returnList[WRITERLIST]
    producerList = returnList[PRODUCERLIST]
    genreList = returnList[GENRELIST]

    movieID = returnList[MOVIEID]

    for actor in actorList:
        print 'actor: %s' % actor
        actorID = personTable.addPerson(actor)

        # adds a spot in the role table as 'Actor'
        roleTable.addRole(actorID, movieID, 0)

    for writer in writerList:
        print 'writer: %s' % writer
        actorID = personTable.addPerson(writer)

        # adds a spot in the role table as 'writer'
        roleTable.addRole(actorID, movieID, 1)

    for director in directorList:
        print 'director: %s' % director
        actorID = personTable.addPerson(director)

        # adds a spot in the role table as 'director'
        roleTable.addRole(actorID, movieID, 2)

    for producer in producerList:
        print 'producer: %s' % producer
        actorID = personTable.addPerson('%s' % producer)

        # adds a spot in the role table as 'producer'
        roleTable.addRole(actorID, movieID, 3)

    for genre in genreList:
        print 'Genre for: %s' % genre
        genreTable.addGenre(movieID, genre)
