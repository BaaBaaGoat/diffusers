from typing import TYPE_CHECKING

from ..utils import (
    DIFFUSERS_SLOW_IMPORT,
    OptionalDependencyNotAvailable,
    _LazyModule,
    get_objects_from_module,
    is_flax_available,
    is_k_diffusion_available,
    is_librosa_available,
    is_note_seq_available,
    is_onnx_available,
    is_torch_available,
    is_transformers_available,
)


# These modules contain pipelines from multiple libraries/frameworks
_dummy_objects = {}
_import_structure = {
    "controlnet": [],
    "controlnet_xs": [],
    "deprecated": [],
    "latent_diffusion": [],
    "stable_diffusion": [],
    "stable_diffusion_xl": [],
}

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_pt_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_pt_objects))
else:
    _import_structure["auto_pipeline"] = [
        "AutoPipelineForImage2Image",
        "AutoPipelineForInpainting",
        "AutoPipelineForText2Image",
    ]
    _import_structure["consistency_models"] = ["ConsistencyModelPipeline"]
    _import_structure["dance_diffusion"] = ["DanceDiffusionPipeline"]
    _import_structure["ddim"] = ["DDIMPipeline"]
    _import_structure["ddpm"] = ["DDPMPipeline"]
    _import_structure["dit"] = ["DiTPipeline"]
    _import_structure["latent_diffusion"].extend(["LDMSuperResolutionPipeline"])
    _import_structure["pipeline_utils"] = [
        "AudioPipelineOutput",
        "DiffusionPipeline",
        "ImagePipelineOutput",
    ]
    _import_structure["deprecated"].extend(
        [
            "PNDMPipeline",
            "LDMPipeline",
            "RePaintPipeline",
            "ScoreSdeVePipeline",
            "KarrasVePipeline",
        ]
    )
try:
    if not (is_torch_available() and is_librosa_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_torch_and_librosa_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_torch_and_librosa_objects))
else:
    _import_structure["deprecated"].extend(["AudioDiffusionPipeline", "Mel"])

try:
    if not (is_transformers_available() and is_torch_available() and is_note_seq_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_transformers_and_torch_and_note_seq_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_transformers_and_torch_and_note_seq_objects))
else:
    _import_structure["deprecated"].extend(
        [
            "MidiProcessor",
            "SpectrogramDiffusionPipeline",
        ]
    )

try:
    if not (is_torch_available() and is_transformers_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_torch_and_transformers_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_torch_and_transformers_objects))
