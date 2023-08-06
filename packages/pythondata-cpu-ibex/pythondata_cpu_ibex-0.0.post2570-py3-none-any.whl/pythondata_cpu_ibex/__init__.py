import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/lowRISC/ibex"

# Module version
version_str = "0.0.post2570"
version_tuple = (0, 0, 2570)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post2570")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post2428"
data_version_tuple = (0, 0, 2428)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post2428")
except ImportError:
    pass
data_git_hash = "0e396d594435c0acca9df785ac40309c76576cc3"
data_git_describe = "v0.0-2428-g0e396d59"
data_git_msg = """\
commit 0e396d594435c0acca9df785ac40309c76576cc3
Author: Harry Callahan <hcallahan@lowrisc.org>
Date:   Wed Oct 5 11:23:06 2022 +0100

    Change failure modes and add comments with more clarifying details

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_ibex."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_ibex".format(f))
    return fn
