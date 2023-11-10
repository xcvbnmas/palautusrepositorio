import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        
    def test_search(self):
        result = self.stats.search("Lemieux")
        self.assertEqual(result.name, "Lemieux")

    def test_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(len(result), 3)

    def test_top(self):
        result = self.stats.top(3)
        self.assertEqual(len(result), 4)
        
