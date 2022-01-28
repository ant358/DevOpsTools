import datetime
import os

####################################80##########################################
class All_Paths(object):
    """All the global paths and settings for a program
    As the program is being developed collect all input 
    and output paths in this class. Then you only have one
    place to change them. 
    
    from settings import All_Paths
    paths = All_Paths()
    """
    def __init__(self, business_unit='XX', country='GB'):
        # get current date to adjust time dependent paths
        self.datestamp     = datetime.datetime.now()
        self.curr_month    = self.datestamp.strftime('%m')
        self.curr_year     = self.datestamp.strftime('%Y')
        self.month_name    = self.datestamp.strftime('%B')
        self.curr_period   = f"{self.curr_year}-{self.curr_month}-01"
        self.business_unit = business_unit
        self.country       = country
        self.user          = os.getlogin()

   
        # code root 
        self.root = (f"C:\\Users\\{self.user}\\OneDrive\\"
        "Documents\\Python\\some_program\\")
        
        # database
        self.sqlite    = 'sqlite:///data/database.db'
        
        # connect to the database from root
        self.sqlite_full_path = f'sqlite:///{self.root}data/database.db'

        # tests
        self.tests = f"C:\\Users\\{self.user}\\OneDrive\\Documents\\Python\\some_program\\tests\\"
        
        # output paths

        # input paths 
        
        # temp output folder
        self.temp_folder = self.root + "temp\\"


if __name__ == "__main__":
    
    pth = AC_Paths()
    # Tests development
    # Is there a correct path to a file NOTE all_paths no longer exists - needs an edit :-)
    for d in pth.all_paths['files'].items():
        print(d[0] + ' exists: ' + str(os.path.isfile(d[1])))
    # does the folder exist?
    for d in pth.all_paths['folders'].items():
        print(d[0] + ' exists: ' + str(os.path.isdir(d[1])))
