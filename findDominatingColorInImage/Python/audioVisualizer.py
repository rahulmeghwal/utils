# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 01:27:45 2019

@author: Rahul Meghwal
"""

import bpy

rows = 3
columns = 3

def spiral(X, Y):
    scn = bpy.context.scene
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            bpy.ops.mesh.primitive_cube_add(location = (x, y, 1))
            obj = bpy.context.active_object

            scn.cursor_location = obj.location
            scn.cursor_location.z -= 1
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            obj.scale = (0.5, 0.5, 7)

            bpy.ops.object.transform_apply(scale=True)
            bpy.ops.anim.keyframe_insert_menu(type='Scaling')

            action = obj.animation_data.action
            action.fcurves[0].lock = True
            action.fcurves[1].lock = True

            bpy.context.area.type = 'GRAPH_EDITOR'

            step = 20000 / (rows * columns)
            fp = r"C:\Folder\Anotherfolder\Cool song.mp3"
            bpy.ops.graph.sound_bake(filepath=fp, low=i*step, high=i*step+step)
            action.fcurves[2].lock = True

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

spiral(rows, columns)