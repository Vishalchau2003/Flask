# __init__.py is used to tell Python:

# "This folder should be treated as a Python package"
# Without __init__.py

# Suppose structure is:

# project/
# │
# ├── main.py
# │
# └── admin/
#     └── second.py

# And you write:

# from admin.second import second

# Python may say:

# ModuleNotFoundError

# because Python does not know:

# is admin just a normal folder?
# or a Python package/module?
# With __init__.py

# Structure:

# project/
# │
# ├── main.py
# │
# └── admin/
#     ├── __init__.py
#     └── second.py

# Now Python understands:

# admin = package

# So this works:

# from admin.second import second