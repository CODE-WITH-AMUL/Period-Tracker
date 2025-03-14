from plyer import notification
import time
#app_iocn = 'Icon/logo.png'
title = 'CycleSync'
message = 'How are you feeling today? {user.username}'
#notification.notify(logo=logo)
notification.notify(title=title, message=message, app_name="CycleSync")
time.sleep(10)
