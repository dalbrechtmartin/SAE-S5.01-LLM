"""
@file diffusion_wrapper.py
@brief Contains the DiffusionWrapper class, a wrapper for the StableDiffusionPipeline.

@author Your Name
"""

from toolkit.wrappers.interface import GenericModelWrapper
from diffusers import StableDiffusionPipeline
import torch

class DiffusionWrapper(GenericModelWrapper):
    """
    @brief A wrapper class for using the StableDiffusionPipeline with the GenericModelWrapper interface.
    """

    def __init__(self, model_config):
        """
        @brief Initializes the DiffusionWrapper.

        @param model_config A dictionary containing configuration parameters for the model.
        """
        super().__init__(model_config)
        # Additional diffusion-specific initialization if needed
        device = torch.device("cpu")
        
        # @code
        # Create a StableDiffusionPipeline instance from the pretrained model specified in the configuration.
        # Set the torch data type to float32 and move the pipeline to the specified device (CPU in this case).
        # @endcode
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_config["diffusion_model"],
            torch_dtype=torch.float32,
        )
        self.pipe = self.pipe.to(device)

    def generate(self, prompt):
        """
        @brief Generates an image using the StableDiffusionPipeline based on the given prompt.

        @param prompt The input prompt for image generation.

        @return The generated image.
        """
        # @code
        # Generate an image using the StableDiffusionPipeline and save it to a file named "test.png".
        # Optionally, you can uncomment the line below to save the image with a filename based on the prompt.
        # @endcode
        image = self.pipe(prompt).images[0]
        image.save("test.png")
        # image.save(prompt.lower().replace(" ", "_") + ".png")
        return image
