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
    

class NODE_OT_copy_selected_nodes(Operator):
    "Copy selected nodes across viewlayers and scenes, changes names"
    bl_idname = "node.copy_selected_nodes"
    bl_label = "Copy Selected Nodes"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.context.scene.node_tree.nodes.active:
            return True
        return False
    
    def get_scenes(self, context, scenes_enum):
        """
        Get list of Scenes objects depending on scenes_enum Property
        """

        scenes_list = []
        if scenes_enum == 'all_scenes':
            for scene in bpy.data.scenes:
                scenes_list.append(scene)
        elif scenes_enum == 'selected_scenes':
            for scene in bpy.data.scenes:
                if any(scene.name == item.name for item in context.scene.scene_list):
                    scenes_list.append(scene)
        else:
            scenes_list.append(context.scene)

        return scenes_list

    def get_viewlayers(self, context, viewlayers_enum):
        """
        Get list of Viewlayer objects depending on scenes_enum Property
        """

        viewlayers_list = []
        if viewlayers_enum == 'all_viewlayers':
            for viewlayer in context.scene.view_layers:
                viewlayers_list.append(viewlayer)
        elif viewlayers_enum == 'selected_viewlayers':
            for viewlayer in context.scene.view_layers:
                if any(viewlayer.name == item.name for item in context.scene.viewlayer_list):
                    try:
                        viewlayers_list.append(viewlayer)
                    except TypeError:
                        pass
        else:
            viewlayers_list.append(context.view_layer)

        return viewlayers_list
    
    def get_selected_nodes(self, context):
        """
        Return a list of the selected nodes from the active scene
        """

        selected_nodes = []
        for node in context.scene.node_tree.nodes:
            if node.select == True:
                selected_nodes.append(node)
        return selected_nodes
    
    def get_node_attributes(self, node):
        """
        Return a list of all propertie identifiers if they shoulnd't be ignored
        """
        ignore_attributes = ("rna_type", "type", "dimensions", "inputs", "outputs", "internal_links", "select")

        attributes = []
        for attr in node.bl_rna.properties:
            #check if the attribute should be copied and add it to the list of attributes to copy
            if not attr.identifier in ignore_attributes and not attr.identifier.split("_")[0] == "bl":
                attributes.append(attr.identifier)

        return attributes
    
    def copy_attributes(self, attributes, old_prop, new_prop):
        """
        Copie the list of attributes from the old to the new prop if the attribute exists
        """
        for attr in attributes:
            
            if hasattr(new_prop, attr):
                setattr(new_prop, attr, getattr(old_prop, attr))
    
    def copy_selected_nodes(self, selected_nodes, scene, viewlayer):
        """
        Copie all nodes from the given list into scene with their attributes
        """

        #the attributes that should be copied for every link
        input_attributes = ("default_value", "name")
        output_attributes = ("default_value", "name")

        for node in selected_nodes:
            #create a new node in the scene and find and copy its attributes
            new_node = scene.node_tree.nodes.new(node.bl_idname)
            node_attributes = self.get_node_attributes(node)
            self.copy_attributes(node_attributes, node, new_node)

            # copy the attributes for all inputs
            for i, inp in enumerate(node.inputs):
                self.copy_attributes(input_attributes, inp, new_node.inputs[i] )

            # copy the attributes for all outputs
            for i, out in enumerate(node.outputs):
                self.copy_attributes(output_attributes, out, new_node.outputs[i] )

    def copy_links(self, context, selected_nodes, scene):
        """
        Copy all links between the nodes in the list to the nodes in the scene
        """

        for node in selected_nodes:
            #find the corresponding node in the scene
            new_node = scene.node_tree.nodes[node.name]

            #enumerate over every link in the nodes inputs
            for i, inp in enumerate(node.inputs):
                for link in inp.links:
                    #find the connected node for the link in the scene
                    connected_node = scene.node_tree.nodes[link.from_node.name]
                    #connect the scene nodes
                    scene.node_tree.links.new(connected_node.outputs[link.from_socket.name], new_node.inputs[i])
    
    #TESTING#
    def change_viewlayer(self, new_node, viewlayer):
        if new_node.type == 'R_LAYERS':
            new_node.layer = viewlayer.name
    #TESTING#

    def execute(self, context):
        """
        Copy selected nodes across viewlayers and scenes
        Change names and paths in nodes if necessary
        """
        na = context.scene.na

        selected_nodes = self.get_selected_nodes(context)
        scenes_list = self.get_scenes(context, na.scenes_enum)

        for scene in scenes_list:
            viewlayers_list = self.get_viewlayers(context, na.viewlayers_enum)
            for viewlayer in viewlayers_list:
                self.copy_selected_nodes(selected_nodes, scene, viewlayer)
                self.copy_links(context, selected_nodes, scene)

        

                

        return {'FINISHED'}

### OPERATORS FOR UI_LIST ### 

class SCENELIST_OT_DeleteItem(Operator):
    "Delete the selected item from the scene_list"
    bl_idname = "scene_list.delete_item"
    bl_label = "Deletes an item"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.scene.scene_list

    def execute(self, context):
        scene_list = context.scene.scene_list
        index = context.scene.na.scene_list_index

        scene_list.remove(index)
        context.scene.na.scene_list_index = min(max(0, index - 1), len(scene_list) - 1)

        return{'FINISHED'}


class SCENELIST_OT_ReloadItems(Operator):
    "Reloads item list"
    bl_idname = "scene_list.reload_items"
    bl_label = "Reloads item list"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        context.scene.scene_list.clear()
        for scene in bpy.data.scenes:
            item = context.scene.scene_list.add()
            item.name = scene.name
        
        return{'FINISHED'}


class VIEWLAYERLIST_OT_DeleteItem(Operator):
    "Delete the selected item from the list"
    bl_idname = "viewlayer_list.delete_item"
    bl_label = "Deletes an item"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.scene.viewlayer_list

    def execute(self, context):
        viewlayer_list = context.scene.viewlayer_list
        index = context.scene.na.scene_list_index

        viewlayer_list.remove(index)
        context.scene.na.scene_list_index = min(max(0, index - 1), len(viewlayer_list) - 1)

        return{'FINISHED'}


class VIEWLAYERLIST_OT_ReloadItems(Operator):
    "Reloads item list"
    bl_idname = "viewlayer_list.reload_items"
    bl_label = "Reloads item list"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        context.scene.viewlayer_list.clear()
        for viewlayer in context.scene.view_layers:
            item = context.scene.viewlayer_list.add()
            item.name = viewlayer.name
        
        return{'FINISHED'}


# Classes to register
classes = [
    NODE_OT_simple_node_setup,
    NODE_OT_copy_selected_nodes,
    SCENELIST_OT_DeleteItem,
    SCENELIST_OT_ReloadItems,
    VIEWLAYERLIST_OT_DeleteItem,
    VIEWLAYERLIST_OT_ReloadItems,
]