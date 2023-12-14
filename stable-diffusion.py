from diffusers import StableDiffusionPipeline
import torch
import sys

def main():
    if len(sys.argv) == 1:
        print("Utilisation: " + sys.argv[0] + " <prompt>")
    else:
        prompt = sys.argv[1]
        device = torch.device("cpu")

        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
        pipe = pipe.to(device)
        print("Génération de l'image en cours...")

        image = pipe(prompt).images[0]

        image.save(prompt.lower().replace(" ", "_") + ".png")

if __name__ == "__main__":
    main()
