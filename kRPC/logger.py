import json
import time
import datetime
import math
import krpc
import sys
from krpc.services.spacecenter import Vessel

# Kind of a workaround for the Math module  
sys.path.insert(0, 'Math/')

from Functions import Vec3Abs

DEFAULT_FILE_NAME = "kRPC/Logs/{}-{}.json"


class Logger:
    def __init__(self):
        self.logging = True
        self.file_name = ""
        self.file = None

    def create_log_file(self, file_name):
        current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
        self.file_name = DEFAULT_FILE_NAME.format(file_name, current_time)
        self.file = open(self.file_name, "a")

    def append_to_log_file(self, data):
        if self.file:
            json.dump(data, self.file)
            self.file.write("\n")

    def stop_logging(self):
        self.logging = False


def collect_data_and_log(logger: Logger, vessel: Vessel):
    start = time.time()
    Sun = vessel.orbit.body.orbit.body
    Kerbin = Sun.satellites[2]
    KerbinRf = Kerbin.reference_frame
    while (
        vessel.situation.name != "splashed"
        and vessel.situation.name != "landed"
        and logger.logging
    ):
        pos = vessel.position(KerbinRf)
        time_since_start = time.time() - start
        velocity = vessel.flight(KerbinRf).velocity
        altitude = vessel.flight().mean_altitude
        mass = vessel.mass

        data = {
            "pos": pos,
            "time": time_since_start,
            "altitude": altitude,
            "Velocity": Vec3Abs(velocity),
            "angle": vessel.control.pitch,
            "mass": mass,
        }

        # Append data to the log file
        logger.append_to_log_file(data)
        time.sleep(0.5)

    print("CLOSING FILE")

    # Close the file
    logger.file.close()
