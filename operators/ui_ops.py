import bpy

from bpy.types import Panel

class NodeCompositorPanel:
        
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Node Automatisation"

    @classmethod
    def poll(cls, context):
        snode = context.space_data
        return snode.tree_type == 'CompositorNodeTree'

class NODE_PT_nodes_creator(NodeCompositorPanel, Panel):

    bl_label = "Create Nodes"


    def draw(self, context):
        na = context.scene.na

        layout = self.layout
        box = layout.box()
        col = box.column()
        col.operator(
            'node.simple_node_setup',
            text="Create node setup",
            icon='NODETREE')
        
        
        col.prop(na, "rlayer_node_bool")
        col.prop(na, "output_node_bool")

        col = layout.column()
        col.prop(na, "viewlayers_enum")
        col.prop(na, "scenes_enum")
        col.operator(
            'node.copy_selected_nodes',
            text="Copy nodes",
            icon='NODE_INSERT_OFF'
        )

    





# Classes to register
classes = [
    NODE_PT_nodes_creator
]