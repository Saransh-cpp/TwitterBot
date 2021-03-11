import sys
import os
from platform import system

# def _load_version_int():
#     try:
#         root = os.path.abspath(os.path.dirname(__file__))
#         with open(os.path.join(root, "version"), "r") as f:
#             version = f.read().strip().split(",")
#         major, minor, revision = [int(x) for x in version]
#         return major, minor, revision
#     except Exception as e:
#         raise RuntimeError("Unable to read version number (" + str(e) + ").")

# from Models.Chen2020Params import *