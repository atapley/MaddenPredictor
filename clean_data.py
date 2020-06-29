import pandas as pd
import helpers
import os

def clean_roster_data(version):

    if version == '11':
        ext = '.xls'
    else:
        ext = '.xlsx'

    teams = helpers.get_teams(version)

    for team in teams:
        print(team)

        if version == '2002':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=0)
            df = df[['Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv')

        if version == '2003':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=0)
            df['First Name'], df['Last Name'] = df['Name'].str.split(' ', 1).str
            df.rename(columns={'Overall Rating': 'Overall'}, inplace=True)
            df = df[['Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv')

        if version == '2004':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=0)
            df['First Name'], df['Last Name'] = df['Name'].str.split(' ', 1).str
            df = df[['Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv')

        if version == '2005' or version == '06':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df.rename(columns={'FIRSTNAME': 'First Name',
                               'LASTNAME': 'Last Name',
                               'OVERALLRATING': 'Overall'},
                      inplace=True)
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

        if version == '07':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df.rename(columns={'PLYR_FIRSTNAME': 'First Name',
                               'PLYR_LASTNAME': 'Last Name',
                               'PLYR_OVERALLRATING': 'Overall'}, inplace=True)
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

        if version == '08':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df.rename(columns={'First_Name': 'First Name',
                               'Last_Name': 'Last Name',
                               'Overall_Rating': 'Overall'}, inplace=True)
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

        if version == '09':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df.rename(columns={'FIRSTNAME': 'First Name',
                               'LASTNAME': 'Last Name',
                               'OVERALL': 'Overall'}, inplace=True)
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

        if version == '10':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=0)
            df.rename(columns={'First': 'First Name',
                               'Last': 'Last Name',
                               'OVR': 'Overall',
                               'POS': 'Position'},
                      inplace=True)
            df = df[['Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv')

        if version == '11':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=0)
            df.rename(columns={'FIRST NAME': 'First Name',
                               'LAST NAME': 'Last Name',
                               'OVERALL RATING': 'Overall',
                               'POSITION': 'Position'},
                      inplace=True)
            df = df[['Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv')

        if version == '12':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df = df.drop(df[df.Name == 'Name'].index)
            df.dropna(subset=['Name'], inplace=True)
            df['First Name'], df['Last Name'] = df['Name'].str.split(' ', 1).str
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

        if version == '13' or version == '17' or version == '18' or version == '25':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=0)
            df = df[['Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv')

        if version == '15':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df.rename(columns={'FIRST': 'First Name',
                               'LAST': 'Last Name',
                               'OVERALL RATING': 'Overall',
                               'POSITION': 'Position'}, inplace=True)
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

        if version == '16':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df.rename(columns={'OVR': 'Overall'}, inplace=True)
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

        if version == '19':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=0)
            df['First Name'], df['Last Name'] = df['Name'].str.split(' ', 1).str
            df = df[['Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv')

        if version == '20':
            df = pd.read_excel('MaddenRosters/' + version + '/' + team + ext, index_col=None)
            df['Team'] = helpers.get_name(team)
            df['First Name'], df['Last Name'] = df['Name'].str.split(' ', 1).str
            df = df[['Team', 'Position', 'First Name', 'Last Name', 'Overall']]
            df['Version'] = version
            df.to_csv('MaddenRosters/' + version + '/' + team + '.csv', index=False)

if __name__ == "__main__":

    valid_version = False

    while not valid_version:
        version = input('Clean Madden NFL roster data! Which Madden game (or ALL)?: ')

        if version not in helpers.versions and version != 'ALL':
            print()
            print('Invalid Madden game! (Make sure the year (2002 vs. 06) is correct!)')
            print()
            valid_version = False

        valid_version = True

    if version == 'ALL':
        for i in helpers.versions:
            print('Cleaning Madden roster data for Madden ' + i + '...')
            clean_roster_data(i)

    else:
        print('Cleaning Madden roster data for Madden ' + version + '...')
        clean_roster_data(version)