from gcm import GCM

from constants.gcm_data import *


class Notification(object):
    """ Wrapper message class for server notifications
    """
    def __init__(self, API_KEY):
        """ Message initializer

        :param API_KEY: the API key from GCM (Google Cloud Messaging)
        """
        self.gcm = GCM(API_KEY)

    def send(self, registration_ids, data):
        """ Send a notification to registered users

        :param registration_ids: list of registration ids of clients
        :param data: payload dict in the format {"device_id": "status"}
        :return: True if everything is OK, response errors if any occured
                 during the request
        """
        response = self.gcm.json_request(registration_ids=registration_ids,
                                         data=data)
        if 'errors' in response:
            return response['errors']
        return True

    def process(self):
        pass

if __name__ == "__main__":
    # testing
    notification = Notification(API_KEY)
    data = {"bad": ["device_id1", "device_id2"],
            "good": ["device_id3", "device_id4", "device_id5"]}
    notification.send(registration_ids=registration_ids, data=data)
    print "notification sent"
