from os import walk
import json
import datetime

# Path to folder containing the spotify data
DATA_FOLDER_PATH = "data/MyData3"

# If you want to use a range of dates you can set the start and end date
# Otherwise set them to None
START_DATE = datetime.date(2022, 1, 1)
END_DATE = datetime.date(2022, 10, 31)

# START_DATE = None
# END_DATE = None


class track:
    def __init__(self, data):
        #self.date = data["endTime"]
        self.date = datetime.date(int(data["endTime"][0:4]), int(data["endTime"][5:7]), int(data["endTime"][8:10]))
        self.artistName = data["artistName"]
        self.trackName = data["trackName"]
        self.msPlayed = data["msPlayed"]

    def getYear(self):
        return str(self.date.year)

    def getDay(self):
        return str(self.date.day)


def openJsonFile():
    data = []
    for (dirpath, dirnames, filenames) in walk(DATA_FOLDER_PATH):
        for f in filenames:
            if f.startswith("StreamingHistory"):
                with open(DATA_FOLDER_PATH + "/" + f, "r", encoding="mbcs") as dataFile:
                    dataJson = json.load(dataFile)
                    data += dataJson

    return data


def calcul(data):
    resTime = {}
    resArtist = {}
    resTrack = {}
    date = []
    for x in data:
        t = track(x)

        if START_DATE is not None and t.date < START_DATE or END_DATE is not None and t.date > END_DATE:
            continue

        date.append(t.date)
        #print(res[t.getYear()])

        if t.trackName in resTrack:
            resTrack[t.trackName] += 1
        else:
            resTrack[t.trackName] = 1

        if t.artistName in resArtist:
            resArtist[t.artistName] += 1
        else:
            resArtist[t.artistName] = 1

        if t.getYear() in resTime:
            resTime[t.getYear()] += t.msPlayed
        else:
            resTime[t.getYear()] = t.msPlayed

    # Error handling
    if len(date) == 0:
        print("No data found")
        return
    afficher(min(date), max(date), resTime, resArtist, resTrack)


def afficher(minDate, maxDate, resTime, resArtist, resTrack):
    print('Donnée du {0} au {1}'.format(minDate, maxDate))
    totalTime = 0
    for x in resTime.keys():
        totalTime += resTime[x]
        minutes = round(resTime[x] / (1000 * 60), 2)
        heures = round(resTime[x] / (1000 * 60 * 60), 2)
        print('Pour l\'année {0} tu as écouté {1} minutes ou {2} heures'.format(x, minutes, heures))

    minutes = round(totalTime / (1000 * 60), 2)
    heures = round(totalTime / (1000 * 60 * 60), 2)
    print('Au total tu as écouté {0} minutes ou {1} heures'.format(minutes, heures))

    art = sorted(resArtist.items(), key=lambda item: item[1])
    print('\nListe des artists que tu as écouté le plus:')
    for x in range(0, 10):
        artist = art[len(art) - 1 - x]
        print('#{0}: {1} pour un total de {2} fois'.format(x + 1, artist[0], artist[1]))

    tracks = sorted(resTrack.items(), key=lambda item: item[1])
    print('\nListe des artists que tu as écouté le plus:')
    for x in range(0, 10):
        track = tracks[len(tracks) - 1 - x]
        print('#{0}: {1} pour un total de {2} fois'.format(x + 1, track[0], track[1]))


if __name__ == "__main__":
    jsonFile = openJsonFile()
    calcul(jsonFile)
