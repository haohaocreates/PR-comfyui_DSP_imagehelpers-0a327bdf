from .nodes.concat import ImageConcatNode

# Dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "dsp-imagehelpers-concat": ImageConcatNode,
}

# Dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "dsp-imagehelpers-concat": "DSP Image Concat",
}