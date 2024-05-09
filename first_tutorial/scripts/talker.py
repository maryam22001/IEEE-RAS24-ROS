#!/usr/bin/env python3


import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('V2V_topic', V2V, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    my_car_info = V2V()  # define your message name
    my_car_info.battery_level = 0.95
    my_car_info.id = 1223
    my_car_info.car_pose.x = 5
    my_car_info.car_speed.linear.x = 30
    pub.publish(my_car_info)
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
