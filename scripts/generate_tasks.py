import os
import json
import subprocess
import re

# Configuration
CATEGORIES = [
    'planning',
    'verification',
    'recovery',
    'abstention',
    'atomic'
]
TARGET_TASKS_PER_CATEGORY = 20

PROMPT_TEMPLATE = """
You are an expert software engineer creating benchmarking tasks for AI coding agents.
Create a task for the category: {category}.
The task should test the agent's ability to handle this category effectively.

Return the result STRICTLY as a raw JSON object with NO markdown formatting, NO backticks, and NO conversational text.
Use this exact schema:
{{
  "task_slug": "task_XXX_name",
  "readme": "# Prompt\\n...",
  "main_filename": "main.py",
  "main_code": "def ...",
  "test_filename": "test_main.py",
  "test_code": "def test_..."
}}
"""

def extract_json(text):
    """Attempt to extract a JSON block if the model included markdown."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Fallback: look for ```json ... ```
        match = re.search(r'```(?:json)?(.*?)```', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1).strip())
            except json.JSONDecodeError:
                pass
    return None

def generate_task(category, task_num):
    """
    Calls the Antigravity CLI (agy) to generate a new task non-interactively.
    """
    prompt = PROMPT_TEMPLATE.format(category=category)
    print(f"  [AGY] Requesting task {task_num} for {category}...")
    
    try:
        result = subprocess.run(
            ['agy', '--dangerously-skip-permissions', '--print', prompt],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode != 0:
            print(f"  [AGY Error] {result.stderr}")
            return None
            
        task_data = extract_json(result.stdout.strip())
        if not task_data:
            print("  [Error] Failed to parse JSON from AGY response.")
            print("Raw response:", result.stdout[:200] + "...")
            return None
            
        return task_data
    except Exception as e:
        print(f"  [Exception] {e}")
        return None

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'benchmark', 'tasks')
    
    for category in CATEGORIES:
        cat_dir = os.path.join(base_dir, category)
        os.makedirs(cat_dir, exist_ok=True)
        
        existing_tasks = [d for d in os.listdir(cat_dir) if os.path.isdir(os.path.join(cat_dir, d))]
        num_existing = len(existing_tasks)
        num_needed = TARGET_TASKS_PER_CATEGORY - num_existing
        
        print(f"\\n=== Category: {category} | Existing: {num_existing} | Needed: {num_needed} ===")
        
        for i in range(num_needed):
            task_num = num_existing + i + 1
            
            task_data = generate_task(category, task_num)
            if not task_data:
                print(f"  [Warning] Skipping task {task_num} due to generation failure.")
                continue
                
            task_slug = task_data.get('task_slug', f"task_{task_num:03d}_generated")
            if not task_slug.startswith(f"task_{task_num:03d}"):
                # Ensure the prefix matches the exact count to keep things orderly
                name_part = task_slug.split('_', 2)[-1] if '_' in task_slug else task_slug
                task_slug = f"task_{task_num:03d}_{name_part}"
                
            repo_dir = os.path.join(cat_dir, task_slug, 'repo_agentrigor')
            os.makedirs(repo_dir, exist_ok=True)
            
            # Write files
            with open(os.path.join(repo_dir, 'README.md'), 'w') as f:
                f.write(task_data.get('readme', ''))
            with open(os.path.join(repo_dir, task_data.get('main_filename', 'main.py')), 'w') as f:
                f.write(task_data.get('main_code', ''))
            with open(os.path.join(repo_dir, task_data.get('test_filename', 'test_main.py')), 'w') as f:
                f.write(task_data.get('test_code', ''))
                
            print(f"  [Success] Created {repo_dir}")

if __name__ == "__main__":
    main()
