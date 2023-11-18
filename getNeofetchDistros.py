import os
import re
from random import random


def getDistros():
    neofetchHelp = os.popen("neofetch --help").read().replace("\t",
                                                              "").replace("\n", "").replace(" ", "")
    stringInitVariable = "ascii_distrodistroWhichDistro'sasciiarttoprintNOTE:"
    distros = neofetchHelp[neofetchHelp.find(
        stringInitVariable) + len(stringInitVariable):neofetchHelp.find("haveasciilogos")]
    distroRx = re.findall('([^,]+)', distros)
    distroRx[len(distroRx) - 1] = distroRx[len(distroRx) - 1][3:]
    return distroRx


def getRandDistro():
    distros = getDistros()
    return distros[round(random() * len(distros) - 1)]


getDistros()