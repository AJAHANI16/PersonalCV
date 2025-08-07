#!/usr/bin/env python3
"""
Development server script for PersonalCV
Serves the website locally with live reload capabilities
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time
from pathlib import Path

class CVHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.dirname(__file__)), **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser(url, delay=1):
    """Open browser after a short delay"""
    time.sleep(delay)
    webbrowser.open(url)

def main():
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            sys.exit(1)
    
    # Change to the project root directory
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    handler = CVHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            url = f"http://localhost:{port}"
            print(f"🚀 PersonalCV Development Server")
            print(f"📂 Serving from: {project_root}")
            print(f"🌐 URL: {url}")
            print(f"📱 Mobile URL: http://0.0.0.0:{port}")
            print(f"⏹️  Press Ctrl+C to stop")
            
            # Open browser in a separate thread
            browser_thread = threading.Thread(target=open_browser, args=(url,))
            browser_thread.daemon = True
            browser_thread.start()
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n👋 Development server stopped")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python3 scripts/dev-server.py {port + 1}")
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()