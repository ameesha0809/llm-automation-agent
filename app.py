from flask import Flask, request, jsonify
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def run_task():
    task = request.args.get("task")
    if not task:
        return jsonify({"error": "No task specified"}), 400
    
    if task == "get_date":
        result = datetime.datetime.now().isoformat()
    
    elif task.startswith("run_script:"):
        script_path = task.split(":", 1)[1]
        if os.path.exists(script_path):
            result = subprocess.run(["python", script_path], capture_output=True, text=True)
            result = result.stdout
        else:
            return jsonify({"error": "Script not found"}), 404

    elif task == "count_wednesdays":
        try:
            subprocess.run(["python", "count_wednesdays.py"], check=True)
            return jsonify({"task": task, "result": "Completed"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Unknown task"}), 400
    
    return jsonify({"task": task, "result": result})

@app.route("/read", methods=["GET"])
def read_file():
    path = request.args.get("path")
    if not path or not os.path.exists(path):
        return jsonify({"error": "File not found"}), 404
    
    with open(path, "r") as file:
        content = file.read()
    
    return jsonify({"path": path, "content": content})

if __name__ == "__main__":
    app.run(debug=True)
