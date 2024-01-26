from toolkit.wrappers.interface import GenericModelWrapper
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy

class MusicgenWrapper(GenericModelWrapper):
    """
    @brief Wrapper class for interacting with a Musicgen model using the toolkit.

    This class extends GenericModelWrapper and provides Musicgen-specific functionality.
    """

    def __init__(self, model_config):
        """
        @brief Constructor for MusicgenWrapper.

        @param model_config A dictionary containing configuration parameters for the model.
        """
        super().__init__(model_config)

        # Additional musicgen-specific initialization if needed
        self.processor = AutoProcessor.from_pretrained(model_config["musicgen_model"])
        self.model = MusicgenForConditionalGeneration.from_pretrained(model_config["musicgen_model"])
        self.model_config = model_config



    def generate(self, prompt):
        """
        @brief Generate music based on the given prompt.

        This function takes a text prompt as input and generates music using the Musicgen model.

        @param prompt The input prompt for generating music.
        """
        # Process the prompt using the model's processor
        inputs = self.processor(
            text=prompt,
            padding=self.model_config["musicgen_padding"],
            return_tensors=self.model_config["musicgen_return_tensors"],
        )

        audio_values = self.model.generate(**inputs, max_new_tokens=self.model_config["musicgen_max_new_tokens"])

        # Get the sampling rate from the model's configuration
        sampling_rate = self.model.config.audio_encoder.sampling_rate

        # Write the generated audio to a WAV file
        scipy.io.wavfile.write("musicgen_out.wav", rate=sampling_rate, data=audio_values[0, 0].numpy())
