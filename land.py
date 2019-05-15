
from pyparrot.Bebop import Bebop
import math

bebop = Bebop()

print("connecting")
success = bebop.connect(20)
print(success)

print("sleeping")
bebop.smart_sleep(5)

bebop.ask_for_state_update()
bebop.safe_takeoff(1)
bebop.smart_sleep(1)
bebop.safe_land(1)

print("DONE - disconnecting")
bebop.disconnect()