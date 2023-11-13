import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        
    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()
        
    def top_scorers_by_nationality(self, nationality):
        players_filtered = filter(lambda player: player.nationality == nationality, self.players)
        players_sorted = sorted(players_filtered, key=lambda player: player.goals + player.assists, reverse=True)
        return players_sorted
        
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__=="__main__":
    main()
