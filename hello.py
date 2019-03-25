#!/usr/bin/env python3
####################################################################################################

import platform

print("Hello, World.")

print(
    "This is python version {}".format(
        platform.python_version()
    )
)

# Change variable name for pull-request.
MoreDescriptive = 7.0
print(MoreDescriptive)
