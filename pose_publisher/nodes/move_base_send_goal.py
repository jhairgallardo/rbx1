#!/usr/bin/env python
import roslib
import rospy

from geometry_msgs.msg import PoseStamped
from std_msgs.msg import UInt8

#Este script se encarga de publicar el punto meta al move base. Esto se hace publicando en el topico
#move_base_simple/goal un mensaje del tipo geometry_msgs/PoseStamped. Este script debe activarse
#para mandar al robot al punto de inicio.

pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=5, latch=True) 
#Se debe activar el latch para poder mandar el comando al move_base. 

def move(flag):
	if flag.data==1:
		rate = rospy.Rate(50) # 50hz
		goal = PoseStamped()
		goal.header.frame_id = 'map'
		#goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = 0
		goal.pose.position.y = 0
		goal.pose.position.z = 0
		goal.pose.orientation.w = 1.0
		pub.publish(goal)
		rate.sleep()
		print goal

if __name__ == '__main__':
	rospy.init_node('simple_goal', anonymous=False) #make node 
	rospy.Subscriber('batery_low', UInt8, move)
	rospy.spin()
#aca se puede agregar el condicional, suscribiendose a un topico del arduino para activar la funcion 
#"move" solo cuando llegue un msj del arduino rospy.Subscriber('/bateria_low', Float32, move)

# Para correr este script debes correr el move base. Segun el libro se puede correr con los siguientes comandos (usando un simulador de un robot)
#roslaunch rbx1_bringup fake_turtlebot.launch
#roslaunch rbx1_nav fake_move_base_blank_map.launch
#rosrun rviz rviz -d `rospack find rbx1_nav`/nav.rviz

