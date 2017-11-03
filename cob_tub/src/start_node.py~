#!/usr/bin/python

import rospy

from simple_script_server import script

import tf
from geometry_msgs.msg import *
from moveit_msgs.srv import *

class MyScript(script):
    def Initialize(self):
        # Initialize the component
        rospy.loginfo("Initializing all components...")
        
        components_to_init = ['tray', 'torso', 'arm', 'base', "gripper"]
        
        for component in components_to_init:
            self.sss.init(component)
                    
        
        self.istener = tf.TransformListener(True, rospy.Duration(10.0))
        
        handle_torso = self.sss.move("torso","home",False)
        # prepare for grasping
        handle_arm = self.sss.move("arm","pregrasp")
        handle_gripper = self.sss.move("gripper","cylopen", False) #true
        
        handle_arm.wait()
        handle_torso.wait()
        handle_gripper.wait()
        
        #print "Please press ENTER to move the COB near to the object"
        #self.sss.wait_for_input()
        
       

    def Run(self):
        rospy.loginfo("Running script...")
       
        #listener = tf.TransformListener(True, rospy.Duration(10.0))
        #rospy.sleep(2)
        
        goLocation = self.getLocation()  
        print "------location: ", goLocation
        
        moveBase = self.sss.move("base", [goLocation[0],goLocation[1], 0.00], False, "omni")
        moveBase.wait()      
        
       
               
        #handle_gripper = self.sss.move("gripper","cylopen", False)
    
       
        ####
                      
        # check list$ rosparam list | grep script_server
        #self.sss.move("arm","folded",false)
        #self.sss.move("tray","down")
        #self.sss.move("torso","front_left_extreme")
        #-self.sss.move("base", [-2.116, 0.089, 0.000], False, "omni")
        #self.sss.move("base", [0.0, 0.0, 0.000], False, "omni")
        #self.sss.move_base_rel("base",[-1.0, 0.0, 0.000]) #0, 0, 1.57
        
        # go to position for grasping
        #moveBase = self.sss.move("base", [-2.116, 0.0, 0.000], False, "omni")
        #moveBase = self.sss.move("base", [-2.221, 0.115, 0.000], False, "omni")
        #moveBase = self.sss.move("base", [0.0, 0.0, 0.000], False, "omni")
        #moveBase.wait()
        
        #self.sss.say("sound", ["Searching for milk"])
    

        #handle01 = self.sss.move("arm","grasp-to-tray",False)
        #self.sss.move("tray","up")
        #handle01.wait()
        #self.sss.move("arm","tray")
        #self.sss.move("gripper","cylopen")
        #handle01 = self.sss.move("arm","tray-to-folded",False)
        #self.sss.sleep(4)
        #self.sss.move("gripper","cylclosed",False)
        #handle01.wait()

        # deliver cup to order position
        
        #self.sss.say("sound", ["Here is your drink."])
        #self.sss.move("torso","nod")
        
        # grasp the object
        #self.sss.move("arm","grasp")
        #self.sss.move("gripper","cylclosed", True)
        
        # put object on tray
        #handle_arm = self.sss.move("arm","grasp-to-tablet",False)
        #self.sss.move("tray","up")
        #handle_arm.wait()
        #self.sss.move("gripper","cylopen")
        
        #detect object
        
        #self.sss.detect('milk')
        #milk_box = PoseStamped()
        #milk_box = self.sss.get_object_pose('milk')
        
        #print "object position %s"%self.sss.get_object_pose('milk')
       
       
    def getLocation(self):
        location = raw_input("Please enter the Location: (example: table OR -2.221, 0.115): ")
        
        locationArray = location.split(',')
        print "--len--: ",len(locationArray)
        
        if(len(locationArray)==1):
            if(locationArray[0] == "table"):
                print "Location is found"
                locationArray = [-2.221, 0.115]
                print "return 1: ",locationArray
                return locationArray     
                
            else:
                print "Location is not found... Try Again!!!"
                del locationArray[:]
                self.getLocation()
        
        elif(len(locationArray)==2):
            print "return 2: ",locationArray
            return locationArray
            
        else:
            print "Wrong Input...Try Again!!!"
            del locationArray[:]
            self.getLocation()
               
                 
     
    
if __name__ == '__main__':
    try:
        print "hello World - cob move"
        MyScript().Start()
        #SCRIPT = MyScript()
        #SCRIPT.Start()
        
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
