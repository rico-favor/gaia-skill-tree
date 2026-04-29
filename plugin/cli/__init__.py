import os
import sys

_PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_REPO_ROOT = os.path.abspath(os.path.join(_PACKAGE_ROOT, ".."))
_SRC_CANDIDATES = [
    os.path.join(_PACKAGE_ROOT, "python"),
    os.path.join(_REPO_ROOT, "src"),
]

for _src_root in _SRC_CANDIDATES:
    if os.path.isdir(_src_root) and _src_root not in sys.path:
        sys.path.insert(0, _src_root)

for _root in (_PACKAGE_ROOT, _REPO_ROOT):
    if os.path.isdir(_root) and _root not in sys.path:
        sys.path.insert(0, _root)
