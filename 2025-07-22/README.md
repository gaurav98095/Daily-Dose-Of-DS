

## Apply LLM To Audio : AssemblyAI


* **Speech-to-Text**: Converts audio into accurate text using advanced LLMs.
* **Speaker Diarization**: Identifies who is speaking in multi-speaker audio.
* **Summarization**: Generates concise summaries of conversations or recordings.
* **Topic Detection**: Extracts main topics discussed in the audio.
* **Sentiment Analysis**: Detects emotions and sentiment in speech.
* **Entity & Keyword Detection**: Identifies names, brands, and key terms.
* **Simple API**: Easy-to-integrate REST API for developers.
* **Use Cases**: Ideal for meetings, podcasts, customer calls, and more.

🔗 **Code File**: [assemblyai.py](./assemblyai.py)

## 4 stages of training LLMs from scratch


### **Stage 0: Randomly Initialized Model**

* **Description**: This is the starting point. The model weights are randomly initialized.
* **State**: It has no knowledge of language, grammar, facts, or reasoning.
* **Purpose**: To provide a clean slate for learning from large text data.
* **Characteristics**:

  * Parameters are untrained.
  * Outputs are essentially noise.
  * Model has no idea what a sentence is.



### **Stage 1: Pre-training**

* **Description**: Train the model on a massive amount of unlabelled text using self-supervised learning (e.g., masked language modeling or next token prediction).
* **Objective**: Learn general representations of language (syntax, semantics, world knowledge).
* **Dataset**: Web pages, books, articles, code, Wikipedia, etc.
* **Training Type**: Unsupervised or self-supervised.
* **Output**:

  * Model understands basic sentence structure and grammar.
  * Knows facts, names, common sense, and some reasoning patterns.
  * Still not aligned with human instructions or intent.



### **Stage 2: Instruction Finetuning (SFT – Supervised Finetuning)**

* **Description**: Teach the model how to follow specific instructions using human-labeled input-output pairs.
* **Dataset**: Curated instruction-response datasets (e.g., "Summarize this article", "Translate to French", etc.).
* **Objective**: Make the model usable for specific tasks.
* **Output**:

  * Model learns to follow prompts and give task-specific responses.
  * Becomes useful for general-purpose querying.
  * However, may still produce verbose, unsafe, or biased answers.



### **Stage 3: Preference Finetuning (RLHF – Reinforcement Learning from Human Feedback)**

* **Description**: Use human feedback to shape model behavior using reward signals.
* **Process**:

  1. Generate multiple completions for a prompt.
  2. Humans rank them based on quality.
  3. Train a **reward model** on those rankings.
  4. Use reinforcement learning (e.g., PPO) to align the model with human preferences.
* **Goal**: Improve helpfulness, safety, tone, and alignment with user intent.
* **Output**:

  * More polite, accurate, and safer responses.
  * Less hallucination and more user-aligned behavior.


### **Stage 4: Reasoning Finetuning**

* **Description**: Specialized training to boost the model’s reasoning abilities (e.g., math, logic, coding, chain-of-thought).
* **Method**:

  * Curated datasets with multi-step reasoning problems.
  * Chain-of-thought prompting.
  * Few-shot or instruction-based logic tasks.
* **Goal**: Improve performance on benchmarks like GSM8K, MATH, or reasoning-heavy tasks.
* **Output**:

  * Stronger logical coherence.
  * Better step-by-step reasoning.
  * Improved capability for advanced tasks like code synthesis, theorem proving, etc.


## Tool Calling In LLM
- LLM may need to invoke external tools or APIs to perform specific tasks beyond its built-in capabilities.

Let's implement tool calling from scratch:
🔗 **Code File**: [tool_calling.py](./tool_calling.py)