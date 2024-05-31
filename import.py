import re
import subprocess

# Define a function to read the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Define a function to process the file content and create import commands
def create_import_commands(tf_content):
    # Use a regular expression to find resource blocks
    resource_pattern = re.compile(
        r'resource\s+"(?P<resource_type>[^"]+)"\s+"(?P<resource_name>[^"]+)"\s*{\s*[^}]*zone_id\s*=\s*"(?P<zone_id>[^"]+)"\s*[^}]*}',
        re.DOTALL
    )
    matches = resource_pattern.findall(tf_content)

    # Create import commands
    commands = []
    for match in matches:
        resource_type, resource_name, zone_id = match
        # Extract the unique_id from the resource_name
        unique_id_match = re.search(r'_(?P<unique_id>[a-f0-9]{32})$', resource_name)
        if unique_id_match:
            unique_id = unique_id_match.group('unique_id')
            command = f'terraform import {resource_type}.{resource_name} {zone_id}/{unique_id}'
            commands.append(command)

    return commands

# Define a function to execute the commands
def execute_commands(commands):
    for command in commands:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Success: {result.stdout}")
        else:
            print(f"Error: {result.stderr}")

# Path to the importing.tf file
file_path = 'importing-example.tf'

# Read the file content
tf_content = read_file(file_path)

# Create the import commands
import_commands = create_import_commands(tf_content)

# Execute the import commands
execute_commands(import_commands)
