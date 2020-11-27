import requests
import json

API_URL = 'https://api.mailjet.com/v4/sms-send'
FROM = 'Integrated'

# Authorisation header with Bearer Token
headers = {"Authorization": "Bearer 632dd8230b2d49c291a0ca582f245e65"}

# Headers from CSV file
NAME_HEADER = "Name"
NUMBER_HEADER = "Number"

# Print debug information if true
DEBUG = True


class Client(object):
    """
    Client Module for Storing Client Information and Sending Messages via Mailjet API
    """
    def __init__(self, data):
        """
        Constructor
        Must ensure data contains required information

        :param data: Client information and message text
        """
        self.information = data
        self.response = None

    def send_message(self):
        """Send message via HTTP POST Request to MailJet API"""

        # JSON Format for sending message via API
        message_data = {
            "FROM": FROM,
            "TO": self.information["Number"],
            "Text": self.information["Message"]
        }

        message_json = json.dumps(message_data)

        if DEBUG:
            print("Sending {}".format(json.loads(message_json)))

        self.response = requests.post(API_URL, data=message_json, headers=headers).json()

        if DEBUG:
            print(self.response)

        if self.response["StatusCode"] != 200:
            return False
        else:
            return True

    def export_failed(self):
        """Return Relevent Information on failed Send"""
        return [self.information[NAME_HEADER], self.information[NUMBER_HEADER], self.response["ErrorMessage"]]
