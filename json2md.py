import json

def json_to_markdown(input_filename, output_filename):
    """Converts a JSON file to Markdown format and saves it to another file.

    Args:
        input_filename: The path to the JSON file.
        output_filename: The name of the file to save the Markdown text to.
    """
    # Read JSON data from file
    with open(input_filename, 'r') as f:
        json_data = json.load(f)

    markdown_text = ""
    for section_name, section_data in json_data.items():  # Iterate over each section
        markdown_text += f"# {section_name}\n\n"  # Add section name as a header
        for item in section_data:  # Iterate over each item within the section
            title = item["title"]  # Access "title" from each item
            text = item["text"]    # Access "text" from each item
            markdown_text += f"## {title}\n\n{text}\n\n"  # Add item to markdown text

    # Write the Markdown text to a file
    with open(output_filename, 'w') as f:
        f.write(markdown_text)

    print(f"Converted Markdown text saved to: {output_filename}")

# Specify input and output filenames (replace with your actual filepaths)
input_filename = "notes.json"
output_filename = "notes.md"

# Convert the JSON data to Markdown and save it to a file
json_to_markdown(input_filename, output_filename)
