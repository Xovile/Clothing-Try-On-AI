# AI Clothing Try-On Model

This project is an AI-based clothing try-on model that utilizes the HR-VITON dataset and Facebook Detectron2 library. It is implemented using CUDA for NVIDIA GPU integration.

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See the [LICENSE](LICENSE) file for details.

## Overview

The AI Clothing Try-On Model provides a virtual try-on experience for clothing items. It leverages state-of-the-art deep learning techniques to seamlessly overlay clothing onto images of individuals.

## Procedural Flow

The AI Clothing Try-On Model follows the procedural flow outlined below:

1. **Input Acquisition**: The user provides input images, including a model image and a cloth image.
   
2. **Preprocessing**:
   - Resizing input image: The input images are resized for compatibility with the model.
   - Generating mask of cloth: The clothing item is segmented from the background to isolate it for overlay.

3. **Pose Detection**:
   - Obtaining openpose coordinate using posenet: The pose of the individual in the model image is detected to ensure accurate placement of the clothing item.

4. **Semantic Segmentation**:
   - Generating semantic segmentation: The clothing item and the model image are processed to generate semantic segmentation masks.

5. **Deep Learning Model**:
   - Constructing DeepLabv3+ model: The DeepLabv3+ model is constructed for semantic segmentation and background removal.

6. **Densepose Image Generation**:
   - Generating Densepose image: Densepose estimation is performed using the Detectron2 library to understand the body pose and shape.

7. **AI Clothing Try-On**:
   - Running HR-VITON-main to generate the final image: The HR-VITON model is applied to overlay the clothing item onto the model image.

8. **Post-processing**:
   - Adding background to generated images: The final output image is composed by adding a suitable background to enhance realism.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- CUDA-enabled GPU
- Libraries: matplotlib, opencv-python, Pillow

## Usage

To use the AI Clothing Try-On Model:

1. Ensure all dependencies are installed.
2. Provide the paths to the input images (model image and cloth image) when prompted.
3. Follow the instructions in the notebook or script to execute the model.
4. View the final output image to see the virtual try-on result.

### Note

The files couldn't be uploaded to Github due to size limitations. You can find these files in the [Releases](https://github.com/Xovile/Clothing-Try-On-AI/releases) section

## Contribution

Contributions are welcome! Feel free to open issues or pull requests for any improvements or fixes.

## Acknowledgments

- [HR-VITON dataset](https://github.com/sangyun884/HR-VITON)
- [Facebook Detectron2 library](https://github.com/facebookresearch/detectron2)
- [Graphonomy library](https://github.com/Gaoyiminggithub/Graphonomy)
- [Posenet library](https://github.com/rwightman/posenet-python)
- [TryYours Virtual Try On](https://github.com/lastdefiance20/TryYours-Virtual-Try-On)