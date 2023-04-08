import bpy
import utils
from bpy.types import Operator

class NODE_OT_simple_node_setup(Operator):
    "Creates render layer and output nodes"
    bl_idname = "node.simple_node_setup"
    bl_label = "Simple Node Setup"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'
            
    def execute(self, context):
        utils.create_rlayer_node('Huy', context.scene)

        return {'FINISHED'}
