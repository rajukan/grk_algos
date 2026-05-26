r'''
*
We are writing software to analyze logs for toll booths on a highway. This highway is a divided highway with limited access; the only way on to or off of the highway is through a toll booth.


There are three types of toll booths:
* ENTRY (E in the diagram) toll booths, where a car goes through a booth as it enters the highway.
* EXIT (X in the diagram) toll booths, where a car goes through a booth as it exits the highway.
* MAINROAD (M in the diagram), which have sensors that record a license plate as a car drives through at full speed.


Exit Booth                         Entry Booth
|                                   |
X                                   E
\                                 /
---<------------<---------M---------<-----------<---------<----
(West-bound side)


===============================================================


(East-bound side)
------>--------->---------M--------->--------->--------->------
/ \
    E                                   X
|                                   |
Entry Booth                         Exit Booth
*/
/*
We are interested in how many people are using the highway, and so we would like to count how many complete journeys are taken in the log file.


A complete journey consists of:
* A driver entering the highway through an ENTRY toll booth.
* The driver passing through some number of MAINROAD toll booths (possibly 0).
* The driver exiting the highway through an EXIT toll booth.


For example, the following excerpt of log lines contains complete journeys for the cars with JOX304 and THX138:


.
.
.
90750.191 JOX304 250E ENTRY
91081.684 JOX304 260E MAINROAD
91082.101 THX138 110E ENTRY
91483.251 JOX304 270E MAINROAD
91873.920 THX138 120E MAINROAD
91874.493 JOX304 280E EXIT
.
.
91982.102 THX138 290E EXIT
92301.302 THX138 300E ENTRY
92371.302 THX138 310E EXIT
.
'''

from typing import List
from collections import defaultdict


class LogEntry:
    """
    Represents a single toll booth log entry.

    Example log line:
    34400.409 SXY288 210E ENTRY
    """

    def __init__(self, log_line: str):
        tokens = log_line.split()

        # Fix: timestamp should be float, not string
        self.timestamp = float(tokens[0])

        self.license_plate = tokens[1]
        self.booth_type = tokens[3]

        location_token = tokens[2]

        # Example: 210E
        self.location = int(location_token[:-1])

        direction_letter = location_token[-1]

        if direction_letter == "E":
            self.direction = "EAST"
        elif direction_letter == "W":
            self.direction = "WEST"
        else:
            raise ValueError("Invalid direction")

    def __repr__(self):
        return (
            f"<LogEntry timestamp={self.timestamp}, "
            f"license={self.license_plate}, "
            f"location={self.location}, "
            f"direction={self.direction}, "
            f"booth_type={self.booth_type}>"
        )


class LogFile:
    """
    Stores all log entries and counts complete journeys.
    """

    def __init__(self, log_lines: List[str]):
        self.log_entries = [LogEntry(line.strip()) for line in log_lines]

    def count_journeys(self) -> int:
        """
        A complete journey:
        ENTRY -> (0 or more MAINROAD) -> EXIT
        """

        active_entries = defaultdict(int)
        completed_journeys = 0

        for log in self.log_entries:

            plate = log.license_plate
            booth = log.booth_type

            # Vehicle entered highway
            if booth == "ENTRY":
                active_entries[plate] += 1

            # Vehicle exited highway
            elif booth == "EXIT":

                # Count only if matching ENTRY exists
                if active_entries[plate] > 0:
                    completed_journeys += 1
                    active_entries[plate] -= 1

        return completed_journeys


# -----------------------------
# Sample Input
# -----------------------------

logs = [
    "90750.191 JOX304 250E ENTRY",
    "91081.684 JOX304 260E MAINROAD",
    "91082.101 THX138 110E ENTRY",
    "91483.251 JOX304 270E MAINROAD",
    "91873.920 THX138 120E MAINROAD",
    "91874.493 JOX304 280E EXIT",
    "91982.102 THX138 290E EXIT",
    "92301.302 THX138 300E ENTRY",
    "92371.302 THX138 310E EXIT",
]


# -----------------------------
# Test Cases
# -----------------------------

def test_complete_journeys():
    """Test basic complete journey counting"""
    logs = [
        "90750.191 JOX304 250E ENTRY",
        "91081.684 JOX304 260E MAINROAD",
        "91874.493 JOX304 280E EXIT",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 1, "Should count 1 complete journey"
    print("✓ test_complete_journeys passed")


def test_multiple_journeys():
    """Test multiple complete journeys"""
    logs = [
        "90750.191 JOX304 250E ENTRY",
        "91874.493 JOX304 280E EXIT",
        "92301.302 THX138 300E ENTRY",
        "92371.302 THX138 310E EXIT",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 2, "Should count 2 complete journeys"
    print("✓ test_multiple_journeys passed")


def test_interleaved_journeys():
    """Test interleaved journeys (from problem description)"""
    logs = [
        "90750.191 JOX304 250E ENTRY",
        "91081.684 JOX304 260E MAINROAD",
        "91082.101 THX138 110E ENTRY",
        "91483.251 JOX304 270E MAINROAD",
        "91873.920 THX138 120E MAINROAD",
        "91874.493 JOX304 280E EXIT",
        "91982.102 THX138 290E EXIT",
        "92301.302 THX138 300E ENTRY",
        "92371.302 THX138 310E EXIT",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 3, "Should count 3 complete journeys"
    print("✓ test_interleaved_journeys passed")


def test_no_entry():
    """Test exit without entry (incomplete journey)"""
    logs = [
        "90750.191 JOX304 250E MAINROAD",
        "91874.493 JOX304 280E EXIT",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 0, "Should not count journey without entry"
    print("✓ test_no_entry passed")


def test_no_exit():
    """Test entry without exit (incomplete journey)"""
    logs = [
        "90750.191 JOX304 250E ENTRY",
        "91081.684 JOX304 260E MAINROAD",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 0, "Should not count journey without exit"
    print("✓ test_no_exit passed")


def test_multiple_entries_single_exit():
    """Test multiple entries, only one exit"""
    logs = [
        "90750.191 JOX304 250E ENTRY",
        "90760.191 JOX304 251E ENTRY",
        "91874.493 JOX304 280E EXIT",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 1, "Should count only 1 journey (one exit)"
    print("✓ test_multiple_entries_single_exit passed")


def test_empty_log():
    """Test empty log file"""
    logs = []
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 0, "Should return 0 for empty log"
    print("✓ test_empty_log passed")


def test_only_mainroad():
    """Test only mainroad entries"""
    logs = [
        "91081.684 JOX304 260E MAINROAD",
        "91483.251 JOX304 270E MAINROAD",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 0, "Should not count journeys with only mainroad"
    print("✓ test_only_mainroad passed")


def test_west_direction():
    """Test journeys with WEST direction"""
    logs = [
        "90750.191 JOX304 250W ENTRY",
        "91081.684 JOX304 260W MAINROAD",
        "91874.493 JOX304 280W EXIT",
    ]
    log_file = LogFile(logs)
    assert log_file.count_journeys() == 1, "Should count west-bound journey"
    print("✓ test_west_direction passed")


if __name__ == "__main__":
    print("Running tests...\n")
    test_complete_journeys()
    test_multiple_journeys()
    test_interleaved_journeys()
    test_no_entry()
    test_no_exit()
    test_multiple_entries_single_exit()
    test_empty_log()
    test_only_mainroad()
    test_west_direction()
    print("\n✓ All tests passed!")

    print("\n" + "="*50)
    print("Running original sample...")
    log_file = LogFile(logs)
    print(f"Complete journeys: {log_file.count_journeys()}")

log_file = LogFile(logs)

print(log_file.count_journeys())