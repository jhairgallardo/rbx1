#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

pub = rospy.Publisher('velocidad_comand', Float32MultiArray, queue_size=5)

def talker(data):       
    rate = rospy.Rate(50) # 50hz
    num = Float32MultiArray()
    num.data=[data.linear.x,data.angular.z]
    rospy.loginfo(num)
    pub.publish(num)
    rate.sleep()

def envia_a_robot():
    rospy.init_node('envia_a_robot',anonymous=False)
    rospy.Subscriber('/cmd_vel', Twist, talker)
    rospy.spin()

if __name__ == '__main__':
    try:
        envia_a_robot()
    except rospy.ROSInterruptException:
        pass
