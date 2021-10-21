import openpyxl
import csv

def csv_filter(analistas, nomeArquivo):
    validator = []
    with open(f'{nomeArquivo}.csv', 'r') as arquivo:
        dados = csv.reader(arquivo)

        for dado in dados:
            if dado[0] in analistas:
                validator.append(dado)
    return validator


def criacao_das_planilhas():
    book = openpyxl.Workbook()
    print(book.sheetnames)


if __name__ == '__main__':
    csv_filter(analistas=['Wesley dos Santos Azevedo', 'Matheus Serafim da Silva', 'Danillo Bellopedo Ferraz', 'Paziana de Jesus Silva', 'Thiago Souza', 'Larissa Evaristo', 'Priscila Prado', 'Igor Nascimento', 'Diana Negreiro', 'Daniel Silva', 'Marco Arcuri', 'Bruna Barbosa'], nomeArquivo='diario')