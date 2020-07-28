import json
import xlsxwriter

def max_length(input_list):
# functia primeste o lista si returneaza lungimea elementului cel mai lung
    len_max = 0
    for i in range(len(input_list)):
        if len(input_list[i]) >= len_max:
            len_max = len(input_list[i])
    return len_max

def excel_2015_2016(file):
    f = open(file)
    data = json.load(f)
    round, date, home, result, away, unibet, betfair, winmasters, betano, fortuna, netbet = ([] for i in range(11))
    headers = ["Date", "Round", "Home", "Result", "Away"] + ["1", "X", "2"] * 4
    case = ["Unibet", "Fortuna", "Betfair", "NetBet"]

    for meci in data:
        # print(meci["Winmasters.ro"])
        # print(meci["Fortuna.ro"])
        round.append(meci["fixture"])
        date.append(meci["date_time"][0])
        home.append(meci["home_team"])
        result.append(meci["result"])
        away.append(meci["away_team"])
        try:
            unibet.append(meci["Unibet"])
        except KeyError:
            unibet.append([" ", " ", " "])
        try:
            fortuna.append(meci["Fortuna.ro"])
        except KeyError:
            fortuna.append([" ", " ", " "])
        try:
            betfair.append(meci["Betfair"])
        except KeyError:
            betfair.append([" ", " ", " "])
        # pt sezonul 2019-2020 nu exista netbet, deci trebuie modificat de la sezon la sezon
        try:
            netbet.append(meci["NetBet"])
        except KeyError:
            netbet.appent([" ", " ", " "])
        # betano.append(meci["Betano"])
        # winmasters.append(meci["Winmasters.ro"])
        # for key, value in meci.items():
        #     print(key, value)
    print(round, date, unibet, betfair, netbet, betano, fortuna, winmasters)
    print(str(len(unibet)) + " Unibet: " + str(unibet))
    print(str(len(netbet)) + " netbet: " + str(netbet))
    print(str(len(betano)) + " betano: " + str(betano))
    print(str(len(fortuna)) + " fortuna: " + str(fortuna))
    print(str(len(betfair)) + " betfair: " + str(betfair))
    print(str(len(winmasters)) + " winmasters: " + str(winmasters))

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

    worksheet.merge_range(0, 0, 0, 4, nume_excel, bold)
    count = 0
    for casa in case:
        worksheet.merge_range(0, 5 + count, 0, 7 + count, casa, bold)
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
        for j in range(3):
            worksheet.write(row + i, 5 + j, unibet[i][j], middle)
            #print(i, j, unibet[i][j])
# astea trebuie puse in ordinea in care sunt colectate din site, altfel da eroare
            print(i, j, fortuna[i][j])
            worksheet.write(row + i, 8 + j, fortuna[i][j], middle)
            worksheet.write(row + i, 11 + j, betfair[i][j], middle)
            worksheet.write(row + i, 14 + j, netbet[i][j], middle)

            #worksheet.write(row + i, 14 + j, betano[i][j], middle)
            #worksheet.write(row + i, 20 + j, winmasters[i][j], middle)
    workbook.close()

#file = "meciuri_salvate_19-20.txt"
#file = "meciuri_salvate_corect_18-19.txt"
file = "meciuri_salvate_15-16.txt"
excel_2015_2016(file)
