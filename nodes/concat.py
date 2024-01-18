import torch

class ImageConcatNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image1": ("IMAGE",),
                "image2": ("IMAGE",),
                "axis": (["horizontal", "vertical"],)
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "concatenate_images"
    OUTPUT_NODE = False
    CATEGORY = "Image Processing"

    def concatenate_images(self, image1, image2, axis):
        axis_value = 1 if axis == "vertical" else 2  # Adjusted axis_value
        concatenated_image = torch.cat([image1, image2], dim=axis_value)
        return (concatenated_image,)