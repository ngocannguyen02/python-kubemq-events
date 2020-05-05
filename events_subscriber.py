from builtins import input
from random import randint
from kubemq.events.subscriber import Subscriber
from kubemq.tools.listener_cancellation_token import ListenerCancellationToken
from kubemq.subscription.subscribe_type import SubscribeType
from kubemq.subscription.events_store_type import EventsStoreType
from kubemq.subscription.subscribe_request import SubscribeRequest

def process_events(event):
    if event:
        print("Subscriber Received Event: Metadata:'%s', Channel:'%s', Body:'%s tags:%s'" % (
            event.metadata,
            event.channel,
            event.body,
            event.tags
        ))

def error_handler(error_msg):
        print("Error event received:%s'" % (
            error_msg
        ))

if __name__ == "__main__":
    print("Subscribing to events on bookmark channel")
    cancel_token=ListenerCancellationToken()

    subscriber = Subscriber("localhost:50000")
    subscribe_req = SubscribeRequest(
        channel="bookmark_event_channel",
        client_id="bookmark_events_subscriber",
        events_store_type=EventsStoreType.Undefined,
        events_store_type_value=0,
        group="",
        subscribe_type=SubscribeType.Events # https://github.com/kubemq-io/kubemq-Python/blob/master/kubemq/subscription/subscribe_type.py
    )
    # https://github.com/kubemq-io/kubemq-Python/blob/master/kubemq/events/subscriber.py
    subscriber.subscribe_to_events(subscribe_req, process_events, error_handler, cancel_token)

    input("Press 'Enter' to stop Listen...\n")
    cancel_token.cancel()
    input("Press 'Enter' to stop the application...\n")
