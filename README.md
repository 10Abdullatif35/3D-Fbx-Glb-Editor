# 3D-Fbx-Glb-Editor

This repository contains a simple command line tool for copying FBX/GLB files
and previewing them in a small 3D viewer. The viewer automatically rotates the
model so you can quickly inspect an asset.

## Usage

```bash
# copy the model to another path
python src/main.py <input_file> <output_file>

# preview a model
python src/main.py <input_file> --preview

# preview without copying by omitting the output file
python src/main.py <input_file>
```
