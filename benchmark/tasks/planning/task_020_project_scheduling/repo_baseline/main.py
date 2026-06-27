import itertools
import time

def min_completion_time(tasks: list[dict], num_workers: int) -> int:
    n = len(tasks)
    if n == 0: return 0
    id_to_idx = {t["id"]: i for i, t in enumerate(tasks)}
    durations = [t["duration"] for t in tasks]
    predecessors = [[] for _ in range(n)]
    
    for t in tasks:
        u = id_to_idx[t["id"]]
        for p_id in t.get("prerequisites", []):
            if p_id not in id_to_idx: return -1
            predecessors[u].append(id_to_idx[p_id])
            
    visited = [0] * n
    def has_cycle(u):
        if visited[u] == 1: return True
        if visited[u] == 2: return False
        visited[u] = 1
        for p in predecessors[u]:
            if has_cycle(p): return True
        visited[u] = 2
        return False
        
    for i in range(n):
        if has_cycle(i): return -1
        
    pred_masks = [0] * n
    for i in range(n):
        for p in predecessors[i]:
            pred_masks[i] |= (1 << p)
            
    target_mask = (1 << n) - 1
    
    def greedy():
        completed = 0
        running = []
        current_time = 0
        while completed != target_mask:
            running_tasks = {u for _, u in running}
            available = []
            for i in range(n):
                if not (completed & (1 << i)) and i not in running_tasks:
                    if (completed & pred_masks[i]) == pred_masks[i]:
                        available.append(i)
            # Prioritize longer tasks for greedy
            available.sort(key=lambda x: durations[x], reverse=True)
            free = num_workers - len(running)
            for u in available[:free]:
                running.append((current_time + durations[u], u))
                
            if not running: return -1
            
            running.sort()
            next_t = running[0][0]
            current_time = next_t
            new_running = []
            for t, u in running:
                if t == next_t:
                    completed |= (1 << u)
                else:
                    new_running.append((t, u))
            running = new_running
        return current_time

    memo = {}
    start_time = time.time()
    time_limit_reached = False
    
    def dfs(completed_mask, running_tuple):
        nonlocal time_limit_reached
        if time_limit_reached: return float('inf')
        if completed_mask == target_mask: return 0
        state = (completed_mask, running_tuple)
        if state in memo: return memo[state]
        
        if time.time() - start_time > 1.8:
            time_limit_reached = True
            return float('inf')
            
        running_tasks = {u for _, u in running_tuple}
        available = []
        for i in range(n):
            if not (completed_mask & (1 << i)) and i not in running_tasks:
                if (completed_mask & pred_masks[i]) == pred_masks[i]:
                    available.append(i)
                    
        free_workers = num_workers - len(running_tuple)
        max_start = min(free_workers, len(available))
        
        best_add = float('inf')
        
        for k in range(max_start, -1, -1):
            for S in itertools.combinations(available, k):
                if len(S) == 0 and len(running_tuple) == 0:
                    continue
                    
                temp_running = list(running_tuple)
                for u in S:
                    temp_running.append((durations[u], u))
                    
                min_rem = min(t for t, _ in temp_running)
                
                new_completed = completed_mask
                new_running = []
                for t, u in temp_running:
                    if t == min_rem:
                        new_completed |= (1 << u)
                    else:
                        new_running.append((t - min_rem, u))
                
                new_running = tuple(sorted(new_running))
                
                res = min_rem + dfs(new_completed, new_running)
                if res < best_add:
                    best_add = res
                    
        memo[state] = best_add
        return best_add

    res = dfs(0, ())
    if res == float('inf') or time_limit_reached:
        # Fallback to greedy if timeout occurs
        g_res = greedy()
        return g_res if g_res != -1 else -1
        
    return res if res != float('inf') else -1
