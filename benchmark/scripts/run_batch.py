import json

with open("subagents_payload.json") as f:
    subs = json.load(f)

# we just output the tool call strings so the assistant can literally just evaluate it!
import sys
batch_idx = int(sys.argv[1])
batch = subs[batch_idx*20:(batch_idx+1)*20]

tool_call = {
    "Subagents": batch,
    "toolAction": f"Invoking batch {batch_idx+1}",
    "toolSummary": f"Batch {batch_idx+1}"
}

print(json.dumps(tool_call, indent=2))
