from toolkit.wrappers.interface import GenericModelWrapper
from diffusers import StableDiffusionPipeline
import torch

class DiffusionWrapper(GenericModelWrapper):
    def __init__(self, model_config):
        super().__init__(model_config)
        # Additional diffusion-specific initialization if needed
        device = torch.device("cpu") if model_config["diffusion_use_cpu"] else torch.device("cuda")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_config["diffusion_model"],
            torch_dtype=torch.float32,
        )
        self.pipe = self.pipe.to(device)

    def generate(self, prompt):
        image = self.pipe(prompt).images[0]
        image.save("generatedImage.png")
        #image.save(prompt.lower().replace(" ", "_") + ".png")
        return image
