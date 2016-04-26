import xlwt
from getPersonInfo import Person
import parseTime
from datetime import datetime

# this is the title row
titleRow = 0

# constants for column
PERSONIDCOL = 0
PERSONFIRSTNAME = 1
PERSONLASTNAME = 2
PERSONDOB = 3
PERSONBIRTHTOWN = 4
PERSONBIRTHSTATE = 5
PERSONBIRTHCOUNTRY = 6

name_PersonID_col = 'PersonID'
name_FirstName_col = 'FName'
name_LastName_col = 'LName'
name_DoB_col = 'DoB'
name_BirthTown_col = 'BirthPlaceTown'
name_BirthState_col = 'BirthPlaceState'
name_BirthCountry_col = 'BirthPlaceCountry'

class writePerson:

    def __init__(self):
        self.book = xlwt.Workbook()
        self.sh = self.book.add_sheet('Persons')

        # keeps track of the current row to be written to
        self.curPersonInTable = 1

        # set up title row
        self.sh.write(titleRow, PERSONIDCOL, name_PersonID_col)
        self.sh.write(titleRow, PERSONFIRSTNAME, name_FirstName_col)
        self.sh.write(titleRow, PERSONLASTNAME, name_LastName_col)
        self.sh.write(titleRow, PERSONDOB, name_DoB_col)
        self.sh.write(titleRow, PERSONBIRTHTOWN, name_BirthTown_col)
        self.sh.write(titleRow, PERSONBIRTHSTATE, name_BirthState_col)
        self.sh.write(titleRow, PERSONBIRTHCOUNTRY, name_BirthCountry_col)

        # save the workbook
        self.book.save('Person.xls')

    def addPerson(self, name):
        person = Person(name)

        # get personID
        personID = person.getPersonID()
        self.sh.write(self.curPersonInTable, PERSONIDCOL, personID)

        # get and parse First and Last name
        personName = person.getName()
        personFirstName = personName[0]
        personLastName = personName[1:]

        self.sh.write(self.curPersonInTable, PERSONFIRSTNAME, personFirstName)
        self.sh.write(self.curPersonInTable, PERSONLASTNAME, personLastName)

        # get and parse Date of Birth
        personDoBString = person.getDoB()
        personDoB = parseTime.parseDate(personDoBString)

        # create the style that the string will be formatted to
        styleDOB = xlwt.easyxf(num_format_str='D-MMM-YY')

        self.sh.write(self.curPersonInTable, PERSONDOB, personDoB, styleDOB)

        # get and parse the Birth Town, Birth State, and Birth Country
        # WON'T WORK CORRECTLY IF MORE THAN 3 ITEMS IN BIRTHPLACE
        birthPlace = person.getBirthPlace()
        birthTown = birthPlace[0]
        birthState = birthPlace[1]
        birthCountry = birthPlace[2]

        self.sh.write(self.curPersonInTable, PERSONBIRTHTOWN, birthTown)
        self.sh.write(self.curPersonInTable, PERSONBIRTHSTATE, birthState)
        self.sh.write(self.curPersonInTable, PERSONBIRTHCOUNTRY, birthCountry)

        # save the Workbook
        self.book.save('Person.xls')

        # increase class counter to put next person in following row
        self.curPersonInTable = self.curPersonInTable + 1

        return personID
