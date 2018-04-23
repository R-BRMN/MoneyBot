import pygsheets
import datetime

class Sheeter:
    """Sheeter is responsible for managing the spreadsheets on Google Drive.

    Attributes:
        gsheets_client: A pygsheets instance associated with the Google account
                        whose client_id credentials are in the client_secret json.
    """
    def __init__(self):
        self.gsheets_client = pygsheets.authorize()

    def sheet_exists(self, name):
        """True or False depending on whether the spreadsheet exists.
        """
        ssheet_list = self.gsheets_client.list_ssheets()
        for ssheet in ssheets_list:
            if ssheet["name"] == name:
                return True
        return False

    def months_sheet_exists(self):
        """True or False depending on whether current's month spreadsheet exists.
        Spreadsheet name format is Month_YY.
        """
        curr_month = datetime.datetime.now().strftime("%B_%y")
        return self.sheet_exists(curr_month)
