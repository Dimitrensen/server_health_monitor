#!/bin/bash
case $1 in
  start)
    echo "Starting server..."
    sudo systemctl start accounts-daemon.service
    ;;
  stop)
    echo "Stopping server..."
    sudo systemctl stop accounts-daemon.service
    ;;
  status)
    sudo systemctl status accounts-daemon.service
    ;;
  *)
    echo "Usage: $0 {start|stop|status}"
    exit 1
    ;;
esac
