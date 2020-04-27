#!/bin/sh

case "$1" in
        start)
                echo "Subscribe."
                mosquitto_sub -h 10.0.0.47 -t test
        ;;
        stop)
        ;;
        *)
                echo "Usage: $0 {start|stop}"
        exit 1
esac
exit 0