# sp20-516-226 E.Cloudmesh.Commone.1-5
import os
import time
from pprint import pprint

from cloudmesh.shell.command import command
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables
from cloudmesh.common.Shell import Shell

class CloudCommon:
    def __init__(self, items):
        self.items = items

    def getItems(self):
        return self.items

    # This Method completes problems 2 and 1.b
    def PrintItemsInDotDict(self):
        HEADING()
        data = dotdict(self.items)
        print("data.ElementOne=" + data.ElementOne)
        print("data[\"ElementOne\"]=" + data["ElementOne"])

if __name__ == "__main__":
    StopWatch.start('script')
    CC = CloudCommon({"ElementOne": "One", "ElementTwo": "Two", "ElementThree": {"SubElementOne":"Three", "SubElementTwo":"Two"}})
    # Shows usage of Flatdict (E.Cloudmesh.Common.3)
    flat = FlatDict(CC.getItems(), sep='.')
    # each banner completes part of 1.a
    banner("Normal Dictionary")
    print(CC.getItems())
    banner("Flat Dictionary")
    print(flat)
    CC.PrintItemsInDotDict()
    banner("Usage of VERBOSE to show info about my dict")
    variables = Variables()
    variables['debug'] = True
    variables['trace'] = True
    variables['verbose'] = 10
    VERBOSE(CC.getItems())
    banner("Execute a shell command for pip")
    res = Shell.pip()
    print(res)
    banner("Let's sleep for three seconds and check our stopwatch")
    time.sleep(3)
    StopWatch.stop('script')
    # Shows StopWatch functionality (E.Cloudmesh.Common.5)
    print("Time to Complete: " + str(StopWatch.get('script')) + " seconds")
