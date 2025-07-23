import asyncio

from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

async def main():
    config = {
        "mcpServers": {
            "stagehand": {
                "command": "node",
                "args": ["path/to/stagehand/dist/index.js"],
                "env": {
                    "LOCAL_CDP_URL": "http://localhost:9222",
                    "DOWNLOADS_DIR": "/Downloads/stagehand"
                }
            }
        }
    }

    # Create agent with the MCP Client
    agent = MCPAgent(
        llm=ChatOllama(model="qwen3"),
        client=MCPClient.from_dict(config)
    )

    result = await agent.run(
        "Chances of rain in Tokyo tomorrow",
    )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
