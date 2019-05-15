from pyparrot.Bebop import Bebop
import math

bebop = Bebop()

print("connecting")
success = bebop.connect(20)
print(success)

print("sleeping")
bebop.smart_sleep(.5)

bebop.ask_for_state_update()

bebop.safe_takeoff(5)

bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-20, duration=1)  # lowwers drown
bebop.smart_sleep(1)
## first movment do not change
bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=4.7) # forward
bebop.fly_direct(roll=0, pitch=-100, yaw=0, vertical_movement=0, duration=1.2)
bebop.smart_sleep(2)

#second movement
bebop.fly_direct(roll=50, pitch=5, yaw=0, vertical_movement=0, duration=1.7) # right
bebop.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=.5)
bebop.smart_sleep(2)

# movment three
bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=2.7) # forward
bebop.smart_sleep(2)
#movment 4
bebop.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=3.8) # left
bebop.fly_direct(roll=100, pitch=0, yaw=0, vertical_movement=0, duration=0.5)
bebop.smart_sleep(2)
#movment 5
bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=20, duration=3.8)
bebop.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=1)
bebop.smart_sleep(2)
#movment 6
bebop.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=2.5)
bebop.fly_direct(roll=-90, pitch=0, yaw=0, vertical_movement=0, duration=1)
bebop.smart_sleep(2)
# movement 7
bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=3.6)
bebop.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=0.5)
bebop.smart_sleep(2)

bebop.smart_sleep(2)
bebop.safe_land(5)



print("DONE - disconnecting")
bebop.disconnect()
