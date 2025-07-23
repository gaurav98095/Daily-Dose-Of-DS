
## Connect Any LLM To MCP

Most developers use MCPs via closed-source tools like Claude or Cursor — but you don’t have to.

With the open-source `mcp-use` library, you can connect **any LLM** (like Qwen, via Ollama or LangChain) to **any MCP server** and build custom Agents without relying on Claude/Cursor.

### Example: Connecting Qwen 3 to Stagehand MCP for browser access

Just 3 simple steps:

1. Import `MCPAgent` and `MCPClient` from `mcp-use`.
2. Define your MCP config (same style as Cursor).
3. Create an Agent with your LLM and config-based Client.

That’s it! Now your Agent can invoke MCP tools just like Cursor does.

### Key features:

* Works with LangChain, Ollama, and more
* Run MCP servers in a sandboxed local setup
* Connect to multiple MCP servers
* Async streaming support
* Tool-level access control
* Built-in debugging mode

This is the easiest way to build fully local, private MCP Agents.


## Why don't we invoke model.forward() in PyTorch?


We use `model(input)` instead of `model.forward(input)` because PyTorch models implement the `__call__()` method, which wraps `forward()` and adds **important functionality** like hooks, pre/post-processing, and mode checks.

### How it works

#### 1. **`nn.Module` defines `__call__`**

When you do `model(x)`, it runs:

```python
def __call__(self, *input, **kwargs):
    # (1) Handle hooks
    # (2) Run self.forward(*input, **kwargs)
    # (3) More internal logic
```

This means:

```python
model(x)   # Recommended
model.forward(x)   # Skips hooks & logic
```


### Example

```python
import torch.nn as nn

class MyModel(nn.Module):
    def forward(self, x):
        print("Inside forward")
        return x * 2

model = MyModel()

# This calls __call__, which internally calls forward
out = model(torch.tensor([1]))  #  Uses __call__
# Output: Inside forward

# This bypasses __call__, and directly calls forward
out2 = model.forward(torch.tensor([1]))  #  Not recommended
# Output: Inside forward
```
