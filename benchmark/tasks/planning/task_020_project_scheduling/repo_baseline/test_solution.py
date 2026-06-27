import math
import random
import time

def solve_bnb(tasks, num_workers):
    n = len(tasks)
    if n == 0: return 0
    id_to_idx = {t["id"]: i for i, t in enumerate(tasks)}
    durations = [t["duration"] for t in tasks]
    predecessors = [[] for _ in range(n)]
    successors = [[] for _ in range(n)]
    for t in tasks:
        u = id_to_idx[t["id"]]
        for p_id in t.get("prerequisites", []):
            if p_id not in id_to_idx: return -1
            p = id_to_idx[p_id]
            predecessors[u].append(p)
            successors[p].append(u)
            
    cp = [-1] * n
    visited_nodes = [0] * n
    
    def get_cp(u):
        if visited_nodes[u] == 1: return -1
        if visited_nodes[u] == 2: return cp[u]
        visited_nodes[u] = 1
        max_succ_cp = 0
        for v in successors[u]:
            res = get_cp(v)
            if res == -1: return -1
            max_succ_cp = max(max_succ_cp, res)
        visited_nodes[u] = 2
        cp[u] = durations[u] + max_succ_cp
        return cp[u]
        
    for i in range(n):
        if visited_nodes[i] == 0:
            if get_cp(i) == -1: return -1
            
    # Remap IDs so that ID 0 has the highest CP
    # This helps branch and bound explore promising paths first
    sorted_tasks = sorted(range(n), key=lambda x: cp[x], reverse=True)
    new_id = {old: new for new, old in enumerate(sorted_tasks)}
    
    durations = [durations[sorted_tasks[i]] for i in range(n)]
    cp = [cp[sorted_tasks[i]] for i in range(n)]
    
    new_predecessors = [[] for _ in range(n)]
    new_successors = [[] for _ in range(n)]
    for old in range(n):
        for p in predecessors[old]:
            new_predecessors[new_id[old]].append(new_id[p])
        for s in successors[old]:
            new_successors[new_id[old]].append(new_id[s])
            
    predecessors = new_predecessors
    successors = new_successors
            
    pred_masks = [0] * n
    for i in range(n):
        for p in predecessors[i]:
            pred_masks[i] |= (1 << p)
            
    target_mask = (1 << n) - 1
    
    def heuristic(completed_mask, running_tuple):
        h_cp = 0
        total_work = 0
        running_tasks = {u for _, u in running_tuple}
        for i in range(n):
            if not (completed_mask & (1 << i)) and i not in running_tasks:
                h_cp = max(h_cp, cp[i])
                total_work += durations[i]
        for rem, u in running_tuple:
            max_succ = 0
            for v in successors[u]:
                max_succ = max(max_succ, cp[v])
            h_cp = max(h_cp, rem + max_succ)
            total_work += rem
        return max(h_cp, math.ceil(total_work / num_workers))
        
    def greedy():
        time = 0
        completed = 0
        running = [] 
        while completed != target_mask:
            running_tasks = {u for _, u in running}
            available = []
            for i in range(n):
                if not (completed & (1 << i)) and i not in running_tasks:
                    if (completed & pred_masks[i]) == pred_masks[i]:
                        available.append(i)
            # Already sorted by CP since i is 0..n-1
            free = num_workers - len(running)
            for u in available[:free]:
                running.append((time + durations[u], u))
            
            if not running: return float('inf')
            
            running.sort()
            next_time = running[0][0]
            time = next_time
            new_running = []
            for t, u in running:
                if t == next_time:
                    completed |= (1 << u)
                else:
                    new_running.append((t, u))
            running = new_running
        return time
        
    best_global = greedy()
    # print("Greedy bound:", best_global)
    
    # Memoization for pruning
    # min_time_to_reach stores the minimum current_time + min_rem to reach a state
    # Wait, simple memo: if we reach (completed, running) at a >= time, we can prune!
    best_time_to_reach = {}
    
    def dfs(completed_mask, running_tuple, current_time, last_idx):
        nonlocal best_global
        if current_time >= best_global: return
        if completed_mask == target_mask:
            if current_time < best_global:
                best_global = current_time
            return
            
        h = heuristic(completed_mask, running_tuple)
        if current_time + h >= best_global:
            return
            
        state = (completed_mask, running_tuple, last_idx)
        if current_time >= best_time_to_reach.get(state, float('inf')):
            return
        best_time_to_reach[state] = current_time
            
        available = []
        running_tasks = {u for _, u in running_tuple}
        for i in range(n):
            if not (completed_mask & (1 << i)) and i not in running_tasks:
                if (completed_mask & pred_masks[i]) == pred_masks[i]:
                    if i > last_idx:
                        available.append(i)
                        
        free_workers = num_workers - len(running_tuple)
        
        # Branch 1: Start a task
        if free_workers > 0:
            for u in available:
                new_running = tuple(sorted(list(running_tuple) + [(durations[u], u)]))
                dfs(completed_mask, new_running, current_time, u)
                
        # Branch 2: Advance time
        if len(running_tuple) > 0:
            min_rem = running_tuple[0][0]
            new_completed = completed_mask
            new_running = []
            for t, u in running_tuple:
                if t == min_rem:
                    new_completed |= (1 << u)
                else:
                    new_running.append((t - min_rem, u))
            dfs(new_completed, tuple(new_running), current_time + min_rem, -1)

    dfs(0, (), 0, -1)
    return best_global

if __name__ == "__main__":
    random.seed(42)
    tasks = [{"id": str(i), "duration": random.randint(1, 100), "prerequisites": []} for i in range(15)]
    t0 = time.time()
    res = solve_bnb(tasks, 5)
    print("BNB Res:", res, "Time:", time.time()-t0)
    
    tasks = [
        {"id": "A", "duration": 3, "prerequisites": []},
        {"id": "B", "duration": 2, "prerequisites": ["A"]},
        {"id": "C", "duration": 4, "prerequisites": ["A"]},
        {"id": "D", "duration": 1, "prerequisites": ["B", "C"]}
    ]
    print("Example res:", solve_bnb(tasks, 2))
