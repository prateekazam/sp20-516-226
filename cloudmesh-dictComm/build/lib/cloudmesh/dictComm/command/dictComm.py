from __future__ import print_function

import subprocess

from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.dictComm.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.systeminfo import systeminfo
from datetime import datetime
import ast

class DictcommCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_dictComm(self, args, arguments):
        """
        ::

          Usage:
                dictComm  time
                dictComm --ping=PING
                dictComm system

          This command does some useful things.

          Arguments:
              PING   a site to ping
          Options:
              -p      specify the site to ping

        """
        arguments.PING = arguments["--ping"] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.time:
            print("option a")
            pprint(datetime.now())

        elif arguments.PING:
            print("option b - ping a site")
            m.list(subprocess.run(["ping", arguments.PING, "-n", "1"]))

        elif arguments.system:
            print("option c - system")
            m.list(arguments)
            pprint(systeminfo())

        Console.error("This is just a sample")
        return ""
