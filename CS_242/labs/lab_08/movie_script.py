import random


class MovieScript(object):

    def __init__(self, script, actors, sceneTimings) -> None:
        self.script = script
        self.actors = actors
        self.sceneTimings = sceneTimings
        # convert the sequence list to a dictionary, with random actors as values
        self.callSheet = {idx: {"sequence": x, "actors": random.sample(
            self.actors, 3)} for idx, x in enumerate(self.script)}

    def __iter__(self):
        cursor = 0
        while cursor < len(self.script):
            # yield sends each item to the caller, the for loop
            yield self.script[cursor]
            cursor += 1

    def __str__(self):
        str = ""
        for x in range(len(self.script)):
            str += f"\u2022 {self.script[x]} \n"
        return str

    # accessors

    def getScript(self) -> list:
        return self.script

    def getActors(self) -> list:
        return self.actors

    def getCallSheet(self) -> dict:
        return self.callSheet

    def getSceneTimings(self) -> list:
        return self.sceneTimings

    def printCallSheet(self) -> str:
        return "\n".join([(f"Sequence {i + 1}: {x['sequence']}, Actors: {', '.join([a for a in x['actors']])}") for (i, x) in self.callSheet.items()])

    def printSceneTimings(self) -> str:
        return "\n".join([f'Scene {i}: {self.sceneTimings[i]}' for i in range(len(self.script) - 1)])

    def searchKeyword(self, keyword) -> str:
        str = ""
        for i in range(len(self.script)):
            if (keyword in self.script[i]):
                str += f"\n{keyword} found in scene sequence number {i + 1}: \"{self.script[i]}\""

        return str if len(str) > 0 else f"{keyword} not found!"

    def searchActors(self, actor) -> str:
        str = ""
        for key in self.callSheet.keys():
            if (actor in self.callSheet[key]['actors']):
                str += f"\n{actor} found in scene sequence number {key}\nSequence: \"{self.callSheet[key]['sequence']}\" \nActor(s): {[f'{i} ' for i in self.callSheet[key]['actors']]}"

        return str if len(str) > 0 else f"{actor} not found!"

    # mutators
    def setScript(self, s) -> None:
        self.script = s
