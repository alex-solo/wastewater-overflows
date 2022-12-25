CREATE TABLE overflows (
	location VARCHAR(25),
	start_date DATE,
  start_time TIME,
  stop_date DATE,
  stop_time TIME,
  duration numeric,
	volume numeric,
	disinfection VARCHAR(10),
	reason_code VARCHAR(25)
);

INSERT INTO overflows(location, start_date, start_time, stop_date, stop_time, duration, volume, disinfection, reason_code)
SELECT
    CAST(location AS VARCHAR(25)),
    CAST(start_date AS DATE),
    CAST(start_time AS TIME),
    CAST(stop_date AS DATE),
    CAST(stop_time AS TIME),
    CAST(duration AS NUMERIC),
    CAST(volume AS NUMERIC),
    CAST(disinfection AS VARCHAR(10)),
    CAST(reason_code AS VARCHAR(25))
FROM overflows_staging;
