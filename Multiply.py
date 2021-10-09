#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import add, addResponse
from beginner_tutorials.msg import multiply

def Mul(x,y):
    rospy.init_node("Mul",anonymous=True)
    rospy.wait_for_service("Add")
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        add_two_ints = rospy.ServiceProxy("Add",add)
        response = add_two_ints(x,y)
        rospy.loginfo("Sum of %d and %d is %d.",x,y,response.result)

        pub = rospy.Publisher('chatter', multiply, queue_size=10)
        msg = multiply()
        msg.c = response.result
        msg.a = 4
        msg.b = msg.c * msg.b
    
    
        pub.publish(msg)
        rate.sleep()
    

if __name__ == '__main__':
    Mul(2,3)
