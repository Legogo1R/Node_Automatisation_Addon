import bpy

def create_rlayer_node(node_name, scene):
    rlayer_node = scene.node_tree.nodes.new(type = 'CompositorNodeRLayers')
    rlayer_node.name = node_name + '_RLayer'
    rlayer_node.show_preview = False
    rlayer_node.label = node_name
    rlayer_node.scene = scene
    rlayer_node.layer = node_name
    # rlayer_node.location = get_location_with_offset(node_locations['rlayer_location'], loc_index)
    return rlayer_node

classes = [

]