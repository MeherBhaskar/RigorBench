import heapq
import time
import random

def solve(tasks_info, num_workers):
    # tasks_info: dict id -> (duration, [pre])
    
    # check cycles
    in_degree = {tid: len(info[1]) for tid, info in tasks_info.items()}
    adj = {tid: [] for tid in tasks_info}
    for tid, info in tasks_info.items():
        for p in info[1]:
            adj[p].append(tid)
            
    q = [tid for tid, deg in in_degree.items() if deg == 0]
    visited = 0
    while q:
        curr = q.pop(0)
        visited += 1
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
                
    if visited != len(tasks_info):
        return -1

    # map tids to 0..N-1
    tids = list(tasks_info.keys())
    tid_to_idx = {tid: i for i, tid in enumerate(tids)}
    N = len(tids)
    
    durations = [tasks_info[tid][0] for tid in tids]
    pre_masks = [0] * N
    for i, tid in enumerate(tids):
        for p in tasks_info[tid][1]:
            pre_masks[i] |= (1 << tid_to_idx[p])
            
    pq = [(0, 0, ())] # time, completed, active (tuple of (rem, idx))
    visited_states = set()
    
    target_mask = (1 << N) - 1
    
    states_visited = 0
    
    while pq:
        curr_time, completed, active = heapq.heappop(pq)
        
        state = (completed, active)
        if state in visited_states:
            continue
        visited_states.add(state)
        states_visited += 1
        
        if completed == target_mask:
            print(f"States visited: {states_visited}")
            return curr_time
            
        free_workers = num_workers - len(active)
        
        active_mask = 0
        for rem, idx in active:
            active_mask |= (1 << idx)
            
        # option 1: start a task
        if free_workers > 0:
            for i in range(N):
                if not (completed & (1 << i)) and not (active_mask & (1 << i)):
                    if (completed & pre_masks[i]) == pre_masks[i]:
                        new_active = tuple(sorted(active + ((durations[i], i),)))
                        new_state = (completed, new_active)
                        if new_state not in visited_states:
                            heapq.heappush(pq, (curr_time, completed, new_active))
                            
        # option 2: advance time
        if active:
            dt = active[0][0]
            new_completed = completed
            new_active = []
            for rem, idx in active:
                if rem == dt:
                    new_completed |= (1 << idx)
                else:
                    new_active.append((rem - dt, idx))
            new_active = tuple(new_active)
            new_state = (new_completed, new_active)
            if new_state not in visited_states:
                heapq.heappush(pq, (curr_time + dt, new_completed, new_active))

    return -1

# Generate a complex test case
random.seed(42)
N = 15
tasks = {}
for i in range(N):
    dur = random.randint(1, 100)
    pre = []
    for j in range(i):
        if random.random() < 0.2:
            pre.append(str(j))
    tasks[str(i)] = (dur, pre)

t0 = time.time()
print(solve(tasks, 5))
print(f"Time: {time.time() - t0}")

