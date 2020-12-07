import csv
with open('select_RNP_instituicoes_sigla_instituica.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:        
        print(f' Institution: \t{row[0]} | id_estatistica: {row[1]} | IP: {row[2]}')
        line_count += 1
    print(f'Processed {line_count} lines.')