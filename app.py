import os
from vision import describe_diagram
from generator import generate_code, save_code

def main():
    print("\n=== Whiteboard to Code Converter ===")
    print("Converts any diagram photo into working code.\n")

    image_path = input("Enter image path (JPG or PNG): ").strip()
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return

    lang = input("Generate in Python or JavaScript? (python/js): ").strip().lower()
    if lang not in ["python", "js"]:
        lang = "python"

    print("\nReading diagram with vision AI...")
    description = describe_diagram(image_path)
    print("\n--- DIAGRAM DESCRIPTION ---")
    print(description)

    print(f"\nGenerating {lang} code...")
    code = generate_code(description, lang)

    print("\n--- GENERATED CODE ---")
    print(code)

    output_path = save_code(code, lang, os.path.basename(image_path))
    print(f"\nCode saved to: {output_path}")
    print("\nDone! Your diagram has been converted to code.")

if __name__ == "__main__":
    main()