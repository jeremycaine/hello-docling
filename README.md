# hello-docling
Experiments with docling

## python
pyenv install 3.12.3
pyenv local 3.12.3

python -m venv .venv
source .venv/bin/activate
pip install -U pip

## env
pip install -U \
  "docling>=2.7,<3" \
  "docling-ibm-models>=3.4" \
  "transformers==4.56.1" \
  "torch>=2.1" \
  torchvision \
  accelerate safetensors

## docling start
