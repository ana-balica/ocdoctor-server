import time

from constants.gcm_data import *
from ocd.notification import Notification

if __name__ == "__main__":
    notification = Notification(API_KEY)
    data = {"bad": ["device_id1", "device_id2"],
            "good": ["device_id3", "device_id4", "device_id5"]}
    for i in xrange(50):
        notification.send(registration_ids=registration_ids, data=data)
        print "notification sent - {0}".format(i)
        time.sleep(30)