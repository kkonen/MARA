# MARA

<a href="http://www.acutronicrobotics.com"><img src="https://acutronicrobotics.com/assets/images/AcutronicRobotics_logo.jpg" align="left" hspace="8" vspace="2" width="200"></a>

This is the official repository of [MARA](https://acutronicrobotics.com/products/mara/) modular robot, world's first modular cobot. MARA is the first robot which runs ROS 2.0 on each joint empowering new possibilities and applications in the professional and industrial landscapes of robotics. Built out of individual modules that natively run ROS 2.0, the modular robot arm can be physically extended in a seamless manner. MARA delivers industrial-grade features such as time synchronization or deterministic communication latencies.

Among other things, you will find in this repository instructions on how to simulate and control MARA in Gazebo Simulator or on the real robot.

## Features

<a href="http://www.acutronicrobotics.com"><img src="https://acutronicrobotics.com/products/mara/images/xv2_MARA2-11.jpg.pagespeed.ic.QRaRP5N01r.webp" align="right" hspace="8" vspace="2" width="200"></a>

- **Powered by ROS 2.0**: a fully distributed software and hardware robotic architecture.

- **Highly customizable**: with daisy chaining, power and communication are exposed at the module level allowing for simplified extensions.

- **Real time data monitoring**: every H-ROS module is able to monitorize a variety of intrinsic aspects in real-time.

- **Power readings**: instantaneous voltage, current and power readings from each module, individually.

- **Automatic re-configuration**: embedded accelerometers, magnetometers and gyroscopes empower each module with inertial data.

- **HW and SW life cycle**: life cycle for each module allows greater control over the state of the ROS system and the underlying components.

- **Controllable from any ROS 2.0 enabled computer**: [ORC](https://acutronicrobotics.com/products/orc/) is the ideal complement for MARA, but not mandatory. Choose yourself how you steer MARA.

## Table of Contents
* [MARA](#mara)
  * [Features](#features)
  * [Table of Contents](#table-of-contents)
    * [Specifications](#specifications)
    * [Packages](#packages)
    * [Dependendent tools](#dependent-tools)
    * [Create a ROS workspace](#create-a-ros-workspace)
    * [Compile the ROS workspace](#compile-the-ros-workspace)
    * [Set up MoveIt! in ROS 1 (optional)](#set-up-optional-moveit-in-ros-1)
      * [Usage in Gazebo Simulator](#usage-in-gazebo-simulator)
        * [Terminal 1 (ROS 2.0):](#terminal-1-ros-2)
        * [Terminal 2 (ROS):](#terminal-2-ros)
        * [Terminal 3 (bridge):](#terminal-3-bridge)
      * [Usage on the real robot](#usage-on-the-real-robot)
        * [Terminal 1 (ROS 2):](#terminal-1-ros-2)
        * [Terminal 2 (ROS):](#terminal-2-ros)
        * [Terminal 3 (bridge):](#terminal-3-bridge)
    * [Example code](#example-code)
    * [Help](#help)

*Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)*

### Specifications

![](https://acutronicrobotics.com/products/mara/images/xMARA_evolution_end.jpg.pagespeed.ic.dVNwzZ6-4i.webp)


| Spec | Value |
|------|-------|
| Degrees of freedom | 6 DoF, extensible |
| Maximum speed | 90º/s |
| Repeatability | ±0.1 mm |
| Rated torque | 9.4/30 Nm |
| Payload | 3 Kg |
| Weight | 21 Kg |
| Height | 871 mm |
| Reach | 656 mm |
| Footprint | 204 mm |
| Robotics framework | ROS 2 Crystal Clemmys |
| Communication interfaces | 1 Gbps Ethernet, Compliant with TSN standards |
| Information model | Hardware Robot Information Model (HRIM®), version Anboto  |
| Security | Encrypted and secure computing environment, Secure data exchange capabilities |
| Automatic updates | Over-the-Air (OTA) |
| Datasheet | [Download datasheet](https://acutronicrobotics.com/products/mara/files/MARA_datasheet_v1.1.pdf) |

### Packages

<a href="http://www.acutronicrobotics.com"><img src="https://acutronicrobotics.com/products/mara/images/v2_MARA6_1-11.png" align="right" hspace="8" vspace="2" width="200"></a>

 - `hros_cognition_mara_components`: Transformations between JointTrajectory messages and module specific HRIM messages.
 - `individual_trajectories_bridge`: Bridge to connect ROS and ROS2.
 - `mara_bringup`: roslaunch scripts for starting the MARA.
 - `mara_contact_publisher`: ROS2 publisher to know if a collision takes place.
 - `mara_description`: 3D models of the MARA for simulation and visualization.
 - `mara_gazebo`: Gazebo simulation package for the MARA.
 - `mara_gazebo_plugins`: MARA Gazebo plugins for sensors and motors.
 - `mara_utils_scripts`: Some scripts to move the MARA or spawn the model.

### Gazebo, ROS 2.0, ROS and MoveIt!
- **Gazebo 9**: following the official instructions, [one-liner or step-by-step](http://gazebosim.org/tutorials?tut=install_ubuntu)
- **ROS 2.0 Crystal**: following the official instructions, [source](https://index.ros.org/doc/ros2/Linux-Development-Setup/) or [debian packages](https://index.ros.org/doc/ros2/Linux-Install-Debians/).

  ROS and MoveIt! are optional, required if you want to use `ìndividual_trajectories_bridge` to controll the MARA, which means using ROS Melodic with MoveIt through bridges.

- **ROS melodic**: following the official instructions, [source](http://wiki.ros.org/melodic/Installation/Source) or [debian_packages](http://wiki.ros.org/melodic/Installation/Ubuntu).
- **MoveIt!**: `sudo apt install ros-melodic-moveit`.

### Dependent tools

```sh
sudo apt install -y python3-vcstool python3-numpy wget ros-melodic-moveit-ros-move-group ros-melodic-moveit-visual-tools
```

### Create a ROS 2.0 workspace
Create the workspace and download source files:

```sh
mkdir -p ~/ros2_mara_ws/src
cd ~/ros2_mara_ws
wget https://raw.githubusercontent.com/acutronicrobotics/MARA/master/mara-ros2.repos
vcs import src < mara-ros2.repos
```

Generate [HRIM](https://github.com/AcutronicRobotics/HRIM) dependencies:

```sh
cd ~/ros2_mara_ws/src/HRIM/installator
python3 setup.py install && cd ..
hrim generate models/actuator/servo/servo.xml
hrim generate models/actuator/gripper/gripper.xml
```

### Compile the ROS workspace

Please  make sure you are not sourcing ROS1 workspaces via `.bashrc` or any other way.

```sh
source /opt/ros/crystal/setup.bash
cd ~/ros2_mara_ws && colcon build --merge-install --packages-skip individual_trajectories_bridge
```

Optional `individual_trajectories_bridge`:

```sh
. /opt/ros/melodic/setup.bash
cd ~/ros2_mara_ws && colcon build --merge-install --packages-select individual_trajectories_bridge
# Building ROS 1 creates conflicts with this ROS 2.0 workspace. Next line ensures the workspace is completely ROS 2.0.
sed -i 's#/opt/ros/melodic#/opt/ros/crystal#g' ~/ros2_mara_ws/install/setup.bash
```

### Set up (optional) MoveIt! in ROS 1

```sh
mkdir -p ~/ros_mara_ws/src
cd ~/catkin_mara_ws/src
git clone https://github.com/AcutronicRobotics/MARA_ROS1
cd ~/catkin_mara_ws/
catkin_make_isolated --install
```

### Usage in Gazebo Simulator

#### Terminal 1 (ROS 2.0):

To spawn the simulated robot in Gazebo, you can choose one of the following ros2 launch files depending on the gripper that you want to use:

```
. ~/ros2_mara_ws/install/setup.bash

ros2 launch mara_gazebo mara.launch.py
ros2 launch mara_gazebo mara_gripper_140.launch.py
ros2 launch mara_gazebo mara_gripper_85.launch.py
ros2 launch mara_gazebo mara_gripper_hande.launch.py
```

#### Terminal 2 (ROS):
```
. ~/catkin_mara_ws/devel/setup.bash

python3 ~/catkin_mara_ws/src/mara_camera/mara_bringup/scripts/follow_joints_trajectory_actions.py ~/catkin_mara_ws/src/mara_camera/mara_bringup/config/motors.yaml &
# change the prefix to match with the gripper used in the Terminal 1
roslaunch mara_bringup mara_bringup_moveit_actions.launch prefix:=140 &

sleep 4
roslaunch mara_moveit_config mara_moveit_planning_execution.launch

```

#### Terminal 3 (bridge):
```sh
source ~/catkin_mara_ws/devel/setup.bash
source ~/ros2_mara_ws/install/setup.bash

ros2 run individual_trajectories_bridge individual_trajectories_bridge_actions -motors ~/ros2_mara_ws/src/mara/individual_trajectories_bridge/config/motors_actions.yaml
```

### Usage on the real robot

#### Terminal 1 (ROS 2.0)
```sh
source ~/ros2_mara_ws/install/setup.bash
# you will need to change the export values according to the SOMs configuration
export RMW_IMPLEMENTATION=rmw_opensplice_cpp
export ROS_DOMAIN_ID=22

ros2 launch mara_bringup mara_bringup_real.launch.py
```

#### Terminal 2 (ROS)
```sh
source ~/catkin_mara_ws/devel/setup.bash
# you will need to change the yaml files to match the topics names on your SOMs
python3 ~/catkin_mara_ws/src/mara_camera/mara_bringup/scripts/follow_joints_trajectory_actions.py ~/catkin_mara_ws/src/mara_camera/mara_bringup/config/motors.yaml &
roslaunch mara_bringup mara_bringup_camera_moveit_actions.launch prefix:=140 yaml:=motors_camera.yaml &

sleep 3
roslaunch mara_moveit_config mara_moveit_planning_execution.launch

```

#### Terminal 3 (bridge)
```sh
source ~/catkin_mara_ws/devel/setup.bash
source ~/ros2_mara_ws/install/setup.bash
# you will need to change the export values according to the SOMs configuration, same as in Terminal 1
export RMW_IMPLEMENTATION=rmw_opensplice_cpp
export ROS_DOMAIN_ID=22
# you will need to change the yaml files to match the topics names on your SOMs
ros2 run individual_trajectories_bridge individual_trajectories_bridge_actions -motors ~/ros2_mara_ws/src/mara/individual_trajectories_bridge/config/motors_actions.yaml &
```

### Example code

 - [mara_examples](https://github.com/AcutronicRobotics/mara_examples.git)

### Help

If you need help with MARA's real robot or its simulation, feel free to raise an issue [here](https://github.com/AcutronicRobotics/MARA/issues).
