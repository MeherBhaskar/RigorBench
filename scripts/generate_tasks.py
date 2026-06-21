import os
import json
import argparse
# import google.generativeai as genai
# import openai

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

Return the result strictly as a JSON object with the following keys:
- "task_slug": A short directory name for the task (e.g., "task_008_sql_parser").
- "readme": The contents of README.md containing the prompt/instructions.
- "main_filename": The name of the main python file (e.g., "parser.py").
- "main_code": The initial buggy or incomplete Python code.
- "test_filename": The name of the test file (e.g., "test_parser.py").
- "test_code": The complete test suite using pytest that validates the task.
"""

def generate_task(category, task_num):
    """
    Calls the LLM API to generate a new task. 
    Replace this with actual API calls to Gemini or OpenAI.
    """
    # Example using Google GenAI (Gemini)
    # genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    # model = genai.GenerativeModel("gemini-1.5-pro")
    # response = model.generate_content(PROMPT_TEMPLATE.format(category=category))
    # return json.loads(response.text.strip('```json').strip('```'))
    
    print(f"Skipping actual LLM call for {category} task {task_num} (No API key configured)")
    return None

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'benchmark', 'tasks')
    
    for category in CATEGORIES:
        cat_dir = os.path.join(base_dir, category)
        os.makedirs(cat_dir, exist_ok=True)
        
        existing_tasks = [d for d in os.listdir(cat_dir) if os.path.isdir(os.path.join(cat_dir, d))]
        num_existing = len(existing_tasks)
        num_needed = TARGET_TASKS_PER_CATEGORY - num_existing
        
        print(f"Category: {category} | Existing: {num_existing} | Needed: {num_needed}")
        
        for i in range(num_needed):
            task_num = num_existing + i + 1
            print(f"  Generating task {task_num} for {category}...")
            
            task_data = generate_task(category, task_num)
            if not task_data:
                continue
                
            task_slug = task_data.get('task_slug', f"task_{task_num:03d}_generated")
            # Ensure the slug matches the numbering scheme
            if not task_slug.startswith(f"task_{task_num:03d}"):
                task_slug = f"task_{task_num:03d}_{task_slug.split('_', 2)[-1]}"
                
            repo_dir = os.path.join(cat_dir, task_slug, 'repo_agentrigor')
            os.makedirs(repo_dir, exist_ok=True)
            
            # Write files
            with open(os.path.join(repo_dir, 'README.md'), 'w') as f:
                f.write(task_data['readme'])
            with open(os.path.join(repo_dir, task_data['main_filename']), 'w') as f:
                f.write(task_data['main_code'])
            with open(os.path.join(repo_dir, task_data['test_filename']), 'w') as f:
                f.write(task_data['test_code'])
                
            print(f"  Created {repo_dir}")

if __name__ == "__main__":
    main()
