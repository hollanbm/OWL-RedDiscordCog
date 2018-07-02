import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


class Match:
    def __init__(self, home_team, home_team_abbrev, away_team, away_team_abbrev, match_date, match_time, match_url):
        self.home_team = home_team
        self.home_team_abbrev = home_team_abbrev
        self.away_team = away_team
        self.away_team_abbrev = away_team_abbrev
        self.match_date = match_date
        self.match_url = 'https://overwatchleague.com/en-us' + match_url
        if match_time is not None:
            self.match_time = match_time
        else:
            self.match_time = 'Match Finished'

    def getText(self):
        return self.match_date + ' ' + self.match_time + ' ' + self.home_team + ' vs ' + self.away_team

    def getAbbrevText(self):
        return self.home_team_abbrev + ' vs ' + self.away_team_abbrev

    def getEmbedText(self):
        return '[' + self.getText() + '](' + self.match_url + ')'

    def isToday(self):
        return self.match_date == 'Today'

def getStandingsHTML():
    return """<div class="Standings"><h1>Standings</h1><p class="Standings-description">Six teams will qualify for the Playoffs, based on their Regular Season records. The top seed from each Division will receive a first-round bye. The next four teams, regardless of Division, will also advance.</p><div class="table-responsive"><table class="table table-striped table-condensed u-verticalPadding--x-small ScrollArea-content"><thead><tr><th></th><th class="Standings-header-team"></th><th class="Standings-header">Division</th><th class="Standings-header">Won</th><th class="Standings-header">Lost</th></tr></thead><tbody><tr><td><b>1</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/page_media/E9MU0AK0JIXT1507858876249.svg" alt="Seoul Dynasty" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Seoul Dynasty</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Seoul Dynasty"><div>SEO</div></span></div></td><td class="Standings-details-division">PAC</td><td class="Standings-details">4</td><td class="Standings-details">0</td></tr><tr><td><b>2</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/page_media/jz/JZHJUJ8QM1AP1508818097057.svg" alt="New York Excelsior" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>New York Excelsior</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="New York Excelsior"><div>NYE</div></span></div></td><td class="Standings-details-division">ATL</td><td class="Standings-details">4</td><td class="Standings-details">0</td></tr><tr><td><b>3</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/HCS229B4DP021507822883016.svg" alt="London Spitfire" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>London Spitfire</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="London Spitfire"><div>LDN</div></span></div></td><td class="Standings-details-division">ATL</td><td class="Standings-details">4</td><td class="Standings-details">0</td></tr><tr><td><b>4</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/page_media/UPM8U5QV3DDU1507858876250.svg" alt="Houston Outlaws" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Houston Outlaws</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Houston Outlaws"><div>HOU</div></span></div></td><td class="Standings-details-division">ATL</td><td class="Standings-details">2</td><td class="Standings-details">2</td></tr><tr><td><b>5</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/L3U59GQVS1ZK1507822882879.svg" alt="Los Angeles Valiant" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Los Angeles Valiant</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Los Angeles Valiant"><div>VAL</div></span></div></td><td class="Standings-details-division">PAC</td><td class="Standings-details">2</td><td class="Standings-details">2</td></tr><tr><td><b>6</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/0SY7LHKHV86R1507822883113.svg" alt="San Francisco Shock" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>San Francisco Shock</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="San Francisco Shock"><div>SFS</div></span></div></td><td class="Standings-details-division">PAC</td><td class="Standings-details">2</td><td class="Standings-details">2</td></tr><tr><td><b>7</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/CHTRRZCBEYGN1507822882862.svg" alt="Los Angeles Gladiators" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Los Angeles Gladiators</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Los Angeles Gladiators"><div>GLA</div></span></div></td><td class="Standings-details-division">PAC</td><td class="Standings-details">2</td><td class="Standings-details">2</td></tr><tr><td><b>8</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/LAKZ6R7QEG6S1507822883033.svg" alt="Philadelphia Fusion" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Philadelphia Fusion</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Philadelphia Fusion"><div>PHI</div></span></div></td><td class="Standings-details-division">ATL</td><td class="Standings-details">2</td><td class="Standings-details">2</td></tr><tr><td><b>9</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/page_media/W4FGQ24HKCB51513383982827.svg" alt="Boston Uprising" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Boston Uprising</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Boston Uprising"><div>BOS</div></span></div></td><td class="Standings-details-division">ATL</td><td class="Standings-details">1</td><td class="Standings-details">3</td></tr><tr><td><b>10</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/M1KNTZW8SGHZ1507822883041.svg" alt="Florida Mayhem" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Florida Mayhem</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Florida Mayhem"><div>FLA</div></span></div></td><td class="Standings-details-division">ATL</td><td class="Standings-details">1</td><td class="Standings-details">3</td></tr><tr><td><b>11</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/YX6JZ6FR89LU1507822882865.svg" alt="Dallas Fuel" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Dallas Fuel</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Dallas Fuel"><div>DAL</div></span></div></td><td class="Standings-details-division">PAC</td><td class="Standings-details">0</td><td class="Standings-details">4</td></tr><tr><td><b>12</b></td><td class="Standings-details-team"><div class="IconLabel"><span class="IconLabel-item"><img src="https://bnetcmsus-a.akamaihd.net/cms/template_resource/ZIVUVIWXNIFL1507822883114.svg" alt="Shanghai Dragons" class="Icon"></span><span class="IconLabel-item hidden-xs"><div>Shanghai Dragons</div></span><span class="IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl" title="Shanghai Dragons"><div>SHD</div></span></div></td><td class="Standings-details-division">PAC</td><td class="Standings-details">0</td><td class="Standings-details">4</td></tr></tbody></table></div></div>"""

