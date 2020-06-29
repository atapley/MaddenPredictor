import requests
import os
import helpers

# Prompt user for specific Madden version to download data from.

def download_roster(version):
    if version == '11':
        ext = '.xls'
    else:
        ext = '.xlsx'

    teams = helpers.get_teams(version)

    if not os.path.exists('MaddenRosters/' + version):
        os.makedirs('MaddenRosters/' + version)

    if version == '2002' or version == '2004' or version == '10' \
            or version == '12' or version == '17' or version == '18' or version == '19'\
            or version == '20':
        file_name = '__madden_nfl_' + version + '_.xlsx'
    elif version == '11':
        file_name = '_madden_nfl_' + version + '.xls'
    elif version == '16':
        file_name = '_(madden_nfl_' + version + ').xlsx'
    else:
        file_name = '_madden_nfl_' + version + '.xlsx'

    for team in teams:
        url = 'https://maddenratings.weebly.com/uploads/1/4/0/9/14097292/' + team + file_name
        r = requests.get(url, allow_redirects=True)
        open('MaddenRosters/' + version + '/' + team + ext, 'wb').write(r.content)
        print(team)

if __name__ == "__main__":

    valid_version = False

    while not valid_version:
        version = input('Download Madden NFL Ratings! Which Madden game (or ALL)?: ')

        if version not in helpers.versions and version != 'ALL':
            print()
            print('Invalid Madden game! (Make sure the year (2002 vs. 06) is correct!)')
            print()
            valid_version = False

        valid_version = True

    if version == 'ALL':
        for i in helpers.versions:
            print('Downloading Madden roster for Madden ' + i + '...')
            download_roster(i)
    else:
        print('Downloading Madden roster for Madden ' + version + '...')
        download_roster(version)