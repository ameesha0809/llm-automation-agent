import os
import subprocess
import openai

# ✅ Use AIProxy's API endpoint
openai.api_base = "https://aiproxy.sanand.workers.dev/openai/"
openai.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjEwMDA5MDFAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.O4pQQS7VDkU_fR8tVyDhmOhqCNIECTNOq-k0oaDvN30"  # Replace with your actual AIProxy token

# Task-to-script mapping
TASK_SCRIPT_MAPPING = {
    "A1": "scripts/generate_data.py",
    "A2": "scripts/format_markdown.py",
    "A3": "scripts/count_wednesdays.py",
    "A4": "scripts/sort_contacts.py",
    "A5": "scripts/process_logs.py",
    "A6": "scripts/extract_md_titles.py",
    "A7": "scripts/extract_email.py",
    "A8": "scripts/extract_credit_card.py",
    "A9": "scripts/find_similar_comments.py",
    "A10": "scripts/process_ticket_sales.py"
}

def get_script_for_task(task_description):
    """Use LLM to determine the script for the given task description."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that maps task descriptions to script names."},
                {"role": "user", "content": f"Given the task '{task_description}', which script should run? Options: {list(TASK_SCRIPT_MAPPING.keys())}"}
            ]
        )
        
        task_id = response['choices'][0]['message']['content'].strip()
        return TASK_SCRIPT_MAPPING.get(task_id, None)

    except openai.error.AuthenticationError as e:
        print(f"❌ Error calling AIProxy API: {e}")
        return None

def execute_script(script_path):
    """Execute the given script and return the output."""
    if not os.path.exists(script_path):
        return f"❌ Error: Script {script_path} not found."
    
    try:
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"❌ Error executing script: {str(e)}"

def main():
    task_description = input("Enter the task description: ").strip()
    print(f"Task entered: {task_description}")

    script_path = get_script_for_task(task_description)
    
    if script_path:
        print(f"🚀 Executing script: {script_path}")
        output = execute_script(script_path)
        print("📝 Output:", output)
    else:
        print("⚠️ No matching script found for the task description.")

if __name__ == "__main__":
    main()
