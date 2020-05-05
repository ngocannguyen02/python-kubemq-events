import datetime
import json

from kubemq.events.lowlevel.event import Event
from kubemq.events.lowlevel.sender import Sender

if __name__ == "__main__":
    try:
        publisher  = Sender("localhost:50000")
        f = open('bookmark_events.json')
        data = json.load(f)
        for event in data:
            event = Event(
                metadata="Bookmark event metadata",
                body =json.dumps(event).encode('utf-8') ,
                store=False,
                channel="bookmark_event_channel",
                client_id="bookmark_events_subscriber"
            )
            print(event)
            res = publisher.send_event(event)
            print(res)
        f.close()
    except Exception as err:
      print(
            "'Error when sending event:'%s'" % (
                err
                        )
        )