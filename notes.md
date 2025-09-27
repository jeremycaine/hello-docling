# Data samepls for AI experiments

## folders
- data: datasets, documents etc
- analysis: programs for AI experiments

## Analysis

### Docling
Create a clean environment for a docling install.
```
brew install xz

pyenv uninstall 3.12.3 -f

# Make sure pyenv picks up Homebrew’s xz headers and libs
export CPPFLAGS="-I$(brew --prefix xz)/include"
export LDFLAGS="-L$(brew --prefix xz)/lib"

pyenv install 3.12.3
pyenv local 3.12.3

python -c "import lzma, sys; print(sys.version, 'lzma OK')"

python -m venv .venv
source .venv/bin/activate
pip install -U pip

# Known-good pins
pip install -U \
  "docling>=2.7,<3" \
  "docling-ibm-models>=3.4" \
  "transformers==4.56.1" \
  "torch>=2.1" \
  torchvision \
  accelerate safetensors

```