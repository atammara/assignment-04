import os
import argparse
from datetime import datetime

def bulk_rename(directory, prefix="", suffix="", extension=None, replace=None, with_str=None, counter=False, counter_digits=3, preview=False):
    """
    Bulk rename files in a directory with various options
    
    Args:
        directory (str): Path to directory containing files
        prefix (str): Text to add before filename
        suffix (str): Text to add after filename
        extension (str): New file extension (without dot)
        replace (str): Text to replace in original filenames
        with_str (str): Replacement text
        counter (bool): Add sequential counter
        counter_digits (int): Number of digits for counter
        preview (bool): Show changes without actually renaming
    """
    try:
        # Get all files in directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        if not files:
            print("No files found in directory!")
            return
        
        print(f"\nFound {len(files)} files in {directory}")
        
        # Process each file
        for i, filename in enumerate(sorted(files)):
            # Split filename and extension
            name, ext = os.path.splitext(filename)
            ext = ext.lower()  # Normalize extension
            
            # Build new filename
            new_name = name
            
            # Replace text if specified
            if replace and with_str:
                new_name = new_name.replace(replace, with_str)
            
            # Add prefix and suffix
            new_name = f"{prefix}{new_name}{suffix}"
            
            # Add counter if specified
            if counter:
                counter_str = f"{i+1:0{counter_digits}d}"
                new_name = f"{new_name}_{counter_str}"
            
            # Handle extension
            new_ext = f".{extension}" if extension else ext
            new_filename = f"{new_name}{new_ext}"
            
            # Generate full paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Skip if no change
            if old_path == new_path:
                continue
                
            # Show preview or rename
            if preview:
                print(f"'{filename}' -> '{new_filename}'")
            else:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed '{filename}' to '{new_filename}'")
                except Exception as e:
                    print(f"Error renaming '{filename}': {e}")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Bulk File Renamer")
    parser.add_argument("directory", help="Directory containing files to rename")
    parser.add_argument("--prefix", default="", help="Text to add before filename")
    parser.add_argument("--suffix", default="", help="Text to add after filename")
    parser.add_argument("--ext", help="New file extension (without dot)")
    parser.add_argument("--replace", help="Text to replace in filenames")
    parser.add_argument("--with", dest="with_str", help="Replacement text")
    parser.add_argument("--counter", action="store_true", help="Add sequential counter")
    parser.add_argument("--digits", type=int, default=3, help="Number of digits for counter")
    parser.add_argument("--preview", action="store_true", help="Preview changes without renaming")
    
    args = parser.parse_args()
    
    # Add timestamp if no prefix/suffix provided
    if not any([args.prefix, args.suffix, args.replace, args.counter, args.ext]):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.prefix = f"{timestamp}_"
        print(f"No renaming options provided. Using timestamp prefix: {args.prefix}")
    
    # Call bulk rename function
    bulk_rename(
        directory=args.directory,
        prefix=args.prefix,
        suffix=args.suffix,
        extension=args.ext,
        replace=args.replace,
        with_str=args.with_str,
        counter=args.counter,
        counter_digits=args.digits,
        preview=args.preview
    )

if __name__ == "__main__":
    main()