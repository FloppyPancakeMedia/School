# Cole McLain Lab 01
# Server status 

from enum import Enum
import random
import time

class AlertPriority(Enum):
    """Helper enum to make identifying alerts easier. In theory."""
    CLEAR = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4

class ServerCluster:
    """A cluster of servers with a name. Uses random generation to give health codes
    and time since last checked."""

    def __init__(self, name : str):
        self.name = name
    
    def get_health_code(self) -> int:
        return random.randint(1, 3)
    
    def get_time_since_last_checked(self) -> int:
        return random.randint(1, 20)

class ServerMonitor:
    """Class that holds clusters it monitors. Can return the status of each
    cluster in its list of clusters."""

    def __init__(self):
        """Create a fun group of server clusters to store in the class"""
        self.clusters : list[ServerCluster] = [ServerCluster("AlphaOne"), 
                                           ServerCluster("JimBob's Funhouse"),
                                           ServerCluster("WamboDambo's Workshop")]
    
    def get_cluster_statuses(self) -> dict[str, int]:
        """Returns the name and alert priority of each cluster"""
        print('\n') # Debug readability
        statuses : dict[str, int] = dict()

        for c in self.clusters:
            # Iterate through each cluster to get info, then set alert priority
            health_code : int = c.get_health_code()
            time_last_checked : int = c.get_time_since_last_checked()

            # Print some debug info
            print(f"({c.name}: health_code = {health_code}  |  time_last_checked = {time_last_checked} hours")
            
            statuses[c.name] = self.get_alert_priority(health_code, time_last_checked)

            time.sleep(0.5) # Just for fun and excitement
        
        print('\n') # Debug readability
        return statuses
    
    def get_alert_priority(self, hc : int, tlc : int) -> int:
        """Parses the health code and time since last checked to return an alert priority"""

        if hc == 1:
            return AlertPriority.HIGH
        elif hc == 2:
            if tlc > 4:
                return AlertPriority.HIGH
            else:
                return AlertPriority.MEDIUM
        elif hc == 3:
             if tlc > 10:
                 return AlertPriority.LOW
             else:
                 return AlertPriority.CLEAR
        else:
            return 0


def parse_status(status_code : int) -> str:
    """Helps convert status codes into text"""
    if status_code == AlertPriority.CLEAR:
        return "CLEAR"
    elif status_code == AlertPriority.LOW:
        return "LOW"
    elif status_code == AlertPriority.MEDIUM:
        return "MEDIUM"
    elif status_code == AlertPriority.HIGH:
        return "HIGH"
    else:
        return "SOMETHING WENT REALLY F***ING WRONG"

# ------------------- Main execution section -------------------------
sm : ServerMonitor = ServerMonitor()
for i in range(2):
    statuses : dict[str, int] = sm.get_cluster_statuses()
    for s in statuses:
        print(f"{s} is at alert priority {parse_status(statuses[s])}")
        time.sleep(0.5)