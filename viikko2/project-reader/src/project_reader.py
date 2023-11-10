from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        t = toml.loads(content)

        p = t.get("tool", {}).get("poetry", {})

        return Project(
            p.get("name", "Name"),
            p.get("description", "Description"),
            p.get("dependencies", []),
            p.get("group", {}).get("dev", {}).get("dependencies", [])
        )