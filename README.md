# Skin Detection

## Description
Detects skin areas in an image and converts them to white, while non-skin areas (hair, eyes, lips, etc.) are turned black.

## File Structure
- `skin_detection.py`: Contains the `detect_skin` function.

## Dependencies
- OpenCV (`cv2`)
- NumPy

## Usage
```python
from skin_detection import detect_skin
skin_image = detect_skin("path/to/image.jpg")
cv2.imwrite("output.jpg", skin_image)
```

