#!/usr/bin/env python
from distutils import command
import rospy
from geometry_msgs.msg import Twist
import time
from nav_msgs.msg import Odometry

x= 0
y = 0
z = 0
odometry_topic = '/odom'

# distance = 3.0
# # speed = 3


# def call_back (msg):
#     print (msg.pose)
#     rospy.init_node('square')
    



def move (speed,distance):
    rospy.init_node('square_Publisher',anonymous=True)
    loop = rospy.Rate(2)
    # sub = rospy.Subscriber(odometry_topic,Odometry,call_back)
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    velocity_message = Twist ()
    velocity_message.linear.x = 2
    

    while not rospy.is_shutdown():
        rospy.loginfo("Now the code has beeen executed")
        pub.publish(velocity_message)


# # # starting all cordinates at initial position 
# # # Therefore;

# # # lets make all coordinate to start at point 0

# # # here we go ;
# # x0 = 0
# # y0 = 0
# # z0 = 0
# rospy.init_node('square',anonymous=True)
# velocity_message = Twist() #Reading the Twist message and saving it in a Variable
# velocity_message.linear.x = 0
# velocity_message.linear.y = 0
# if distance == 3.0 :
#    speed +=2
# #    velocity_message.linear.x = 2
#    velocity_message.angular.z = 2
#    velocity_message.linear.x = 0
#    velocity_message.linear.x = 2

# elif distance < 3.0:
#     velocity_message.linear.x = 2
#     velocity_message.angular.y =  2
#     velocity_message.linear.x = 2
#     velocity_message.angular.y = 2
# else :
#     velocity_message.angular.z = 3

# loop = rospy.Rate (2)
# pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)


# while not rospy.is_shutdown():
#     sub = rospy.Subscriber(odometry_topic,Odometry,call_back)
#     rospy.loginfo("The action has been taking")
#     pub.publish(velocity_message)



if __name__ == '__main__':
    try :
        # sub = rospy.Subscriber(odometry_topic,Odometry,call_back)
        move (1.0,5.0)

    
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")



