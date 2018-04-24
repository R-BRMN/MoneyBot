from Sheeter import *

if __name__ == "__main__":
    print (Sheeter)
    Sheeter.initialize_gsheets()
    print (Sheeter.get_month_sheet())
    # Sheeter.create_sheet("test1234", first_worksheet="this_worked!")
    print(Sheeter.workbook_exist("test1234","this_worked!"))
