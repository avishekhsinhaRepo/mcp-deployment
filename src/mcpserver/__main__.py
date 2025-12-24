import sys
from mcpserver.server import mcp

def main():
    # Ensure clean stdio for JSON-RPC communication
    sys.stderr = sys.__stderr__
    mcp.run()

if __name__ == "__main__":
    main()