else:
    _import_structure["deprecated"].extend(
        [
            "VQDiffusionPipeline",
            "AltDiffusionPipeline",
            "AltDiffusionImg2ImgPipeline",
            "CycleDiffusionPipeline",
            "StableDiffusionInpaintPipelineLegacy",
            "StableDiffusionPix2PixZeroPipeline",
            "StableDiffusionParadigmsPipeline",
            "StableDiffusionModelEditingPipeline",
            "VersatileDiffusionDualGuidedPipeline",
            "VersatileDiffusionImageVariationPipeline",
            "VersatileDiffusionPipeline",
            "VersatileDiffusionTextToImagePipeline",
        ]
    )
    _import_structure["animatediff"] = ["AnimateDiffPipeline"]
    _import_structure["audioldm"] = ["AudioLDMPipeline"]
    _import_structure["audioldm2"] = [
        "AudioLDM2Pipeline",
        "AudioLDM2ProjectionModel",
        "AudioLDM2UNet2DConditionModel",
    ]
    _import_structure["blip_diffusion"] = ["BlipDiffusionPipeline"]
    _import_structure["controlnet"].extend(
        [
            "BlipDiffusionControlNetPipeline",
            "StableDiffusionControlNetImg2ImgPipeline",
            "StableDiffusionControlNetInpaintPipeline",
            "StableDiffusionControlNetPipeline",
            "StableDiffusionXLControlNetImg2ImgPipeline",
            "StableDiffusionXLControlNetInpaintPipeline",
            "StableDiffusionXLControlNetPipeline",
        ]
    )
    _import_structure["controlnet_xs"].extend(
        [
            "StableDiffusionControlNetXSPipeline",
            "StableDiffusionXLControlNetXSPipeline",
        ]
    )
    _import_structure["deepfloyd_if"] = [
        "IFImg2ImgPipeline",
        "IFImg2ImgSuperResolutionPipeline",
        "IFInpaintingPipeline",
        "IFInpaintingSuperResolutionPipeline",
        "IFPipeline",
        "IFSuperResolutionPipeline",
    ]
    _import_structure["kandinsky"] = [
        "KandinskyCombinedPipeline",
        "KandinskyImg2ImgCombinedPipeline",
        "KandinskyImg2ImgPipeline",
        "KandinskyInpaintCombinedPipeline",
        "KandinskyInpaintPipeline",
        "KandinskyPipeline",
        "KandinskyPriorPipeline",
    ]
    _import_structure["kandinsky2_2"] = [
        "KandinskyV22CombinedPipeline",
        "KandinskyV22ControlnetImg2ImgPipeline",
        "KandinskyV22ControlnetPipeline",
        "KandinskyV22Img2ImgCombinedPipeline",
        "KandinskyV22Img2ImgPipeline",
        "KandinskyV22InpaintCombinedPipeline",
        "KandinskyV22InpaintPipeline",
        "KandinskyV22Pipeline",
        "KandinskyV22PriorEmb2EmbPipeline",
        "KandinskyV22PriorPipeline",
    ]
    _import_structure["kandinsky3"] = [
        "Kandinsky3Img2ImgPipeline",
        "Kandinsky3Pipeline",
    ]
    _import_structure["latent_consistency_models"] = [
        "LatentConsistencyModelImg2ImgPipeline",
        "LatentConsistencyModelPipeline",
    ]
    _import_structure["latent_diffusion"].extend(["LDMTextToImagePipeline"])
    _import_structure["musicldm"] = ["MusicLDMPipeline"]
    _import_structure["paint_by_example"] = ["PaintByExamplePipeline"]
    _import_structure["pixart_alpha"] = ["PixArtAlphaPipeline"]
    _import_structure["semantic_stable_diffusion"] = ["SemanticStableDiffusionPipeline"]
    _import_structure["shap_e"] = ["ShapEImg2ImgPipeline", "ShapEPipeline"]
    _import_structure["stable_diffusion"].extend(
        [
            "CLIPImageProjection",
            "StableDiffusionAttendAndExcitePipeline",
            "StableDiffusionDepth2ImgPipeline",
            "StableDiffusionGLIGENPipeline",
            "StableDiffusionGLIGENPipeline",
            "StableDiffusionGLIGENTextImagePipeline",
            "StableDiffusionImageVariationPipeline",
            "StableDiffusionImg2ImgPipeline",
            "StableDiffusionInpaintPipeline",
            "StableDiffusionInstructPix2PixPipeline",
            "StableDiffusionLatentUpscalePipeline",
            "StableDiffusionLDM3DPipeline",
            "StableDiffusionPanoramaPipeline",
            "StableDiffusionPipeline",
            "StableDiffusionSAGPipeline",
            "StableDiffusionUpscalePipeline",
            "StableUnCLIPImg2ImgPipeline",
            "StableUnCLIPPipeline",
        ]
    )
    _import_structure["stable_diffusion_safe"] = ["StableDiffusionPipelineSafe"]
    _import_structure["stable_video_diffusion"] = ["StableVideoDiffusionPipeline"]
    _import_structure["stable_diffusion_xl"].extend(
        [
            "StableDiffusionXLImg2ImgPipeline",
            "StableDiffusionXLInpaintPipeline",
            "StableDiffusionXLInstructPix2PixPipeline",
            "StableDiffusionXLPipeline",
        ]
    )
    _import_structure["stable_diffusion_diffedit"] = ["StableDiffusionDiffEditPipeline"]
    _import_structure["t2i_adapter"] = [
        "StableDiffusionAdapterPipeline",
        "StableDiffusionXLAdapterPipeline",
    ]
    _import_structure["text_to_video_synthesis"] = [
        "TextToVideoSDPipeline",
        "TextToVideoZeroPipeline",
        "TextToVideoZeroSDXLPipeline",
        "VideoToVideoSDPipeline",
    ]
    _import_structure["unclip"] = ["UnCLIPImageVariationPipeline", "UnCLIPPipeline"]
    _import_structure["unidiffuser"] = [
        "ImageTextPipelineOutput",
        "UniDiffuserModel",
        "UniDiffuserPipeline",
        "UniDiffuserTextDecoder",
    ]
    _import_structure["wuerstchen"] = [
        "WuerstchenCombinedPipeline",
        "WuerstchenDecoderPipeline",
        "WuerstchenPriorPipeline",
    ]
