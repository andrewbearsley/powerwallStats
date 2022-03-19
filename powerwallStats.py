# Get Powerwall Stats for troubleshooting

from dotenv import load_dotenv
from pypowerwall import pypowerwall
import json
import os

# pypowerwall.set_debug(True) # Optional: Turn on Debug Mode

# Credentials for Powerwall - Customer Login
load_dotenv()
host = os.environ.get('TESLA_PW_HOST')  # IP of your Powerwall
email = os.environ.get('TESLA_PW_EMAIL') # Customer email eg. 'email@example.com'
password = os.environ.get('TESLA_PW_PASSWORD') # Last 5 digits of powerwall gateway WIFI password
timezone = os.environ.get('TESLA_PW_TIMEZONE')   # Your local timezone/tz

# Connect to Powerwall
pw = pypowerwall.Powerwall(host,password,email,timezone)

# Display Metric Examples
print("Battery power level: %0.0f%%" % pw.level())
print("Power response: %r" % pw.power())
print("Grid Power: %0.2fkW" % (float(pw.grid())/1000.0))
print("Solar Power: %0.2fkW" % (float(pw.solar())/1000.0))
print("Battery Power: %0.2fkW" % (float(pw.battery())/1000.0))
print("Home Power: %0.2fkW" % (float(pw.home())/1000.0))

# Raw JSON Data Examples
print("Alerts: %r" % pw.alerts())
print(json.dumps(pw.battery_blocks(), indent=4))
print(json.dumps(pw.vitals(), indent=4))
