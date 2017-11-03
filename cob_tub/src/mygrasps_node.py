#!/usr/bin/python
import rospy

from simple_script_server import script

import tf
from geometry_msgs.msg import *
from moveit_msgs.srv import *



class mygrasps_node(script):
    def Run(self):
        rospy.loginfo("Initializing all components...")
        
        components_to_init = ['tray', 'torso', 'arm', 'base', "gripper"]
        
        for component in components_to_init:
            self.sss.init(component)
            
        
        self.sss.move("gripper","cylclosed")
        '''self.sss.move("arm","hold")
        
        handle01 = self.sss.move("arm","grasp-to-tray",False)
        self.sss.move("tray","up")
        handle01.wait()
        self.sss.move("arm","tray")
        self.sss.move("gripper","cylopen")
        self.sss.move("arm","tray-to-folded",False)'''

if __name__=='__main__':
    try:
        print "====Grasp Now" 
        mygrasps_node().Start()
    except rospy.ROSInterruptException:
        pass