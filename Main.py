from Code.DynDNS import DynDNS
from configparser import ConfigParser

config = ConfigParser()
config.read("Settings.conf")

if __name__ == "__main__":
    dyndns = DynDNS(config["DynDNS"]["username"], config["DynDNS"]["password"], int(config["DynDNS"]["port"]) if config["DynDNS"]["port"] else None)

    dyndns.run()