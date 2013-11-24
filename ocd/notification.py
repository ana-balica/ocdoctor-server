from gcm import GCM


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
