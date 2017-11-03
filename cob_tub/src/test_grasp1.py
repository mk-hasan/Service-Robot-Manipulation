#!/usr/bin/python
import roslib
roslib.load_manifest('cob_script_server')

from simple_script_server import script

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

#### Please change: cob_controller_configuration_gazebo/launch/robots/default_controllers_cob3-2.launch

class MyGrasp(script):
    def Run(self):
        print "============ Starting test grasp-----------------2"
        #rospy.init_node('test_grasp',
        #               anonymous=True)
       
        
        moveit_commander.roscpp_initialize(sys.argv)
        robot = moveit_commander.RobotCommander()
        
        scene = moveit_commander.PlanningSceneInterface()
        
        group = moveit_commander.MoveGroupCommander("arm")
        
        display_trajectory_publisher = rospy.Publisher(
                                            '/move_group/display_planned_path',
                                            moveit_msgs.msg.DisplayTrajectory)
        
        print "============ Waiting for RVIZ..."
        #rospy.sleep(10)
        print "============ Reference get_planning frame: %s" % group.get_planning_frame()
        print "============ Reference end_effector frame: %s" % group.get_end_effector_link()
        print "============ Reference end_effector frame: %s" % group.get_current_pose(group.get_end_effector_link())
        
        print "============ Robot Groups:"
        print robot.get_group_names()
        
        print "------------------- initial joint value: %s" %group.get_current_joint_values()
        
        
        print "============ Printing robot state"
        print robot.get_current_state()
        print " ====== ====== "
        
        ## Planning to a Pose goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        oldPose = group.get_current_pose().pose
        print "OLD POSE: ", oldPose
        
        ##shaon end
        print "============ Generating plan 1"
        pose_target = geometry_msgs.msg.Pose()
        pose_target.orientation = oldPose.orientation
        pose_target.position.x = oldPose.position.x
        pose_target.position.y = oldPose.position.y + 0.04 
        pose_target.position.z = oldPose.position.z 
        group.set_pose_target(pose_target)
        
        print "target POSE: ", pose_target
    
        plan1 = group.plan()
        group.go(wait=True)
        
   
                
        print " ********************************************************* \n *****************************************"
        group_variable_values_current = group.get_current_joint_values()
        print "============ get_current_joint_values: ", group_variable_values_current
        
        
        
        
    
    

if __name__ == '__main__':
    try:
        print "hello World - cob moveit_group"
        
        SCRIPT = MyGrasp()
        SCRIPT.Start()
        
        count = 0
        while not rospy.is_shutdown():
           # rate = rospy.Rate(1)
            #rate.sleep()
            if(count<3):
                print "-------------------- %s"%count
            elif(count ==3):  
                print "-------------------- script completed............" 
                
            count = count + 1
        
        
    except rospy.ROSInterruptException:
        pass
