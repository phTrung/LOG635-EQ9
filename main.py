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
import time
import cozmo
from cozmo.util import distance_mm, speed_mmps, degrees
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject
from PIL import Image


def main(robot: cozmo.robot.Robot):
    
    # say_something(robot,"hello")
    greeting(robot)
    # find_face(robot)
    # play_animation(robot,cozmo.anim.Triggers.CodeLabEnergyEat)
    # turn_around(robot,720)
    # play_faces(robot,cozmo.faces.FACIAL_EXPRESSION_HAPPY)
    # wheelie(robot)
    # stack(robot)
    # unstack(robot)
    find_Bottle(robot)
    
def greeting(robot):
    
    cleaner = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                        CustomObjectMarkers.Triangles5,
                                        30, 
                                        30, 30, True)
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    say_something(robot,"Hello")


def find_Bottle(robot):
    bottle = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                        CustomObjectMarkers.Circles4,
                                        30, 
                                        30, 30, True)
    print('hi')
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes1 = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    say_something(robot,"I'm Thirsty")
    # print(cubes[0])

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

robot = cozmo.robot.Robot
cozmo.run_program(main, use_3d_viewer=True, use_viewer=True)
