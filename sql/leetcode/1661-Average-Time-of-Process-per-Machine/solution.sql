-- 1661. Average Time of Process per Machine
-- Problem Link: https://leetcode.com/problems/average-time-of-process-per-machine

-- Finding the 'start'' time of each process
WITH startTime AS (
    SELECT
        *
    FROM
        Activity
    WHERE
        activity_type = 'start'
),

-- Finding the 'end' time of each process
endTime AS (
    SELECT
        machine_id,
        process_id,
        activity_type,
        timestamp
    FROM
        Activity
    WHERE
        activity_type = 'end'
),

-- Finding the time taken by each process for each machine
MachinePerProcessTime AS (
    SELECT
    stime.machine_id,
    stime.process_id,
    ROUND(SUM(etime.timestamp - stime.timestamp), 3) AS process_time
FROM
    startTime AS stime
INNER JOIN
    endTime as etime
    ON stime.machine_id = etime.machine_id
        AND stime.process_id = etime.process_id
        AND stime.activity_type <> etime.activity_type
WHERE
    stime.activity_type = 'start' AND etime.activity_type = 'end'
GROUP BY
    stime.machine_id,
    stime.process_id
)

-- Finding the AVERAGE TIME taken for a PROCESS by each machine for completing a process
SELECT
    machine_id,
    ROUND(SUM(process_time) / COUNT(machine_id), 3) AS processing_time
FROM
    MachinePerProcessTime
GROUP BY
    machine_id