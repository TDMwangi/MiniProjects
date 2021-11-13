import time
from plyer import notification

while(True):
    notification.notify(
        title = "Coding time!",
        message = "Stop gaming and start coding!",
        app_icon = "icon.ico",
        timeout = 10
    )
    time.sleep(10)