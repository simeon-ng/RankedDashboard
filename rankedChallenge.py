from __future__ import print_function
from datetime import date

import os.path

# Google APIS
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import league

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1gtOx7SgM5onKwiPO4POPxtiuOGd64hxNofSr_yhaZnI'
RANGE_NAME_SUMMONERS = 'Summoners'
RANGE_NAME_RANKEDHISTORY = 'RankHistory!2:2'
CLEAR_RANGE = "A2:I6"

def createHistory(summoner):
    snapshot = []
    snapshot.append(summoner[0])
    snapshot.append(summoner[4] + " " + summoner[5])
    snapshot.append(summoner[8])
    snapshot.append(str(date.today()))
    return snapshot

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()

        clear_request_body = {}

        value_input_option = "USER_ENTERED"

        # Get league data
        Simeon = league.getSummonerData("Funeral Home")
        Jung = league.getSummonerData("Bushido ßrown")
        Joe = league.getSummonerData("Best URGOT in NA")
        Richard = league.getSummonerData("Voldemort")
        Jian = league.getSummonerData("NeftLut")
        #Jung2 = league.getSummonerData("IMGONNADOIT")

        # Values to update: Each array is a row.
        summonerValues = [
            ["summonerName", "id", "puuid", "summonerLevel", "tier", "rank", "wins", "losses", "leaguePoints"],
            Simeon,
            Jung,
            Joe,
            Richard,
            Jian
            #Jung2
        ]
        body = {
            'values': summonerValues
        }

        simeonHistory = createHistory(Simeon)
        jungHistory = createHistory(Jung)
        joeHistory = createHistory(Joe)
        richardHistory = createHistory(Richard)
        jianHistory = createHistory(Jian)

        rankHistoryValues = [
            simeonHistory,
            jungHistory,
            joeHistory,
            richardHistory,
            jianHistory
        ]
        historyBody = {
            'values': rankHistoryValues
        }

        # Clear and update sheet
        request = sheet.values().clear(spreadsheetId = SPREADSHEET_ID, range = CLEAR_RANGE,
            body = clear_request_body).execute()
        request = sheet.values().update(spreadsheetId = SPREADSHEET_ID, range = RANGE_NAME_SUMMONERS, 
            valueInputOption = value_input_option, body = body).execute()
        request = sheet.values().append(spreadsheetId = SPREADSHEET_ID, range = RANGE_NAME_RANKEDHISTORY,
            valueInputOption = value_input_option, body = historyBody).execute()

        print("Updated.")

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()