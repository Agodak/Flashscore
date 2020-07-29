import json
import xlsxwriter
import os
import shutil

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
    shutil.move(os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//text files", file[:-3] + 'xlsx'),
                os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//excel files", file[:-3] + 'xlsx'))


def excel_2016_2017(file):
    f = open(file)
    data = json.load(f)
    round, date, home, result, away, unibet, betfair, winmasters, betano, fortuna, netbet, bet365 = ([] for i in range(12))
    headers = ["Date", "Round", "Home", "Result", "Away"] + ["1", "X", "2"] * 5
    case = ["Unibet", "Fortuna", "Winmasters", "Betfair", "NetBet"]

    for meci in data:
        # print(meci["Winmasters.ro"])
        # print(meci["Fortuna.ro"])
        try:
            round.append(meci["fixture"])
        except KeyError:
            round.append(" ")
        try:
            date.append(meci["date_time"][0])
        except KeyError:
            date.append(" ")
        try:
            home.append(meci["home_team"])
        except KeyError:
            home.append(" ")
        try:
            result.append(meci["result"])
        except KeyError:
            result.append(" ")
        try:
            away.append(meci["away_team"])
        except KeyError:
            away.append(" ")
        try:
            unibet.append(meci["Unibet"])
        except KeyError:
            unibet.append([" ", " ", " "])
        try:
            fortuna.append(meci["Fortuna.ro"])
        except KeyError:
            fortuna.append([" ", " ", " "])
        try:
            winmasters.append(meci["Winmasters.ro"])
        except KeyError:
            winmasters.append([" ", " ", " "])
        try:
            betfair.append(meci["Betfair"])
        except KeyError:
            betfair.append([" ", " ", " "])
        try:
            netbet.append(meci["NetBet"])
        except KeyError:
            netbet.append([" ", " ", " "])
        # pt sezonul 2019-2020 nu exista netbet, deci trebuie modificat de la sezon la sezon

        # betano.append(meci["Betano"])
        # winmasters.append(meci["Winmasters.ro"])
        # for key, value in meci.items():
        #     print(key, value)
    print(round, date, bet365, unibet, betfair, netbet, betano, fortuna, winmasters)
    print(str(len(bet365)) + "bet365: " + str(bet365))
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
            worksheet.write(row + i, 8 + j, fortuna[i][j], middle)
            worksheet.write(row + i, 11 + j, winmasters[i][j], middle)
            worksheet.write(row + i, 14 + j, betfair[i][j], middle)
            worksheet.write(row + i, 17 + j, netbet[i][j], middle)
            #print(i, j, unibet[i][j])
# astea trebuie puse in ordinea in care sunt colectate din site, altfel da eroare
            print(i, j, fortuna[i][j])




            #worksheet.write(row + i, 14 + j, betano[i][j], middle)

    workbook.close()

    shutil.move(os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//text files", file[:-3] + 'xlsx'),
                os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//excel files", file[:-3] + 'xlsx'))


def excel_2017_2018(file):
    f = open(file)
    data = json.load(f)
    round, date, home, result, away, unibet, betfair, winmasters, betano, fortuna, netbet, bet365 = ([] for i in range(12))
    headers = ["Date", "Round", "Home", "Result", "Away"] + ["1", "X", "2"] * 6
    case = ["Bet 365", "Betfair", "NetBet", "Unibet", "Fortuna", "Winmasters"]

    for meci in data:
        # print(meci["Winmasters.ro"])
        # print(meci["Fortuna.ro"])
        try:
            round.append(meci["fixture"])
        except KeyError:
            round.append(" ")
        try:
            date.append(meci["date_time"][0])
        except KeyError:
            date.append(" ")
        try:
            home.append(meci["home_team"])
        except KeyError:
            home.append(" ")
        try:
            result.append(meci["result"])
        except KeyError:
            result.append(" ")
        try:
            away.append(meci["away_team"])
        except KeyError:
            away.append(" ")
        try:
            bet365.append(meci["bet365"])
        except KeyError:
            bet365.append([" ", " ", " "])
        try:
            betfair.append(meci["Betfair"])
        except KeyError:
            betfair.append([" ", " ", " "])
        try:
            netbet.append(meci["NetBet"])
        except KeyError:
            netbet.append([" ", " ", " "])
        try:
            unibet.append(meci["Unibet"])
        except KeyError:
            unibet.append([" ", " ", " "])
        try:
            fortuna.append(meci["Fortuna.ro"])
        except KeyError:
            fortuna.append([" ", " ", " "])
        try:
            winmasters.append(meci["Winmasters.ro"])
        except KeyError:
            winmasters.append([" ", " ", " "])

        # pt sezonul 2019-2020 nu exista netbet, deci trebuie modificat de la sezon la sezon

        # betano.append(meci["Betano"])
        # winmasters.append(meci["Winmasters.ro"])
        # for key, value in meci.items():
        #     print(key, value)
    print(round, date, bet365, unibet, betfair, netbet, betano, fortuna, winmasters)
    print(str(len(bet365)) + "bet365: " + str(bet365))
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
            worksheet.write(row + i, 5 + j, bet365[i][j], middle)
            worksheet.write(row + i, 8 + j, betfair[i][j], middle)
            worksheet.write(row + i, 11 + j, netbet[i][j], middle)
            worksheet.write(row + i, 14 + j, unibet[i][j], middle)
            worksheet.write(row + i, 17 + j, fortuna[i][j], middle)
            worksheet.write(row + i, 20 + j, winmasters[i][j], middle)
            #print(i, j, unibet[i][j])
# astea trebuie puse in ordinea in care sunt colectate din site, altfel da eroare
            print(i, j, fortuna[i][j])




            #worksheet.write(row + i, 14 + j, betano[i][j], middle)

    workbook.close()
    shutil.move(os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//text files", file[:-3] + 'xlsx'),
                os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//excel files", file[:-3] + 'xlsx'))

def excel_2018_2019(file):
    f = open(file)
    data = json.load(f)
    round, date, home, result, away, unibet, betfair, winmasters, betano, fortuna, netbet, bet365 = ([] for i in range(12))
    headers = ["Date", "Round", "Home", "Result", "Away"] + ["1", "X", "2"] * 6
    case = ["Unibet", "Betfair", "NetBet", "Betano", "Fortuna", "Winmasters"]

    for meci in data:
        # print(meci["Winmasters.ro"])
        # print(meci["Fortuna.ro"])
        try:
            round.append(meci["fixture"])
        except KeyError:
            round.append(" ")
        try:
            date.append(meci["date_time"][0])
        except KeyError:
            date.append(" ")
        try:
            home.append(meci["home_team"])
        except KeyError:
            home.append(" ")
        try:
            result.append(meci["result"])
        except KeyError:
            result.append(" ")
        try:
            away.append(meci["away_team"])
        except KeyError:
            away.append(" ")
        try:
            unibet.append(meci["Unibet"])
        except KeyError:
            unibet.append([" ", " ", " "])
        try:
            betfair.append(meci["Betfair"])
        except KeyError:
            betfair.append([" ", " ", " "])
        try:
            netbet.append(meci["NetBet"])
        except KeyError:
            netbet.append([" ", " ", " "])
        try:
            betano.append(meci["Betano"])
        except KeyError:
            betano.append([" ", " ", " "])
        try:
            fortuna.append(meci["Fortuna.ro"])
        except KeyError:
            fortuna.append([" ", " ", " "])
        try:
            winmasters.append(meci["Winmasters.ro"])
        except KeyError:
            winmasters.append([" ", " ", " "])

        # pt sezonul 2019-2020 nu exista netbet, deci trebuie modificat de la sezon la sezon

        # betano.append(meci["Betano"])
        # winmasters.append(meci["Winmasters.ro"])
        # for key, value in meci.items():
        #     print(key, value)
    print(round, date, bet365, unibet, betfair, netbet, betano, fortuna, winmasters)
    print(str(len(bet365)) + "bet365: " + str(bet365))
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
            worksheet.write(row + i, 8 + j, betfair[i][j], middle)
            worksheet.write(row + i, 11 + j, netbet[i][j], middle)
            worksheet.write(row + i, 14 + j, betano[i][j], middle)
            worksheet.write(row + i, 17 + j, fortuna[i][j], middle)
            worksheet.write(row + i, 20 + j, winmasters[i][j], middle)
            #print(i, j, unibet[i][j])
# astea trebuie puse in ordinea in care sunt colectate din site, altfel da eroare
            print(i, j, fortuna[i][j])




            #worksheet.write(row + i, 14 + j, betano[i][j], middle)

    workbook.close()
    shutil.move(os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//text files", file[:-3] + 'xlsx'),
                os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//excel files", file[:-3] + 'xlsx'))


def excel_for_all(file):
    f = open(file)
    data = json.load(f)
    # toate casele de pariuri
    case_pariuri = list(data[0].keys())[5:]
    print(case_pariuri)
    round, date, home, result, away = ([] for i in range(5))
    # unibet, betfair, winmasters, betano, fortuna, netbet, bet365 = ([] for i in range(12))
    cote_dict = {casa: [] for casa in case_pariuri}
    print(cote_dict)
    headers = ["Date", "Round", "Home", "Result", "Away"] + ["1", "X", "2"] * len(case_pariuri)
    # case = ["Unibet", "Betfair", "NetBet", "Betano", "Fortuna", "Winmasters"]

    for meci in data:
        # print(meci["Winmasters.ro"])
        # print(meci["Fortuna.ro"])
        try:
            round.append(meci["fixture"])
        except KeyError:
            round.append(" ")
        try:
            date.append(meci["date_time"][0])
        except KeyError:
            date.append(" ")
        try:
            home.append(meci["home_team"])
        except KeyError:
            home.append(" ")
        try:
            result.append(meci["result"])
        except KeyError:
            result.append(" ")
        try:
            away.append(meci["away_team"])
        except KeyError:
            away.append(" ")
        for i in range(len(case_pariuri)):
            try:
                cote_dict[case_pariuri[i]].append(meci[case_pariuri[i]])
            except KeyError:
                cote_dict[case_pariuri[i]].append([" ", " ", " "])

    print(cote_dict)
    print(len(cote_dict[case_pariuri[0]]))
    # [print(len(cote_dict[case_pariuri[i]])) for i in range(len(case_pariuri))]

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
    worksheet.set_column(5, len(case_pariuri), max_length(cote_dict[case_pariuri[0]]) + 3)

    row = 1
    column = 0

    worksheet.merge_range(0, 0, 0, 4, nume_excel, bold)
    count = 0
    for casa in case_pariuri:
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
        k_step = 5
        for k in range(len(case_pariuri)):
            for j in range(3):
                worksheet.write(row + i, k_step + j, cote_dict[case_pariuri[k]][i][j], middle)
            k_step += 3

    workbook.close()
    shutil.move(os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//text files_corecte", file[:-3] + 'xlsx'),
                os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//excel files", file[:-3] + 'xlsx'))
    # shutil.move(os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//text files", file[:-4] + '_test.xlsx'),
    #             os.path.join("C://Users//Matei//Documents//GitHub//Flashscore//excel files", file[:-4] + '_test.xlsx'))
os.chdir(os.path.join("C://Users//Matei//Documents//GitHub//Flashscore", "text files_corecte"))
print(os.getcwd())
#file = "meciuri_salvate_19-20.txt"
#file = "meciuri_salvate_corect_18-19.txt"
#file = "meciuri_salvate_17-18.txt"
#file = "meciuri_salvate_16-17.txt"
#file = "meciuri_salvate_corect_18-19.txt"
#excel_2018_2019(file)
#file = "meciuri_salvate_18-19(2).txt"
file = "meciuri_salvate_19-20.txt"
excel_for_all(file)
