import pygsheets

class Sheeter:
    """Sheeter is responsible for managing the Spreadsheets on Google Drive.

    Attributes:
        gsheets_client: A pygsheets instance associated with the Google account
                        whose client_id credentials are in the client_secret json.
    """
    def __init__(self):
        self.gsheets_client = pygsheets.authorize()
