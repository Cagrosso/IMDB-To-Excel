import sys
import random

try:
    import imdb
except ImportError:
    print "IMDbPy not found, please install"
    sys.exit(1)

class Person:

    def __init__(self, submittedName):
        # Initializes the Person object.  'submittedName' is the unchedked
        # name given by the user

        self.submittedName = submittedName
        # this is the IMDb object to retrieve information
        self.i = imdb.IMDb()

        try:
            # takes the best match of the returned list
            self.result = self.i.search_person(self.submittedName)[0]
        except imdb.IMDbError, e:
            print "Error searching for person"
            print e
            sys.exit(0)

        if not self.result:
            print "No such person of '%s' name found" % self.submittedName
            sys.exit(0)

        self.i.update(self.result)

    def getKeys(self):
        return sorted(self.result.keys())

    def getDoB(self):
        # return the birth year of the person
        # returns randomly generated DoB if none returned
        try:
            year = int(self.result.get('birth date'))
        except:
            year = random.randint(1940, 1995)

        day = random.randint(1, 27)
        month = random.randint(1, 12)

        birthdate = '%s %s %s' % (day, month, year)

        return birthdate

    def getPersonID(self):
        # return the IMDb personID
        return self.result.personID

    def getName(self):
        # return the person's name in a list
        fullName = self.result.get('name').split()
        return fullName

    def getBirthPlace(self):
        # return comma split list of birth place
        birthplace = self.result.get('birth notes')

        # if None is returned, put San Francisco
        try:
            birthplace = birthplace.split(',')
        except:
            birthplace = ['San Francisco', 'California', 'USA']
            
        # assumes just town and country given
        if len(birthplace) == 2:
            birthplace = [birthplace[0], 'None', birthplace[1]]

        # assumes just country given
        if len(birthplace) == 1:
            birthplace = ['None', 'None', birthplace[0]]

        return birthplace
