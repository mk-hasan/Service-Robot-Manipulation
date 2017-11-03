import rospy
from gpd.msg import GraspConfigList


grasps = []


def callback(msg):
    global grasps
    grasps = msg.grasps


# Create a ROS node.
rospy.init_node('get_grasps')

# Subscribe to the ROS topic that contains the grasps.
sub = rospy.Subscriber('/detect_grasps/clustered_grasps', GraspConfigList, callback)

# Wait for grasps to arrive.
rate = rospy.Rate(1)

while not rospy.is_shutdown():    
    if len(grasps) > 0:
        rospy.loginfo('Received %d grasps.', len(grasps))
        break
    
grasp = grasps #highest valued grasp 

for counter,graspvalue in enumerate(grasp):

  	print "score of grasp value ",counter," is ", graspvalue.score
	print 'selected grasp:', graspvalue 
