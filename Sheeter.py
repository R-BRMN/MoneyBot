import pygsheets
import datetime

class Sheeter:
    """Sheeter is responsible for managing the spreadsheets on Google Drive.
    Static class.

    Parameters:
        gsheets_client: The pygsheets client facing the Google spreadsheets.
    """

    @staticmethod
    def initialize_gsheets():
        """Approves the pygsheets client to work with the Google account whose
        credentials are in the client_secret file.
        """
        global gsheets_client
        gsheets_client = pygsheets.authorize()

    @staticmethod
    def sheet_exist(name):
        """Depends on whether the spreadsheet exists.

        Returns: True / False
        """
        ssheet_list = gsheets_client.list_ssheets()
        for ssheet in ssheet_list:
            if ssheet["name"] == name:
                return True
        return False

    @staticmethod
    def month_sheet_exist():
        """True or False depending on whether current's month spreadsheet exists.
        Spreadsheet name format is Month_YY.

        Returns: True / False
        """
        curr_month = datetime.datetime.now().strftime("%B_%y")
        return Sheeter.sheet_exist(curr_month)

    @staticmethod
    def get_sheet(name):
        """Returns the spreadsheet for the param name

        Returns: Spreadsheet object / None
        """
        if Sheeter.sheet_exist(name):
            return gsheets_client.open(name)
        return

    @staticmethod
    def create_sheet(name, first_worksheet=None):
        """Creates a spreadsheet with one workbook(Sheet1 unless specified).

        Returns: Spreadsheet object
        """
        sheet = gsheets_client.create(name)
        if first_worksheet:
                sheet.add_worksheet(first_worksheet) #TODO change add_worksheet to a local better method.
                sheet.del_worksheet(sheet.worksheet_by_title("Sheet1"))
        return sheet


    @staticmethod
    def get_month_sheet():
        """Return this months spreadsheet object, whether it existed before or not.

        Returns: Spreadsheet object
        """
        curr_month = datetime.datetime.now().strftime("%B_%y")
        if Sheeter.month_sheet_exist():
            return Sheeter.get_sheet(curr_month)
        return Sheeter.create_sheet(curr_month)

#test
#gfdgd
