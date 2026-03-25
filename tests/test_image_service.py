import unittest
from types import SimpleNamespace

from app.services.grok.services.image import ImageGenerationService


class ImageGenerationServiceTests(unittest.TestCase):
    def test_app_chat_mode_drops_fast_mode_for_image_generation(self):
        model_info = SimpleNamespace(model_mode="MODEL_MODE_FAST")

        self.assertIsNone(ImageGenerationService._app_chat_mode(model_info))

    def test_app_chat_mode_preserves_other_modes(self):
        model_info = SimpleNamespace(model_mode="MODEL_MODE_AUTO")

        self.assertEqual(
            ImageGenerationService._app_chat_mode(model_info),
            "MODEL_MODE_AUTO",
        )


if __name__ == "__main__":
    unittest.main()
