import heapq
from itertools import combinations
import math

def min_completion_time(tasks: list[dict], num_workers: int) -> int:
    n = len(tasks)
    if n == 0:
        return 0
        
    task_index = {t["id"]: i for i, t in enumerate(tasks)}
    
    # Check validity of prerequisites
    for t in tasks:
        for p in t["prerequisites"]:
            if p not in task_index:
                return -1

    durations = [0] * n
    prereqs = [0] * n
    prereqs_list = [[] for _ in range(n)]
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for t in tasks:
        idx = task_index[t["id"]]
        durations[idx] = t["duration"]
        mask = 0
        for p in t["prerequisites"]:
            pidx = task_index[p]
            mask |= (1 << pidx)
            prereqs_list[idx].append(pidx)
            adj[pidx].append(idx)
            in_degree[idx] += 1
        prereqs[idx] = mask

    # Topological sort for cycle detection and to get top_order
    q = [i for i in range(n) if in_degree[i] == 0]
    top_order = []
    while q:
        curr = q.pop(0)
        top_order.append(curr)
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
                
    if len(top_order) != n:
        return -1
        
    def get_h(completed, active_tuple):
        active_dict = dict(active_tuple)
        EC = [0] * n
        total_work = 0
        for i in top_order:
            if (completed & (1 << i)):
                continue
                
            est = 0
            for p_idx in prereqs_list[i]:
                if not (completed & (1 << p_idx)):
                    est = max(est, EC[p_idx])
                    
            if i in active_dict:
                rem = active_dict[i]
                EC[i] = est + rem
                total_work += rem
            else:
                dur = durations[i]
                EC[i] = est + dur
                total_work += dur
                
        h1 = max(EC) if EC else 0
        h2 = math.ceil(total_work / num_workers)
        return max(h1, h2)

    start_active = ()
    start_completed = 0
    start_time = 0
    start_h = get_h(start_completed, start_active)
    
    pq = [(start_h, start_time, start_completed, start_active)]
    visited = {}
    
    all_completed_mask = (1 << n) - 1

    while pq:
        f, time, completed, active = heapq.heappop(pq)
        
        if completed == all_completed_mask:
            return time
            
        state_key = (completed, active)
        if state_key in visited and visited[state_key] <= time:
            continue
        visited[state_key] = time
        
        num_free = num_workers - len(active)
        active_ids = {task_idx for task_idx, _ in active}
        
        ready = []
        for i in range(n):
            if not (completed & (1 << i)) and i not in active_ids:
                if (completed & prereqs[i]) == prereqs[i]:
                    ready.append(i)
                    
        max_start = min(num_free, len(ready))
        
        for k in range(max_start + 1):
            if k == 0 and len(active) == 0:
                continue
                
            for subset in combinations(ready, k):
                new_active = list(active)
                for task_idx in subset:
                    new_active.append((task_idx, durations[task_idx]))
                    
                if not new_active:
                    continue
                    
                time_step = min(rem for idx, rem in new_active)
                
                next_active = []
                next_completed = completed
                
                for idx, rem in new_active:
                    if rem == time_step:
                        next_completed |= (1 << idx)
                    else:
                        next_active.append((idx, rem - time_step))
                        
                next_active.sort()
                next_active_tuple = tuple(next_active)
                
                next_time = time + time_step
                
                next_state_key = (next_completed, next_active_tuple)
                if next_state_key not in visited or visited[next_state_key] > next_time:
                    h = get_h(next_completed, next_active_tuple)
                    heapq.heappush(pq, (next_time + h, next_time, next_completed, next_active_tuple))

    return -1
