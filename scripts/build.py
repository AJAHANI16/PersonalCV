#!/usr/bin/env python3
"""
Build script for PersonalCV
Optimizes assets, minifies CSS/JS, and prepares for deployment
"""

import os
import sys
import shutil
import json
import re
from pathlib import Path
from datetime import datetime

def minify_css(css_content):
    """Simple CSS minification"""
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove extra whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    # Remove whitespace around special characters
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
    return css_content.strip()

def minify_js(js_content):
    """Simple JavaScript minification"""
    # Remove single-line comments
    js_content = re.sub(r'//.*?$', '', js_content, flags=re.MULTILINE)
    # Remove multi-line comments
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    # Remove extra whitespace
    js_content = re.sub(r'\s+', ' ', js_content)
    return js_content.strip()

def build_project():
    """Build the PersonalCV project"""
    project_root = Path(__file__).parent.parent
    build_dir = project_root / "build"
    
    print("🏗️  Building PersonalCV...")
    
    # Create build directory
    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir()
    
    # Copy HTML files
    print("📄 Copying HTML files...")
    for html_file in project_root.glob("*.html"):
        shutil.copy2(html_file, build_dir)
    
    # Process CSS files
    print("🎨 Processing CSS files...")
    css_dir = build_dir / "css"
    css_dir.mkdir()
    
    for css_file in (project_root / "css").glob("*.css"):
        with open(css_file, 'r') as f:
            css_content = f.read()
        
        minified_css = minify_css(css_content)
        
        with open(css_dir / css_file.name, 'w') as f:
            f.write(minified_css)
    
    # Process JavaScript files if they exist
    if (project_root / "js").exists():
        print("⚡ Processing JavaScript files...")
        js_dir = build_dir / "js"
        js_dir.mkdir()
        
        for js_file in (project_root / "js").glob("*.js"):
            with open(js_file, 'r') as f:
                js_content = f.read()
            
            minified_js = minify_js(js_content)
            
            with open(js_dir / js_file.name, 'w') as f:
                f.write(minified_js)
    
    # Copy images
    if (project_root / "images").exists():
        print("🖼️  Copying images...")
        shutil.copytree(project_root / "images", build_dir / "images")
    
    # Copy assets if they exist
    if (project_root / "assets").exists():
        print("📦 Copying assets...")
        shutil.copytree(project_root / "assets", build_dir / "assets")
    
    # Generate build info
    build_info = {
        "build_time": datetime.now().isoformat(),
        "version": "1.0.0",
        "files": [str(f.relative_to(build_dir)) for f in build_dir.rglob("*") if f.is_file()]
    }
    
    with open(build_dir / "build-info.json", 'w') as f:
        json.dump(build_info, f, indent=2)
    
    print(f"✅ Build complete! Output in: {build_dir}")
    print(f"📊 Built {len(build_info['files'])} files")
    
    return build_dir

def deploy_to_github_pages():
    """Deploy to GitHub Pages"""
    build_dir = build_project()
    
    print("🚀 Preparing for GitHub Pages deployment...")
    
    # Create .nojekyll file to bypass Jekyll processing
    (build_dir / ".nojekyll").touch()
    
    print("📝 Instructions for GitHub Pages deployment:")
    print("1. Copy all files from the build/ directory to your gh-pages branch")
    print("2. Or use: git subtree push --prefix build origin gh-pages")
    print("3. Enable GitHub Pages in your repository settings")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "deploy":
        deploy_to_github_pages()
    else:
        build_project()

if __name__ == "__main__":
    main()