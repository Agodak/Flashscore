import json
import xlsxwriter

def max_length(input_list):
# functia primeste o lista si returneaza lungimea elementului cel mai lung
    len_max = 0
    for i in range(len(input_list)):
        if len(input_list[i]) >= len_max:
            len_max = len(input_list[i])
    return len_max

#file = "meciuri_salvate_19-20.txt"
file = "meciuri_salvate_corect_18-19.txt"
f = open(file)
data = json.load(f)
round, date, home, result, away, unibet, betfair, winmasters, betano, fortuna, netbet = ([] for i in range(11))
headers = ["Date", "Round", "Home", "Result", "Away"] + ["1", "X", "2"] * 6
case = ["Unibet", "Betfair", "NetBet", "Betano", "Fortuna", "Winmasters"]

for meci in data:
    # print(meci["Winmasters.ro"])
    # print(meci["Betano"])
    round.append(meci["fixture"])
    date.append(meci["date_time"][0])
    home.append(meci["home_team"])
    result.append(meci["result"])
    away.append(meci["away_team"])
    try:
        unibet.append(meci["Unibet"])
        betfair.append(meci["Betfair"])
    # pt sezonul 2019-2020 nu exista netbet, deci trebuie modificat de la sezon la sezon
        netbet.append(meci["NetBet"])
        betano.append(meci["Betano"])
        fortuna.append(meci["Fortuna.ro"])
        winmasters.append(meci["Winmasters.ro"])
    except:
        pass
print(round, date)
print(headers)
workbook = xlsxwriter.Workbook(file[:-3] + 'xlsx')
worksheet = workbook.add_worksheet()
nume_excel = "Premier League " + file[-9:-4]
print(nume_excel)
bold = workbook.add_format({'bold': True})
middle = workbook.add_format()
middle.set_align('center')
bold.set_align('center')
worksheet.set_column('A:A', max_length(date), middle)
worksheet.set_column('C:C', max_length(home))
worksheet.set_column('E:E', max_length(away))
worksheet.set_column('F:T', max_length(betano) + 5)


row = 1
column = 0


worksheet.merge_range(0,0,0,4, nume_excel,bold)
count = 0
for casa in case:
    worksheet.merge_range(0,5+count,0,7+count, casa, bold)
    count += 3



for header in headers:
    worksheet.write(row, column, header, bold)
    column += 1

row = 2
for i in range(len(date)):
    worksheet.write(row + i, 0, date[i])
    worksheet.write(row + i, 1, round[i], middle)
    worksheet.write(row + i, 2, home[i])
    worksheet.write(row + i, 3, "-".join(result[i]), middle)
    worksheet.write(row + i, 4, away[i])
    try:
        for j in range(3):
            worksheet.write(row + i, 5+j, unibet[i][j], middle)
            worksheet.write(row + i, 8+j, betfair[i][j], middle)
            worksheet.write(row + i, 11+j, netbet[i][j], middle)
            worksheet.write(row + i, 14+j, betano[i][j], middle)
            worksheet.write(row + i, 17+j, fortuna[i][j], middle)
            worksheet.write(row + i, 20+j, winmasters[i][j], middle)
    except IndexError:
        pass
workbook.close()