from requests import *

###############################################################################
# Ninja Legends Cheat
# - Instant Mission
# - Hunting House
###############################################################################
# YOU CAN CHANGE THIS LINE BELOW

# input your username
USERNAME = ""
# input your password
PASSWORD = ""
# input profile ID
PROFILE_ID = ""

# input total mission and total hunting house that you want to do
# set it to 0 (zero) if you don't want to do any mission or hunting house
TOTAL_RUN_MISSION = 0
TOTAL_RUN_HUNTING_HOUSE = 0

# input mission id (1 - 10)
MISSION_ID = 1

# input boss num (0-1)
# 0 -> Ginkotsu
# 1 -> Shikigami Yanki
BOSS_NUM = 0

###############################################################################
# DON'T TOUCH THIS LINE BELOW

api_url = "http://103.176.78.226:10001/"
instant_mission_url = api_url + "instant_mission"
hunting_house_url = api_url + "hunting_house"

def instant_mission():
    data = {
        "username": USERNAME,
        "password": PASSWORD,
        "profile_id": PROFILE_ID,
        "mission_id": MISSION_ID,
    }

    for i in range(TOTAL_RUN_MISSION):
        r = post(instant_mission_url, json=data)
        if (r.status_code == 200 and r.json()["error"] == 0):
            print(f"Mission complete ({i+1}/{TOTAL_RUN_MISSION})")
        else:
            print(f"Mission failed")
            break


def hunting_house():
    data = {
        "username": USERNAME,
        "password": PASSWORD,
        "profile_id": PROFILE_ID,
        "boss_num": BOSS_NUM,
    }

    for i in range(TOTAL_RUN_HUNTING_HOUSE):
        r = post(hunting_house_url, json=data)
        if (r.status_code == 200 and r.json()["error"] == 0):
            print(f"Hunting house complete ({i+1}/{TOTAL_RUN_HUNTING_HOUSE})")
        else:
            print(f"Hunting house failed")
            break

instant_mission()
hunting_house()