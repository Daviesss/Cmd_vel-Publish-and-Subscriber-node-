#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def call_back (msg):
    print (msg.pose)
    
    
rospy.init_node('square_subscriber')
loop = rospy.Rate(2)
sub = rospy.Subscriber('/odom',Odometry,call_back)
rospy.spin()


    
