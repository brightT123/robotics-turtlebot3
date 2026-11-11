#!/bin/bash
set -e

# Load ROS 2 Humble base environment
if [ -f "/opt/ros/humble/setup.bash" ]; then
    source "/opt/ros/humble/setup.bash" --
fi

# Load local workspace environment if built
if [ -f "/ws/install/setup.bash" ]; then
    source "/ws/install/setup.bash" --
fi

exec "$@"
