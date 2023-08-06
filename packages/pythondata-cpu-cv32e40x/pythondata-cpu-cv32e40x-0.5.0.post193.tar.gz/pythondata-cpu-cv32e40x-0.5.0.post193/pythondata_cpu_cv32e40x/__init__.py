import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post193"
version_tuple = (0, 5, 0, 193)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post193")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post51"
data_version_tuple = (0, 5, 0, 51)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post51")
except ImportError:
    pass
data_git_hash = "ac236895bbea034dbd35857ffb01f96d42c5b321"
data_git_describe = "0.5.0-51-gac236895"
data_git_msg = """\
commit ac236895bbea034dbd35857ffb01f96d42c5b321
Merge: b042f3b2 376d3164
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 4 08:24:01 2022 +0200

    Merge pull request #679 from silabs-oysteink/silabs-oysteink_rvfi_intr_shv
    
    Fix for missing rvfi_intr on CLIC SHV interrupts.

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
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
