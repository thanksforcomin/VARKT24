import json
import time
import datetime

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


def collect_data_and_log(logger: Logger, vessel):
    Sun = vessel.orbit.body.orbit.body
    Kerbin = Sun.satellites[2]
    KerbinRf = Kerbin.reference_frame
    while (
        vessel.situation.name != "splashed"
        and vessel.situation.name != "landed"
        and logger.logging
    ):
        pos = vessel.position(KerbinRf)
        # velocity = vessel.flight(vessel.orbit.body.reference_frame).velocity
        # altitude = vessel.flight().mean_altitude
        # acceleration = vessel.flight().g_force

        data = {
            "pos": pos,
            # "Velocity": velocity,
            # "Acceleration": acceleration,
            # "Altitude": altitude,
        }

        # Вносим данные
        logger.append_to_log_file(data)
        time.sleep(0.5)

    print("CLOSING FILE")
    # Закрываем файл, когда полёт окончен
    logger.file.close()
