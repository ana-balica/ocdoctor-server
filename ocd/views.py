import logging
import json

from flask import request
from werkzeug.exceptions import MethodNotAllowed, BadRequest
from ocd import app

from constants.gcm_data import *
from notification import Notification


@app.route("/register", methods=["POST"])
def add_registration_id():
    """ Register a new user with its registration id
    """
    if request.method != "POST":
        return MethodNotAllowed(valid_methods=["POST"])

    device_id = request.data.get("id")
    if device_id:
        registration_ids.extend([device_id])


@app.route("/notification", methods=["POST"])
def push_notification():
    """ Send a notification with the device name and status
    """
    if request.method != "POST":
        return MethodNotAllowed(valid_methods=["POST"])

    data = json.loads(request.data)
    device_name = data.get("device_name")
    status = data.get("status")

    if not device_name or not status:
        return BadRequest(description="Parameters <device_name> and <status> are mandatory")

    notification = Notification(API_KEY)
    notification.send(registration_ids=registration_ids, data=data)
    logging.info("Notification sent about {0} with status '{1}'".format(device_name, status))
    return "200 OK"
