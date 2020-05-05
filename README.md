# Python KubeMQ Publisher/Subscriber

Example KubeMQ Pub/Sub pattern. Publisher will publish bookmarks event on a channel. Subscriber is listening on it.

## Installation

https://kubemq.io/quick-start/

```bash
python3 -m venv dev
source dev/bin/activate
pip3 install requirements.txt
kubemqctl cluster create -t <licenceId>
kubemqctl set cluster proxy
```

## Usage

```bash
python3 events_publisher.py
python3 events_subscriber.py
```

## TODO
Add hbase persistence


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
None