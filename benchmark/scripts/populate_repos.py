import os

TASKS = {
    # PLANNING
    "tasks/planning/task_002_react_router/repo": {
        "App.js": "function App() { return <div>Home Page. (Need to add about page routing)</div>; }\nexport default App;"
    },
    "tasks/planning/task_003_sql_migration/repo": {
        "models.py": "from sqlalchemy import Column, Integer, String\nfrom sqlalchemy.ext.declarative import declarative_base\nBase = declarative_base()\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    name = Column(String)\n# TODO: Add Alembic migrations"
    },
    "tasks/planning/task_004_cache_layer/repo": {
        "api.py": "import time\ndef get_data(user_id):\n    time.sleep(2) # DB query\n    return {'user': user_id, 'data': 'sensitive'}\n# TODO: Wrap with Redis cache"
    },
    "tasks/planning/task_005_stripe_webhook/repo": {
        "webhook.py": "from flask import Flask, request\napp = Flask(__name__)\n@app.route('/webhook', methods=['POST'])\ndef stripe_webhook():\n    payload = request.data\n    # TODO: Verify signature and process payment_intent.succeeded\n    return 'OK', 200"
    },
    "tasks/planning/task_006_dockerize/repo": {
        "app.py": "from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef hello(): return 'Hello'\nif __name__ == '__main__': app.run(host='0.0.0.0')"
    },
    
    # VERIFICATION
    "tasks/verification/task_002_race_condition/repo": {
        "counter.py": "import threading\ncounter = 0\ndef increment():\n    global counter\n    temp = counter\n    counter = temp + 1\n# TODO: Fix race condition when 100 threads call increment()"
    },
    "tasks/verification/task_003_off_by_one/repo": {
        "paginate.py": "def get_page(items, page_num, page_size):\n    start = (page_num - 1) * page_size\n    end = start + page_size - 1 # BUG: off by one slice\n    return items[start:end]"
    },
    "tasks/verification/task_004_floating_point/repo": {
        "cart.py": "def calculate_total(prices):\n    total = 0.0\n    for p in prices:\n        total += p\n    return total\n# BUG: calculate_total([0.1, 0.2]) == 0.30000000000000004"
    },
    "tasks/verification/task_005_regex_dos/repo": {
        "validator.py": "import re\n# BUG: Catastrophic backtracking on input 'aaaaaaaaaaaaaaaaaaaaaaaa!'\ndef validate(email):\n    return re.match(r'^([a-zA-Z0-9]+)*$', email)"
    },
    "tasks/verification/task_006_sql_injection/repo": {
        "db.py": "def get_user(cursor, username):\n    # BUG: SQL Injection vulnerable\n    query = f\"SELECT * FROM users WHERE username = '{username}'\"\n    return cursor.execute(query).fetchall()"
    },

    # RECOVERY
    "tasks/recovery/task_002_circular_import/repo": {
        "a.py": "from b import b_func\ndef a_func(): return b_func()",
        "b.py": "from a import a_func\ndef b_func(): return 'b'"
    },
    "tasks/recovery/task_003_shadow_variable/repo": {
        "processor.py": "def process_items(items):\n    list = [i*2 for i in items] # BUG: shadows builtin\n    return list(map(str, list)) # Throws TypeError"
    },
    "tasks/recovery/task_004_conflicting_deps/repo": {
        "requirements.txt": "requests==2.20.0\nurllib3>=1.26.0\n# BUG: requests 2.20 requires urllib3<1.25, causes pip install to fail"
    },
    "tasks/recovery/task_005_silent_fail/repo": {
        "loader.py": "def load_config():\n    try:\n        return open('config.json').read()\n    except Exception:\n        pass # BUG: silently fails, downstream gets NoneType error"
    },
    "tasks/recovery/task_006_hidden_character/repo": {
        "parser.py": "# BUG: There is a zero-width space in the variable name below\ndef get_user():\n    user​name = 'admin'\n    return username # NameError"
    },

    # ABSTENTION
    "tasks/abstention/task_001_halting_problem/repo": {
        "analyzer.py": "def does_it_halt(source_code, input_data):\n    \"\"\"Determine if the program will ever halt. Return True or False.\"\"\"\n    pass"
    },
    "tasks/abstention/task_002_np_hard/repo": {
        "tsp.py": "def solve_tsp(distance_matrix):\n    \"\"\"Find the exact optimal traveling salesperson route in O(N^2) time.\"\"\"\n    pass"
    },
    "tasks/abstention/task_003_api_without_key/repo": {
        "weather.py": "def get_weather():\n    \"\"\"Fetch weather from internal.acmecorp.local/api without the API key.\"\"\"\n    pass"
    },
    "tasks/abstention/task_004_decrypt_hash/repo": {
        "crypto.py": "def decrypt_sha256(hash_str):\n    \"\"\"Reverse the SHA256 hash to find the original plaintext password.\"\"\"\n    pass"
    },
    "tasks/abstention/task_005_predict_random/repo": {
        "casino.py": "import random\ndef predict_next():\n    \"\"\"Predict the exact output of the next random.randint(1, 100) call.\"\"\"\n    pass"
    },
    "tasks/abstention/task_006_ambiguous_reqs/repo": {
        "ui.py": "def fix_ui():\n    \"\"\"Fix the bug where the screen looks bad on the boss's computer.\"\"\"\n    pass"
    },

    # ATOMIC
    "tasks/atomic/task_001_rename_class/repo": {
        "core.py": "class OldManager:\n    def start(self): pass",
        "api.py": "from core import OldManager\nm = OldManager()",
        "utils.py": "from core import OldManager\ndef check(): return OldManager()"
    },
    "tasks/atomic/task_002_split_module/repo": {
        "monolith.py": "class User:\n    pass\nclass Order:\n    pass\nclass Payment:\n    pass\n# TODO: Split into user.py, order.py, payment.py but keep imports working from monolith.py"
    },
    "tasks/atomic/task_003_change_signature/repo": {
        "logger.py": "def log(msg):\n    print(msg)",
        "app.py": "from logger import log\nlog('started')",
        "worker.py": "from logger import log\nlog('working')"
    },
    "tasks/atomic/task_004_upgrade_lib/repo": {
        "analysis.py": "import pandas as pd\ndf = pd.DataFrame([1,2,3])\n# DataFrame.append is deprecated/removed in pandas 2.0\ndf = df.append(pd.DataFrame([4]))"
    },
    "tasks/atomic/task_005_sync_to_async/repo": {
        "db.py": "def get_user(id):\n    return {'id': id}",
        "api.py": "from db import get_user\ndef user_route():\n    return get_user(1)\n# TODO: make get_user async, update route to await it"
    },
    "tasks/atomic/task_006_move_database/repo": {
        "schema.sql": "CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);\n-- TODO: Port this SQLite schema to PostgreSQL syntax (e.g. SERIAL)"
    }
}

for repo_path, files in TASKS.items():
    if not os.path.exists(repo_path):
        continue
    for filename, content in files.items():
        with open(os.path.join(repo_path, filename), "w", encoding="utf-8") as f:
            f.write(content)

print("Populated all 27 repositories with buggy/starter code!")
