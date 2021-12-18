_Author_ = "Karthik Vaidhyanathan"

# Initalizing all basic configurations

from configparser import ConfigParser
import traceback

CONFIG_FILE = "settings.conf"
CONFIG_SECTION = "settings"
CONFIG_SECTION_THINGS = "thingsboard"

class Initialize():
    def __init__(self):
        try:
            parser = ConfigParser()
            parser.read(CONFIG_FILE)
            # Read the Cupcarbon data path and the log file path
            self.data_path = parser.get(CONFIG_SECTION, "data_path")
            self.data_file = parser.get(CONFIG_SECTION, "data_file")
            self.kafka_host = parser.get(CONFIG_SECTION, "kafka_host")

            #ThingsBoard Related configurations
            self.things_host = parser.get(CONFIG_SECTION_THINGS,"thingsboard_host")



        except Exception as e:
            traceback.print_exc()

