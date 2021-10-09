#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import add , addResponse


def callback(request):
    return addResponse(request.d + request.e)
   

def addition():
    rospy.init_node("Add")
    service = rospy.Service("Add",add,callback)
    rospy.spin()


if __name__ == '__main__':
    Add()
