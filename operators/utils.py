import bpy

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