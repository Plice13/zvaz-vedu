import os
import re

def fix_hugo_urls(directory_path):
    """
    Finds and replaces hardcoded absolute paths (href="/..." and src="/...")
    in HTML files within a directory and its subdirectories with Hugo template
    variables.

    Args:
        directory_path (str): The path to the directory to process.
    """
    # Regex to find href="/..." or src="/..."
    # It captures:
    # Group 1: The attribute name (href or src)
    # Group 2: The quote character (' or ")
    # Group 3: The path segment after the leading slash
    pattern = re.compile(r'(href|src|img)=(["\'])\/([^"\'>]*)\2')

    # Replacement string: attribute="{{ .Site.BaseURL }}path"
    # \1 is the captured attribute name (href or src)
    # \2 is the captured quote character
    # {{ .Site.BaseURL }} is the literal Hugo template variable
    # \3 is the captured path segment after the slash
    # \2 is the captured closing quote character
    replacement = r'\1=\2{{ .Site.BaseURL }}\3\2'

    print(f"Starting URL fix in directory: {directory_path}")

    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found at {directory_path}")
        # This error is less likely now that we get the current directory,
        # but good practice to keep.
        return

    processed_files_count = 0
    replacements_count = 0

    # Walk through the directory tree
    for root, _, files in os.walk(directory_path):
        for file in files:
            # Process only HTML files
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                processed_files_count += 1
                print(f"Processing {file_path}...")

                try:
                    # Read the file content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Perform the replacement using regex
                    # count=0 means replace all occurrences
                    new_content, num_replacements = re.subn(pattern, replacement, content)

                    if num_replacements > 0:
                        replacements_count += num_replacements
                        print(f"  Found and replaced {num_replacements} instances.")

                        # Write the modified content back to the file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                    else:
                        print("  No matching patterns found.")

                except Exception as e:
                    print(f"  Error processing {file_path}: {e}")

    print("\n--------------------")
    print("Processing complete.")
    print(f"Processed {processed_files_count} HTML files.")
    print(f"Total replacements made: {replacements_count}")
    print("--------------------")
    print("Remember to rebuild your Hugo site if you ran this script on your source files (like layouts).")


if __name__ == "__main__":
    # Get the directory where the script is located
    # This will be the starting point for os.walk()
    target_directory = os.path.dirname(os.path.abspath(__file__))

    # Run the fix function on the script's directory
    fix_hugo_urls(target_directory)
