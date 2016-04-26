import xlwt

# this is the title row
titleRow = 0

# constants for columns
ROLEIDCOL = 0
PERSONIDCOL = 1
MOVIEIDCOL = 2
ISACTORCOL = 3
ISWRITERCOL = 4
ISDIRECTORCOL = 5
ISPRODUCERCOL = 6

# names of the columns
name_RoleID_col = 'RoleID'
name_MovieID_col = 'MovieID'
name_PersonID_col = 'PersonID'
name_isActor_col = 'isActor'
name_isWriter_col = 'isWriter'
name_isDirector_col = 'isDirector'
name_isProducer_col = 'isProducer'

class writeRole:

    def __init__(self):
        self.book = xlwt.Workbook()
        self.sh = self.book.add_sheet('Role')

        # keeps track of the current row to be written too
        self.curRoleInTable = 1

        # set up title row
        self.sh.write(titleRow, ROLEIDCOL, name_RoleID_col)
        self.sh.write(titleRow, PERSONIDCOL, name_PersonID_col)
        self.sh.write(titleRow, MOVIEIDCOL, name_MovieID_col)
        self.sh.write(titleRow, ISACTORCOL, name_isActor_col)
        self.sh.write(titleRow, ISWRITERCOL, name_isWriter_col)
        self.sh.write(titleRow, ISDIRECTORCOL, name_isDirector_col)
        self.sh.write(titleRow, ISPRODUCERCOL, name_isProducer_col)

        # save thee workbook
        self.book.save('Role.xls')

    def addRole(self, PersonID, MovieID, role):

        # curRoleInTable will be the RoleID
        self.sh.write(self.curRoleInTable, ROLEIDCOL, self.curRoleInTable)
        self.sh.write(self.curRoleInTable, PERSONIDCOL, PersonID)
        self.sh.write(self.curRoleInTable, MOVIEIDCOL, MovieID)

        # determine role
        # 0 = actor
        # 1 = writer
        # 2 = director
        # 3 = producer

        if(role == 0):
            self.sh.write(self.curRoleInTable, ISACTORCOL, 'yes')
            self.sh.write(self.curRoleInTable, ISWRITERCOL, 'no')
            self.sh.write(self.curRoleInTable, ISDIRECTORCOL, 'no')
            self.sh.write(self.curRoleInTable, ISPRODUCERCOL, 'no')
        elif(role == 1):
            self.sh.write(self.curRoleInTable, ISACTORCOL, 'no')
            self.sh.write(self.curRoleInTable, ISWRITERCOL, 'yes')
            self.sh.write(self.curRoleInTable, ISDIRECTORCOL, 'no')
            self.sh.write(self.curRoleInTable, ISPRODUCERCOL, 'no')
        elif(role == 2):
            self.sh.write(self.curRoleInTable, ISACTORCOL, 'no')
            self.sh.write(self.curRoleInTable, ISWRITERCOL, 'no')
            self.sh.write(self.curRoleInTable, ISDIRECTORCOL, 'yes')
            self.sh.write(self.curRoleInTable, ISPRODUCERCOL, 'no')
        elif(role == 3):
            self.sh.write(self.curRoleInTable, ISACTORCOL, 'no')
            self.sh.write(self.curRoleInTable, ISWRITERCOL, 'no')
            self.sh.write(self.curRoleInTable, ISDIRECTORCOL, 'no')
            self.sh.write(self.curRoleInTable, ISPRODUCERCOL, 'yes')

        # save the workbook
        self.book.save('Role.xls')

        self.curRoleInTable = self.curRoleInTable + 1
