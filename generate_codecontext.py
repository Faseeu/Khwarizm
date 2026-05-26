from pathlib import Path
from typing import Dict, List, Set

def generate_context() -> None:
    output_file = Path("codecontext.md")
    project_root = Path(".")
    
    # 1. Configuration & Rules
    ignore_dirs: Set[str] = {
        '__pycache__', 'tests', 'venv', '.venv', '.git', 
        '.env', '.ephemeral_venv', '.temp_venv', '.idea', '.vscode'
    }
    allowed_extensions: Set[str] = {'.py', '.md', '.txt', '.html', '.json', '.yaml', '.yml'}
    
    lang_mapping: Dict[str, str] = {
        '.py': 'python',
        '.html': 'html',
        '.md': 'markdown',
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml'
    }

    # Tracking metrics for the top header summary
    total_files_scanned = 0
    total_lines_scanned = 0
    
    tree_lines: List[str] = ["# Project Architecture\n\n```text\n"]
    context_lines: List[str] = ["\n# Source Code Deep-Dive\n\n"]

    # 2. Build the Visual Tree Structure (Recursive Helper for Perfect Box-Drawing)
    def build_tree(dir_path: Path, prefix: str = "") -> None:
        nonlocal total_files_scanned, total_lines_scanned
        
        # Gather and sort directory contents (directories first, then files)
        try:
            entries = sorted(
                [e for e in dir_path.iterdir() if e.name not in ignore_dirs and not e.name.startswith('.')],
                key=lambda e: (e.is_file(), e.name.lower())
            )
        except PermissionError:
            return

        for i, entry in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = "└── " if is_last else "├── "
            
            if entry.is_dir():
                tree_lines.append(f"{prefix}{connector}{entry.name}/\n")
                # Extend the prefix bar for nested children
                next_prefix = prefix + ("    " if is_last else "│   ")
                build_tree(entry, next_prefix)
            
            elif entry.is_file():
                tree_lines.append(f"{prefix}{connector}{entry.name}\n")
                
                # Append file content context if extension matches rules
                if entry.suffix in allowed_extensions and entry != output_file:
                    total_files_scanned += 1
                    lang = lang_mapping.get(entry.suffix, 'text')
                    
                    context_lines.append(f"## File: `{entry.as_posix()}`\n")
                    context_lines.append(f"Content Type: `{lang.upper()}`\n\n```{lang}\n")
                    
                    try:
                        content = entry.read_text(encoding="utf-8")
                        total_lines_scanned += len(content.splitlines())
                        context_lines.append(content)
                    except Exception as e:
                        context_lines.append(f"// Error reading file: {e}")
                        
                    context_lines.append("\n```\n\n---\n\n")

    # 3. Process Architecture & File Writes
    tree_lines.append(f"{project_root.resolve().name}/\n")
    build_tree(project_root)
    tree_lines.append("```\n")

    # 4. Generate the High-Value Analytics Summary Header
    summary_header = (
        f"# System Context Report\n\n"
        f"| Metric | Status / Value |\n"
        f"| :--- | :--- |\n"
        f"| **Scanned Files** | {total_files_scanned} source targets |\n"
        f"| **Total Source Lines** | {total_lines_scanned} lines parsed |\n"
        f"| **Target Environment** | Minimalist Agent Framework (Khwarizm) |\n\n"
        f"---\n\n"
    )

    # Compile and stream everything to disk instantly
    full_payload = summary_header + "".join(tree_lines + context_lines)
    output_file.write_text(full_payload, encoding="utf-8")
    
    print(f"🚀 Context perfectly mapped into {output_file} ({total_files_scanned} files, {total_lines_scanned} lines processed).")

if __name__ == "__main__":
    generate_context()