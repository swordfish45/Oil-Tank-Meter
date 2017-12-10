import logger
import sensor

def main():
    s = sensor.sensor()
    logger.log_level(s.get_distance())
if __name__ == "__main__":
    main()
