# OpenAg-MVP-EXTRA

Code follows the board number convention.

- 3 - SDA to si7021
- 5 - SCL to si7021
- 29 - light relay (relay #4)
- 31 - pump/mister (relay #3)
- 33 - (reserved for relay #2)
- 35 - GPIO13 fan control (relay #1)

## Aeroponic pump/mister

This code doesn't care what is attached to this GPIO, but the assumption is that a rely is connected to the pin, and a high pressure water pump is controlled by the relay.  This pump provides the misting to the plant roots.
Current code turns on the pump every 5 minutes, and it runs for 5 seconds.  Both of these settings can be changed by modifying the persistent variable, or changing the crontab entry.

The Python code should be placed in the /home/pi/python directory (or wherever you put your Python code)

The duration of the pump being on is controlled by a persistent variable stored in the shelf file.  Click on the aeroSetup.py file to open it in Python, and run it to initialize the variable.

The frequency of the action is controled by the cron job that invokes the Python code.  Place the following line in the crontab file:

> */5 * * * * python /home/pi/python/aeroponicPump.py



