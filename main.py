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

import cozmo
from cozmo.util import distance_mm, speed_mmps, degrees

def main(robot: cozmo.robot.Robot):
    say_something(robot,"hello")
    find_face(robot)
    play_animation(robot,cozmo.anim.Triggers.CodeLabEnergyEat)
    #play_faces(robot,cozmo.faces.FACIAL_EXPRESSION_HAPPY)

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
    
def play_faces(robot,expression):
    print("play_faces started")
    robot.play_anim_trigger(expression).wait_for_completed()    
    print("play_faces ended")


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

    if len(cubes) < 2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
    else:
        # Essai de ramasser le 1er cube
        current_action = robot.pickup_object(cubes[0], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        # Maintenant, essai de placer ce cube sur le 2ème.
        current_action = robot.place_on_object(cubes[1], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        print("Cozmo successfully stacked 2 blocks!")
    
def unstack(robot:cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()

    if len(cubes) < 2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
    else:
        robot.pickup_object(cubes[1], num_retries=3).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.place_object_on_ground_here(cubes[1])

    while True:
        time.sleep(0.1)

robot = cozmo.robot.Robot
cozmo.run_program(main)
