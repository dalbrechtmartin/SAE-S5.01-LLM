from toolkit.wrappers.interface import GenericModelWrapper
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy

class MusicgenWrapper(GenericModelWrapper):
    def __init__(self, model_config):
        super().__init__(model_config)
        # Additional musicgen-specific initialization if needed
        self.processor = AutoProcessor.from_pretrained(model_config["musicgen_model"])
        self.model = MusicgenForConditionalGeneration.from_pretrained(model_config["musicgen_model"])
        self.model_config = model_config



    def generate(self, prompt):
        inputs = self.processor(
            text=prompt,
            padding=self.model_config["musicgen_padding"],
            return_tensors=self.model_config["musicgen_return_tensors"],
        )

        audio_values = self.model.generate(**inputs, max_new_tokens=self.model_config["musicgen_max_new_tokens"])

        sampling_rate = self.model.config.audio_encoder.sampling_rate
        scipy.io.wavfile.write("musicgen_out.wav", rate=sampling_rate, data=audio_values[0, 0].numpy())
