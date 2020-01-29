import os

from cloudmesh.common.util import banner


class Provider:

    def __init__(self, name):
        self.name = name

    def list(self, format=""):
        if(format in {"yaml","json","csv"}):
            banner(f"List Images {format}")
            format = "--format " + format
        else:
            format = ""
            banner(f"List Images")
        os.system(f"multipass list {format}")

    def delete(self, purge=True):
        banner(f"Delete instance - {self.name}")
        os.system(f"multipass delete {self.name}")
        if purge:
            os.system(f"multipass purge")

    def start(self):
        banner(f"Start instance - {self.name}")
        os.system(f"multipass start {self.name}")

    def stop(self):
        banner(f"Stop instance - {self.name}")
        os.system(f"multipass stop {self.name}")

    def shell(self):
        banner("shell")
        os.system("multipass shell")

    def run(self, command):
        banner(f"run {command}")
        os.system(f"multipass exec {command}")

    def launch(self):
        banner(f"Launching New Instance -  {self.name}")
        os.system(f"multipass launch --name {self.name}")

if __name__ == "__main__":
    p = Provider("ubuntu-lts")
    #p.delete(True)
    #p.launch()
    #p.run("help")
    p.list()
    #p.stop()
    #p.list()
    #p.start()
    p.list("json")
    p.list("csv")
    p.list("yaml")
    p.list("blorp")