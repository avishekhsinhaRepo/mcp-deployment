import asyncio
from mcpserver.server import mcp

def main():
    asyncio.run(mcp.run(transport="stdio"))

if __name__ == "__main__":
    main()
