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
        print "============ Robot Groups:"
        print robot.get_group_names()
        
        print "------------------- initial joint value: %s" %group.get_current_joint_values()
        
        
        print "============ Printing robot state"
        print robot.get_current_state()
	print "end-effector-position in 'global frame'?", group.get_current_pose(), group.get_pose_reference_frame()
        print "============"
        
        ## Planning to a Pose goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        print "============ Generating plan 1"
        pose_target = geometry_msgs.msg.Pose()

	print "target frame is apparently", group.get_pose_reference_frame()
        pose_target.position.x = -0.404119013305 + 0.3
        pose_target.position.y = -0.385958369706 + 0.1
        pose_target.position.z = 1.5646035069
        pose_target.orientation.x = -0.727368525818
        pose_target.orientation.y = -0.569617540043
        pose_target.orientation.z = -0.301556482574
        pose_target.orientation.w = 0.235657746621

        group.set_pose_target(pose_target)
        #joint_target = geometry_msgs.msg.Joint()
        plan1 = group.plan()

	print "============ Visualizing plan1"
	display_trajectory = moveit_msgs.msg.DisplayTrajectory()
	
	display_trajectory.trajectory_start = robot.get_current_state()
	display_trajectory.trajectory.append(plan1)
	display_trajectory_publisher.publish(display_trajectory);
	
	print "============ Waiting while plan1 is visualized (again)..."
	rospy.sleep(5)
	
	"""
	for i in [5]: #xrange(7):
		gjs = [0] * 7
		gjs[i] = 1.5
	        group.set_joint_value_target(gjs)
	        plan1 = group.plan()
       
		print "============ Visualizing plan1"
		display_trajectory = moveit_msgs.msg.DisplayTrajectory()
		
		display_trajectory.trajectory_start = robot.get_current_state()
		display_trajectory.trajectory.append(plan1)
		display_trajectory_publisher.publish(display_trajectory);
		
		print "============ Waiting while plan1 is visualized (again)..."
		rospy.sleep(5)

		group.execute(plan1)
		
		print "moved to target position >>", group.get_current_pose()
	"""
       
        # Uncomment below line when working with a real robot
        #group.go(wait=True)
        group.execute(plan1)
        
        print " ********************************************************* \n *****************************************"
        group_variable_values_current = group.get_current_joint_values()
        print "============ get_current_joint_values: ", group_variable_values_current
        
        group_variable_values_target = group.get_joint_value_target()# group.get_current_joint_values()
        print "============ get_joint_value_target: ", group_variable_values_target
        
        print " ********************************************************* \n *****************************************"
        
        #print "============ moving arm plan 1: ". group.get_current_joint_values()
        
        #self.sss.move("arm",[group.get_current_joint_values()])
        
        '''group.clear_pose_targets()
        
        ## Then, we will get the current set of joint values for the group
        group_variable_values = group.get_current_joint_values()
        print "============ Joint values: ", group_variable_values
        
        ## Now, let's modify one of the joints, plan to the new joint
        ## space goal and visualize the plan
        #group_variable_values[0] = 1.0
        group.set_joint_value_target(group_variable_values)
        
        plan2 = group.plan()'''
        
        
        print "============ moving arm plan 2: ", group_variable_values_current
        
        #ssjoinvalues = [2.4660451412200928, -1.6569322347640991, 1.8512247800827026, 1.3687270879745483, -1.1863553524017334, 1.0297310352325439, 0.68611335754394531]
        #ssjoinHome = [[0.0,0.0,0.0,0.0,0.0,0.0,0.0]]
        
        #rArm = self.sss.move("arm",[group_variable_values_target])
        #rArm.wait()
        
        #rGripper = self.sss.move("gripper","cylclose", False)
        #rGripper.wait()
        
        #rArm = self.sss.move("arm","home")
        
    
    
    
    
    

if __name__ == '__main__':
    try:
        print "hello World - cob moveit_group"
        
        SCRIPT = MyGrasp()
        SCRIPT.Run()
        
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
	#
        pass
