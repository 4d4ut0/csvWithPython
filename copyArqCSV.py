import csv, sys
nome_ficheiro = 'aqui.csv'
nome_ficheiro_saida = 'new.csv'
writer = csv.writer(open(nome_ficheiro_saida, 'wb'))
with open(nome_ficheiro, 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    try:
        for linha in reader:
            print linha
            writer.writerow(linha)

    except csv.Error as e:
        sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))