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
import os
import time
import cozmo
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
                                        CustomObjectMarkers.Circles4, # right
                                        30,30, 30, True)
    
    if (pushpush is not None):
        print("Pushpush defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    bouteille = robot.world.define_custom_cube(CustomObjectTypes.CustomType01,
                                        CustomObjectMarkers.Triangles4, # right
                                        30,30, 30, True)
    
    if (bouteille is not None):
        print("bouteille defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    bread = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                        CustomObjectMarkers.Circles2, # right
                                        30,30, 30, True)
    
    if (bread is not None):
        print("bread defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    
    case = robot.world.define_custom_cube(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles3, # right
                                        30,30, 30, True)
    
    if (case is not None):
        print("case defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    
    laptop = robot.world.define_custom_cube(CustomObjectTypes.CustomType04,
                                        CustomObjectMarkers.Hexagons3, # right
                                        30,30, 30, True)
    
    if (laptop is not None):
        print("case defined successfully!")
    else:
        print("One or more object definitions failed!")
        return
    lookaround(robot)
    
def lookaround(robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=CustomObject, timeout=60)
    lookaround.stop()
    
    for cube in cubes:
        print(cube.object_type)
        if (cube.object_type == CustomObjectTypes.CustomType00):
            pushpush(robot,cube)
            print('Found spray')
        if (cube.object_type == CustomObjectTypes.CustomType01):
            pushpush(robot,cube)
            print('Found bread')
        if (cube.object_type == CustomObjectTypes.CustomType02):
            pushpush(robot,cube)
            print('Found Bread2')
        if (cube.object_type == CustomObjectTypes.CustomType03):
            pushpush(robot,cube)
            print('Found my case')
        if (cube.object_type == CustomObjectTypes.CustomType04):
            pushpush(robot,cube)
            say_something('beepboop')
            print('Beepboop')
    
def pushpush(robot: cozmo.robot.Robot,cubes):
# Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet

    
    save_photo(robot,'Circles','Circles2')

    print("Found object")
    print(cubes.pose)
    robot.say_text("Time to clean").wait_for_completed()
    x1=cubes.pose.position.x-300
    y1=cubes.pose.position.y
    z1=cubes.pose.position.z
    action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
    action.wait_for_completed()
    print("Completed action: result = %s" % action)
    print("Done.")

def BouteilleEau(robot: cozmo.robot.Robot):
# Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet


    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Circle','Circle5')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("I'm Thristy").wait_for_completed()
        x1=cubes[0].pose.position.x-300
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

    
def greeting(robot):
    cleaner = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                        CustomObjectMarkers.Triangles5,
                                        30, 
                                        30, 30, True)
    bottle = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                        CustomObjectMarkers.Circles4,
                                        30, 
                                        30, 30, True)
    print(cleaner)
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    say_something(robot,"Hello")
    print("greeting")
    print(cubes)
    

def find_Bottle(robot):
    print('hi')
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes1 = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    say_something(robot,"I'm Thirsty")
    turn_around(robot,720)
    print("bottls")
    print(cubes1)

def say_something(robot: cozmo.robot.Robot,thingToSay: str):
    print(thingToSay)
    robot.say_text(thingToSay).wait_for_completed()
    #find_face(robot)
    #play_animation(robot,cozmo.anim.Triggers.CodeLabEnergyEat)
    #play_faces(robot,cozmo.faces.FACIAL_EXPRESSION_HAPPY)

    
    
def play_animation(robot,animation):
    print("play_animation started")
    robot.play_anim_trigger(animation).wait_for_completed()
    print("play_animation ended")
    
def turn_around(robot,degree):
    robot.turn_in_place(cozmo.util.Angle(degrees=degree)).wait_for_completed()
    
def play_faces(robot,expression):
    raw_images= [(),]
    faces = []
    img =  Image.open('./photos/Cercles/cercles2/animal.jpg')
    resized = img.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)
    face = cozmo.oled_face.convert_image_to_screen_data(resized, invert_image=True)
    robot.display_oled_face_image(face,2000).wait_for_completed()
    play_animation(robot,cozmo.anim.Triggers.CodeLabEnergyEat)

    play_animation(robot,cozmo.anim.Triggers.CodeLabEnergyEat)

        

def find_face(robot: cozmo.robot.Robot):
    print("find_face started")
    findfaces= robot.start_behavior(cozmo.behavior.BehaviorTypes.FindFaces)    
    face = robot.world.wait_for_observed_face(timeout=None, include_existing=True)
    findfaces.stop()
    
    if face is not None:
        robot.say_text(f"{face.name}").wait_for_completed()
    print("find_face ended")

def show_emotion(robot: cozmo.robot.Robot):
    print("place holder")
    
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
    robot.drive_wheels(-500,-500,l_wheel_acc=999,r_wheel_acc=999,duration=1)
        
    
def unstack(robot:cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()


    cube1 = robot.world.get_light_cube(cozmo.objects.LightCube1Id)
    cube2 = robot.world.get_light_cube(cozmo.objects.LightCube2Id)
    
    
    print(cube1)
    print(cube2)
    robot.pickup_object(cube1, num_retries=3).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.place_object_on_ground_here(cube1)

    while True:
        time.sleep(0.1)

def wheelie(robot: cozmo.robot.Robot):
    print('Start wheelie')
    robot.pop_a_wheelie(robot.world.get_light_cube(1)).wait_for_completed()
    
    robot.drive_wheels(-100,100,l_wheel_acc=999,r_wheel_acc=999,duration=2)
    robot.drive_wheels(100,-100,l_wheel_acc=999,r_wheel_acc=999,duration=2)
    robot.drive_wheels(-100,100,l_wheel_acc=999,r_wheel_acc=999,duration=2)
    robot.drive_wheels(500,500,l_wheel_acc=999,r_wheel_acc=999,duration=.75)
    robot.drive_wheels(-500,-500,l_wheel_acc=999,r_wheel_acc=999,duration=.2)
    print('End wheelie')
    play_faces(robot,cozmo.faces.FACIAL_EXPRESSION_HAPPY)

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
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        global familyDirectory, shapeDirectory
        pilImage.save(f"photos/{familyDirectory}/{shapeDirectory}/photo-{kwargs['image'].image_number}.jpg", "JPEG")

robot = cozmo.robot.Robot
cozmo.run_program(main, use_3d_viewer=True, use_viewer=True)
