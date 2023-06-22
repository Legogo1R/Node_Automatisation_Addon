import bpy

from bpy.types import Panel, UIList


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


class SCENES_UL_List(UIList):
    
    def draw_item(
            self, context, layout, data, item,
            icon, active_data, active_propname):
        
        scene_icon = 'SCENE_DATA'

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name,icon=scene_icon)
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon=scene_icon)


class VIEWLAYERS_UL_List(UIList):
    
    def draw_item(
            self, context, layout, data, item,
            icon, active_data, active_propname):
        
        scene = data
        viewlayer = item
        vl_icon = 'RENDERLAYERS'

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name,icon=vl_icon)
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon=vl_icon)            
            

class NODE_PT_custom_selection(NodeCompositorPanel, Panel):

    bl_label = "Select Scenes/Viewlayers"


    def draw(self, context):
        na = context.scene.na
        layout = self.layout

        ### SCENES UI_List ###
        row = layout.row()
        row.template_list("SCENES_UL_List", "Scene_List", context.scene,
                          "scene_list", na, "scene_list_index")
        
        col = row.column(align=True)
        col.operator(
            'scene_list.delete_item',
            text='',
            icon='REMOVE'
            )
        col.operator(
            'scene_list.reload_items',
            text='',
            icon='FILE_REFRESH'
            )

        ### VIEWLAYERS UI_List ###
        row = layout.row()
        row.template_list("VIEWLAYERS_UL_List", "The_List", context.scene,
                          "viewlayer_list", na, "viewlayer_list_index")
        
        col = row.column(align=True)
        col.operator(
            'viewlayer_list.delete_item',
            text='',
            icon='REMOVE'
            )
        col.operator(
            'viewlayer_list.reload_items',
            text='',
            icon='FILE_REFRESH'
            )






# Classes to register
classes = [
    NODE_PT_nodes_creator,
    NODE_PT_custom_selection,
    SCENES_UL_List,
    VIEWLAYERS_UL_List,
]