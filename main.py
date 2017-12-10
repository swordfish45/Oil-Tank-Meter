import logger
import sensor

def main():
    logger.log_level(sensor.get_distance())
if __name__ == "__main__":
    main()