try:
    if not is_onnx_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_onnx_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_onnx_objects))
else:
    _import_structure["onnx_utils"] = ["OnnxRuntimeModel"]
try:
    if not (is_torch_available() and is_transformers_available() and is_onnx_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_torch_and_transformers_and_onnx_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_torch_and_transformers_and_onnx_objects))
else:
    _import_structure["stable_diffusion"].extend(
        [
            "OnnxStableDiffusionImg2ImgPipeline",
            "OnnxStableDiffusionInpaintPipeline",
            "OnnxStableDiffusionPipeline",
            "OnnxStableDiffusionUpscalePipeline",
            "StableDiffusionOnnxPipeline",
        ]
    )

try:
    if not (is_torch_available() and is_transformers_available() and is_k_diffusion_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import (
        dummy_torch_and_transformers_and_k_diffusion_objects,
    )

    _dummy_objects.update(get_objects_from_module(dummy_torch_and_transformers_and_k_diffusion_objects))
else:
    _import_structure["stable_diffusion"].extend(["StableDiffusionKDiffusionPipeline"])
try:
    if not is_flax_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_flax_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_flax_objects))
else:
    _import_structure["pipeline_flax_utils"] = ["FlaxDiffusionPipeline"]
try:
    if not (is_flax_available() and is_transformers_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ..utils import dummy_flax_and_transformers_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_flax_and_transformers_objects))
else:
    _import_structure["controlnet"].extend(["FlaxStableDiffusionControlNetPipeline"])
    _import_structure["stable_diffusion"].extend(
        [
            "FlaxStableDiffusionImg2ImgPipeline",
            "FlaxStableDiffusionInpaintPipeline",
            "FlaxStableDiffusionPipeline",
        ]
    )
    _import_structure["stable_diffusion_xl"].extend(
        [
            "FlaxStableDiffusionXLPipeline",
        ]
    )

