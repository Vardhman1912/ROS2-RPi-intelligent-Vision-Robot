import gpiozero 
import time

Robot1 = gpiozero.Robot(left=(4, 14), right=(17, 18))

def main():
    print("Moving forward for 2 seconds")
    Robot1.forward()
    time.sleep(2)
    print("Moving in reverse for 2 seconds")
    Robot1.backward()
    time.sleep(2)
    print("Moving left for 2 seconds")
    Robot1.left()
    time.sleep(2)
    print("Moving right for 2 seconds")
    Robot1.right()
    time.sleep(2)
    print("Stopping for 2 seconds")
    Robot1.stop()
    time.sleep(2) 

    
# The above code is a simple example of how to control a robot using the gpiozero library in Python.

if __name__ == "__main__":
    main()