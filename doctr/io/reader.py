# Copyright (C) 2021-2022, Mindee.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

from pathlib import Path
from typing import List, Sequence, Union

import numpy as np

from doctr.utils.common_types import AbstractFile

from .image import read_img_as_numpy

__all__ = ['DocumentFile']


class DocumentFile:
    """Read a document from multiple extensions"""


    @classmethod
    def from_images(cls, files: Union[Sequence[AbstractFile], AbstractFile], **kwargs) -> List[np.ndarray]:
        """Read an image file (or a collection of image files) and convert it into an image in numpy format

        Example::
            >>> from doctr.documents import DocumentFile
            >>> pages = DocumentFile.from_images(["path/to/your/page1.png", "path/to/your/page2.png"])

        Args:
            files: the path to the image file or a binary stream, or a collection of those
        Returns:
            the list of pages decoded as numpy ndarray of shape H x W x 3
        """
        if isinstance(files, (str, Path, bytes)):
            files = [files]

        return [read_img_as_numpy(file, **kwargs) for file in files]
