import xlrd
import xlwt
import pandas

file_path = input("Please insert file location")
file_name = input("Please insert file name")

def optimizer(file_path, file_name):
    file = file_path + file_name

    df = pandas.read_excel(file, header=None)
    print(df.head(2))
    df = df.drop([0], axis=0)
    print(df.head(2))

    # wrkbk = xlrd.open_workbook(file)
    # wrkst = wrkbk.sheet_by_index(0)
    # row_zero = wrkst.row(0)
    # print(row_zero)
    # row_zero.flush_row_data()
    # print(row_zero)

optimizer(file_path, file_name)