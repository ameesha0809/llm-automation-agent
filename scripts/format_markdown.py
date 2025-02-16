import subprocess

def format_markdown(file_path):
    npx_path = "C:\\Program Files\\nodejs\\npx.cmd"  # Update this path if needed
    try:
        subprocess.run([npx_path, "prettier@3.4.2", "--write", file_path], check=True)
        print(f"Formatted {file_path} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error formatting {file_path}: {e}")

if __name__ == "__main__":
    file_path = "../data/format.md"  # Adjust path if needed
    format_markdown(file_path)
