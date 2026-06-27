import itertools

def min_completion_time(tasks: list[dict], num_workers: int) -> int:
    if not tasks:
        return 0
        
    n = len(tasks)
    
    # Map task id to integer index
    id_to_idx = {task["id"]: i for i, task in enumerate(tasks)}
    
    durations = [0] * n
    prereq_masks = [0] * n
    
    for i, task in enumerate(tasks):
        durations[i] = task["duration"]
        for p in task["prerequisites"]:
            if p not in id_to_idx:
                return -1 # Invalid prereq
            prereq_masks[i] |= (1 << id_to_idx[p])
            
    # Check for cycles
    visited = [0] * n
    def has_cycle(u):
        if visited[u] == 1:
            return True
        if visited[u] == 2:
            return False
        visited[u] = 1
        for v in range(n):
            if (prereq_masks[u] & (1 << v)):
                if has_cycle(v):
                    return True
        visited[u] = 2
        return False
        
    for i in range(n):
        if has_cycle(i):
            return -1
            
    memo = {}
    target_completed_mask = (1 << n) - 1
    
    def solve(completed_mask, running):
        # running is a tuple of (task_idx, time_remaining) sorted by task_idx
        state = (completed_mask, running)
        if state in memo:
            return memo[state]
            
        if completed_mask == target_completed_mask:
            return 0
            
        free_workers = num_workers - len(running)
        
        # Find available tasks
        avail = []
        if free_workers > 0:
            for i in range(n):
                if not (completed_mask & (1 << i)):
                    # Not completed
                    is_running = any(r[0] == i for r in running)
                    if not is_running:
                        # Prereqs met?
                        if (prereq_masks[i] & completed_mask) == prereq_masks[i]:
                            avail.append(i)
                            
        min_cost = float('inf')
        
        max_to_start = min(free_workers, len(avail))
        
        for k in range(max_to_start + 1):
            for subset in itertools.combinations(avail, k):
                new_running = list(running) + [(idx, durations[idx]) for idx in subset]
                
                if not new_running:
                    continue
                    
                min_rem = min(r[1] for r in new_running)
                
                next_running = []
                next_completed_mask = completed_mask
                
                for r in new_running:
                    rem = r[1] - min_rem
                    if rem == 0:
                        next_completed_mask |= (1 << r[0])
                    else:
                        next_running.append((r[0], rem))
                        
                next_running.sort(key=lambda x: x[0])
                next_running_tuple = tuple(next_running)
                
                cost = min_rem + solve(next_completed_mask, next_running_tuple)
                if cost < min_cost:
                    min_cost = cost
                    
        memo[state] = min_cost
        return min_cost
        
    ans = solve(0, ())
    return ans if ans != float('inf') else -1
