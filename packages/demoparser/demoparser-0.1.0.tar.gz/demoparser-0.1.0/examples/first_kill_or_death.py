from asyncio import events
from typing import List
from unicodedata import name
import demoparser
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def transform_props(dims, arr, cols):
    cols.append("tick")
    cols.append("entid")
    arr = arr[:dims[0]]
    arr = arr.reshape(dims[1], dims[2], order='F')
    d = {}
    k = ""
    v = ""
    for i in range(3, len(dims)):
        if i % 2 == 0:
            k = dims[i]
        else:
            v = dims[i]
            d[k] = v
    df = pd.DataFrame(arr, columns=cols)
    df = df.replace({"entid": d})
    df["entid"].astype("int64")
    df["tick"].astype("int64")
    return df

def clean_events(events):
    cleaned_events = []
    for i in range(len(events)):
        subd = {}
        for k,v in events[i].items():
            subd[k] = v[0]
        cleaned_events.append(subd)
    return cleaned_events

class PythonDemoParser:
    def __init__(self, file: str) -> None:
        self.path = file

    def parse_props(self, props_names) -> pd.DataFrame:
        out_arr = np.zeros((10000000), order='F')
        dims = demoparser.parse_props(self.path, props_names, out_arr)
        df = transform_props(dims, out_arr, cols=props_names)
        return df

    def parse_events(self, game_events) -> list:
        game_events = demoparser.parse_events(self.path, game_events)
        game_events = clean_events(game_events)
        return game_events


demo_name = "/home/laiho/.steam/steam/steamapps/common/Counter-Strike Global Offensive/csgo/replays/match730_003571866312135147584_0815469279_189.dem"
#demo_name = "/home/laiho/.steam/steam/steamapps/common/Counter-Strike Global Offensive/csgo/replays/match730_003571109800890597417_2128991285_181.dem"

import glob
import time



event_name = "round_stadftgsrt"
files = glob.glob("/home/laiho/Documents/demos/rclonetest/*")
deaths = []
rounds_ends = []

from collections import Counter

#file = "/home/laiho/.steam/steam/steamapps/common/Counter-Strike Global Offensive/csgo/replays/match730_003571109800890597417_2128991285_181.dem"

import time

# BENU 76561198134270402
# EMIL 76561198194694750

total_attackers = []
total_victims = []

files = glob.glob("/home/laiho/Documents/demos/mm/*")
okfiles = []
for file in files:
        if "info" not in file:
            okfiles.append(file)


def first_bloods(file):
    parser = PythonDemoParser(file)
    before = time.time()
    game_events = parser.parse_events("dfdsfasd")


    round_starts = []
    deaths = []

    for event in game_events:
        if event["event_name"] == "player_death":
            deaths.append(event)

        if event["event_name"] == "round_start":
            round_starts.append(event)



    df = pd.DataFrame(deaths)
    df.to_csv("deaths.csv")

    df = pd.DataFrame(round_starts)
    df.to_csv("round_start_ticks.csv")
    exit()



import multiprocessing


if __name__ == "__main__":
    attackers = []
    victims = []
    with multiprocessing.Pool(processes=24) as pool:
        results = pool.map(first_bloods, okfiles[:200])
    
    for tuple in results:
        attackers.extend(tuple[0])
        victims.extend(tuple[1])
    
    
