from sensor import Sensor
from socket_client import Client
from config_utils import Config
from apscheduler.schedulers.blocking import BlockingScheduler



def update(sensor, client):
    client.send(sensor.get_environment())


if __name__ == "__main__":
    config = Config()

    interval = config.get_value("interval")
    sensor_id = config.get_value("sensor_id")
    host, port = config.get_data_center_config()

    sensor = Sensor(sensor_id)

    scheduler = BlockingScheduler()
    client = Client(host, port, scheduler)
    client.connect()

    scheduler.add_job(update, 'interval', seconds=interval, max_instances=100, id='update', args=[sensor, client])
    client.update_job_started = True
    scheduler.start()
