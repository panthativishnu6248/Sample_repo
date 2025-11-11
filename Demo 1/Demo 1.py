import sys
from awsglue.utils import getResolvedOptions

# Define the parameter you expect
args = getResolvedOptions(sys.argv, ['Test_param'])

# Print the parameter value
print("The value of Test_param is:", args['Test_param'])
