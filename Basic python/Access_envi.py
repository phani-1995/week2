import os
import pprint

# Get the list of user's
# environment variables

en_var=os.environ

# Print the list of user's
# environment variables

print("User's Environment variable:")
pprint.pprint(dict(en_var), width = 1)


