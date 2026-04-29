# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Make Idle Anim
# 
# Description:  Makes a one frame Idle animation from the current frame:
#               Takes the selected skeleton and copies its animation at the 
#               current frame to the frames 0:1and sets the frame range to 0:1 
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

import maya.cmds as cmds

def get_full_joint_hierarchy(start_joints):
    """Return full descendant joint hierarchy from selection."""
    all_joints = set()

    for j in start_joints:
        descendants = cmds.listRelatives(j, ad=True, type='joint') or []
        all_joints.add(j)
        all_joints.update(descendants)

    return list(all_joints)


def copy_current_frame_to_idle_clip():
    sel = cmds.ls(selection=True, type='joint')

    if not sel:
        cmds.error("Select at least one joint from the skeleton.")
        return

    # Expand to full hierarchy
    joints = get_full_joint_hierarchy(sel)

    current_time = cmds.currentTime(query=True)

    attrs = ["translateX","translateY","translateZ",
             "rotateX","rotateY","rotateZ",
             "scaleX","scaleY","scaleZ"]

    # Store current pose
    pose_data = {}

    for j in joints:
        pose_data[j] = {}
        for a in attrs:
            plug = f"{j}.{a}"
            if cmds.objExists(plug):
                pose_data[j][a] = cmds.getAttr(plug)

    # Remove all animation on full skeleton
    cmds.cutKey(joints, clear=True)

    # Apply to frames 0 and 1
    for t in [0, 1]:
        cmds.currentTime(t)

        for j in joints:
            for a, value in pose_data[j].items():
                plug = f"{j}.{a}"
                cmds.setKeyframe(plug, value=value, time=t)

    # Set playback range
    cmds.playbackOptions(min=0, max=1)
    cmds.playbackOptions(animationStartTime=0, animationEndTime=1)

    cmds.currentTime(0)

    print("Done: skeleton converted to idle 0–1 clip.")

# Run
copy_current_frame_to_idle_clip()
import maya.cmds as cmds

def get_full_joint_hierarchy(start_joints):
    """Return full descendant joint hierarchy from selection."""
    all_joints = set()

    for j in start_joints:
        descendants = cmds.listRelatives(j, ad=True, type='joint') or []
        all_joints.add(j)
        all_joints.update(descendants)

    return list(all_joints)


def copy_current_frame_to_idle_clip():
    sel = cmds.ls(selection=True, type='joint')

    if not sel:
        cmds.error("Select at least one joint from the skeleton.")
        return

    # Expand to full hierarchy
    joints = get_full_joint_hierarchy(sel)

    current_time = cmds.currentTime(query=True)

    attrs = ["translateX","translateY","translateZ",
             "rotateX","rotateY","rotateZ",
             "scaleX","scaleY","scaleZ"]

    # Store current pose
    pose_data = {}

    for j in joints:
        pose_data[j] = {}
        for a in attrs:
            plug = f"{j}.{a}"
            if cmds.objExists(plug):
                pose_data[j][a] = cmds.getAttr(plug)

    # Remove all animation on full skeleton
    cmds.cutKey(joints, clear=True)

    # Apply to frames 0 and 1
    for t in [0, 1]:
        cmds.currentTime(t)

        for j in joints:
            for a, value in pose_data[j].items():
                plug = f"{j}.{a}"
                cmds.setKeyframe(plug, value=value, time=t)

    # Set playback range
    cmds.playbackOptions(min=0, max=1)
    cmds.playbackOptions(animationStartTime=0, animationEndTime=1)

    cmds.currentTime(0)

    print("Done: skeleton converted to idle 0–1 clip.")

# Run
copy_current_frame_to_idle_clip()
