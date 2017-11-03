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
import tf

#### Please change: cob_controller_configuration_gazebo/launch/robots/default_controllers_cob3-2.launch

class MoveArm(script):
    def Initialize(self):
        
        components_to_init = ['arm', "gripper"]
        
        for component in components_to_init:
            self.sss.init(component)
        
            
        
            
        '''handle_arm = self.sss.move("arm","pregrasp")
        handle_gripper = self.sss.move("gripper","cylopen", False) #true
        
        handle_arm.wait()
        handle_gripper.wait()'''
        
    
    def Run(self):
        print "============ Starting test grasp-----------------2"
        #self.istener = tf.TransformListener(True, rospy.Duration(10.0))
        #rospy.sleep(2)
        #handle_gripper = self.sss.move("gripper","cylopen", False) #true
        #handle_gripper.wait()
        
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
        
        '''pose_target.orientation.x=0.56087230074
        pose_target.orientation.y=-0.443264064483
        pose_target.orientation.z=0.555458003164
        pose_target.orientation.w=-0.4247418488'''
        '''pose_target.position.x = -2.843390372571#-2.8639596#-0.82 -0.75
        pose_target.position.y = -0.130325016132
        pose_target.position.z =  1'''
        pose_target.position.x =-2.949845417327#-2.8209518560517 #-2.843390372571#-2.8639596#-0.82 -0.75
        pose_target.position.y =0.132591305957#-0.130466889935 #-0.130325016132
        pose_target.position.z = 1.06
        group.set_pose_target(pose_target)
        
        print "target POSE: ", pose_target
    
        group.plan()
        group.go(wait=True)
        
        
        #moveit_commander.roscpp_shutdown()
        #handle_gripper = self.sss.move("gripper","cylclosed", False) #true
        #handle_gripper.wait()
        
        '''handle_arm = self.sss.move("arm","hold")
        handle_arm.wait() '''
        
       
        
    
    

if __name__ == '__main__':
    try:
        print "hello World - cob moveit_group"
        
        SCRIPT = MoveArm()
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
