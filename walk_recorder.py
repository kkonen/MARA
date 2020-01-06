import csv
import time
import numpy as np


# ROS 2
import rclpy
from gazebo_msgs.msg import ContactsState
from std_msgs.msg import Float32


def timer_callback():
    line = []
    #print(c1_forward)
    for leg in legs:
        #line.append(1 if contact_msgs["tibia_" + leg] is 0 and c1_forward[leg] is 1 else 0)
        line.append(contact_msgs["tibia_" + leg])
        contact_msgs["tibia_" + leg] = 0
    for leg in legs: 
        line.append(c1_forward[leg])
        c1_forward[leg] = 0
    csv_writer.writerow(line)

def leg_contact_callback(message):
    if message.states:
        if message.states[0].collision1_name.split("::")[0] == message.states[0].collision2_name.split("::")[0]:
            return
        contact_msgs[message.states[0].collision2_name.split("::")[1]] = 1


#IF LEFT SIDE IS NEGATIVE: LEG IS MOVING FORWARDS
#IF RIGHT SIDE IS POSITIVE: LEG IS MOVING FORWARDS!
def c1_lf_callback(message):
#    print('lf' + str(message.data))
    c1_forward['lf'] = 1 if message.data < 0 else 0
def c1_lm_callback(message):
#    print('lm' + str(message.data))
    c1_forward['lm'] = 1 if message.data < 0 else 0
def c1_lr_callback(message):
#    print('lr' + str(message.data))
    c1_forward['lr'] = 1 if message.data < 0 else 0
def c1_rf_callback(message):
#    print('rf' + str(message.data))
    c1_forward['rf'] = 1 if message.data > 0 else 0
def c1_rm_callback(message):
#    print('rm' + str(message.data))
    c1_forward['rm'] = 1 if message.data > 0 else 0
def c1_rr_callback(message):
#    print('rr' + str(message.data))
    c1_forward['rr'] = 1 if message.data > 0 else 0
#print("init")
rclpy.init()
node = rclpy.create_node("locomotion_plotter")
#print("start")
legs = ['lf', 'lm', 'lr', 'rf', 'rm', 'rr']
contact_msgs = {}
c1_forward = {}
contact_sc = {}
c1_sc = {}

for leg in legs:
    contact_sc["tibia_" + leg] = node.create_subscription(ContactsState, '/tibia_' + leg + '_collision', leg_contact_callback)
    contact_msgs["tibia_" + leg] = 0
    c1_forward[leg] = 0

c1_sc['lf'] = node.create_subscription(Float32, '/j_c1_lf/force', c1_lf_callback)
c1_sc['lm'] = node.create_subscription(Float32, '/j_c1_lm/force', c1_lm_callback)
c1_sc['lr'] = node.create_subscription(Float32, '/j_c1_lr/force', c1_lr_callback)
c1_sc['rf'] = node.create_subscription(Float32, '/j_c1_rf/force', c1_rf_callback)
c1_sc['rm'] = node.create_subscription(Float32, '/j_c1_rm/force', c1_rm_callback)
c1_sc['rr'] = node.create_subscription(Float32, '/j_c1_rr/force', c1_rr_callback)

csv_file = open('locomotion.csv', mode='w')
csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(['lf_contact','lm_contact','lr_contact','rf_contact','rm_contact','rr_contact','lf_forward','lm_forward','lr_forward','rf_forward','rm_forward','rr_forward'])

timer = node.create_timer(1/25, timer_callback)

rclpy.spin(node)