def getMatchList():
    match_url = 'https://overwatchleague.com/en-us/schedule'
    #display = Display(visible=0, size=(1920, 1080)).start()
    browser = webdriver.Chrome()  # replace with .Firefox(), or with the browser of your choice
    browser.get(match_url)
    sleep(5)
    html = browser.execute_script("return document.getElementsByClassName('ScheduleMatchList')[0].innerHTML")
    soup = BeautifulSoup(html, "html.parser")
    browser.close()
    matchList = []
    for matchSchedule in soup.find_all(class_='MatchSchedule'):
        if matchSchedule.find(class_='MatchRow-day') is None:
            match_date = matchSchedule.find(class_='Date-dayOfWeek').get_text() + ' ' + matchSchedule.find(
                class_='Date-monthAndDay').get_text()
        else:
            match_date = matchSchedule.find(class_='MatchRow-day').get_text()

        match_times = matchSchedule.find_all(class_='MatchStatus')
        match_urls = matchSchedule.find_all('a',
                                            attrs={'class': 'MatchRow-contentWrapper MatchRow-contentWrapper--hover'})
        home_teams = matchSchedule.find_all(class_='TeamLabel-name hidden-sm hidden-xs')[0::2]
        home_team_abbrevs = matchSchedule.find_all(class_='TeamLabel-name hidden-md hidden-lg')[0::2]
        away_teams = matchSchedule.find_all(class_='TeamLabel-name hidden-sm hidden-xs')[1::2]
        away_team_abbrevs = matchSchedule.find_all(class_='TeamLabel-name hidden-md hidden-lg')[1::2]

        for i in range(len(match_times)):
            matchList.append(Match(home_teams[i].get_text(), home_team_abbrevs[i].get_text(), away_teams[i].get_text(),
                                   away_team_abbrevs[i].get_text(), match_date, match_times[i].get_text(),
                                   match_urls[i].get('href')))
    return matchList


def getMatchListText():
    text = ''
    for match in self.getMatchList():
        text += match.getText() + '\r\n'
    return text


def getStandingsText():
    standings_url = 'https://overwatchleague.com/en-us/standings'
    #display = Display(visible=0, size=(1920, 1080)).start()
    #browser = webdriver.Chrome()  # replace with .Firefox(), or with the browser of your choice
    #browser.get(standings_url)
    #sleep(5)
    #html = browser.execute_script("return document.getElementById('standings').innerHTML")
    #browser.close()
    soup = BeautifulSoup(getStandingsHTML(), "html.parser")

    for abbrev in soup.find_all(class_='IconLabel-item hidden-sm hidden-md hidden-lg hidden-xl'):
        abbrev.extract()
    # for fullName in soup.find_all(class_='IconLabel-item hidden-xs'):
    #    fullName.extract()
    table = soup.find('table', attrs={
        'class': 'table table-striped table-condensed u-verticalPadding--x-small ScrollArea-content'})
    rows = table.find('tbody').find_all('tr')
    rankSpacing, teamSpacing, divisionSpacing, wonSpacing, lostSpacing = 6, 24, 10, 6, 6
    teamSpacing
    text = 'Rank'.ljust(rankSpacing, ' ') + 'Team'.ljust(teamSpacing, ' ') + 'Division'.ljust(divisionSpacing, ' ') + 'Won'.ljust(wonSpacing, ' ') + 'Lost\r\n'.ljust(lostSpacing, ' ')
    for row in rows:
        cols = row.find_all('td')
        i = 0
        for ele in cols:
            eleText = ele.get_text()
            if i == 0:
                while len(eleText) < rankSpacing:
                    eleText += ' '
            elif i == 1:
                while len(eleText) < teamSpacing:
                    eleText += ' '
            elif i == 2:
                while len(eleText) < divisionSpacing:
                    eleText += ' '
            elif i == 3:
                while len(eleText) < wonSpacing:
                    eleText += ' '
            elif i == 4:
                while len(eleText) < lostSpacing:
                    eleText += ' '
            i += 1
            text += eleText
        text += '\r\n'
    return text

def today():
    noMatchesToday = True
    for match in getMatchList():
        if match.isToday():  # match.match_date[:-2] == datetime.date.today().strftime('%B %#d'):
            print(match.getText())
            noMatchesToday = False
    if noMatchesToday:
        print('No OWL matches today')


def main():
    print(getStandingsText())


main()
