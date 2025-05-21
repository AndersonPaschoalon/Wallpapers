import os
from pathlib import Path

def generate_wallpaper_markdown(root_dir='.', output_file='README.md'):
    # Supported image extensions (comprehensive list)
    image_extensions = [
        '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi',  # JPEG formats
        '.png', '.apng', '.gif', '.bmp', '.dib',            # Common formats
        '.tiff', '.tif', '.webp', '.svg', '.svgz',          # Additional formats
        '.ico', '.heic', '.heif',                           # Modern formats
        '.raw', '.arw', '.cr2', '.nrw', '.k25'              # RAW formats
    ]
    
    # Start markdown content
    markdown_content = """# My Wallpapers Repository

A curated collection of high-quality wallpapers for all devices and moods. 
Find your perfect background in these organized categories.

"""

    # Walk through directory structure
    for root, dirs, files in os.walk(root_dir):
        # Skip the .git directory if it exists
        if '.git' in dirs:
            dirs.remove('.git')
        
        path = Path(root)
        relative_path = path.relative_to(root_dir)
        
        # Skip the root directory itself
        if str(relative_path) == '.':
            continue
            
        # Check if directory has any image files
        has_images = any(file.lower().endswith(tuple(image_extensions)) for file in files)
        if not has_images:
            continue
            
        # Determine heading level
        depth = len(relative_path.parts)
        
        if depth == 1:
            # Level 1 heading (main category)
            markdown_content += f"\n# {relative_path}\n\n"
        else:
            # Level 2 heading (subcategory - show full path)
            markdown_content += f"\n## {relative_path}\n\n"
        
        # Add images for this directory
        for file in sorted(files):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                file_path = Path(root) / file
                relative_file_path = file_path.relative_to(root_dir)
                # Use HTML for better image sizing control
                markdown_content += f'<img src="{relative_file_path}" alt="{file}" width="200" style="margin:5px;border:1px solid #ddd;border-radius:5px;"/> '

    # Write to README.md
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Successfully generated {output_file}")

if __name__ == '__main__':
    generate_wallpaper_markdown()
