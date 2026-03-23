FROM ros:humble-desktop-full

# Needed Dev tools 
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-pip \
    ros-humble-gazebo-ros-pkgs \
    && rm -rf /var/lib/apt/lists/* 

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Source ROS2 on container start with bashrc 
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

WORKDIR /ros2_ws