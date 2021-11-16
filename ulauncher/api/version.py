import re

api_version = '2.1'


# Very simplistic version compatibility checking just for Ulaunchers simple needs. In order to
# be compatible with the previous semver version library it treats x as 0 and ignores all characters
# except digits and dots. It only really checks that the Ulauncher version is higher or the
# same as the specified version, and the same major version.

def get_version(version_string):
    sanitized = re.sub(r"[^\d\.]+", "", version_string.replace("x", "0"))
    major, minor, *_ = f"{sanitized}.0".split(".")
    return (int(major), int(minor))


def satisfies(version_string, expected_string):
    version = get_version(version_string)
    expected = get_version(expected_string)
    return version[0] == expected[0] and version >= expected


def valid_range(range):
    return bool(get_version(range))
