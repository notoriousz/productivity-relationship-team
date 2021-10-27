# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import openpyxl
import csv
import sys
from configparser import ConfigParser

file_name = sys.argv
# %%

def analysts_names(filename="analysts.ini", section="analysts"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {} # will return the dict with the config
    if parser.has_section(section):
        params = parser.items(section)
        for key, value in params:
            db[key] = value
    else:
        raise Exception(f"Section {section} has no found")
    return db

def main(analysts_args):
    filter_datas = []

    with open(f'{file_name[1]}', 'r') as archive:
        datas = csv.reader(archive) # read the datas
        for data in datas:
            if data[0] in analysts:
                filter_datas.append(data)
    # %%
    # create sheet
    book = openpyxl.Workbook()
    # create pages
    for name in analysts:
        book.create_sheet(name)

    # add datas for each page
    for analyst in analysts:
        actual_page = book[analyst]
        actual_page.append(["Nome do atualizador","Atualização - Data","."]) # header from columns
        for datas in filter_datas:
            if datas[0] == analyst:
                actual_page.append(datas)
    # save
    book.save('produtividade-gigantes.xlsx')

if __name__ == '__main__':
    analysts_filter_names = analysts_names()
    analysts = list(analysts_filter_names.values())
    main(analysts)