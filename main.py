import time
import argparse
import redis

class PingPong():
    def __init__(self, command):
        self.command = command
        self.client = redis.Redis("redis-server")
        self.pubsub = self.client.pubsub(ignore_subscribe_messages=True)
        self.pubsub.subscribe(**{'channel0': self.event_handler})
        self.pubsub.run_in_thread(sleep_time=1)

    def event_handler(self, msg):
        print(msg)
        if msg and msg.get('type') == 'message':
            data = msg["data"]
            if self.command == "ping":
                if data == b"ping":
                    time.sleep(1)
                    self.client.publish("channel0", "pong")
            elif self.command == "pong":
                if data == b"pong":
                    time.sleep(1)
                    self.client.publish("channel0", "ping")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('command', action = 'store', type = str, help = 'ping or pong' )
    args = parser.parse_args()
    ping_pong = PingPong(args.command)