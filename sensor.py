import random
import time


class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.temperature = 0
        self.humidity = 0

    def get_temperature(self):
        self.temperature = round(random.randint(2400, 2600) / float(100), 2)

    def get_humidity(self):
        self.humidity = round(random.randint(7500, 8000) / float(100), 2)

    def get_environment(self):
        self.get_temperature()
        self.get_humidity()
        environment = {
            "data_type": 20,
            "sensor_id": self.sensor_id,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "updated_at": int(time.time())
        }
        return environment

