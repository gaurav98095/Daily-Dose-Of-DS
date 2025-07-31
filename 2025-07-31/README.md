

## Graph ML – 6 Graph Feature Engineering Techniques
### 1–3) Node Degree Features

Measure direct connectivity of nodes:

* **In-Degree:** Number of incoming edges (followers) → indicates influence.
* **Out-Degree:** Number of outgoing edges (followings) → indicates activity.
* **Total Degree:** Sum of in-degree and out-degree.

```python
G.in_degree(x)    # Followers of node x
G.out_degree(x)   # Followings of node x
G.degree(x)       # Total degree of node x
```

---

### 4–6) Node Centrality Features

Capture influence based on network position:

* **Betweenness Centrality:** How often a node appears on shortest paths.

  > Identifies “bridge” nodes in information flow.
* **Closeness Centrality:** How close a node is to others via shortest paths.

  > Higher values → faster information spread.
* **Eigenvector Centrality:** Measures influence based on connections to other influential nodes.

  > Captures both direct and indirect influence.


## 100% private Agentic RAG API
```bash
pip install crewai crewai-tools litserve
ollama pull qwen3
python server.py
python client.py --query "What is the Qwen3?"
```