import mysql.connector
import csv
import helpers

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS maddenpredictor")
mycursor.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="maddenpredictor",
  autocommit=True)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS madden_overalls (team VARCHAR(255), position VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255), overall INTEGER, madden_version VARCHAR(4))")

for version in helpers.versions:
    print('Importing version ' + version + '...')
    for team in helpers.get_teams(version):
        print(team)
        with open('MaddenRosters/' + version + '/' + team + '.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    mycursor.execute('INSERT INTO madden_overalls(team, position, first_name, last_name, overall, madden_version) VALUES("' + row[0] + '", "' + row[1] + '", "' + row[2] + '", "' + row[3] + '", "' + row[4] + '", "' + row[5] + '")')
                    line_count += 1

mycursor.close()