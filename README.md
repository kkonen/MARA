## Install

### ROS 2.0

- **ROS 2.0 Dashing**: following the official instructions, [source](https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Development-Setup/) or [debian packages](https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Install-Debians/). Make sure that you have colcon in your machine if you are installing from Debian packages.
`sudo apt install python3-colcon-common-extensions`

## Dependent tools
- **Gazebo 9.9.0**.
   - Install the latest available version of Gazebo via [one-liner instructions](http://gazebosim.org/tutorials?tut=install_ubuntu#Defaultinstallation:one-liner). Lower versions like **9.0.0 will not work**. Additional information is available [here](https://github.com/AcutronicRobotics/gym-gazebo2/issues/31#issuecomment-501660211).
     ```sh
     curl -sSL http://get.gazebosim.org | sh
     ```
- ROS 2 extra packages
```sh
sudo apt update && sudo apt install -y \
ros-dashing-rttest \
ros-dashing-rclcpp-action \
ros-dashing-gazebo-dev \
ros-dashing-gazebo-msgs \
ros-dashing-gazebo-plugins \
ros-dashing-gazebo-ros \
ros-dashing-gazebo-ros-pkgs

sudo apt install -y \
python3-pip python3-vcstool python3-numpy wget python3-pyqt5 python3-colcon-common-extensions git

```

### Create a ROS 2.0 workspace
Create the workspace and download source files:

```
mkdir -p ~/ros2_phantomx_ws/src
cd ~/ros2_phantomx_ws/src
git clone https://github.com/kkonen/PhantomX.git```
```

### Compile the ROS 2.0 workspace

Please  make sure you are not sourcing ROS workspaces via `.bashrc` or any other way.

```sh
source /opt/ros/dashing/setup.bash
cd ~/ros2_phantomx_ws && colcon build --merge-install
```
**Installation completed!** 
