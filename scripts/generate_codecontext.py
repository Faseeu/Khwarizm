import datetime
from pathlib import Path
from typing import Dict, List, Set

def generate_context() -> None:
    output_file = Path("docs/codecontext.md")
    project_root = Path("../")
    
    # --- CONFIGURATION & SAFETY SAFETY VALVES ---
    MAX_FILE_SIZE_BYTES = 200 * 1024  # 200 KB individual file ceiling guard
    
    ignore_dirs: Set[str] = {
        '__pycache__', 'tests', 'venv', '.venv', '.git', 
        '.env', '.ephemeral_venv', '.temp_venv', '.idea',
        '.vscode','.agent_projects','scripts','assets','in_beta'
    }
    ignore_files: Set[str] = {
        'codecontext.md',
        'problems.md',
        'project_structure.html',
        'context.md',
        'Agent1_memory.json',
        'main2.py',
        
    }

    allowed_extensions: Set[str] = {'.py', '.md', '.txt', '.html', '.yaml', '.yml'}
    
    lang_mapping: Dict[str, str] = {
        '.py': 'python', '.html': 'html', '.md': 'markdown',
        '.json': 'json', '.yaml': 'yaml', '.yml': 'yaml'
    }

    # Reporting Metrics
    total_files_scanned = 0
    total_lines_scanned = 0
    truncated_files_count = 0
    
    tree_lines: List[str] = ["# Project Architecture\n\n```text\n"]
    context_lines: List[str] = ["\n# Source Code Deep-Dive\n\n"]

    # --- RECURSIVE ENGINE WITH TIMESTAMPS & SIZE CHECKS ---
    def build_tree(dir_path: Path, prefix: str = "") -> None:
        nonlocal total_files_scanned, total_lines_scanned, truncated_files_count
        
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
            
            # Fetch last modified timestamp dynamically
            mtime = entry.stat().st_mtime
            timestamp = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
            
            if entry.is_dir():
                tree_lines.append(f"{prefix}{connector}{entry.name}/ [{timestamp}]\n")
                next_prefix = prefix + ("    " if is_last else "│   ")
                build_tree(entry, next_prefix)
            
            elif entry.is_file():
                file_size_kb = entry.stat().st_size / 1024
                tree_lines.append(f"{prefix}{connector}{entry.name} ({file_size_kb:.1f} KB) [{timestamp}]\n")
                
                # Content Processing Block
                if entry.suffix in allowed_extensions and entry.name not in ignore_files:
                    total_files_scanned += 1
                    lang = lang_mapping.get(entry.suffix, 'text')
                    
                    # Structural Markdown Title
                    context_lines.append(f"## File: `{entry.as_posix()}`\n")
                    context_lines.append(f"**Last Modified:** `{timestamp}` | **Size:** `{file_size_kb:.2f} KB`\n\n")
                    
                    # AI-Directives: XML opening anchor tags for crisp context parsing
                    context_lines.append(f'<file path="{entry.as_posix()}" type="{lang}">\n```{lang}\n')
                    
                    # Enforce Maximum File Size Limit Guard
                    if entry.stat().st_size > MAX_FILE_SIZE_BYTES:
                        context_lines.append(f"// [SYSTEM WARNING: File content truncated. Exceeds safely limit of {MAX_FILE_SIZE_BYTES // 1024} KB]\n")
                        truncated_files_count += 1
                    else:
                        try:
                            content = entry.read_text(encoding="utf-8")
                            total_lines_scanned += len(content.splitlines())
                            context_lines.append(content)
                        except Exception as e:
                            context_lines.append(f"// Error reading file contents: {e}")
                    
                    # AI-Directives: XML closing tags
                    context_lines.append(f'\n```\n</file>\n\n---\n\n')

    # Run the builder
    root_timestamp = datetime.datetime.fromtimestamp(project_root.resolve().stat().st_mtime).strftime('%Y-%m-%d %H:%M')
    tree_lines.append(f"{project_root.resolve().name}/ [{root_timestamp}]\n")
    build_tree(project_root)
    tree_lines.append("```\n")

    # --- SUMMARY DASHBOARD GENERATION ---
    summary_header = (
        f"# System Context Report\n\n"
        f"| Metric | Status / Value |\n"
        f"| :--- | :--- |\n"
        f"| **Scanned Files** | {total_files_scanned} source targets |\n"
        f"| **Total Lines Parsed** | {total_lines_scanned} lines processed |\n"
        f"| **Truncated Safety Alerts** | {truncated_files_count} files skipped |\n"
        f"| **Target Environment** | Minimalist Agent Framework (Khwarizm) |\n\n"
        f"---\n\n"
    )

    # Fast Single-Pass RAM Array compilation to Disk
    full_payload = summary_header + "".join(tree_lines + context_lines)
    output_file.write_text(full_payload, encoding="utf-8")
    
    print(f"🚀 Context completely mapped into {output_file} | Total Lines: {total_lines_scanned} | Truncated: {truncated_files_count}")

if __name__ == "__main__":
    generate_context()