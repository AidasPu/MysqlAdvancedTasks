from datetime import datetime
from . import DatabaseContextManager

def create_table_bikesharing():
    query = """CREATE TABLE `bikesharing` (
    `tstamp` timestamp,
    `cnt` integer,
    `temperature` decimal(5, 2),
    `temperature_feels` decimal(5, 2),
    `humidity` decimal(4, 1),
    `wind_speed` decimal(5,2),
    `weather_code` integer,
    `is_holiday` boolean,
    `is_weekend` boolean,
    `season` integer);"""

    with DatabaseContextManager() as db:
        db.execute(query)


def convert_line_to_values(line):
    values = line.split(",")
    # convert timestamp to datetime
    values[0] = datetime.st(values[0], "%Y-%m-%d %H:%M:%S")
    return values

    sql = """
        INSERT INTO bikesharing
        (tstamp, cnt, temperature, temperature_feels, humidity, wind_speed,
        weather_code, is_holiday, is_weekend, season) VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    with DatabaseContextManager() as cursor:
        with open("london-bikes.csv") as f:
            for i, line in enumerate(f):
                if i == 0:
                    continue
                values = convert_line_to_values(line)
                cursor.execute(sql, values)
                if i % 100 == 0:
                    db.commit()
        db.commit()
    db.close()

datetime.hour

