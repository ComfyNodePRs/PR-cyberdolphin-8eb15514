from .cyberdolphin_gradio import CyberDolphinGradioApi
from .cyberdolphin_openai_advanced import CyberdolphinOpenAIAdvanced
from .cyberdolphin_openai_simple import CyberdolphinOpenAISimple
from .cyberdolphin_openai_compatible import CyberdolphinOpenAICompatible
from .cyberdolphin_imageneering import CyberDolphinImageneering

NODE_CLASS_MAPPINGS = {
    "🐬 Gradio ChatInterface": CyberDolphinGradioApi,
    "🐬 OpenAI Simple": CyberdolphinOpenAISimple,
    "🐬 OpenAI Advanced": CyberdolphinOpenAIAdvanced,
    "🐬 OpenAI Compatible": CyberdolphinOpenAICompatible,
    "🐬 OpenAI DALL·E": CyberDolphinImageneering,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CyberDolphin Gradio": "🐬 CyberDolphin Gradio",
    "CyberDolphin GPT-3.5 (Simple)": "🐬 CyberDolphin GPT-3.5 (Simple)",
    "CyberDolphin OpenAI (Advanced)": "🐬 CyberDolphin OpenAI (Advanced)",
    "CyberDolphin OpenAI Compatible": "🐬 CyberDolphin OpenAI Compatible",
    "CyberDolphin OpenAI DALL·E": "🐬 CyberDolphin OpenAI DALL·E",
}
