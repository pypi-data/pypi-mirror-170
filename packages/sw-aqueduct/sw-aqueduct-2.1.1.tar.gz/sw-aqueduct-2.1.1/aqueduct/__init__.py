# -*- coding: utf-8 -*-
import importlib.util

spec = importlib.util.find_spec("swimlane")
if spec is None:
    from .utils.exceptions import MissingDependencyError

    raise MissingDependencyError(
        "Unable to find 'Swimlane' python package. Make sure it is installed before continuing."
    )


from .aqueduct import Aqueduct
from .instance import SwimlaneInstance

__title__ = "sw-aqueduct"
__name__ = "aqueduct"
__description__ = "A Swimlane content delivery system written in Python"
__url__ = "https://github.com/swimlane/aqueduct"
__version__ = "2.1.1"
__author__ = "Swimlane"
__author_email__ = "info@swimlane.com"
__maintainer__ = "MSAdministrator"
__maintainer_email__ = "rickardja@live.com"
__license__ = "MIT"
__copyright__ = "Copyright 2022 Swimlane"


__all__ = [
    "Aqueduct",
    "SwimlaneInstance",
    "__title__",
    "__name__",
    "__description__",
    "__url__",
    "__version__",
    "__author__",
    "__author_email__",
    "__maintainer__",
    "__maintainer_email__",
    "__license__",
    "__copyright__",
    "__logo__",
]
