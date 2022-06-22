#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Hello World

Make Cozmo say 'Hello World' in this simple Cozmo SDK example program.
'''

from ctypes import resize
from itertools import count
from lib2to3.refactor import MultiprocessingUnsupported
import os
import time
import cozmo
import asyncio
from cozmo.util import distance_mm, speed_mmps, degrees, Pose
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject
from PIL import Image

liveCamera = False

def main(robot: cozmo.robot.Robot):
     buildObjects(robot)
    # customObject(robot)
    # pushpush(robot)
    # BouteilleEau(robot)
    # greeting(robot)
    # find_Bottle(robot)
    # wheelie(robot)
    # find_face(robot)
    # stack(robot)
    # unstack(robot)
    
def buildObjects(robot):
    pushpush = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
                                        CustomObjectMarkers.Triangles4, # right
                                        30,30, 30, True)
    
    if (pushpush is not None):
        print("Pushpush defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    bouteille = robot.world.define_custom_cube(CustomObjectTypes.CustomType01,
                                        CustomObjectMarkers.Diamonds2, # right
                                        30,30, 30, True)
    
    if (bouteille is not None):
        print("bouteille defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    montre = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                        CustomObjectMarkers.Circles4, # right
                                        30,30, 30, True)
    
    if (montre is not None):
        print("montre defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    
    
    papier = robot.world.define_custom_cube(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles2, # right
                                        30,30, 30, True)
    
    if (papier is not None):
        print("papier defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    lookaround(robot)
    
def lookaround(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=4, object_type=CustomObject, timeout=60)
    lookaround.stop()
    
    print(len(cubes))
    for cube in cubes:
        print(cube.object_type)
        if (cube.object_type == CustomObjectTypes.CustomType00):
            pushpush(robot,cube)
            say_something(robot,'Spray')
            print('Found spray')
        if (cube.object_type == CustomObjectTypes.CustomType01):
            bouteille(robot,cube)
            say_something(robot,'Water')
            print('Found bread')
        if (cube.object_type == CustomObjectTypes.CustomType02):
            montre(robot,cube)
            say_something(robot,'Watch')
            print('Found Bread2')
        if (cube.object_type == CustomObjectTypes.CustomType03):
            papier(robot,cube)
            say_something(robot,'Paper')
            print('Found my case')
    
    robot.turn_in_place(degrees(45)).wait_for_completed()
    find_face(robot)
    wheelie(robot)
    find_face(robot)
    stack(robot)
    find_face(robot)
    unstack(robot)
    
    
def pushpush(robot: cozmo.robot.Robot,cubes):
# Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    print(cubes.pose)
    robot.say_text("Time to clean").wait_for_completed()
    x1=cubes.pose.position.x-200
    y1=cubes.pose.position.y
    z1=cubes.pose.position.z
    action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
    action.wait_for_completed()
    save_photo(robot,'Triangles','Triangle4')
    print("Completed action: result = %s" % action)
    print("Done.")

def say_something(robot, text):
    robot.say_text(text).wait_for_completed()

    
def bouteille(robot: cozmo.robot.Robot,cubes):
# Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet

    

    print(cubes.pose)
    robot.say_text("I'm Thristy").wait_for_completed()
    x1=cubes.pose.position.x+200
    y1=cubes.pose.position.y
    z1=cubes.pose.position.z
    action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(180)),relative_to_robot=False)
    action.wait_for_completed()
    save_photo(robot,'Diamond','Diamond2')
    print("Completed action: result = %s" % action)
    print("Done.")

def montre(robot: cozmo.robot.Robot,cubes):
    #  Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet

    

    print(cubes.pose)
    robot.say_text("What Time is it").wait_for_completed()
    x1=cubes.pose.position.x+200
    y1=cubes.pose.position.y
    z1=cubes.pose.position.z
    action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(180)),relative_to_robot=False)
    action.wait_for_completed()
    save_photo(robot,'Circles','Circles4')
    play_faces(robot,'clock')
    print("Completed action: result = %s" % action)
    print("Done.")   
    
def papier(robot: cozmo.robot.Robot,cubes):
# Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet

    

    print(cubes.pose)
    robot.say_text("Looking for paper").wait_for_completed()
    x1=cubes.pose.position.x-200
    y1=cubes.pose.position.y
    z1=cubes.pose.position.z
    action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
    action.wait_for_completed()
    save_photo(robot,'Circles','Circles2')
    print("Completed action: result = %s" % action)
    print("Done.")
    
def play_animation(robot,animation):
    print("play_animation started")
    robot.play_anim_trigger(animation).wait_for_completed()
    print("play_animation ended")
    
    
def play_faces(robot,letter):
    raw_images= [(),]
    faces = []
    img =  Image.open('./photos/display/'+ letter +'.jpg')
    resized = img.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)
    face = cozmo.oled_face.convert_image_to_screen_data(resized, invert_image=True)
    robot.display_oled_face_image(face,2000).wait_for_completed()

        

def find_face(robot: cozmo.robot.Robot):
    print("find_face started")
    findfaces= robot.start_behavior(cozmo.behavior.BehaviorTypes.FindFaces)    
    face = robot.world.wait_for_observed_face(timeout=None, include_existing=True)
    findfaces.stop()
    
    if face is not None:
        robot.say_text(f"{face.name}").wait_for_completed()
        if face.name == "Stephano":
            save_photo(robot,"Faces","Stephano")
            play_faces(robot,"s")
        elif face.name == "raja":
            save_photo(robot,"Faces","Raja")
            play_faces(robot,"r")
        elif face.name == "Alex":
            save_photo(robot,"Faces","Alex")
            play_faces(robot,"a")
        else:
            save_photo(robot,"Faces","Unknown")
            play_faces(robot,"question")
    
    print("find_face ended")

    
def stack(robot: cozmo.robot.Robot):
    # Essai d'émpiler 2 cubes

    # Regarde autour de soi, jusqu'à ce que Cozmo sache où sont au moins 2 cubes :
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    
    cube1 = robot.world.get_light_cube(cozmo.objects.LightCube1Id)
    cube2 = robot.world.get_light_cube(cozmo.objects.LightCube2Id)

   
    # Essai de ramasser le 1er cube
    current_action = robot.pickup_object(cube1, num_retries=3)
    current_action.wait_for_completed()
    if current_action.has_failed:
        code, reason = current_action.failure_reason
        result = current_action.result
        print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
        return

    # Maintenant, essai de placer ce cube sur le 2ème.
    current_action = robot.place_on_object(cube2, num_retries=3)
    current_action.wait_for_completed()
    if current_action.has_failed:
        code, reason = current_action.failure_reason
        result = current_action.result
        print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
        return

    print("Cozmo successfully stacked 2 blocks!")
    robot.drive_wheels(-300,-300,l_wheel_acc=999,r_wheel_acc=999,duration=1)
        
    
def unstack(robot:cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()


    cube1 = robot.world.get_light_cube(cozmo.objects.LightCube1Id)
    cube2 = robot.world.get_light_cube(cozmo.objects.LightCube2Id)
    
    
    robot.pickup_object(cube1, num_retries=3).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.place_object_on_ground_here(cube1).wait_for_completed()

    dock(robot)
    while True:
        time.sleep(0.1)

def dock(robot : cozmo.robot.Robot):
    print('go to charger')
    # try to find the charger
    charger = None
    # see if Cozmo already knows where the charger is
    if robot.world.charger:
        if robot.world.charger.pose.is_comparable(robot.pose):
            print("Cozmo already knows where the charger is!")
            charger = robot.world.charger
        else:
            # Cozmo knows about the charger, but the pose is not based on the
            # same origin as the robot (e.g. the robot was moved since seeing
            # the charger) so try to look for the charger first
            pass

    if not charger:
        # Tell Cozmo to look around for the charger
        look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        try:
            charger = robot.world.wait_for_observed_charger(timeout=30)
            print("Found charger: %s" % charger)
        except asyncio.TimeoutError:
            print("Didn't see the charger")
        finally:
            # whether we find it or not, we want to stop the behavior
            look_around.stop()

    if charger:
        # Attempt to drive near to the charger, and then stop.
        action = robot.go_to_object(charger, distance_mm(65.0))
        action.wait_for_completed()
        save_photo(robot,"Charger","Charger dock")
        print("Completed action: result = %s" % action)
        print("Done.")     
        

def wheelie(robot: cozmo.robot.Robot):
    print('Start wheelie')
    save_photo(robot, "Cube","Cube1")
    robot.pop_a_wheelie(robot.world.get_light_cube(1)).wait_for_completed()
    
    robot.drive_wheels(-150,-150,l_wheel_acc=999,r_wheel_acc=999,duration=3)
    robot.drive_wheels(500,500,l_wheel_acc=999,r_wheel_acc=999,duration=.75)
    robot.drive_wheels(100,100,l_wheel_acc=999,r_wheel_acc=999,duration=.2)
    print('End wheelie')

def save_photo(robot: cozmo.robot.Robot, shapeFamily, shapeId):
    # Chaque fois que Cozmo voit une "nouvelle" image, prends une photo
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)
    
    # Indiquer le dossier pour stocker les photos
    global familyDirectory, shapeDirectory
    familyDirectory = f"{shapeFamily}"
    shapeDirectory = f"{shapeId}"
    if not os.path.exists('Photos'):
        os.makedirs('Photos')
    if not os.path.exists(f'Photos/{familyDirectory}'):
        os.makedirs(f'Photos/{familyDirectory}')
    if not os.path.exists(f'Photos/{familyDirectory}/{shapeDirectory}'):
        os.makedirs(f'Photos/{familyDirectory}/{shapeDirectory}')

    take_photo(robot)

def take_photo(robot: cozmo.robot.Robot):
    global liveCamera    
    
    # Assurez-vous que la tête et le bras de Cozmo sont à un niveau raisonnable
    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()
        
    liveCamera = True
    time.sleep(0.1)    
    liveCamera = False   

def on_new_camera_image(evt, **kwargs):    
    global liveCamera
    if liveCamera:
        print("cheese ! ;)")
        pilImage = kwargs['image'].raw_image
        global familyDirectory, shapeDirectory
        pilImage.save(f"photos/{familyDirectory}/{shapeDirectory}/photo-{kwargs['image'].image_number}.jpg", "JPEG")

robot = cozmo.robot.Robot
cozmo.run_program(main, use_3d_viewer=True, use_viewer=True)
