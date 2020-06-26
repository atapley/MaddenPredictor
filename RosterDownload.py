import requests
import os

def download_roster(version):
    if version == '11':
        ext = '.xls'
    else:
        ext = '.xlsx'

    if version == '2002':
        #No Houston Texans Data
        teams = ['buffalo_bills',
                 'miami_dolphins',
                 'new_england_patriots',
                 'new_york_jets',
                 'baltimore_ravens',
                 'cincinnati_bengals',
                 'cleveland_browns',
                 'pittsburgh_steelers',
                 'indianapolis_colts',
                 'jacksonville_jaguars',
                 'tennessee_titans',
                 'denver_broncos',
                 'kansas_city_chiefs',
                 'oakland_raiders',
                 'san_diego_chargers',
                 'dallas_cowboys',
                 'philadelphia_eagles',
                 'washington_redskins',
                 'new_york_giants',
                 'chicago_bears',
                 'detroit_lions',
                 'green_bay_packers',
                 'minnesota_vikings',
                 'atlanta_falcons',
                 'carolina_panthers',
                 'new_orleans_saints',
                 'tampa_bay_buccaneers',
                 'arizona_cardinals',
                 'st._louis_rams',
                 'san_francisco_49ers',
                 'seattle_seahawks']

    elif int(version) in range (2003, 2006) or int(version) in range(6,17) or version == '25':
        teams = ['buffalo_bills',
                 'miami_dolphins',
                 'new_england_patriots',
                 'new_york_jets',
                 'baltimore_ravens',
                 'cincinnati_bengals',
                 'cleveland_browns',
                 'pittsburgh_steelers',
                 'indianapolis_colts',
                 'jacksonville_jaguars',
                 'tennessee_titans',
                 'denver_broncos',
                 'kansas_city_chiefs',
                 'oakland_raiders',
                 'san_diego_chargers',
                 'dallas_cowboys',
                 'philadelphia_eagles',
                 'washington_redskins',
                 'new_york_giants',
                 'chicago_bears',
                 'detroit_lions',
                 'green_bay_packers',
                 'minnesota_vikings',
                 'atlanta_falcons',
                 'carolina_panthers',
                 'new_orleans_saints',
                 'tampa_bay_buccaneers',
                 'arizona_cardinals',
                 'st._louis_rams',
                 'san_francisco_49ers',
                 'seattle_seahawks',
                 'houston_texans']

    elif version == '17':
        #LA Rams
        teams = ['buffalo_bills',
                 'miami_dolphins',
                 'new_england_patriots',
                 'new_york_jets',
                 'baltimore_ravens',
                 'cincinnati_bengals',
                 'cleveland_browns',
                 'pittsburgh_steelers',
                 'indianapolis_colts',
                 'jacksonville_jaguars',
                 'tennessee_titans',
                 'denver_broncos',
                 'kansas_city_chiefs',
                 'oakland_raiders',
                 'san_diego_chargers',
                 'dallas_cowboys',
                 'philadelphia_eagles',
                 'washington_redskins',
                 'new_york_giants',
                 'chicago_bears',
                 'detroit_lions',
                 'green_bay_packers',
                 'minnesota_vikings',
                 'atlanta_falcons',
                 'carolina_panthers',
                 'new_orleans_saints',
                 'tampa_bay_buccaneers',
                 'arizona_cardinals',
                 'los_angeles_rams',
                 'san_francisco_49ers',
                 'seattle_seahawks',
                 'houston_texans']

    elif int(version) in range(18, 21):
        #LA Chargers
        teams = ['buffalo_bills',
                 'miami_dolphins',
                 'new_england_patriots',
                 'new_york_jets',
                 'baltimore_ravens',
                 'cincinnati_bengals',
                 'cleveland_browns',
                 'pittsburgh_steelers',
                 'indianapolis_colts',
                 'jacksonville_jaguars',
                 'tennessee_titans',
                 'denver_broncos',
                 'kansas_city_chiefs',
                 'oakland_raiders',
                 'los_angeles_chargers',
                 'dallas_cowboys',
                 'philadelphia_eagles',
                 'washington_redskins',
                 'new_york_giants',
                 'chicago_bears',
                 'detroit_lions',
                 'green_bay_packers',
                 'minnesota_vikings',
                 'atlanta_falcons',
                 'carolina_panthers',
                 'new_orleans_saints',
                 'tampa_bay_buccaneers',
                 'arizona_cardinals',
                 'los_angeles_rams',
                 'san_francisco_49ers',
                 'seattle_seahawks',
                 'houston_texans']

    else:
        raise ValueError('No data for this version!')

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

    versions = ['2002',
                '2003',
                '2004',
                '2005',
                '06',
                '07',
                '08',
                '09',
                '10',
                '11',
                '12',
                '13',
                '15',
                '16',
                '17',
                '18',
                '19',
                '20',
                '25']

    version = None

    while version is None:
        version = input('Download Madden NFL Ratings! Which Madden game (or ALL)?: ')

        if version not in versions and version != 'ALL':
            print()
            print('Invalid Madden game! (Make sure the year (2002 vs. 06) is correct!)')
            print()
            version = None

    if version == 'ALL':
        for i in versions:
            print('Downloading Madden roster for Madden ' + i + '...')
            download_roster(i)
    else:
        print('Downloading Madden roster for Madden ' + version + '...')
        download_roster(version)