#testing ranked project
from riotwatcher import LolWatcher, ApiError
import time

lol_watcher = LolWatcher('')
my_region = 'na1'

def getSummonerData(summonerName):
    summonerData = []

    summoner = lol_watcher.summoner.by_name(my_region, summonerName)

    summonerData.append(summoner["name"])
    summonerData.append(summoner["id"])
    summonerData.append(summoner["puuid"])
    summonerData.append(summoner["summonerLevel"])

    League_Entry = lol_watcher.league.by_summoner(my_region, summoner["id"])

    if League_Entry[0]["queueType"] == "RANKED_SOLO_5x5":
        summonerData.append(League_Entry[0]["tier"])
        summonerData.append(League_Entry[0]["rank"])
        summonerData.append(League_Entry[0]["wins"])
        summonerData.append(League_Entry[0]["losses"])
        summonerData.append(League_Entry[0]["leaguePoints"])
    else:
        summonerData.append(League_Entry[1]["tier"])
        summonerData.append(League_Entry[1]["rank"])
        summonerData.append(League_Entry[1]["wins"])
        summonerData.append(League_Entry[1]["losses"])
        summonerData.append(League_Entry[1]["leaguePoints"])

    return summonerData

    # Jung = lol_watcher.summoner.by_name(my_region, 'Bushido ßrown')
    # Joe = lol_watcher.summoner.by_name(my_region, 'Best URGOT in NA')
    # Richard = lol_watcher.summoner.by_name(my_region, 'Voldemort')
    # Jian = lol_watcher.summoner.by_name(my_region, 'NeftLut')
    #friendsList = [Simeon, Jung, Joe, Richard, Jian]
    #for i in friendsList:
        # id = i["id"]
        # name = i["name"]
        # name.strip()

        # League_Entry = lol_watcher.league.by_summoner(my_region, id)
        # rank = League_Entry[0]["tier"] + " " + League_Entry[0]["rank"]
        # print(name + "'s rank is: " +rank)

    #rankedMatches = lol_watcher.match.matchlist_by_puuid(my_region, puuid)
    #print(rankedMatches)

    #testMatchID = rankedMatches[1]
    #testMatch = lol_watcher.match.by_id(my_region, testMatchID)

# Simeon = getSummonerData("Funeral Home")
# print(Simeon)