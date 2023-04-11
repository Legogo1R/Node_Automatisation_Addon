import bpy

def get_scenes(scenes_enum):
    """
    Get list of Scenes objects depending on scenes_enum Property
    """

    scenes_list = []
    if scenes_enum == 'all_scenes':
        for scene in bpy.data.scenes:
            scenes_list.append(scene)
    else:
        pass

    return scenes_list

def get_viewlayers(scene, viewlayers_enum):
    """
    Get list of Viewlayer objects depending on scenes_enum Property
    """

    viewlayers_list = []
    if viewlayers_enum == 'all_viewlayers':
        for viewlayer in scene.view_layers:
            viewlayers_list.append(viewlayer)
    elif viewlayers_enum == 'selected_viewlayers':
        pass
    else:
        viewlayers_list.append(bpy.context.view_layer)

    return viewlayers_list

def create_rlayer_node(node_name, scene):
    """
    Create Render Layer node
    """

    rlayer_node = scene.node_tree.nodes.new(type = 'CompositorNodeRLayers')
    rlayer_node.name = node_name + '_RLayerNode'
    rlayer_node.show_preview = False
    rlayer_node.label = node_name
    rlayer_node.scene = scene
    rlayer_node.layer = node_name
    # rlayer_node.location = get_location_with_offset(node_locations['rlayer_location'], loc_index)
    return rlayer_node

def create_output_node(node_name, scene, output_path):
    """
    Create File Output node
    """

    output_node = scene.node_tree.nodes.new(type = 'CompositorNodeOutputFile')
    output_node.name = node_name + '_FOutputNode'
    output_node.file_slots.remove(output_node.inputs[0])
    output_node.base_path = '//Renders\\' + output_path + '\\'
    output_node.format.file_format = 'PNG'
    output_node.format.color_mode = 'RGB'
    output_node.format.color_depth = '8'
    output_node.format.compression = 50
    # output_node.location = get_location_with_offset(node_locations['output_location'], index)
    return output_node






# Classes to register
classes = [

]