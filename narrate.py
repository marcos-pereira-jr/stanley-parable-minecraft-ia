# narrate.py
import time
from mine import *
from sys import argv
import urllib2
import json
import sys

mc = Minecraft()
# Define the server and the endpoint

url = "http://127.0.0.1:5000/narrate"

mc.postToChat("Versao principal do Python:" + str(sys.version_info))
while True:
    time.sleep(1)

    pos = mc.player.getTilePos()
    mc.postToChat("Position: ")
    mc.postToChat(pos)
    block = mc.getBlock(pos.x, pos.y-1, pos.z)
    print(block)
    block_types = {
    0: "AIR",
    1: "STONE",
    2: "GRASS",
    3: "DIRT",
    4: "COBBLESTONE",
    5: "WOOD_PLANKS",
    6: "SAPLING",
    7: "BEDROCK",
    8: "WATER_FLOWING",
    9: "WATER_STATIONARY",
    10: "LAVA_FLOWING",
    11: "LAVA_STATIONARY",
    12: "SAND",
    13: "GRAVEL",
    14: "GOLD_ORE",
    15: "IRON_ORE",
    16: "COAL_ORE",
    17: "WOOD",
    18: "LEAVES",
    20: "GLASS",
    21: "LAPIS_LAZULI_ORE",
    22: "LAPIS_LAZULI_BLOCK",
    24: "SANDSTONE",
    26: "BED",
    30: "COBWEB",
    31: "GRASS_TALL",
    35: "WOOL",
    37: "FLOWER_YELLOW",
    38: "FLOWER_CYAN",
    39: "MUSHROOM_BROWN",
    40: "MUSHROOM_RED",
    41: "GOLD_BLOCK",
    42: "IRON_BLOCK",
    43: "STONE_SLAB_DOUBLE",
    44: "STONE_SLAB",
    45: "BRICK_BLOCK",
    46: "TNT",
    47: "BOOKSHELF",
    48: "MOSS_STONE",
    49: "OBSIDIAN",
    50: "TORCH",
    51: "FIRE",
    53: "STAIRS_WOOD",
    54: "CHEST",
    56: "DIAMOND_ORE",
    57: "DIAMOND_BLOCK",
    58: "CRAFTING_TABLE",
    60: "FARMLAND",
    61: "FURNACE_INACTIVE",
    62: "FURNACE_ACTIVE",
    64: "DOOR_WOOD",
    65: "LADDER",
    67: "STAIRS_COBBLESTONE",
    71: "DOOR_IRON",
    73: "REDSTONE_ORE",
    78: "SNOW",
    79: "ICE",
    80: "SNOW_BLOCK",
    81: "CACTUS",
    82: "CLAY",
    83: "SUGAR_CANE",
    85: "FENCE",
    89: "GLOWSTONE_BLOCK",
    95: "BEDROCK_INVISIBLE",
    98: "STONE_BRICK",
    102: "GLASS_PANE",
    103: "MELON",
    107: "FENCE_GATE",
    246: "GLOWING_OBSIDIAN",
    247: "NETHER_REACTOR_CORE",
    }

    mc.postToChat(block)
    payload = {
        "event": "I step on a {}".format(block_types.get(block))
    }
    payload_json = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    req = urllib2.Request(url, payload_json, headers)

    try:
        response = urllib2.urlopen(req)
        # Ler e imprimir a resposta
        conteudo_resposta = response.read()
        print("Resposta do servidor:", conteudo_resposta)
    except urllib2.HTTPError as e:
        print("Resposta do servidor:" + e.read())
    except urllib2.URLError as e:
        print("Erro na solicitacao. Motivo:" +  e.reason)