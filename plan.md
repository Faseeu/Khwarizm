# Project Cleanup and Categorization Plan

The root directory has become cluttered. This plan outlines the migration of files into logical subdirectories to maintain the `Khwarizm` project structure.

## 1. Categorization Strategy
- **Core Orchestration**: Keep `main.py`, `main2.py`, and `workflow.py` in the root.
- **Documentation**: Move all `.md` and `.html` files into a `/docs` directory.
- **Scripts/Utilities**: Move `generate_codecontext.py` and `compress_context.py` into a `/scripts` directory.
- **Project Assets**: Move `.png` and `.mermaid` files into an `/assets` directory.
- **Agent Memory**: Move `Agent1_memory.json` into the `/memory` directory.

## 2. Execution Steps
1. Create `/docs`, `/scripts`, and `/assets` directories.
2. Relocate files using shell commands.
3. Update imports in `main.py` and related files to reflect the new paths.
4. Verify system integrity by running the agent.

## 3. Immediate Actions
- [ ] Create directory structure.
- [ ] Execute `mv` commands for identified files.
- [ ] Run a test to ensure the agent still initializes correctly.