import pandas as pd

def column_header_reader(excel_file, print_columns=False):
   """
   The function returns the column headers of the imported excel_file.

   Args:
     excel_file: imported Excel file to be saved into a pandas DataFrame.
     print_columns: boolean value (optional). If print_columns is True the list is also displayed.

   Output:
     column_headers: list of column headers of the Excel file.

   """
   dataframe = pd.read_excel(excel_file)
   column_headers = list(dataframe.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
