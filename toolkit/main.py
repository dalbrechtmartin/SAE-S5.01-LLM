from toolkit.wrappers.interface import GenericModelWrapper
from toolkit.wrappers.llama_wrapper import LlamaWrapper
from toolkit.wrappers.diffusion_wrapper import DiffusionWrapper
from toolkit.wrappers.musicgen_wrapper import MusicgenWrapper
import yaml
import sys

ALL = "all"
LLAMA = "llama"
DIFFUSION = "diffusion"
MUSICGEN = "musicgen"

def load_model_wrapper(model_type, model_config):
    if model_type == LLAMA:
        return LlamaWrapper(model_config)
    elif model_type == DIFFUSION:
        return DiffusionWrapper(model_config)
    elif model_type == MUSICGEN:
        return MusicgenWrapper(model_config)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

def display_response(response):
    print(f"Response: {response}")

def main():
    models = [LLAMA, DIFFUSION, MUSICGEN]

    if len(sys.argv) < 3:
        print("Usage: python main.py <model_type> <prompt>")
        sys.exit(1)

    model_type = sys.argv[1]
    prompt = sys.argv[2]

    with open('toolkit/config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    if model_type != ALL:
        models = [model_type]

    for model_type in models:
        print(f"=================================================")
        print(f" ")
        print(f"Running prompt \"{prompt}\" on {model_type}...")
        print(f" ")
        print(f"=================================================")
        model_wrapper = load_model_wrapper(model_type, config)
        response = model_wrapper.generate(prompt)
        display_response(response)

if __name__ == "__main__":
    main()
