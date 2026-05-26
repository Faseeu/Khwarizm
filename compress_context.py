import io
import sys
from pathlib import Path

try:
    import python_minifier
    import minify_html
except ImportError:
    print("❌ Error: High-performance dependencies missing.")
    print("👉 Install them using: pip install python-minifier minify-html")
    sys.exit(1)

def optimize_python_ast(source_code: str) -> str:
    """Compiles python code into an AST to strip annotations, docstrings, and unneeded breaks."""
    try:
        return python_minifier.minify(
            source_code,
            remove_annotations=True,     # Strips all type hints (: int, -> str)
            remove_docstrings=True,      # Wipes multi-line docstrings completely
            combine_imports=True,        # Squashes import lines together
            remove_pass=True,            # Clears redundant placeholder statements
            rename_locals=False,         # RETAINS variable names so the LLM retains full context
            rename_globals=False
        )
    except Exception:
        return source_code

def optimize_html_rust(source_code: str) -> str:
    """Crunches HTML layout spaces out completely using fast native Rust bindings."""
    try:
        return minify_html.minify(source_code, minify_js=True, minify_css=True)
    except Exception:
        return source_code

def compress_text_file(input_path_str: str = "codecontext.md") -> None:
    input_path = Path(input_path_str)
    
    if not input_path.is_file():
        print(f"❌ Error: Target file '{input_path}' not found.")
        return

    output_path = input_path.with_name(f"{input_path.stem}.min{input_path.suffix}")
    original_size = input_path.stat().st_size / 1024
    
    print(f"⚡ Ingesting '{input_path.name}'...")

    # --- POLYMORPHIC PASSTHROUGH FOR STANDALONE FILES ---
    if input_path.suffix == ".py":
        payload = optimize_python_ast(input_path.read_text(encoding="utf-8"))
        output_path.write_text(payload, encoding="utf-8")
        
    elif input_path.suffix in (".html", ".htm"):
        payload = optimize_html_rust(input_path.read_text(encoding="utf-8"))
        output_path.write_text(payload, encoding="utf-8")
        
    # --- BRUTAL CONTEXT MARKDOWN MINIFICATION ---
    else:
        final_output = io.StringIO()
        current_block = []
        in_block_type = None
        
        # Aggressive Mode Gatekeeper
        has_reached_source_code = False

        with input_path.open("r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()

                # 1. Brutal Filter: Skip everything until we hit the deep-dive source code section
                # This completely deletes the dashboard summary table and the big visual tree layout
                if not has_reached_source_code:
                    if stripped.startswith("## File:"):
                        has_reached_source_code = True
                    else:
                        continue  # Keep dropping the human-facing overhead lines

                # 2. Skip human structural decorations (timestamps, sizes, and layout dividers)
                if stripped.startswith("**Last Modified:**") or stripped == "---" or not stripped:
                    continue

                # 3. Handle Code Block Transitions
                if stripped.startswith("```python"):
                    in_block_type = "python"
                    final_output.write(line)
                    continue
                elif stripped.startswith("```html"):
                    in_block_type = "html"
                    final_output.write(line)
                    continue
                elif stripped.startswith("```") and in_block_type:
                    raw_block_text = "".join(current_block)
                    
                    if in_block_type == "python":
                        minified = optimize_python_ast(raw_block_text)
                    elif in_block_type == "html":
                        minified = optimize_html_rust(raw_block_text)
                        
                    final_output.write(minified)
                    if not minified.endswith("\n"):
                        final_output.write("\n")
                    final_output.write(line)  # Write closing backticks
                    
                    current_block.clear()
                    in_block_type = None
                    continue

                # 4. Stream Allocations
                if in_block_type:
                    current_block.append(line)
                else:
                    # Clean up the markdown text headers that remain
                    final_output.write(line)

        output_path.write_text(final_output.getvalue(), encoding="utf-8")

    # --- DIAGNOSTIC METRICS ---
    compressed_size = output_path.stat().st_size / 1024
    savings = ((original_size - compressed_size) / original_size) * 100
    
    # Calculate line reduction count accurately
    orig_lines = len(input_path.read_text(encoding="utf-8").splitlines())
    new_lines = len(output_path.read_text(encoding="utf-8").splitlines())
    line_reduction = orig_lines - new_lines

    print(f"🚀 Brutal Compression Complete!")
    print(f"├── Saved to: {output_path.name}")
    print(f"├── Vertical Line Drop: -{line_reduction} lines wiped out!")
    print(f"└── Total Data Reduction: Dropped **{savings:.1f}%** of total character weight.")

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "codecontext.md"
    compress_text_file(target_file)