"""Build collage of images from dataset for visualization."""

from pathlib import Path

import numpy as np
from PIL import Image

OUT_PATH = Path('./output/images')
OUT_PATH.mkdir(exist_ok=True, parents=True)


def build_collage(
    labels,
    images,
    name,
    out_path=OUT_PATH,
    rows=3,
    cols=5,
):
    """Build collage of images from dataset for visualization.

    Args:
        labels (np.ndarray): Labels of images.
        images (np.ndarray): Images.
        name (str): Name of collage.
        out_path (Path): Path to save collage.
        rows (int): Number of rows in collage.
        cols (int): Number of columns in collage.

    Returns:
        None
    """
    label_map = {
        0: 'rough',
        1: 'smooth',
    }
    size = images[0].shape[:2]
    for label in [0, 1]:
        idx = np.random.choice(
            np.where(labels == label)[0],
            size=rows * cols,
            replace=False,
        )

        # create a collage of images
        collage = Image.new('RGB', (size[1] * cols, size[0] * rows))
        for i, idx in enumerate(idx):
            image = Image.fromarray(images[idx])
            collage.paste(image, (size[1] * (i % cols), size[0] * (i // cols)))

        # scale down the collage
        collage = collage.resize((size[1] * cols // 2, size[0] * rows // 2))
        collage.save('{0}/{1}_{2}_collage.png'.format(
            out_path,
            label_map[label],
            name,
        ))
