# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import openpyxl
import csv
import sys
file_name = sys.argv
# %%
analysts=['Wesley dos Santos Azevedo', 'Matheus Serafim da Silva', 'Danillo Bellopedo Ferraz', 'Paziana de Jesus Silva', 'Thiago Souza', 'Larissa Evaristo', 'Priscila Prado', 'Igor Nascimento', 'Diana Negreiro', 'Daniel Silva', 'Marco Arcuri', 'Bruna Barbosa']

filter_datas = []
with open(f'{file_name[1]}', 'r') as archive:
    datas = csv.reader(archive) # read the datas
    for data in datas:
        if data[0] in analysts:
            filter_datas.append(data)


# %%
book = openpyxl.Workbook() # create sheet

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