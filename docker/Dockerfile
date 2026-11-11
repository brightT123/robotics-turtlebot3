FROM ros:humble-ros-base-jammy

ARG USERNAME=dev
ARG UID=1000
ARG GID=1000

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    python3-pip \
    python3-rosdep \
    ros-humble-rviz2 \
    ros-humble-slam-toolbox \
    ros-humble-nav2-map-server \
    ros-humble-rqt-graph \
    ros-humble-demo-nodes-cpp \
    ros-humble-demo-nodes-py \
    git nano iputils-ping net-tools sudo \
    ros-humble-turtlebot3-gazebo \
    ros-humble-turtlebot3-simulations \
    ros-humble-gazebo-ros-pkgs \
    && rm -rf /var/lib/apt/lists/*

# Hapus user default 'ubuntu' jika UID 1000 sudah terpakai di Ubuntu 22.04 (Jammy)
RUN if id -u ${UID} >/dev/null 2>&1; then userdel -r $(id -un ${UID}) 2>/dev/null || true; fi && \
    groupadd -g ${GID} ${USERNAME} 2>/dev/null || true && \
    useradd -m -u ${UID} -g ${GID} -s /bin/bash ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Buat direktori kerja & atur hak milik sebelum berpindah USER
RUN mkdir -p /ws && chown -R ${UID}:${GID} /ws

RUN echo "source /opt/ros/humble/setup.bash" >> /home/${USERNAME}/.bashrc && \
    echo "[ -f /ws/install/setup.bash ] && source /ws/install/setup.bash" >> /home/${USERNAME}/.bashrc

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER ${USERNAME}
WORKDIR /ws

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]

