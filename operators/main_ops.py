import bpy

from bpy.types import Operator
from . import utils


class NODE_OT_simple_node_setup(Operator):
    "Creates simple node setup"
    bl_idname = "node.simple_node_setup"
    bl_label = "Simple Node Setup"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'
    
    def execute(self, context):
        """
        Creates Simple node setup with selected Properties
        """
        na = context.scene.na
       
        if na.rlayer_node_bool == True:
            utils.create_rlayer_node(context.view_layer.name,context.scene)
        if na.output_node_bool == True:
            utils.create_output_node(context.view_layer.name,context.scene,context.scene.name)
        return {'FINISHED'}
    

class NODE_OT_create_selected_nodes(Operator):
    "Copy selected nodes across viewlayers and scenes, changes names"
    bl_idname = "node.copy_selected_nodes"
    bl_label = "Copy Selected Nodes"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'
    
    def execute(self, context):
        """
        Copy selected nodes across viewlayers and scenes
        Change names and paths in nodes if necessary
        """
        na = context.scene.na

        scenes_list = utils.get_scenes(na.scenes_enum)
        viewlayers_list = utils.get_viewlayers(na.viewlayers_enum)

        for scene in scenes_list:
            for view_layer in viewlayers_list:
                pass


        return {'FINISHED'}


# Classes to register
classes = [
    NODE_OT_simple_node_setup,
    NODE_OT_create_selected_nodes
]