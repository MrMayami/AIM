# interpreter.py

import json

def interpret_aim_command(aim_command):
    """
    Interpret AIM command and execute corresponding action.
    """
    parts = aim_command.split(':')
    action = parts[0].strip()
    if action == 'create':
        return create_action(parts[1:])
    else:
        return f"Unknown action: {action}"

def create_action(args):
    """
    Execute create action based on provided arguments.
    """
    # Parse arguments
    if len(args) < 2:
        return "Invalid create action: Insufficient arguments"
    element_type = args[0].strip()
    properties = json.loads(args[1].strip())

    # Generate HTML/CSS code based on element type and properties
    if element_type == 'text':
        return generate_text_element(properties)
    else:
        return f"Unsupported element type: {element_type}"

def generate_text_element(properties):
    """
    Generate HTML/CSS code for a text element based on provided properties.
    """
    # Example: Generate HTML code for a text element
    html = f'<div style="font-family: {properties["font-family"]}; font-size: {properties["font-size"]}px; ' \
           f'color: {properties["color"]}; text-align: {properties["align"]}">{properties["text"]}</div>'
    return html
