
import re
from pathlib import Path

from docling.datamodel import vlm_model_specs
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    VlmPipelineOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline

# Convert a public arXiv PDF; replace with a local path if preferred.
#source = "https://arxiv.org/pdf/2501.17887"
source = "./big-bang-pilot.pdf"

###### USING MACOS MPS ACCELERATOR
# Demonstrates using MLX on macOS with MPS acceleration (macOS only).
# For more options see the `compare_vlm_models.py` example.

pipeline_options = VlmPipelineOptions(
    vlm_options=vlm_model_specs.GRANITEDOCLING_MLX,
)

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=VlmPipeline,
            pipeline_options=pipeline_options,
        ),
    }
)

doc = converter.convert(source=source).document

# Prefer plain text (avoids pre-existing markdown headings that could confuse parsing)
markdown_output = doc.export_to_markdown()

# Save to disk
output_file = "output.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown_output)

print(f"Markdown saved to {output_file}")