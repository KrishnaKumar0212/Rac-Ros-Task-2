#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import multiply

def callback(data):
    rospy.loginfo("Multiplication of %d with the sum %d is %d.",data.a,data.b,data.c)
    
def Ans():


    rospy.init_node('Ans', anonymous=True)

    rospy.Subscriber("chatter", multiply, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    Ans()
