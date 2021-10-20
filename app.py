import openpyxl
import csv

def csv_filter(analistas, nomeArquivo):
    validator = []
    with open(f'{nomeArquivo}.csv', 'r') as arquivo:
        dados = csv.reader(arquivo) # le os dados que estão no csv

        for dado in dados:
            if dado[0] in analistas:
                validator.append(dado)
    return validator


def criacao_das_planilhas():
    # criar planilha
    book = openpyxl.Workbook()
    # Paginas
    print(book.sheetnames)
    # Criando pagina para cada analista


if __name__ == '__main__':
    csv_filter(analistas=['Wesley dos Santos Azevedo', 'Matheus Serafim da Silva', 'Danillo Bellopedo Ferraz', 'Paziana de Jesus Silva', 'Thiago Souza', 'Larissa Evaristo', 'Priscila Prado', 'Igor Nascimento', 'Diana Negreiro', 'Daniel Silva', 'Marco Arcuri', 'Bruna Barbosa'], nomeArquivo='diario')

    # criacao_das_planilhas()