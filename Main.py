from Code.DynDNS import DynDNS
from configparser import ConfigParser

if __name__ == "__main__":
    config = ConfigParser()
    config.read("Settings.conf")

    dyndns = DynDNS(config["DynDNS"]["username"], config["DynDNS"]["password"], int(config["DynDNS"]["port"]) if config["DynDNS"]["port"] else None)

    dyndns.run()