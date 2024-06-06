from skimage import io
from pathlib import Path
import numpy as np

def load_image(p: Path) -> np.ndarray:
    return io.imread(p)