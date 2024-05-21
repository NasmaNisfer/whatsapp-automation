
import pywhatkit

# The message will be sent at 14:30 (2:30 PM). You can change this to your desired time.
# Time is in 24-hour format.

try:
    pywhatkit.sendwhatmsg("+PHONE_NUMBER", "Your message here", 14, 30)
    print("Successfully sent the message!")
except Exception as e:
    print(f"An error occurred: {e}")
