import bpy

from bpy.types import Operator
from .utils import create_rlayer_node

class NODE_OT_simple_node_setup(Operator):
    "Creates render layer and output nodes"
    bl_idname = "node.simple_node_setup"
    bl_label = "Simple Node Setup"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'
            
    def execute(self, context):
        create_rlayer_node(context.view_layer.name, context.scene)

        return {'FINISHED'}

classes = [
    NODE_OT_simple_node_setup
]