if TYPE_CHECKING or DIFFUSERS_SLOW_IMPORT:
    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        from ..utils.dummy_pt_objects import *  # noqa F403

    else:
        from .auto_pipeline import (
            AutoPipelineForImage2Image,
            AutoPipelineForInpainting,
            AutoPipelineForText2Image,
        )
        from .consistency_models import ConsistencyModelPipeline
        from .dance_diffusion import DanceDiffusionPipeline
        from .ddim import DDIMPipeline
        from .ddpm import DDPMPipeline
        from .deprecated import KarrasVePipeline, LDMPipeline, PNDMPipeline, RePaintPipeline, ScoreSdeVePipeline
        from .dit import DiTPipeline
        from .latent_diffusion import LDMSuperResolutionPipeline
        from .pipeline_utils import (
            AudioPipelineOutput,
            DiffusionPipeline,
            ImagePipelineOutput,
        )

    try:
        if not (is_torch_available() and is_librosa_available()):
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        from ..utils.dummy_torch_and_librosa_objects import *
    else:
        from .deprecated import AudioDiffusionPipeline, Mel

    try:
        if not (is_torch_available() and is_transformers_available()):
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        from ..utils.dummy_torch_and_transformers_objects import *
    else:
        from .animatediff import AnimateDiffPipeline
        from .audioldm import AudioLDMPipeline
        from .audioldm2 import (
            AudioLDM2Pipeline,
            AudioLDM2ProjectionModel,
            AudioLDM2UNet2DConditionModel,
        )
        from .blip_diffusion import BlipDiffusionPipeline
        from .controlnet import (
            BlipDiffusionControlNetPipeline,
            StableDiffusionControlNetImg2ImgPipeline,
            StableDiffusionControlNetInpaintPipeline,
            StableDiffusionControlNetPipeline,
            StableDiffusionXLControlNetImg2ImgPipeline,
            StableDiffusionXLControlNetInpaintPipeline,
            StableDiffusionXLControlNetPipeline,
        )
        from .controlnet_xs import (
            StableDiffusionControlNetXSPipeline,
            StableDiffusionXLControlNetXSPipeline,
        )
        from .deepfloyd_if import (
            IFImg2ImgPipeline,
            IFImg2ImgSuperResolutionPipeline,
            IFInpaintingPipeline,
            IFInpaintingSuperResolutionPipeline,
            IFPipeline,
            IFSuperResolutionPipeline,
        )
        from .deprecated import (
            AltDiffusionImg2ImgPipeline,
            AltDiffusionPipeline,
            CycleDiffusionPipeline,
            StableDiffusionInpaintPipelineLegacy,
            StableDiffusionModelEditingPipeline,
            StableDiffusionParadigmsPipeline,
            StableDiffusionPix2PixZeroPipeline,
            VersatileDiffusionDualGuidedPipeline,
            VersatileDiffusionImageVariationPipeline,
            VersatileDiffusionPipeline,
            VersatileDiffusionTextToImagePipeline,
            VQDiffusionPipeline,
        )
        from .kandinsky import (
            KandinskyCombinedPipeline,
            KandinskyImg2ImgCombinedPipeline,
            KandinskyImg2ImgPipeline,
            KandinskyInpaintCombinedPipeline,
            KandinskyInpaintPipeline,
            KandinskyPipeline,
            KandinskyPriorPipeline,
        )
        from .kandinsky2_2 import (
            KandinskyV22CombinedPipeline,
            KandinskyV22ControlnetImg2ImgPipeline,
            KandinskyV22ControlnetPipeline,
            KandinskyV22Img2ImgCombinedPipeline,
            KandinskyV22Img2ImgPipeline,
            KandinskyV22InpaintCombinedPipeline,
            KandinskyV22InpaintPipeline,
            KandinskyV22Pipeline,
            KandinskyV22PriorEmb2EmbPipeline,
            KandinskyV22PriorPipeline,
        )
        from .kandinsky3 import (
            Kandinsky3Img2ImgPipeline,
            Kandinsky3Pipeline,
        )
        from .latent_consistency_models import (
            LatentConsistencyModelImg2ImgPipeline,
            LatentConsistencyModelPipeline,
        )
        from .latent_diffusion import LDMTextToImagePipeline
        from .musicldm import MusicLDMPipeline
        from .paint_by_example import PaintByExamplePipeline
        from .pixart_alpha import PixArtAlphaPipeline
        from .semantic_stable_diffusion import SemanticStableDiffusionPipeline
        from .shap_e import ShapEImg2ImgPipeline, ShapEPipeline
        from .stable_diffusion import (
            CLIPImageProjection,
            StableDiffusionAttendAndExcitePipeline,
            StableDiffusionDepth2ImgPipeline,
            StableDiffusionGLIGENPipeline,
            StableDiffusionGLIGENTextImagePipeline,
            StableDiffusionImageVariationPipeline,
            StableDiffusionImg2ImgPipeline,
            StableDiffusionInpaintPipeline,
            StableDiffusionInstructPix2PixPipeline,
            StableDiffusionLatentUpscalePipeline,
            StableDiffusionLDM3DPipeline,
            StableDiffusionPanoramaPipeline,
            StableDiffusionPipeline,
            StableDiffusionSAGPipeline,
            StableDiffusionUpscalePipeline,
            StableUnCLIPImg2ImgPipeline,
            StableUnCLIPPipeline,
        )
        from .stable_diffusion_diffedit import StableDiffusionDiffEditPipeline
        from .stable_diffusion_safe import StableDiffusionPipelineSafe
        from .stable_diffusion_xl import (
            StableDiffusionXLImg2ImgPipeline,
            StableDiffusionXLInpaintPipeline,
            StableDiffusionXLInstructPix2PixPipeline,
            StableDiffusionXLPipeline,
        )
        from .stable_video_diffusion import StableVideoDiffusionPipeline
        from .t2i_adapter import (
            StableDiffusionAdapterPipeline,
            StableDiffusionXLAdapterPipeline,
        )
        from .text_to_video_synthesis import (
            TextToVideoSDPipeline,
            TextToVideoZeroPipeline,
            TextToVideoZeroSDXLPipeline,
            VideoToVideoSDPipeline,
        )
        from .unclip import UnCLIPImageVariationPipeline, UnCLIPPipeline
        from .unidiffuser import (
            ImageTextPipelineOutput,
            UniDiffuserModel,
            UniDiffuserPipeline,
            UniDiffuserTextDecoder,
        )
        from .wuerstchen import (
            WuerstchenCombinedPipeline,
            WuerstchenDecoderPipeline,
            WuerstchenPriorPipeline,
        )

        try:
            if not is_onnx_available():
                raise OptionalDependencyNotAvailable()
        except OptionalDependencyNotAvailable:
            from ..utils.dummy_onnx_objects import *  # noqa F403

        else:
            from .onnx_utils import OnnxRuntimeModel

        try:
            if not (is_torch_available() and is_transformers_available() and is_onnx_available()):
                raise OptionalDependencyNotAvailable()
        except OptionalDependencyNotAvailable:
            from ..utils.dummy_torch_and_transformers_and_onnx_objects import *
        else:
            from .stable_diffusion import (
                OnnxStableDiffusionImg2ImgPipeline,
                OnnxStableDiffusionInpaintPipeline,
                OnnxStableDiffusionPipeline,
                OnnxStableDiffusionUpscalePipeline,
                StableDiffusionOnnxPipeline,
            )

        try:
            if not (is_torch_available() and is_transformers_available() and is_k_diffusion_available()):
                raise OptionalDependencyNotAvailable()
        except OptionalDependencyNotAvailable:
            from ..utils.dummy_torch_and_transformers_and_k_diffusion_objects import *
        else:
            from .stable_diffusion import StableDiffusionKDiffusionPipeline

        try:
            if not is_flax_available():
                raise OptionalDependencyNotAvailable()
        except OptionalDependencyNotAvailable:
            from ..utils.dummy_flax_objects import *  # noqa F403
        else:
            from .pipeline_flax_utils import FlaxDiffusionPipeline

        try:
            if not (is_flax_available() and is_transformers_available()):
                raise OptionalDependencyNotAvailable()
        except OptionalDependencyNotAvailable:
            from ..utils.dummy_flax_and_transformers_objects import *
        else:
            from .controlnet import FlaxStableDiffusionControlNetPipeline
            from .stable_diffusion import (
                FlaxStableDiffusionImg2ImgPipeline,
                FlaxStableDiffusionInpaintPipeline,
                FlaxStableDiffusionPipeline,
            )
            from .stable_diffusion_xl import (
                FlaxStableDiffusionXLPipeline,
            )

        try:
            if not (is_transformers_available() and is_torch_available() and is_note_seq_available()):
                raise OptionalDependencyNotAvailable()
        except OptionalDependencyNotAvailable:
            from ..utils.dummy_transformers_and_torch_and_note_seq_objects import *  # noqa F403

        else:
            from .deprecated import (
                MidiProcessor,
                SpectrogramDiffusionPipeline,
            )

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
    for name, value in _dummy_objects.items():
        setattr(sys.modules[__name__], name, value)
