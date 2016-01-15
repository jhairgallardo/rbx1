#!/usr/bin/env python
import roslib
import rospy

from nav_msgs.msg import Odometry
from rbx1_nav.transform_utils import quat_to_angle, normalize_angle
from std_msgs.msg import Float32MultiArray

pub = rospy.Publisher('pose_xytheta', Float32MultiArray, queue_size=5)

def odometryCb(msg):
	rate = rospy.Rate(50) # 50hz
	pose = Float32MultiArray()
	quat = msg.pose.pose.orientation
	position = msg.pose.pose.position
	euler = quat_to_angle(quat)
	pose.data = [position.x,position.y,euler]
	pub.publish(pose)
	rate.sleep()
    #print msg.pose.pose.orientation
    

if __name__ == "__main__":
    rospy.init_node('pose_publisher', anonymous=True) #make node 
    rospy.Subscriber('scanmatch_odom',Odometry,odometryCb)
    rospy.spin()