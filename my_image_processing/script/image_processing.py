import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = CvBridge()  # Create a bridge

def image_callback(ros_image):
    print("Received an image")
    try:
        # Convert ROS image message to OpenCV format (BGR8)
        cv_image = bridge.imgmsg_to_cv2(ros_image, 'bgr8')
    except CvBridgeError as e:
        print(e)
        return

    # Now you can work with OpenCV commands:
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

def main(args):
    rospy.init_node('image_converter', anonymous=True)
    image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
