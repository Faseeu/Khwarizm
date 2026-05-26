# System Context Report

| Metric | Status / Value |
| :--- | :--- |
| **Scanned Files** | 94 source targets |
| **Total Lines Parsed** | 10633 lines processed |
| **Truncated Safety Alerts** | 0 files skipped |
| **Target Environment** | Minimalist Agent Framework (Khwarizm) |

---

# Project Architecture

```text
projects/ [2026-05-23 09:25]
├── Database Project/ [2026-05-25 07:50]
│   ├── ai_agent_system/ [2026-05-23 18:50]
│   │   ├── data/ [2026-05-23 14:38]
│   │   │   ├── __init__.py (0.0 KB) [2026-05-23 12:35]
│   │   │   └── sample_data.py (11.1 KB) [2026-05-23 14:28]
│   │   ├── database/ [2026-05-23 12:29]
│   │   │   ├── __init__.py (0.0 KB) [2026-05-23 09:28]
│   │   │   ├── config.py (0.2 KB) [2026-05-23 12:28]
│   │   │   ├── connection.py (1.3 KB) [2026-05-23 14:23]
│   │   │   └── setup.py (0.0 KB) [2026-05-23 09:28]
│   │   ├── pages/ [2026-05-23 12:38]
│   │   │   ├── __init__.py (0.0 KB) [2026-05-23 09:28]
│   │   │   ├── agents.py (4.7 KB) [2026-05-23 18:48]
│   │   │   ├── logs.py (5.2 KB) [2026-05-23 18:50]
│   │   │   ├── memory.py (4.5 KB) [2026-05-23 18:48]
│   │   │   ├── sessions.py (4.1 KB) [2026-05-23 18:50]
│   │   │   ├── tasks.py (5.5 KB) [2026-05-23 18:48]
│   │   │   ├── tool_usage.py (3.8 KB) [2026-05-23 18:50]
│   │   │   ├── tools.py (4.0 KB) [2026-05-23 18:48]
│   │   │   └── users.py (3.8 KB) [2026-05-23 18:47]
│   │   ├── app.py (44.9 KB) [2026-05-23 18:47]
│   │   ├── requirements.txt (0.0 KB) [2026-05-23 09:28]
│   │   ├── test_connection.py (2.7 KB) [2026-05-23 12:29]
│   │   └── utils.py (8.5 KB) [2026-05-23 18:47]
│   ├── ai_agent_system.zip (73.6 KB) [2026-05-23 19:56]
│   └── mysql_setup.sh (4.0 KB) [2026-05-23 10:28]
├── Khwarizm/ [2026-05-26 13:08]
│   ├── agents/ [2026-05-25 12:05]
│   │   ├── __init__.py (0.0 KB) [2026-05-19 11:39]
│   │   ├── baseagent.py (6.6 KB) [2026-05-26 06:47]
│   │   └── config.py (1.1 KB) [2026-05-25 12:48]
│   ├── assets/ [2026-05-26 13:06]
│   │   ├── architecture_flow.mermaid (1.4 KB) [2026-05-21 08:45]
│   │   └── baseagent.png (4034.3 KB) [2026-05-21 08:22]
│   ├── docs/ [2026-05-26 13:07]
│   │   ├── codecontext.md (401.5 KB) [2026-05-26 13:08]
│   │   ├── codecontext.min.md (85.7 KB) [2026-05-26 07:32]
│   │   ├── context.md (27.1 KB) [2026-05-25 11:45]
│   │   ├── problems.md (21.7 KB) [2026-05-25 13:09]
│   │   ├── project_structure.html (1.6 KB) [2026-05-23 08:29]
│   │   ├── project_structure.txt (0.9 KB) [2026-05-23 08:27]
│   │   └── report.md (1.8 KB) [2026-05-23 07:35]
│   ├── llms/ [2026-05-16 12:53]
│   │   ├── __init__.py (0.1 KB) [2026-05-09 07:26]
│   │   ├── basellm.py (0.1 KB) [2026-05-26 07:06]
│   │   ├── geminiclient.py (0.9 KB) [2026-05-16 14:30]
│   │   └── groqclient.py (0.8 KB) [2026-05-19 11:43]
│   ├── memory/ [2026-05-26 13:06]
│   │   ├── __init__.py (0.0 KB) [2026-05-15 18:13]
│   │   ├── Agent1_memory.json (18.7 KB) [2026-05-26 13:04]
│   │   ├── ltm.py (1.5 KB) [2026-05-26 06:44]
│   │   ├── memory.py (0.5 KB) [2026-05-15 18:30]
│   │   └── stm.py (0.8 KB) [2026-05-26 06:31]
│   ├── scripts/ [2026-05-26 13:06]
│   │   ├── __init__.py (0.0 KB) [2026-05-09 20:19]
│   │   ├── compress_context.py (5.4 KB) [2026-05-26 07:30]
│   │   └── generate_codecontext.py (5.1 KB) [2026-05-26 13:08]
│   ├── skills/ [2026-05-26 08:56]
│   │   ├── llm_client_skill.md (1.9 KB) [2026-05-26 08:55]
│   │   └── toolSkill.md (1.7 KB) [2026-05-26 08:41]
│   ├── tools/ [2026-05-26 09:12]
│   │   ├── agent_made/ [2026-05-25 07:44]
│   │   │   ├── __init__.py (0.0 KB) [2026-05-23 07:04]
│   │   │   ├── directory_watcher.py (0.6 KB) [2026-05-23 07:18]
│   │   │   ├── git_manager.py (1.0 KB) [2026-05-23 07:18]
│   │   │   ├── light_python_runner.py (1.3 KB) [2026-05-23 07:21]
│   │   │   └── terminal_executor.py (0.9 KB) [2026-05-23 07:04]
│   │   ├── __init__.py (0.2 KB) [2026-05-16 06:08]
│   │   ├── basetool.py (0.8 KB) [2026-05-25 11:45]
│   │   ├── calculator.py (0.6 KB) [2026-05-22 18:22]
│   │   ├── filereader.py (0.8 KB) [2026-05-22 18:29]
│   │   ├── filewriter.py (1.3 KB) [2026-05-25 11:45]
│   │   ├── in_process_runner_tool.py (12.9 KB) [2026-05-26 09:11]
│   │   ├── project_runner.py (35.5 KB) [2026-05-26 12:49]
│   │   ├── registry.py (0.6 KB) [2026-05-22 18:33]
│   │   └── s.txt (0.1 KB) [2026-05-25 07:42]
│   ├── utils/ [2026-05-19 12:10]
│   │   └── chat_ui.py (0.4 KB) [2026-05-19 11:41]
│   ├── Agent1_memory.json (19.2 KB) [2026-05-26 13:06]
│   ├── main.py (4.3 KB) [2026-05-26 13:04]
│   ├── main2.py (4.2 KB) [2026-05-23 07:13]
│   ├── plan.md (1.1 KB) [2026-05-26 13:05]
│   ├── README.md (22.3 KB) [2026-05-21 09:24]
│   ├── requirements.txt (0.1 KB) [2026-05-26 07:28]
│   └── workflow.py (1.1 KB) [2026-05-23 06:18]
├── OOP/ [2026-02-11 13:17]
│   └── class/ [2026-03-22 07:20]
│       ├── asignmnts/ [2026-05-13 08:07]
│       │   ├── bankassign.py (0.0 KB) [2026-05-13 08:07]
│       │   ├── s-a-dict.py (1.0 KB) [2026-03-24 08:06]
│       │   ├── s-a-set.py (0.7 KB) [2026-03-24 07:01]
│       │   └── sessional-assinmnt-stack.py (0.9 KB) [2026-05-13 08:06]
│       ├── class4-3-26.py (1.0 KB) [2026-03-04 08:53]
│       ├── class5-3-26.py (0.7 KB) [2026-03-22 07:41]
│       ├── classOPOV.py (0.5 KB) [2026-02-26 08:47]
│       ├── com.py (0.3 KB) [2026-02-25 09:00]
│       ├── complex.py (0.6 KB) [2026-02-25 08:45]
│       ├── context.md (0.8 KB) [2026-02-12 07:01]
│       ├── distance.py (0.7 KB) [2026-02-26 09:03]
│       ├── employee.py (0.8 KB) [2026-02-12 07:01]
│       ├── funcprac.py (0.3 KB) [2026-02-18 09:24]
│       └── lmethods.py (0.5 KB) [2026-02-18 09:15]
├── practice/ [2026-02-16 18:36]
│   ├── 7-1-26/ [2026-01-08 11:11]
│   │   ├── tier1.py (4.9 KB) [2026-01-07 18:39]
│   │   ├── tier2.py (5.1 KB) [2026-01-08 12:14]
│   │   └── warmup.py (1.6 KB) [2026-01-07 14:55]
│   ├── coolSlides/ [2026-02-16 19:09]
│   │   ├── =3.20 (0.4 KB) [2026-02-16 19:10]
│   │   ├── hand_landmarker.task (4077.4 KB) [2026-02-16 11:01]
│   │   ├── main.py (0.6 KB) [2026-02-18 10:06]
│   │   ├── requirements.txt (0.1 KB) [2026-02-16 18:51]
│   │   ├── test.py (1.2 KB) [2026-02-16 11:02]
│   │   └── wget-log (0.0 KB) [2026-02-16 11:02]
│   ├── polioMap/ [2026-02-12 07:02]
│   │   └── testfolum.py (0.0 KB) [2026-02-12 07:02]
│   ├── unip/ [2025-12-14 16:12]
│   │   ├── h.py (0.9 KB) [2025-12-14 09:54]
│   │   ├── main.py (0.1 KB) [2025-12-14 09:06]
│   │   ├── pyproject.toml (0.2 KB) [2025-12-14 09:07]
│   │   ├── r.py (0.0 KB) [2025-12-14 16:12]
│   │   ├── README.md (0.0 KB) [2025-12-14 09:06]
│   │   └── uv.lock (26.8 KB) [2025-12-14 09:07]
│   ├── hand_landmarker.task (7635.8 KB) [2023-04-26 08:33]
│   ├── hodia.py (0.4 KB) [2026-01-03 11:51]
│   └── ulamspiral.py (6.0 KB) [2026-01-03 12:32]
├── ProjectBOT/ [2026-03-23 07:38]
│   ├── bot/ [2026-03-23 07:41]
│   │   ├── __init__.PY (0.0 KB) [2026-03-23 07:40]
│   │   ├── ai.py (0.0 KB) [2026-03-23 09:02]
│   │   ├── db.py (2.7 KB) [2026-03-23 09:17]
│   │   ├── handler.py (0.5 KB) [2026-03-28 11:01]
│   │   ├── states.py (8.8 KB) [2026-03-28 10:49]
│   │   └── telegram.py (0.8 KB) [2026-03-23 08:05]
│   ├── app.py (0.0 KB) [2026-03-23 07:33]
│   └── requirements.txt (0.0 KB) [2026-03-23 08:04]
├── Khwarizm-backup.zip (49473.1 KB) [2026-05-23 07:10]
└── Khwarizm[semi-final].zip (48281.2 KB) [2026-05-19 19:03]
```

# Source Code Deep-Dive

## File: `../Database Project/ai_agent_system/data/__init__.py`
**Last Modified:** `2026-05-23 12:35` | **Size:** `0.02 KB`

<file path="../Database Project/ai_agent_system/data/__init__.py" type="python">
```python
# database package

```
</file>

---

## File: `../Database Project/ai_agent_system/data/sample_data.py`
**Last Modified:** `2026-05-23 14:28` | **Size:** `11.15 KB`

<file path="../Database Project/ai_agent_system/data/sample_data.py" type="python">
```python
"""
Sample data insertion script
Populates all 8 tables with realistic test data
"""

from database.connection import execute_query
from datetime import datetime, timedelta


def clear_all_data():
    """Delete all existing data (careful!)"""
    print("Clearing existing data...")
    
    # Order matters - delete children before parents
    tables = ['log', 'tool_usage', 'session', 'task', 'memory', 'agent', 'tool', 'user']
    
    for table in tables:
        execute_query(f"DELETE FROM {table}")
        print(f"  ✓ Cleared {table}")


def insert_users():
    """Insert sample users"""
    print("\nInserting users...")
    
    users = [
        ("Alice Johnson", "alice@example.com", "pro"),
        ("Bob Smith", "bob@example.com", "enterprise"),
        ("Charlie Brown", "charlie@example.com", "free"),
        ("Diana Prince", "diana@example.com", "pro"),
        ("Eve Davis", "eve@example.com", "free")
    ]
    
    query = """
    INSERT INTO user (user_name, user_email, user_subscription_tier)
    VALUES (%s, %s, %s)
    """
    
    for user in users:
        execute_query(query, user)
    
    print(f"  ✓ Inserted {len(users)} users")


def insert_agents():
    """Insert sample agents"""
    print("\nInserting agents...")
    
    agents = [
        (1, "Research Assistant Alpha", "assistant", "active", "2.1"),
        (1, "Code Helper Beta", "specialized", "active", "1.5"),
        (2, "Enterprise Bot Gamma", "autonomous", "active", "3.0"),
        (3, "Personal Assistant Delta", "assistant", "paused", "1.0"),
        (4, "Data Analyzer Epsilon", "specialized", "active", "2.0"),
        (5, "Task Manager Zeta", "autonomous", "terminated", "1.2")
    ]
    
    query = """
    INSERT INTO agent (user_id, agent_name, agent_type, agent_status, agent_version)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    for agent in agents:
        execute_query(query, agent)
    
    print(f"  ✓ Inserted {len(agents)} agents")


def insert_memories():
    """Insert sample memories"""
    print("\nInserting memories...")
    
    memories = [
        (1, "short-term", "User prefers detailed explanations", 0.75, None),
        (1, "long-term", "User is working on a machine learning project", 0.90, None),
        (1, "episodic", "User asked about neural networks on 2024-01-15", 0.60, 
         (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')),
        (2, "long-term", "User prefers Python over JavaScript", 0.85, None),
        (2, "short-term", "Currently debugging a Flask application", 0.70, 
         (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')),
        (3, "long-term", "User manages a team of 50 employees", 0.95, None),
        (3, "episodic", "Last week discussed Q4 financial reports", 0.65, 
         (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')),
        (4, "short-term", "Working on essay about climate change", 0.80, 
         (datetime.now() + timedelta(hours=12)).strftime('%Y-%m-%d %H:%M:%S')),
        (5, "long-term", "User is a data scientist specializing in NLP", 0.92, None),
        (5, "episodic", "Analyzed sentiment data from Twitter last month", 0.68, None)
    ]
    
    query = """
    INSERT INTO memory (agent_id, memory_type, memory_content, 
                       memory_importance_score, memory_expires_at)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    for memory in memories:
        execute_query(query, memory)
    
    print(f"  ✓ Inserted {len(memories)} memories")


def insert_tools():
    """Insert sample tools"""
    print("\nInserting tools...")
    
    tools = [
        ("Web Search", "Searches the internet for information", "search", True),
        ("Code Executor", "Runs Python code in a sandbox", "compute", True),
        ("Email Sender", "Sends emails on behalf of the user", "communicate", True),
        ("Database Query", "Retrieves data from databases", "retrieve", True),
        ("File Reader", "Reads and parses documents", "retrieve", True),
        ("Calculator", "Performs mathematical computations", "compute", True),
        ("Weather API", "Fetches current weather data", "search", False),
        ("Translation Service", "Translates text between languages", "communicate", True)
    ]
    
    query = """
    INSERT INTO tool (tool_name, tool_description, tool_type, tool_is_active)
    VALUES (%s, %s, %s, %s)
    """
    
    for tool in tools:
        execute_query(query, tool)
    
    print(f"  ✓ Inserted {len(tools)} tools")


def insert_tasks():
    """Insert sample tasks"""
    print("\nInserting tasks...")
    
    tasks = [
        (1, 1, "Research neural network architectures", 
         "Find papers on CNN and RNN architectures", "completed", "high", 
         (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')),
        (1, 1, "Summarize machine learning trends", 
         "Create a summary of 2024 ML trends", "in_progress", "medium", None),
        (2, 1, "Debug Flask route error", 
         "Fix the 404 error on /api/users endpoint", "completed", "critical", 
         (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')),
        (3, 2, "Generate quarterly report", 
         "Compile financial data for Q4 2024", "completed", "high", 
         (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')),
        (3, 2, "Schedule team meeting", 
         "Find available time slots for all 50 members", "pending", "medium", None),
        (4, 3, "Proofread climate essay", 
         "Check grammar and flow of 3000-word essay", "in_progress", "high", None),
        (5, 4, "Analyze sentiment data", 
         "Process 10k tweets for sentiment classification", "failed", "medium", None),
        (2, 1, "Write unit tests", 
         "Create tests for authentication module", "pending", "low", None)
    ]
    
    query = """
    INSERT INTO task (agent_id, user_id, task_title, task_description, 
                     task_status, task_priority, task_completed_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    for task in tasks:
        execute_query(query, task)
    
    print(f"  ✓ Inserted {len(tasks)} tasks")


def insert_tool_usage():
    """Insert sample tool usage records"""
    print("\nInserting tool usage records...")
    
    usage = [
        (1, 1, True, "Found 15 relevant papers on arXiv"),
        (1, 5, True, "Downloaded and parsed 3 PDF files"),
        (2, 1, True, "Searched for ML trends articles"),
        (2, 6, True, "Calculated trend percentages"),
        (3, 2, True, "Executed test code to reproduce error"),
        (3, 4, True, "Queried database for user routes"),
        (4, 4, True, "Retrieved financial data from database"),
        (4, 6, True, "Computed quarterly statistics"),
        (6, 5, True, "Read essay draft file"),
        (7, 1, False, "Web search timed out"),
        (7, 4, True, "Retrieved tweet dataset from database")
    ]
    
    query = """
    INSERT INTO tool_usage (task_id, tool_id, success, output_summary)
    VALUES (%s, %s, %s, %s)
    """
    
    for record in usage:
        execute_query(query, record)
    
    print(f"  ✓ Inserted {len(usage)} tool usage records")


def insert_sessions():
    """Insert sample sessions"""
    print("\nInserting sessions...")
    
    sessions = [
        (1, 1, 
         (datetime.now() - timedelta(days=2, hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
         (datetime.now() - timedelta(days=2, hours=1)).strftime('%Y-%m-%d %H:%M:%S'),
         "web"),
        (1, 1,
         (datetime.now() - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S'),
         None,
         "web"),
        (2, 1,
         (datetime.now() - timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S'),
         (datetime.now() - timedelta(hours=3, minutes=30)).strftime('%Y-%m-%d %H:%M:%S'),
         "api"),
        (3, 2,
         (datetime.now() - timedelta(days=5, hours=3)).strftime('%Y-%m-%d %H:%M:%S'),
         (datetime.now() - timedelta(days=5, hours=1)).strftime('%Y-%m-%d %H:%M:%S'),
         "web"),
        (4, 3,
         (datetime.now() - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
         None,
         "mobile"),
        (5, 4,
         (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
         (datetime.now() - timedelta(days=1, hours=-1)).strftime('%Y-%m-%d %H:%M:%S'),
         "web")
    ]
    
    query = """
    INSERT INTO session (agent_id, user_id, session_started_at, 
                        session_ended_at, session_channel)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    for session in sessions:
        execute_query(query, session)
    
    print(f"  ✓ Inserted {len(sessions)} sessions")


def insert_logs():
    """Insert sample log entries"""
    print("\nInserting log entries...")
    
    logs = [
        (1, 1, 1, "memory_read", "Retrieved user preference for detailed explanations", "success"),
        (1, 1, 1, "task_update", "Started research on neural networks", "success"),
        (1, 1, 1, "tool_call", "Called Web Search tool", "success"),
        (1, 1, 1, "tool_call", "Called File Reader tool", "success"),
        (1, 1, 1, "memory_write", "Stored search results summary", "success"),
        (2, 3, 3, "memory_read", "Retrieved Flask debugging context", "success"),
        (2, 3, 3, "tool_call", "Called Code Executor tool", "success"),
        (2, 3, 3, "task_update", "Completed debugging task", "success"),
        (3, 4, 4, "tool_call", "Called Database Query tool", "success"),
        (3, 4, 4, "tool_call", "Called Calculator tool", "success"),
        (3, 4, 4, "task_update", "Completed quarterly report", "success"),
        (4, 5, 6, "memory_read", "Retrieved essay topic and requirements", "success"),
        (4, 5, 6, "tool_call", "Called File Reader tool", "success"),
        (5, 6, 7, "tool_call", "Called Web Search tool", "failure"),
        (5, 6, 7, "task_update", "Task failed due to tool timeout", "failure")
    ]
    
    query = """
    INSERT INTO log (agent_id, session_id, task_id, log_action_type, 
                    log_description, log_status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    for log in logs:
        execute_query(query, log)
    
    print(f"  ✓ Inserted {len(logs)} log entries")


def verify_data():
    """Verify all data was inserted"""
    print("\n" + "="*60)
    print("Verifying inserted data...")
    print("="*60)
    
    tables = ['user', 'agent', 'memory', 'tool', 'task', 
              'tool_usage', 'session', 'log']
    
    for table in tables:
        query = f"SELECT COUNT(*) as count FROM {table}"
        result = execute_query(query, fetch=True)
        if result:
            count = result[0]['count']
            print(f"  {table:15} : {count} records")


if __name__ == "__main__":
    print("="*60)
    print("Sample Data Insertion")
    print("="*60)
    
    # Ask for confirmation
    response = input("\nThis will DELETE all existing data. Continue? (yes/no): ")
    
    if response.lower() != 'yes':
        print("Aborted.")
        exit()
    
    # Insert all data
    clear_all_data()
    insert_users()
    insert_agents()
    insert_memories()
    insert_tools()
    insert_tasks()
    insert_tool_usage()
    insert_sessions()
    insert_logs()
    
    # Verify
    verify_data()
    
    print("\n" + "="*60)
    print("✓ Sample data insertion complete!")
    print("="*60)
```
</file>

---

## File: `../Database Project/ai_agent_system/database/__init__.py`
**Last Modified:** `2026-05-23 09:28` | **Size:** `0.02 KB`

<file path="../Database Project/ai_agent_system/database/__init__.py" type="python">
```python
# database package

```
</file>

---

## File: `../Database Project/ai_agent_system/database/config.py`
**Last Modified:** `2026-05-23 12:28` | **Size:** `0.20 KB`

<file path="../Database Project/ai_agent_system/database/config.py" type="python">
```python
"""
Database configuration file
Stores MySQL connection credentials
"""

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "ai_agent_system"
}
```
</file>

---

## File: `../Database Project/ai_agent_system/database/connection.py`
**Last Modified:** `2026-05-23 14:23` | **Size:** `1.28 KB`

<file path="../Database Project/ai_agent_system/database/connection.py" type="python">
```python
"""
MySQL database connection handler
"""

import mysql.connector
from mysql.connector import Error
from database.config import DB_CONFIG


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
        return None
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()


def execute_query(query, params=None, fetch=False):
    connection = get_connection()
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        if fetch:
            results = cursor.fetchall()
            cursor.close()
            close_connection(connection)
            return results
        else:
            connection.commit()
            last_id = cursor.lastrowid
            cursor.close()
            close_connection(connection)
            return last_id
    except Error as e:
        print(f"Error executing query: {e}")
        if connection:
            close_connection(connection)
        return None
```
</file>

---

## File: `../Database Project/ai_agent_system/database/setup.py`
**Last Modified:** `2026-05-23 09:28` | **Size:** `0.00 KB`

<file path="../Database Project/ai_agent_system/database/setup.py" type="python">
```python

```
</file>

---

## File: `../Database Project/ai_agent_system/pages/__init__.py`
**Last Modified:** `2026-05-23 09:28` | **Size:** `0.02 KB`

<file path="../Database Project/ai_agent_system/pages/__init__.py" type="python">
```python
# pages package

```
</file>

---

## File: `../Database Project/ai_agent_system/pages/agents.py`
**Last Modified:** `2026-05-23 18:48` | **Size:** `4.73 KB`

<file path="../Database Project/ai_agent_system/pages/agents.py" type="python">
```python
"""
pages/agents.py — Agent management
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, metric_row, table, error_msg


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_agents():
    return execute_query(
        """
        SELECT a.agent_id, a.agent_name, a.agent_type, a.agent_status,
               a.agent_version, a.agent_created_at, u.user_name
        FROM   agent a
        JOIN   user  u ON a.user_id = u.user_id
        ORDER  BY a.agent_id
        """,
        fetch=True,
    )

def get_agent_by_id(agent_id):
    return execute_query("SELECT * FROM agent WHERE agent_id = %s", (agent_id,), fetch=True)

def get_all_users():
    return execute_query("SELECT user_id, user_name FROM user", fetch=True)

def add_agent(user_id, name, agent_type, status, version):
    execute_query(
        "INSERT INTO agent (user_id, agent_name, agent_type, agent_status, agent_version) VALUES (%s,%s,%s,%s,%s)",
        (user_id, name, agent_type, status, version),
    )

def update_agent(agent_id, name, agent_type, status, version):
    execute_query(
        "UPDATE agent SET agent_name=%s, agent_type=%s, agent_status=%s, agent_version=%s WHERE agent_id=%s",
        (name, agent_type, status, version, agent_id),
    )

def delete_agent(agent_id):
    execute_query("DELETE FROM agent WHERE agent_id = %s", (agent_id,))


# ── Page ─────────────────────────────────────────────────────────────────────

TYPES    = ["assistant", "autonomous", "specialized"]
STATUSES = ["active", "paused", "terminated"]


def show():
    page_header("agents", "manage AI agents and their configurations")

    users = get_all_users()
    if not users:
        empty_state("no users found — add a user before creating agents")
        return

    user_map = {u["user_name"]: u["user_id"] for u in users}
    agents   = get_all_agents()

    # ── Stats ──
    section("overview")
    total      = len(agents) if agents else 0
    active     = sum(1 for a in agents if a.get("agent_status") == "active")     if agents else 0
    paused     = sum(1 for a in agents if a.get("agent_status") == "paused")     if agents else 0
    terminated = sum(1 for a in agents if a.get("agent_status") == "terminated") if agents else 0
    metric_row([("Total Agents", total), ("Active", active), ("Paused", paused), ("Terminated", terminated)])

    # ── Add agent ──
    section("add agent")
    with st.expander("new agent", expanded=False):
        with st.form("add_agent_form"):
            owner      = st.selectbox("owner (user)", list(user_map.keys()))
            name       = st.text_input("agent name")
            agent_type = st.selectbox("type",    TYPES)
            status     = st.selectbox("status",  STATUSES)
            version    = st.text_input("version", value="1.0")
            if st.form_submit_button("add agent"):
                if name:
                    add_agent(user_map[owner], name, agent_type, status, version)
                    st.rerun()
                else:
                    error_msg("agent name is required")

    # ── Table ──
    section("all agents")
    if agents:
        table(agents, badge_cols=["agent_status", "agent_type"])
    else:
        empty_state("no agents found")
        return

    # ── Edit / delete ──
    section("edit or delete")
    agent_options = {f"{a['agent_id']} — {a['agent_name']}": a['agent_id'] for a in agents}
    selected      = st.selectbox("select agent", list(agent_options.keys()), label_visibility="collapsed")
    selected_id   = agent_options[selected]
    agent_data    = get_agent_by_id(selected_id)

    if agent_data:
        a = agent_data[0]
        with st.form("edit_agent_form"):
            new_name    = st.text_input("agent name", value=a["agent_name"])
            new_type    = st.selectbox("type",   TYPES,    index=TYPES.index(a["agent_type"]))
            new_status  = st.selectbox("status", STATUSES, index=STATUSES.index(a["agent_status"]))
            new_version = st.text_input("version", value=a["agent_version"])
            col1, col2  = st.columns(2)
            with col1:
                if st.form_submit_button("update agent"):
                    update_agent(selected_id, new_name, new_type, new_status, new_version)
                    st.rerun()
            with col2:
                if st.form_submit_button("delete agent"):
                    delete_agent(selected_id)
                    st.rerun()
```
</file>

---

## File: `../Database Project/ai_agent_system/pages/logs.py`
**Last Modified:** `2026-05-23 18:50` | **Size:** `5.24 KB`

<file path="../Database Project/ai_agent_system/pages/logs.py" type="python">
```python
"""
pages/logs.py — Log viewer (read-heavy, with add)
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, metric_row, table


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_logs():
    return execute_query(
        """
        SELECT l.log_id, a.agent_name, s.session_id,
               t.task_title, l.log_action_type,
               l.log_description, l.log_timestamp, l.log_status
        FROM   log     l
        JOIN   agent   a ON l.agent_id   = a.agent_id
        JOIN   session s ON l.session_id = s.session_id
        JOIN   task    t ON l.task_id    = t.task_id
        ORDER  BY l.log_timestamp DESC
        """,
        fetch=True,
    )

def get_log_stats():
    return execute_query(
        "SELECT log_status, COUNT(*) AS count FROM log GROUP BY log_status",
        fetch=True,
    )

def get_action_breakdown():
    return execute_query(
        """
        SELECT log_action_type, COUNT(*) AS count
        FROM   log
        GROUP  BY log_action_type
        ORDER  BY count DESC
        """,
        fetch=True,
    )

def get_all_agents():
    return execute_query("SELECT agent_id, agent_name FROM agent", fetch=True)

def get_all_sessions():
    return execute_query("SELECT session_id FROM session", fetch=True)

def get_all_tasks():
    return execute_query("SELECT task_id, task_title FROM task", fetch=True)

def add_log(agent_id, session_id, task_id, action_type, description, status):
    execute_query(
        """
        INSERT INTO log (agent_id, session_id, task_id,
                         log_action_type, log_description, log_status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (agent_id, session_id, task_id, action_type, description, status),
    )


# ── Page ─────────────────────────────────────────────────────────────────────

ACTION_TYPES = ["memory_read", "memory_write", "tool_call", "task_update"]
STATUSES     = ["success", "failure"]


def show():
    page_header("logs", "full audit trail of every agent action")

    # ── Stats ──
    section("overview")
    stats = get_log_stats()
    if stats:
        stat_map = {s["log_status"]: s["count"] for s in stats}
        metric_row([
            ("Success", stat_map.get("success", 0)),
            ("Failure", stat_map.get("failure", 0)),
        ])
    else:
        metric_row([("Total Logs", 0)])

    # ── Action breakdown ──
    section("action breakdown")
    breakdown = get_action_breakdown()
    if breakdown:
        cols = st.columns(min(len(breakdown), 4))
        for col, row in zip(cols, breakdown):
            col.metric(row["log_action_type"].replace("_", " "), row["count"])
    else:
        empty_state("no actions recorded")

    # ── Add log entry ──
    agents   = get_all_agents()
    sessions = get_all_sessions()
    tasks    = get_all_tasks()

    if agents and sessions and tasks:
        section("add log entry")
        agent_map   = {a["agent_name"]:       a["agent_id"]   for a in agents}
        session_map = {str(s["session_id"]):  s["session_id"] for s in sessions}
        task_map    = {t["task_title"]:        t["task_id"]    for t in tasks}

        with st.expander("new log entry", expanded=False):
            with st.form("add_log_form"):
                agent       = st.selectbox("agent",       list(agent_map.keys()))
                session     = st.selectbox("session id",  list(session_map.keys()))
                task        = st.selectbox("task",        list(task_map.keys()))
                action_type = st.selectbox("action type", ACTION_TYPES)
                description = st.text_area("description")
                status      = st.selectbox("status",      STATUSES)
                if st.form_submit_button("add log entry"):
                    add_log(
                        agent_map[agent],
                        session_map[session],
                        task_map[task],
                        action_type,
                        description,
                        status,
                    )
                    st.rerun()

    # ── Filter + table ──
    section("all log entries")
    col1, col2 = st.columns(2)
    with col1:
        filter_status = st.selectbox(
            "filter by status",
            ["all"] + STATUSES,
            label_visibility="collapsed",
        )
    with col2:
        filter_action = st.selectbox(
            "filter by action",
            ["all"] + ACTION_TYPES,
            label_visibility="collapsed",
        )

    logs = get_all_logs()
    if logs:
        if filter_status != "all":
            logs = [l for l in logs if l["log_status"] == filter_status]
        if filter_action != "all":
            logs = [l for l in logs if l["log_action_type"] == filter_action]

        if logs:
            table(logs, badge_cols=["log_status", "log_action_type"])
        else:
            empty_state("no logs match this filter")
    else:
        empty_state("no log entries found")
```
</file>

---

## File: `../Database Project/ai_agent_system/pages/memory.py`
**Last Modified:** `2026-05-23 18:48` | **Size:** `4.52 KB`

<file path="../Database Project/ai_agent_system/pages/memory.py" type="python">
```python
"""
pages/memory.py — Memory management
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, metric_row, table, error_msg


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_memories():
    return execute_query(
        """
        SELECT m.memory_id, a.agent_name, m.memory_type,
               m.memory_content, m.memory_importance_score,
               m.memory_created_at, m.memory_expires_at
        FROM   memory m
        JOIN   agent  a ON m.agent_id = a.agent_id
        ORDER  BY m.memory_importance_score DESC
        """,
        fetch=True,
    )

def get_all_agents():
    return execute_query("SELECT agent_id, agent_name FROM agent", fetch=True)

def get_memory_stats():
    return execute_query(
        """
        SELECT memory_type, COUNT(*) as count,
               AVG(memory_importance_score) as avg_score
        FROM   memory
        GROUP  BY memory_type
        """,
        fetch=True,
    )

def add_memory(agent_id, memory_type, content, score, expires_at):
    execute_query(
        """
        INSERT INTO memory (agent_id, memory_type, memory_content,
                            memory_importance_score, memory_expires_at)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (agent_id, memory_type, content, score, expires_at),
    )

def delete_memory(memory_id):
    execute_query("DELETE FROM memory WHERE memory_id = %s", (memory_id,))


# ── Page ─────────────────────────────────────────────────────────────────────

MEMORY_TYPES = ["short-term", "long-term", "episodic"]


def show():
    page_header("memory", "view and manage agent memory records")

    agents = get_all_agents()
    if not agents:
        empty_state("no agents found — add an agent before creating memories")
        return

    agent_map = {a["agent_name"]: a["agent_id"] for a in agents}

    # ── Stats ──
    section("overview")
    stats = get_memory_stats()
    if stats:
        cols = st.columns(len(stats))
        for col, s in zip(cols, stats):
            avg = float(s["avg_score"]) if s["avg_score"] else 0.0
            col.metric(s["memory_type"], s["count"], f"avg score {avg:.2f}")
    else:
        metric_row([("Memories", 0)])

    # ── Add memory ──
    section("add memory")
    with st.expander("new memory", expanded=False):
        with st.form("add_memory_form"):
            agent       = st.selectbox("agent", list(agent_map.keys()))
            memory_type = st.selectbox("memory type", MEMORY_TYPES)
            content     = st.text_area("memory content")
            score       = st.slider("importance score", 0.0, 1.0, 0.5, 0.05)
            has_expiry  = st.checkbox("set expiry date")
            expires_at  = None
            if has_expiry:
                expiry_date = st.date_input("expires at")
                expires_at  = str(expiry_date) + " 00:00:00"
            if st.form_submit_button("add memory"):
                if content:
                    add_memory(agent_map[agent], memory_type, content, score, expires_at)
                    st.rerun()
                else:
                    error_msg("memory content is required")

    # ── Filter + table ──
    section("all memories")
    filter_agent = st.selectbox(
        "filter by agent",
        ["all agents"] + list(agent_map.keys()),
        label_visibility="collapsed",
    )

    memories = get_all_memories()
    if memories:
        if filter_agent != "all agents":
            memories = [m for m in memories if m["agent_name"] == filter_agent]

        if memories:
            table(memories, badge_cols=["memory_type"])
        else:
            empty_state(f"no memories for {filter_agent}")
    else:
        empty_state("no memories found")
        return

    # ── Delete ──
    section("delete a memory")
    memory_options = {
        f"{m['memory_id']} — {m['agent_name']} — {str(m['memory_content'])[:40]}": m["memory_id"]
        for m in memories
    }
    if memory_options:
        selected    = st.selectbox("select memory", list(memory_options.keys()), label_visibility="collapsed")
        selected_id = memory_options[selected]
        if st.button("delete memory"):
            delete_memory(selected_id)
            st.rerun()
```
</file>

---

## File: `../Database Project/ai_agent_system/pages/sessions.py`
**Last Modified:** `2026-05-23 18:50` | **Size:** `4.12 KB`

<file path="../Database Project/ai_agent_system/pages/sessions.py" type="python">
```python
"""
pages/sessions.py — Session management
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, metric_row, table


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_sessions():
    return execute_query(
        """
        SELECT s.session_id, a.agent_name, u.user_name,
               s.session_started_at, s.session_ended_at,
               s.session_channel,
               CASE WHEN s.session_ended_at IS NULL THEN 'active' ELSE 'ended' END AS session_state
        FROM   session s
        JOIN   agent a ON s.agent_id = a.agent_id
        JOIN   user  u ON s.user_id  = u.user_id
        ORDER  BY s.session_started_at DESC
        """,
        fetch=True,
    )

def get_session_stats():
    active = execute_query(
        "SELECT COUNT(*) AS n FROM session WHERE session_ended_at IS NULL", fetch=True
    )
    total  = execute_query("SELECT COUNT(*) AS n FROM session", fetch=True)
    a = active[0]["n"] if active else 0
    t = total[0]["n"]  if total  else 0
    return a, t

def get_all_agents():
    return execute_query("SELECT agent_id, agent_name FROM agent", fetch=True)

def get_all_users():
    return execute_query("SELECT user_id, user_name FROM user", fetch=True)

def add_session(agent_id, user_id, channel):
    execute_query(
        "INSERT INTO session (agent_id, user_id, session_channel) VALUES (%s,%s,%s)",
        (agent_id, user_id, channel),
    )

def end_session(session_id):
    execute_query(
        "UPDATE session SET session_ended_at = NOW() WHERE session_id = %s",
        (session_id,),
    )

def delete_session(session_id):
    execute_query("DELETE FROM session WHERE session_id = %s", (session_id,))


# ── Page ─────────────────────────────────────────────────────────────────────

CHANNELS = ["web", "api", "mobile"]


def show():
    page_header("sessions", "track active and historical agent sessions")

    agents = get_all_agents()
    users  = get_all_users()
    if not agents or not users:
        empty_state("add agents and users before starting sessions")
        return

    agent_map = {a["agent_name"]: a["agent_id"] for a in agents}
    user_map  = {u["user_name"]:  u["user_id"]  for u in users}

    # ── Stats ──
    section("overview")
    active_count, total_count = get_session_stats()
    metric_row([
        ("Total Sessions",  total_count),
        ("Active",          active_count),
        ("Ended",           total_count - active_count),
    ])

    # ── Start session ──
    section("start session")
    with st.expander("new session", expanded=False):
        with st.form("add_session_form"):
            agent     = st.selectbox("agent",   list(agent_map.keys()))
            user      = st.selectbox("user",    list(user_map.keys()))
            channel   = st.selectbox("channel", CHANNELS)
            if st.form_submit_button("start session"):
                add_session(agent_map[agent], user_map[user], channel)
                st.rerun()

    # ── Table ──
    section("all sessions")
    sessions = get_all_sessions()
    if sessions:
        table(sessions, badge_cols=["session_state", "session_channel"])
    else:
        empty_state("no sessions found")
        return

    # ── End / delete ──
    section("end or delete")
    session_options = {
        f"{s['session_id']} — {s['agent_name']} — {s['session_state']}": s["session_id"]
        for s in sessions
    }
    selected    = st.selectbox("select session", list(session_options.keys()), label_visibility="collapsed")
    selected_id = session_options[selected]
    col1, col2  = st.columns(2)
    with col1:
        if st.button("end session"):
            end_session(selected_id)
            st.rerun()
    with col2:
        if st.button("delete session"):
            delete_session(selected_id)
            st.rerun()
```
</file>

---

## File: `../Database Project/ai_agent_system/pages/tasks.py`
**Last Modified:** `2026-05-23 18:48` | **Size:** `5.48 KB`

<file path="../Database Project/ai_agent_system/pages/tasks.py" type="python">
```python
"""
pages/tasks.py — Task management
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, table, error_msg


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_tasks():
    return execute_query(
        """
        SELECT t.task_id, t.task_title, t.task_status, t.task_priority,
               a.agent_name, u.user_name, t.task_created_at, t.task_completed_at
        FROM   task  t
        JOIN   agent a ON t.agent_id = a.agent_id
        JOIN   user  u ON t.user_id  = u.user_id
        ORDER  BY FIELD(t.task_priority,'critical','high','medium','low'),
                  t.task_created_at DESC
        """,
        fetch=True,
    )

def get_task_by_id(task_id):
    return execute_query("SELECT * FROM task WHERE task_id = %s", (task_id,), fetch=True)

def get_all_agents():
    return execute_query("SELECT agent_id, agent_name FROM agent", fetch=True)

def get_all_users():
    return execute_query("SELECT user_id, user_name FROM user", fetch=True)

def get_task_stats():
    return execute_query(
        "SELECT task_status, COUNT(*) as count FROM task GROUP BY task_status",
        fetch=True,
    )

def add_task(agent_id, user_id, title, description, status, priority):
    execute_query(
        """
        INSERT INTO task (agent_id, user_id, task_title, task_description,
                          task_status, task_priority)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (agent_id, user_id, title, description, status, priority),
    )

def update_task_status(task_id, status):
    completed_clause = "NOW()" if status == "completed" else "NULL"
    execute_query(
        f"UPDATE task SET task_status=%s, task_completed_at={completed_clause} WHERE task_id=%s",
        (status, task_id),
    )

def delete_task(task_id):
    execute_query("DELETE FROM task WHERE task_id = %s", (task_id,))


# ── Page ─────────────────────────────────────────────────────────────────────

STATUSES   = ["pending", "in_progress", "completed", "failed"]
PRIORITIES = ["low", "medium", "high", "critical"]


def show():
    page_header("tasks", "assign, track, and update agent tasks")

    agents = get_all_agents()
    users  = get_all_users()
    if not agents or not users:
        empty_state("add agents and users before creating tasks")
        return

    agent_map = {a["agent_name"]: a["agent_id"] for a in agents}
    user_map  = {u["user_name"]:  u["user_id"]  for u in users}

    # ── Stats ──
    section("overview")
    stats = get_task_stats()
    stat_map = {s["task_status"]: s["count"] for s in stats} if stats else {}
    cols = st.columns(4)
    for col, key in zip(cols, STATUSES):
        col.metric(key.replace("_", " "), stat_map.get(key, 0))

    # ── Add task ──
    section("add task")
    with st.expander("new task", expanded=False):
        with st.form("add_task_form"):
            agent       = st.selectbox("assigned agent",     list(agent_map.keys()))
            user        = st.selectbox("created by (user)",  list(user_map.keys()))
            title       = st.text_input("task title")
            description = st.text_area("task description")
            status      = st.selectbox("status",   STATUSES)
            priority    = st.selectbox("priority", PRIORITIES)
            if st.form_submit_button("add task"):
                if title:
                    add_task(agent_map[agent], user_map[user], title, description, status, priority)
                    st.rerun()
                else:
                    error_msg("task title is required")

    # ── Filter + table ──
    section("all tasks")
    filter_status = st.selectbox(
        "filter by status",
        ["all"] + STATUSES,
        label_visibility="collapsed",
    )

    tasks = get_all_tasks()
    if tasks:
        if filter_status != "all":
            tasks = [t for t in tasks if t["task_status"] == filter_status]
        if tasks:
            table(tasks, badge_cols=["task_status", "task_priority"])
        else:
            empty_state(f"no {filter_status} tasks")
    else:
        empty_state("no tasks found")
        return

    # ── Update / delete ──
    section("update or delete")
    all_tasks    = get_all_tasks()
    task_options = {f"{t['task_id']} — {t['task_title']}": t['task_id'] for t in all_tasks}

    if task_options:
        selected    = st.selectbox("select task", list(task_options.keys()), label_visibility="collapsed")
        selected_id = task_options[selected]
        task_data   = get_task_by_id(selected_id)

        if task_data:
            t          = task_data[0]
            cur_status = t["task_status"] if t["task_status"] in STATUSES else STATUSES[0]
            new_status = st.selectbox(
                "update status", STATUSES,
                index=STATUSES.index(cur_status),
                label_visibility="collapsed",
            )
            col1, col2 = st.columns(2)
            with col1:
                if st.button("update status"):
                    update_task_status(selected_id, new_status)
                    st.rerun()
            with col2:
                if st.button("delete task"):
                    delete_task(selected_id)
                    st.rerun()
```
</file>

---

## File: `../Database Project/ai_agent_system/pages/tool_usage.py`
**Last Modified:** `2026-05-23 18:50` | **Size:** `3.80 KB`

<file path="../Database Project/ai_agent_system/pages/tool_usage.py" type="python">
```python
"""
pages/tool_usage.py — Tool usage log
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, table


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_tool_usage():
    return execute_query(
        """
        SELECT tu.usage_id, t.task_title, tl.tool_name,
               tu.used_at, tu.success, tu.output_summary
        FROM   tool_usage tu
        JOIN   task t  ON tu.task_id = t.task_id
        JOIN   tool tl ON tu.tool_id = tl.tool_id
        ORDER  BY tu.used_at DESC
        """,
        fetch=True,
    )

def get_usage_stats():
    return execute_query(
        """
        SELECT tl.tool_name,
               COUNT(*)            AS total_uses,
               SUM(tu.success)     AS successful,
               COUNT(*) - SUM(tu.success) AS failed
        FROM   tool_usage tu
        JOIN   tool tl ON tu.tool_id = tl.tool_id
        GROUP  BY tl.tool_name
        ORDER  BY total_uses DESC
        """,
        fetch=True,
    )

def get_all_tasks():
    return execute_query("SELECT task_id, task_title FROM task", fetch=True)

def get_all_tools():
    return execute_query("SELECT tool_id, tool_name FROM tool WHERE tool_is_active = TRUE", fetch=True)

def add_tool_usage(task_id, tool_id, success, output_summary):
    execute_query(
        "INSERT INTO tool_usage (task_id, tool_id, success, output_summary) VALUES (%s,%s,%s,%s)",
        (task_id, tool_id, success, output_summary),
    )

def delete_tool_usage(usage_id):
    execute_query("DELETE FROM tool_usage WHERE usage_id = %s", (usage_id,))


# ── Page ─────────────────────────────────────────────────────────────────────

def show():
    page_header("tool usage", "log and review every agent tool call")

    # ── Performance stats ──
    section("tool performance")
    stats = get_usage_stats()
    if stats:
        table(stats)
    else:
        empty_state("no tool usage records yet")

    # ── Log new usage ──
    tasks = get_all_tasks()
    tools = get_all_tools()

    section("log new usage")
    if not tasks or not tools:
        empty_state("add tasks and active tools before logging usage")
    else:
        task_map = {t["task_title"]: t["task_id"] for t in tasks}
        tool_map = {t["tool_name"]:  t["tool_id"] for t in tools}

        with st.expander("new tool usage record", expanded=False):
            with st.form("add_usage_form"):
                task      = st.selectbox("task", list(task_map.keys()))
                tool      = st.selectbox("tool", list(tool_map.keys()))
                success   = st.checkbox("successful", value=True)
                output    = st.text_area("output summary")
                if st.form_submit_button("log usage"):
                    add_tool_usage(task_map[task], tool_map[tool], success, output)
                    st.rerun()

    # ── All records ──
    section("all usage records")
    usage_records = get_all_tool_usage()
    if usage_records:
        table(usage_records, bool_cols=["success"])
    else:
        empty_state("no usage records found")
        return

    # ── Delete ──
    section("delete a record")
    usage_options = {
        f"{r['usage_id']} — {r['task_title']} — {r['tool_name']}": r["usage_id"]
        for r in usage_records
    }
    selected    = st.selectbox("select record", list(usage_options.keys()), label_visibility="collapsed")
    selected_id = usage_options[selected]
    if st.button("delete record"):
        delete_tool_usage(selected_id)
        st.rerun()
```
</file>

---

## File: `../Database Project/ai_agent_system/pages/tools.py`
**Last Modified:** `2026-05-23 18:48` | **Size:** `3.97 KB`

<file path="../Database Project/ai_agent_system/pages/tools.py" type="python">
```python
"""
pages/tools.py — Tool management
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, metric_row, table, error_msg


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_tools():
    return execute_query("SELECT * FROM tool ORDER BY tool_id", fetch=True)

def get_tool_by_id(tool_id):
    return execute_query("SELECT * FROM tool WHERE tool_id = %s", (tool_id,), fetch=True)

def add_tool(name, description, tool_type, is_active):
    execute_query(
        "INSERT INTO tool (tool_name, tool_description, tool_type, tool_is_active) VALUES (%s,%s,%s,%s)",
        (name, description, tool_type, is_active),
    )

def update_tool(tool_id, name, description, tool_type, is_active):
    execute_query(
        "UPDATE tool SET tool_name=%s, tool_description=%s, tool_type=%s, tool_is_active=%s WHERE tool_id=%s",
        (name, description, tool_type, is_active, tool_id),
    )

def delete_tool(tool_id):
    execute_query("DELETE FROM tool WHERE tool_id = %s", (tool_id,))


# ── Page ─────────────────────────────────────────────────────────────────────

TOOL_TYPES = ["search", "compute", "communicate", "retrieve"]


def show():
    page_header("tools", "manage agent tools and their availability")

    tools = get_all_tools()

    # ── Stats ──
    section("overview")
    total    = len(tools) if tools else 0
    active   = sum(1 for t in tools if t.get("tool_is_active"))     if tools else 0
    inactive = sum(1 for t in tools if not t.get("tool_is_active")) if tools else 0
    metric_row([("Total Tools", total), ("Active", active), ("Inactive", inactive)])

    # ── Add tool ──
    section("add tool")
    with st.expander("new tool", expanded=False):
        with st.form("add_tool_form"):
            name        = st.text_input("tool name")
            description = st.text_area("description")
            tool_type   = st.selectbox("type", TOOL_TYPES)
            is_active   = st.checkbox("active", value=True)
            if st.form_submit_button("add tool"):
                if name:
                    add_tool(name, description, tool_type, is_active)
                    st.rerun()
                else:
                    error_msg("tool name is required")

    # ── Table ──
    section("all tools")
    if tools:
        table(tools, badge_cols=["tool_type"], bool_cols=["tool_is_active"])
    else:
        empty_state("no tools found")
        return

    # ── Edit / delete ──
    section("edit or delete")
    tool_options = {f"{t['tool_id']} — {t['tool_name']}": t['tool_id'] for t in tools}
    selected     = st.selectbox("select tool", list(tool_options.keys()), label_visibility="collapsed")
    selected_id  = tool_options[selected]
    tool_data    = get_tool_by_id(selected_id)

    if tool_data:
        t = tool_data[0]
        with st.form("edit_tool_form"):
            new_name   = st.text_input("tool name",   value=t["tool_name"])
            new_desc   = st.text_area("description",  value=t["tool_description"] or "")
            cur_type   = t["tool_type"] if t["tool_type"] in TOOL_TYPES else TOOL_TYPES[0]
            new_type   = st.selectbox("type", TOOL_TYPES, index=TOOL_TYPES.index(cur_type))
            new_active = st.checkbox("active", value=bool(t["tool_is_active"]))
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("update tool"):
                    update_tool(selected_id, new_name, new_desc, new_type, new_active)
                    st.rerun()
            with col2:
                if st.form_submit_button("delete tool"):
                    delete_tool(selected_id)
                    st.rerun()
```
</file>

---

## File: `../Database Project/ai_agent_system/pages/users.py`
**Last Modified:** `2026-05-23 18:47` | **Size:** `3.84 KB`

<file path="../Database Project/ai_agent_system/pages/users.py" type="python">
```python
"""
pages/users.py — User management
"""

import streamlit as st
from database.connection import execute_query
from utils import section, badge, empty_state, page_header, metric_row, table, success_msg, error_msg


# ── Queries ──────────────────────────────────────────────────────────────────

def get_all_users():
    return execute_query("SELECT * FROM user ORDER BY user_id", fetch=True)

def get_user_by_id(user_id):
    return execute_query("SELECT * FROM user WHERE user_id = %s", (user_id,), fetch=True)

def add_user(name, email, tier):
    execute_query(
        "INSERT INTO user (user_name, user_email, user_subscription_tier) VALUES (%s, %s, %s)",
        (name, email, tier),
    )

def update_user(user_id, name, email, tier):
    execute_query(
        "UPDATE user SET user_name=%s, user_email=%s, user_subscription_tier=%s WHERE user_id=%s",
        (name, email, tier, user_id),
    )

def delete_user(user_id):
    execute_query("DELETE FROM user WHERE user_id = %s", (user_id,))


# ── Page ─────────────────────────────────────────────────────────────────────

def show():
    page_header("users", "manage user accounts and subscription tiers")

    users = get_all_users()

    # ── Stats ──
    section("overview")
    total      = len(users) if users else 0
    enterprise = sum(1 for u in users if u.get("user_subscription_tier") == "enterprise") if users else 0
    pro        = sum(1 for u in users if u.get("user_subscription_tier") == "pro")        if users else 0
    free       = sum(1 for u in users if u.get("user_subscription_tier") == "free")       if users else 0
    metric_row([("Total Users", total), ("Enterprise", enterprise), ("Pro", pro), ("Free", free)])

    # ── Add user ──
    section("add user")
    with st.expander("new user", expanded=False):
        with st.form("add_user_form"):
            name  = st.text_input("full name")
            email = st.text_input("email address")
            tier  = st.selectbox("subscription tier", ["free", "pro", "enterprise"])
            if st.form_submit_button("add user"):
                if name and email:
                    add_user(name, email, tier)
                    st.rerun()
                else:
                    error_msg("name and email are required")

    # ── Table ──
    section("all users")
    if users:
        table(users, badge_cols=["user_subscription_tier"])
    else:
        empty_state("no users found")
        return

    # ── Edit / delete ──
    section("edit or delete")
    user_options = {f"{u['user_id']} — {u['user_name']}": u['user_id'] for u in users}
    selected     = st.selectbox("select user", list(user_options.keys()), label_visibility="collapsed")
    selected_id  = user_options[selected]
    user_data    = get_user_by_id(selected_id)

    if user_data:
        u = user_data[0]
        with st.form("edit_user_form"):
            new_name  = st.text_input("full name",      value=u["user_name"])
            new_email = st.text_input("email address",  value=u["user_email"])
            tiers     = ["free", "pro", "enterprise"]
            new_tier  = st.selectbox(
                "subscription tier", tiers,
                index=tiers.index(u["user_subscription_tier"]),
            )
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("update user"):
                    update_user(selected_id, new_name, new_email, new_tier)
                    st.rerun()
            with col2:
                if st.form_submit_button("delete user"):
                    delete_user(selected_id)
                    st.rerun()
```
</file>

---

## File: `../Database Project/ai_agent_system/app.py`
**Last Modified:** `2026-05-23 18:47` | **Size:** `44.94 KB`

<file path="../Database Project/ai_agent_system/app.py" type="python">
```python
# # # # ============================================================
# # # # AI AGENT MEMORY & TASK MANAGEMENT SYSTEM
# # # # Main Dashboard Entry Point
# # # # ============================================================
# # # # This file is the homepage of the entire application.
# # # # It uses Streamlit's sidebar navigation to switch
# # # # between all 8 management pages.
# # # #
# # # # Run this file with:
# # # #   streamlit run app.py
# # # # ============================================================

# # # import streamlit as st
# # # from database.connection import get_connection, run_query

# # # # Import all dashboard pages
# # # from pages import users
# # # from pages import agents
# # # from pages import memory
# # # from pages import tasks
# # # from pages import tools
# # # from pages import tool_usage
# # # from pages import sessions
# # # from pages import logs


# # # # ============================================================
# # # # PAGE CONFIGURATION
# # # # ============================================================
# # # # Sets the browser tab title, icon, and layout.
# # # # Must be called before any other Streamlit command.
# # # # ============================================================

# # # st.set_page_config(
# # #     page_title = "AI Agent System",
# # #     page_icon  = "🤖",
# # #     layout     = "wide"
# # # )


# # # # ============================================================
# # # # SIDEBAR NAVIGATION
# # # # ============================================================
# # # # A single dropdown that lets the user switch pages.
# # # # ============================================================

# # # st.sidebar.title("AI Agent System")
# # # st.sidebar.markdown("---")

# # # page = st.sidebar.radio(
# # #     "Navigate to:",
# # #     [
# # #         "Home",
# # #         "Users",
# # #         "Agents",
# # #         "Memory",
# # #         "Tasks",
# # #         "Tools",
# # #         "Tool Usage",
# # #         "Sessions",
# # #         "Logs"
# # #     ]
# # # )

# # # st.sidebar.markdown("---")
# # # st.sidebar.caption("DBMS Project — Phase 3")


# # # # ============================================================
# # # # CONNECTION STATUS CHECK
# # # # ============================================================
# # # # At the top of every page, show whether the database
# # # # is connected. If not, stop the app and show an error.
# # # # ============================================================

# # # def check_database():
# # #     """
# # #     Verifies the MySQL connection on every page load.
# # #     Shows status in the sidebar.
# # #     """
# # #     connection = get_connection()

# # #     if connection is None:
# # #         st.sidebar.error("Database: NOT CONNECTED")
# # #         st.error("Cannot connect to MySQL. Check that:")
# # #         st.write("- MySQL server is running")
# # #         st.write("- Credentials in database/config.py are correct")
# # #         st.stop()
# # #     else:
# # #         st.sidebar.success("Database: CONNECTED")
# # #         connection.close()


# # # check_database()


# # # # ============================================================
# # # # HOME PAGE
# # # # ============================================================
# # # # Shows quick stats from all 8 tables.
# # # # Acts as the project overview.
# # # # ============================================================

# # # def show_home():
# # #     st.title("AI Agent Memory & Task Management System")
# # #     st.caption("A relational database system for managing AI agents, memory, tasks, tools, and audit logs.")

# # #     st.markdown("---")

# # #     # Quick stats from each table
# # #     st.subheader("System Overview")

# # #     col1, col2, col3, col4 = st.columns(4)

# # #     with col1:
# # #         result = run_query("SELECT COUNT(*) AS count FROM user", fetch=True)
# # #         st.metric("Users", result[0]["count"] if result else 0)

# # #     with col2:
# # #         result = run_query("SELECT COUNT(*) AS count FROM agent", fetch=True)
# # #         st.metric("Agents", result[0]["count"] if result else 0)

# # #     with col3:
# # #         result = run_query("SELECT COUNT(*) AS count FROM memory", fetch=True)
# # #         st.metric("Memories", result[0]["count"] if result else 0)

# # #     with col4:
# # #         result = run_query("SELECT COUNT(*) AS count FROM task", fetch=True)
# # #         st.metric("Tasks", result[0]["count"] if result else 0)

# # #     col5, col6, col7, col8 = st.columns(4)

# # #     with col5:
# # #         result = run_query("SELECT COUNT(*) AS count FROM tool", fetch=True)
# # #         st.metric("Tools", result[0]["count"] if result else 0)

# # #     with col6:
# # #         result = run_query("SELECT COUNT(*) AS count FROM tool_usage", fetch=True)
# # #         st.metric("Tool Usages", result[0]["count"] if result else 0)

# # #     with col7:
# # #         result = run_query("SELECT COUNT(*) AS count FROM session", fetch=True)
# # #         st.metric("Sessions", result[0]["count"] if result else 0)

# # #     with col8:
# # #         result = run_query("SELECT COUNT(*) AS count FROM log", fetch=True)
# # #         st.metric("Logs", result[0]["count"] if result else 0)

# # #     st.markdown("---")

# # #     # Project description
# # #     st.subheader("About This System")

# # #     st.markdown("""
# # #     This system models the backend infrastructure of an AI agent platform.
# # #     It stores everything an AI agent needs to remember, every task it performs,
# # #     every tool it uses, and a complete audit trail of all its actions.

# # #     **Entities in this system:**

# # #     - **User** — humans who own and interact with agents
# # #     - **Agent** — the AI agents themselves
# # #     - **Memory** — short-term, long-term, and episodic memory
# # #     - **Task** — work assigned to agents
# # #     - **Tool** — capabilities agents can use
# # #     - **Tool Usage** — bridge table tracking each tool call
# # #     - **Session** — interaction periods between user and agent
# # #     - **Log** — full audit trail of every action

# # #     Use the sidebar on the left to navigate between pages.
# # #     """)


# # # # ============================================================
# # # # PAGE ROUTER
# # # # ============================================================
# # # # Based on the sidebar selection, render the chosen page.
# # # # ============================================================

# # # if page == "Home":
# # #     show_home()

# # # elif page == "Users":
# # #     users.show()

# # # elif page == "Agents":
# # #     agents.show()

# # # elif page == "Memory":
# # #     memory.show()

# # # elif page == "Tasks":
# # #     tasks.show()

# # # elif page == "Tools":
# # #     tools.show()

# # # elif page == "Tool Usage":
# # #     tool_usage.show()

# # # elif page == "Sessions":
# # #     sessions.show()

# # # elif page == "Logs":
# # #     logs.show()

# # """
# # Main Streamlit Dashboard
# # AI Agent Memory and Task Management System
# # """

# # import streamlit as st
# # from database.connection import execute_query

# # # ── Page Configuration ─────────────────────────────────────
# # st.set_page_config(
# #     page_title="AI Agent System",
# #     page_icon="🤖",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # ── Import Pages ───────────────────────────────────────────
# # from pages import users, agents, memory, tasks, tools, tool_usage, sessions, logs


# # def get_summary_stats():
# #     """Fetch counts from all 8 tables for dashboard overview"""
# #     tables = ['user', 'agent', 'memory', 'task', 'tool', 'tool_usage', 'session', 'log']
# #     stats  = {}

# #     for table in tables:
# #         result = execute_query(f"SELECT COUNT(*) as count FROM {table}", fetch=True)
# #         stats[table] = result[0]['count'] if result else 0

# #     return stats


# # def show_home():
# #     """Main dashboard homepage"""

# #     st.title("🤖 AI Agent Memory & Task Management System")
# #     st.markdown("A relational database system for managing AI agent memory, tasks, and operations.")
# #     st.markdown("---")

# #     # ── Summary Cards ──────────────────────────────────────
# #     st.subheader("📊 Database Overview")
# #     stats = get_summary_stats()

# #     col1, col2, col3, col4 = st.columns(4)

# #     with col1:
# #         st.metric("👤 Users",    stats['user'])
# #         st.metric("🔧 Tools",   stats['tool'])

# #     with col2:
# #         st.metric("🤖 Agents",  stats['agent'])
# #         st.metric("🔄 Tool Usage", stats['tool_usage'])

# #     with col3:
# #         st.metric("🧠 Memories", stats['memory'])
# #         st.metric("💬 Sessions", stats['session'])

# #     with col4:
# #         st.metric("📋 Tasks",   stats['task'])
# #         st.metric("📝 Logs",    stats['log'])

# #     st.markdown("---")

# #     # ── Recent Tasks ───────────────────────────────────────
# #     st.subheader("🔥 Recent Tasks")

# #     recent_tasks = execute_query("""
# #         SELECT t.task_title, t.task_status, t.task_priority,
# #                a.agent_name, u.user_name, t.task_created_at
# #         FROM task t
# #         JOIN agent a ON t.agent_id = a.agent_id
# #         JOIN user  u ON t.user_id  = u.user_id
# #         ORDER BY t.task_created_at DESC
# #         LIMIT 5
# #     """, fetch=True)

# #     if recent_tasks:
# #         st.dataframe(recent_tasks, use_container_width=True)
# #     else:
# #         st.info("No tasks yet.")

# #     st.markdown("---")

# #     # ── Recent Logs ────────────────────────────────────────
# #     st.subheader("📋 Recent Log Entries")

# #     recent_logs = execute_query("""
# #         SELECT l.log_action_type, l.log_status,
# #                a.agent_name, l.log_description, l.log_timestamp
# #         FROM log l
# #         JOIN agent a ON l.agent_id = a.agent_id
# #         ORDER BY l.log_timestamp DESC
# #         LIMIT 5
# #     """, fetch=True)

# #     if recent_logs:
# #         st.dataframe(recent_logs, use_container_width=True)
# #     else:
# #         st.info("No logs yet.")

# #     st.markdown("---")

# #     # ── Active Sessions ────────────────────────────────────
# #     st.subheader("💬 Currently Active Sessions")

# #     active_sessions = execute_query("""
# #         SELECT s.session_id, a.agent_name, u.user_name,
# #                s.session_started_at, s.session_channel
# #         FROM session s
# #         JOIN agent a ON s.agent_id = a.agent_id
# #         JOIN user  u ON s.user_id  = u.user_id
# #         WHERE s.session_ended_at IS NULL
# #     """, fetch=True)

# #     if active_sessions:
# #         st.dataframe(active_sessions, use_container_width=True)
# #     else:
# #         st.info("No active sessions.")


# # # ── Sidebar Navigation ─────────────────────────────────────
# # with st.sidebar:
# #     st.image(
# #         "https://img.icons8.com/color/96/artificial-intelligence.png",
# #         width=80
# #     )
# #     st.title("Navigation")
# #     st.markdown("---")

# #     page = st.radio(
# #         "Go to",
# #         [
# #             "🏠 Home",
# #             "👤 Users",
# #             "🤖 Agents",
# #             "🧠 Memory",
# #             "📋 Tasks",
# #             "🔧 Tools",
# #             "🔄 Tool Usage",
# #             "💬 Sessions",
# #             "📝 Logs"
# #         ]
# #     )

# #     st.markdown("---")
# #     st.markdown("**AI Agent System**")
# #     st.markdown("DBMS University Project")
# #     st.markdown("Phase 3 — Implementation")


# # # ── Page Routing ───────────────────────────────────────────
# # if   page == "🏠 Home":        show_home()
# # elif page == "👤 Users":       users.show()
# # elif page == "🤖 Agents":      agents.show()
# # elif page == "🧠 Memory":      memory.show()
# # elif page == "📋 Tasks":       tasks.show()
# # elif page == "🔧 Tools":       tools.show()
# # elif page == "🔄 Tool Usage":  tool_usage.show()
# # elif page == "💬 Sessions":    sessions.show()
# # elif page == "📝 Logs":        logs.show()

# """
# Main Streamlit Dashboard
# AI Agent Memory and Task Management System
# """

# import streamlit as st
# from database.connection import execute_query

# # ── Page Configuration ─────────────────────────────────────
# st.set_page_config(
#     page_title="AgentOps | Command Center",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom minimal styling to elevate metrics and UI elements
# st.markdown("""
#     <style>
#     [data-testid="stMetricValue"] { font-size: 28px; font-weight: 700; }
#     [data-testid="stMetricLabel"] { font-size: 14px; color: #808495; }
#     div.stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: 600; padding: 10px 20px; }
#     </style>
# """, unsafe_allow_html=True)

# # ── Import Pages ───────────────────────────────────────────
# from pages import users, agents, memory, tasks, tools, tool_usage, sessions, logs


# def get_summary_stats():
#     """Fetch counts from all 8 tables for dashboard overview"""
#     tables = ['user', 'agent', 'memory', 'task', 'tool', 'tool_usage', 'session', 'log']
#     stats  = {}
#     for table in tables:
#         try:
#             result = execute_query(f"SELECT COUNT(*) as count FROM {table}", fetch=True)
#             stats[table] = result[0]['count'] if result else 0
#         except Exception:
#             stats[table] = 0
#     return stats


# def show_home():
#     """Main dashboard homepage - Optimized Operations Engine Layout"""

#     # Top Hero Banner & System State
#     col_title, col_status = st.columns([3, 1])
#     with col_title:
#         st.title("🤖 AgentOps Command Center")
#         st.caption("Relational telemetry engine across AI agent instances, memory allocation vectors, and task threads.")
#     with col_status:
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.info("⚡ **System Status:** Operational", icon="🟢")

#     st.markdown("---")

#     # ── Summary Cards (Categorized 4-Column Grid) ─────────────────
#     stats = get_summary_stats()
    
#     m_col1, m_col2, m_col3, m_col4 = st.columns(4)
#     with m_col1:
#         with st.container(border=True):
#             st.metric("Core Accounts", f"{stats['user']} Users")
#     with m_col2:
#         with st.container(border=True):
#             st.metric("Active Run-times", f"{stats['agent']} Agents")
#     with m_col3:
#         with st.container(border=True):
#             st.metric("Memory Blocks", f"{stats['memory']} Vectors")
#     with m_col4:
#         with st.container(border=True):
#             st.metric("Total Executions", f"{stats['task']} Tasks")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ── Operational Streams (Tabbed View removes scrolling friction) ──
#     tab_activity, tab_sessions, tab_capabilities = st.tabs([
#         "🔥 Live Activity Stream", 
#         "💬 Active Sessions", 
#         "🔧 System Infrastructure"
#     ])

#     with tab_activity:
#         col_left, col_right = st.columns(2)

#         with col_left:
#             st.subheader("📋 Recent Task Lifecycle")
#             recent_tasks = execute_query("""
#                 SELECT t.task_title as "Task", t.task_status as "Status", t.task_priority as "Priority",
#                        a.agent_name as "Assigned Agent", u.user_name as "Owner"
#                 FROM task t
#                 JOIN agent a ON t.agent_id = a.agent_id
#                 JOIN user  u ON t.user_id  = u.user_id
#                 ORDER BY t.task_id DESC
#                 LIMIT 6
#             """, fetch=True)

#             if recent_tasks:
#                 st.dataframe(
#                     recent_tasks, 
#                     use_container_width=True,
#                     hide_index=True,
#                     column_config={
#                         "Status": st.column_config.SelectboxColumn(
#                             options=["completed", "in_progress", "pending"],
#                             required=True,
#                         ),
#                         "Priority": st.column_config.TextColumn(help="Task priority level")
#                     }
#                 )
#             else:
#                 st.info("No task activity streams recorded.")

#         with col_right:
#             st.subheader("📝 Live Engine Logs")
#             recent_logs = execute_query("""
#                 SELECT l.log_action_type as "Action", l.log_status as "State",
#                        a.agent_name as "Agent", l.log_description as "Payload"
#                 FROM log l
#                 JOIN agent a ON l.agent_id = a.agent_id
#                 ORDER BY l.log_id DESC
#                 LIMIT 6
#             """, fetch=True)

#             if recent_logs:
#                 st.dataframe(
#                     recent_logs, 
#                     use_container_width=True,
#                     hide_index=True,
#                     column_config={
#                         "State": st.column_config.TextColumn()
#                     }
#                 )
#             else:
#                 st.info("Log sequence is currently empty.")

#     with tab_sessions:
#         st.subheader("📡 Monitored User-Agent Channels")
#         active_sessions = execute_query("""
#             SELECT s.session_id as "Session ID", a.agent_name as "Active Agent", u.user_name as "User Entity",
#                    s.session_channel as "Channel Interface"
#             FROM session s
#             JOIN agent a ON s.agent_id = a.agent_id
#             JOIN user  u ON s.user_id  = u.user_id
#             WHERE s.session_ended_at IS NULL
#         """, fetch=True)

#         if active_sessions:
#             st.dataframe(
#                 active_sessions, 
#                 use_container_width=True,
#                 hide_index=True
#             )
#         else:
#             st.info("No active interactive sockets open right now.")

#     with tab_capabilities:
#         st.subheader("⚙️ System Infrastructure Directory")
#         infra_col1, infra_col2 = st.columns(2)
        
#         with infra_col1:
#             st.markdown(f"**Registered Toolsets:** `{stats['tool']}` systems online")
#             st.markdown(f"**Cumulative Tool Calls:** `{stats['tool_usage']}` successful matches")
#         with infra_col2:
#             st.markdown("""
#             Each core pipeline runs under isolated relational normalization models. 
#             Navigate to individual sidebar views to dispatch modifications, trigger manual tool overrides, or parse extended memory states.
#             """)


# # ── Sidebar Navigation ─────────────────────────────────────
# with st.sidebar:
#     st.markdown(
#         "<div style='text-align: center;'><img src='https://img.icons8.com/color/96/artificial-intelligence.png' width='65'></div>", 
#         unsafe_allow_html=True
#     )
#     st.markdown("<h2 style='text-align: center; margin-top: 0px;'>AgentOps Pro</h2>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center; color: #808495; font-size: 12px;'>DBMS Architecture — Phase 3</p>", unsafe_allow_html=True)
#     st.markdown("---")

#     page = st.radio(
#         "Navigation Matrix",
#         [
#             "🏠 Home Center",
#             "👤 Users Database",
#             "🤖 Agent Register",
#             "🧠 Memory Blocks",
#             "📋 Task Queues",
#             "🔧 Tool Repositories",
#             "🔄 Tool Usage Logs",
#             "💬 Active Sessions",
#             "📝 Master Audit Logs"
#         ]
#     )

#     st.markdown("---")
#     st.caption("🛡️ Core Security Constraints Active")


# # ── Page Routing ───────────────────────────────────────────
# if   page == "🏠 Home Center":         show_home()
# elif page == "👤 Users Database":      users.show()
# elif page == "🤖 Agent Register":     agents.show()
# elif page == "🧠 Memory Blocks":       memory.show()
# elif page == "📋 Task Queues":         tasks.show()
# elif page == "🔧 Tool Repositories":   tools.show()
# elif page == "🔄 Tool Usage Logs":     tool_usage.show()
# elif page == "💬 Active Sessions":     sessions.show()
# elif page == "📝 Master Audit Logs":    logs.show()

#ver 4

"""
AI Agent Memory & Task Management System
Main Dashboard — app.py

Run with:  streamlit run app.py
"""

import streamlit as st
from datetime import datetime
from database.connection import execute_query

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AgentSys",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Design system ────────────────────────────────────────────────────────────
# Semantic color tokens (dark-theme palette)
# Blue  #5b8af5 / bg #0d1a35   → info, IDs, links
# Green #3ec97f / bg #0e2318   → success, active, live
# Amber #e0933a / bg #221a09   → warning, pending, medium
# Red   #e05b5b / bg #220d0d   → critical, failed, high priority
# Muted #3d4558               → labels, secondary text
# ────────────────────────────────────────────────────────────────────────────

STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@300;400;500&display=swap');

/* ── Reset & base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #0b0d12 !important;
    color: #c8cdd8 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
}

/* ── Scrollbar ── */
* { scrollbar-width: thin; scrollbar-color: #1e2230 transparent; }
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #1e2230; border-radius: 2px; }

/* ── Page fade-in ── */
[data-testid="stMainBlockContainer"] > div {
    animation: fadein 0.18s ease;
}
@keyframes fadein { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: none; } }

/* ── Main content area ── */
.main .block-container {
    padding: 1.5rem 2.5rem 3rem !important;
    max-width: 1600px !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0f1117 !important;
    border-right: 1px solid #1a1d27 !important;
}
[data-testid="stSidebar"] > div { padding-top: 0 !important; }

/* Sidebar radio nav */
[data-testid="stSidebar"] .stRadio > div { gap: 0 !important; }
[data-testid="stSidebar"] .stRadio label {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.72rem !important;
    color: #4a5068 !important;
    padding: 0.55rem 0.75rem !important;
    border-radius: 6px !important;
    transition: color 0.12s, background 0.12s !important;
    cursor: pointer !important;
    display: block !important;
    letter-spacing: 0.04em !important;
}
[data-testid="stSidebar"] .stRadio label:hover { color: #9ba3be !important; background: #13161f !important; }
[data-testid="stSidebar"] [aria-checked="true"] + div label,
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:has(input:checked) label {
    color: #e0e4ef !important;
    background: #161b28 !important;
}
/* Hide the actual radio circles */
[data-testid="stSidebar"] [data-baseweb="radio"] > div:first-child { display: none !important; }

/* ── Typography ── */
h1, h2, h3, h4 {
    font-family: 'IBM Plex Mono', monospace !important;
    font-weight: 600 !important;
    color: #e0e4ef !important;
    letter-spacing: -0.02em !important;
}
p, li { color: #8a90a4 !important; font-size: 0.875rem !important; }

/* ── Metric cards ── */
[data-testid="stMetric"] {
    background: #0f1117 !important;
    border: 1px solid #1a1d27 !important;
    border-radius: 8px !important;
    padding: 1.1rem 1.25rem !important;
    transition: border-color 0.15s !important;
}
[data-testid="stMetric"]:hover { border-color: #2a2f45 !important; }
[data-testid="stMetricLabel"] p {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.62rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    color: #3d4558 !important;
}
[data-testid="stMetricValue"] {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 1.75rem !important;
    color: #e0e4ef !important;
    font-weight: 600 !important;
}

/* ── Dataframes ── */
[data-testid="stDataFrame"] iframe { border: none !important; }
[data-testid="stDataFrame"] {
    border: 1px solid #1a1d27 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
}

/* ── Dividers ── */
hr { border: none !important; border-top: 1px solid #1a1d27 !important; margin: 1.25rem 0 !important; }

/* ── Alerts / info boxes ── */
[data-testid="stAlert"] {
    background: #0f1117 !important;
    border: 1px solid #1a1d27 !important;
    border-radius: 6px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.75rem !important;
    color: #4a5068 !important;
}

/* ── Text inputs & selectboxes ── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
textarea,
[data-testid="stSelectbox"] > div > div {
    background: #0f1117 !important;
    border: 1px solid #1a1d27 !important;
    color: #c8cdd8 !important;
    border-radius: 6px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.78rem !important;
}
[data-testid="stTextInput"] input:focus { border-color: #5b8af5 !important; box-shadow: 0 0 0 2px rgba(91,138,245,0.12) !important; }

/* ── Buttons ── */
.stButton > button {
    background: transparent !important;
    border: 1px solid #1e2230 !important;
    color: #6b748c !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.72rem !important;
    border-radius: 6px !important;
    letter-spacing: 0.06em !important;
    padding: 0.4rem 0.9rem !important;
    transition: all 0.14s !important;
}
.stButton > button:hover {
    border-color: #5b8af5 !important;
    color: #5b8af5 !important;
    background: rgba(91,138,245,0.06) !important;
}
.stButton > button[kind="primary"] {
    border-color: #5b8af5 !important;
    color: #5b8af5 !important;
}

/* ── Form submit buttons ── */
[data-testid="stForm"] [data-testid="stFormSubmitButton"] button {
    border-color: #3ec97f !important;
    color: #3ec97f !important;
}

/* ── Expanders ── */
[data-testid="stExpander"] {
    border: 1px solid #1a1d27 !important;
    border-radius: 8px !important;
    background: #0f1117 !important;
}
[data-testid="stExpander"] summary {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.75rem !important;
    color: #6b748c !important;
}

/* ── Column gaps ── */
[data-testid="stHorizontalBlock"] { gap: 12px !important; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"] { display: none !important; }
</style>
"""

# ── Import pages ─────────────────────────────────────────────────────────────
from pages import users, agents, memory, tasks, tools, tool_usage, sessions, logs


# ── Utilities ────────────────────────────────────────────────────────────────

def count(table: str) -> int:
    """Single-table COUNT(*) — safe, no joins."""
    result = execute_query(f"SELECT COUNT(*) AS n FROM `{table}`", fetch=True)
    return result[0]["n"] if result else 0


def check_db() -> bool:
    try:
        execute_query("SELECT 1", fetch=True)
        return True
    except Exception:
        return False


def badge(value: str) -> str:
    """
    Returns an HTML badge string for a status/priority value.
    Maps known values to semantic colors; falls back to muted.
    """
    v = (value or "").lower().strip()
    mapping = {
        # status
        "completed": ("#0e2318", "#3ec97f", "#1a3d2a"),
        "done":      ("#0e2318", "#3ec97f", "#1a3d2a"),
        "active":    ("#0e2318", "#3ec97f", "#1a3d2a"),
        "running":   ("#0e2318", "#3ec97f", "#1a3d2a"),
        "success":   ("#0e2318", "#3ec97f", "#1a3d2a"),
        "pending":   ("#221a09", "#e0933a", "#3a2e10"),
        "in_progress": ("#221a09", "#e0933a", "#3a2e10"),
        "in progress": ("#221a09", "#e0933a", "#3a2e10"),
        "warning":   ("#221a09", "#e0933a", "#3a2e10"),
        "failed":    ("#220d0d", "#e05b5b", "#3d1616"),
        "error":     ("#220d0d", "#e05b5b", "#3d1616"),
        "cancelled": ("#220d0d", "#e05b5b", "#3d1616"),
        # priority
        "high":      ("#220d0d", "#e05b5b", "#3d1616"),
        "critical":  ("#220d0d", "#e05b5b", "#3d1616"),
        "medium":    ("#221a09", "#e0933a", "#3a2e10"),
        "low":       ("#0d1a35", "#5b8af5", "#1a2c55"),
        "info":      ("#0d1a35", "#5b8af5", "#1a2c55"),
    }
    bg, fg, border = mapping.get(v, ("#13161f", "#4a5068", "#1e2230"))
    label = value if value else "—"
    return (
        f'<span style="background:{bg};color:{fg};border:1px solid {border};'
        f'padding:2px 8px;border-radius:3px;font-size:0.62rem;font-weight:600;'
        f'letter-spacing:0.07em;text-transform:uppercase;'
        f'font-family:\'IBM Plex Mono\',monospace;">{label}</span>'
    )


def section(label: str):
    st.markdown(
        f'<div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.58rem;'
        f'text-transform:uppercase;letter-spacing:0.14em;color:#2a2f45;'
        f'padding-bottom:0.6rem;border-bottom:1px solid #1a1d27;'
        f'margin-bottom:0.9rem;">{label}</div>',
        unsafe_allow_html=True,
    )


def empty_state(message: str = "no records found"):
    st.markdown(
        f'<div style="text-align:center;padding:2rem 1rem;border:1px dashed #1a1d27;'
        f'border-radius:8px;font-family:\'IBM Plex Mono\',monospace;'
        f'font-size:0.72rem;color:#2a2f45;letter-spacing:0.08em;">{message}</div>',
        unsafe_allow_html=True,
    )


def command_bar(page_name: str, db_ok: bool):
    """Top command bar: breadcrumb left, status + clock right."""
    now = datetime.now().strftime("%H:%M")
    status_color = "#3ec97f" if db_ok else "#e05b5b"
    status_label = "mysql connected" if db_ok else "mysql disconnected"
    st.markdown(
        f'''<div style="display:flex;align-items:center;justify-content:space-between;
            padding:0.7rem 0;border-bottom:1px solid #1a1d27;margin-bottom:1.75rem;">
          <div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.65rem;
               color:#2a2f45;letter-spacing:0.12em;">
            AGENTSYS &nbsp;/&nbsp;
            <span style="color:#6b748c;">{page_name.upper()}</span>
          </div>
          <div style="display:flex;align-items:center;gap:1.5rem;">
            <span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.65rem;
                  color:{status_color};letter-spacing:0.08em;">
              ● {status_label}
            </span>
            <span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.65rem;
                  color:#2a2f45;">{now}</span>
          </div>
        </div>''',
        unsafe_allow_html=True,
    )


# ── Home page ────────────────────────────────────────────────────────────────

def show_home(db_ok: bool):
    command_bar("home", db_ok)

    st.markdown("# dashboard")
    st.markdown(
        '<p style="margin-top:-0.5rem;margin-bottom:1.5rem;">'
        "AI agent memory &amp; task management system</p>",
        unsafe_allow_html=True,
    )

    # ── Metric grid ──
    section("system overview")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Users",      count("user"))
    c2.metric("Agents",     count("agent"))
    c3.metric("Memories",   count("memory"))
    c4.metric("Tasks",      count("task"))

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Tools",      count("tool"))
    c6.metric("Tool Usage", count("tool_usage"))
    c7.metric("Sessions",   count("session"))
    c8.metric("Logs",       count("log"))

    st.markdown("---")

    # ── Agent status panel ──
    section("agent status")
    agent_rows = execute_query(
        """
        SELECT a.agent_name, a.agent_status, a.agent_type,
               COUNT(t.task_id) AS open_tasks
        FROM   agent a
        LEFT JOIN task t
               ON t.agent_id = a.agent_id
              AND t.task_status NOT IN ('completed', 'done', 'cancelled')
        GROUP  BY a.agent_id, a.agent_name, a.agent_status, a.agent_type
        ORDER  BY a.agent_name
        LIMIT  8
        """,
        fetch=True,
    )
    if agent_rows:
        cols = st.columns(min(len(agent_rows), 4))
        for i, row in enumerate(agent_rows):
            col = cols[i % 4]
            status = (row.get("agent_status") or "unknown").lower()
            dot_color = "#3ec97f" if status in ("active", "running", "online") else "#2a2f45"
            name  = row.get("agent_name", "—")
            atype = row.get("agent_type", "")
            tasks_n = row.get("open_tasks", 0)
            col.markdown(
                f'''<div style="background:#0f1117;border:1px solid #1a1d27;
                    border-radius:8px;padding:0.9rem 1rem;margin-bottom:8px;">
                  <div style="display:flex;align-items:center;gap:7px;margin-bottom:6px;">
                    <span style="width:7px;height:7px;border-radius:50%;
                          background:{dot_color};display:inline-block;flex-shrink:0;"></span>
                    <span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.78rem;
                          font-weight:600;color:#e0e4ef;">{name}</span>
                  </div>
                  <div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.62rem;
                       color:#3d4558;margin-bottom:4px;">{atype or "agent"}</div>
                  <div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.65rem;
                       color:#4a5068;">{tasks_n} open task{"s" if tasks_n != 1 else ""}</div>
                </div>''',
                unsafe_allow_html=True,
            )
    else:
        empty_state("no agents registered")

    st.markdown("---")

    # ── Activity feed + recent tasks side by side ──
    left, right = st.columns([1, 1])

    with left:
        section("activity feed")
        log_rows = execute_query(
            """
            SELECT l.log_action_type, l.log_status,
                   a.agent_name, l.log_description, l.log_timestamp
            FROM   log   l
            JOIN   agent a ON l.agent_id = a.agent_id
            ORDER  BY l.log_timestamp DESC
            LIMIT  10
            """,
            fetch=True,
        )
        if log_rows:
            items_html = ""
            for row in log_rows:
                ts        = str(row.get("log_timestamp", ""))[:16]
                action    = row.get("log_action_type", "action")
                status    = row.get("log_status", "")
                agent_n   = row.get("agent_name", "?")
                desc      = row.get("log_description") or ""
                dot_c = "#3ec97f" if str(status).lower() in ("success","completed","done") \
                        else "#e05b5b" if str(status).lower() in ("failed","error") \
                        else "#e0933a"
                items_html += f"""
                <div style="display:flex;gap:12px;padding:8px 0;
                     border-bottom:1px solid #13161f;">
                  <div style="flex-shrink:0;display:flex;flex-direction:column;
                       align-items:center;padding-top:4px;">
                    <span style="width:7px;height:7px;border-radius:50%;
                          background:{dot_c};display:block;"></span>
                    <span style="width:1px;flex:1;background:#1a1d27;
                          display:block;margin-top:4px;min-height:16px;"></span>
                  </div>
                  <div style="flex:1;min-width:0;">
                    <div style="display:flex;align-items:center;gap:8px;
                         flex-wrap:wrap;margin-bottom:2px;">
                      <span style="font-family:'IBM Plex Mono',monospace;font-size:0.72rem;
                            font-weight:600;color:#c8cdd8;">{action}</span>
                      <span style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;
                            color:#3d4558;">via {agent_n}</span>
                    </div>
                    {'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:0.72rem;color:#4a5068;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">' + desc[:60] + '</div>' if desc else ''}
                    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.6rem;
                         color:#2a2f45;margin-top:2px;">{ts}</div>
                  </div>
                </div>"""
            st.markdown(
                f'<div style="max-height:400px;overflow-y:auto;">{items_html}</div>',
                unsafe_allow_html=True,
            )
        else:
            empty_state("no log entries yet")

    with right:
        section("recent tasks")
        task_rows = execute_query(
            """
            SELECT t.task_title, t.task_status, t.task_priority,
                   a.agent_name, u.user_name, t.task_created_at
            FROM   task  t
            JOIN   agent a ON t.agent_id = a.agent_id
            JOIN   user  u ON t.user_id  = u.user_id
            ORDER  BY t.task_created_at DESC
            LIMIT  10
            """,
            fetch=True,
        )
        if task_rows:
            rows_html = ""
            for row in task_rows:
                title    = row.get("task_title", "—")
                status   = row.get("task_status", "")
                priority = row.get("task_priority", "")
                agent_n  = row.get("agent_name", "")
                user_n   = row.get("user_name", "")
                ts       = str(row.get("task_created_at", ""))[:16]
                rows_html += f"""
                <div style="padding:8px 0;border-bottom:1px solid #13161f;">
                  <div style="display:flex;align-items:flex-start;
                       justify-content:space-between;gap:8px;margin-bottom:4px;">
                    <span style="font-family:'IBM Plex Mono',monospace;font-size:0.74rem;
                          color:#c8cdd8;font-weight:500;">{title}</span>
                    <div style="display:flex;gap:4px;flex-shrink:0;">
                      {badge(priority)}
                      {badge(status)}
                    </div>
                  </div>
                  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;
                       color:#3d4558;">{agent_n} · {user_n} · {ts}</div>
                </div>"""
            st.markdown(
                f'<div style="max-height:400px;overflow-y:auto;">{rows_html}</div>',
                unsafe_allow_html=True,
            )
        else:
            empty_state("no tasks yet")

    st.markdown("---")

    # ── Active sessions ──
    section("active sessions")
    session_rows = execute_query(
        """
        SELECT s.session_id, a.agent_name, u.user_name,
               s.session_started_at, s.session_channel
        FROM   session s
        JOIN   agent  a ON s.agent_id = a.agent_id
        JOIN   user   u ON s.user_id  = u.user_id
        WHERE  s.session_ended_at IS NULL
        """,
        fetch=True,
    )
    if session_rows:
        rows_html = ""
        for row in session_rows:
            sid     = str(row.get("session_id", ""))[:12]
            agent_n = row.get("agent_name", "")
            user_n  = row.get("user_name", "")
            started = str(row.get("session_started_at", ""))[:16]
            channel = row.get("session_channel", "")
            rows_html += f"""
            <div style="display:flex;align-items:center;gap:1rem;
                 padding:8px 0;border-bottom:1px solid #13161f;flex-wrap:wrap;">
              <span style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;
                    color:#5b8af5;min-width:100px;">{sid}…</span>
              <span style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;
                    color:#e0e4ef;min-width:80px;">{agent_n}</span>
              <span style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;
                    color:#4a5068;flex:1;">{user_n}</span>
              <span style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;
                    color:#3d4558;">{channel}</span>
              <span style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;
                    color:#2a2f45;">{started}</span>
              <span style="width:7px;height:7px;border-radius:50%;
                    background:#3ec97f;flex-shrink:0;"></span>
            </div>"""
        st.markdown(rows_html, unsafe_allow_html=True)
    else:
        empty_state("no active sessions")


# ── Sidebar ──────────────────────────────────────────────────────────────────

db_ok = check_db()

with st.sidebar:
    st.markdown(
        '<div style="padding:1.5rem 1rem 1rem;">'
        '<div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.85rem;'
        'font-weight:600;color:#e0e4ef;letter-spacing:0.04em;">AGENTSYS</div>'
        '<div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.58rem;'
        'color:#2a2f45;letter-spacing:0.1em;margin-top:2px;">DBMS · PHASE 3</div>'
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown('<div style="padding:0 1rem 0.75rem;">', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.62rem;'
        f'color:{"#3ec97f" if db_ok else "#e05b5b"};letter-spacing:0.07em;">'
        f'● {"connected" if db_ok else "disconnected"}</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div style="height:1px;background:#1a1d27;margin:0 1rem 1rem;"></div>',
        unsafe_allow_html=True,
    )

    NAV = {
        "Home":       "dashboard",
        "Users":      "users",
        "Agents":     "agents",
        "Memory":     "memory",
        "Tasks":      "tasks",
        "Tools":      "tools",
        "Tool Usage": "tool_usage",
        "Sessions":   "sessions",
        "Logs":       "logs",
    }
    page = st.radio(
        label="",
        options=list(NAV.keys()),
        label_visibility="collapsed",
    )

    if not db_ok:
        st.markdown(
            '<div style="margin:1rem;padding:0.75rem;background:#220d0d;'
            'border:1px solid #3d1616;border-radius:6px;font-family:\'IBM Plex Mono\','
            'monospace;font-size:0.65rem;color:#e05b5b;line-height:1.6;">'
            "Cannot reach MySQL.<br>Check database/config.py.</div>",
            unsafe_allow_html=True,
        )
        st.stop()


# ── Inject global styles ──────────────────────────────────────────────────────
st.markdown(STYLES, unsafe_allow_html=True)


# ── Route ────────────────────────────────────────────────────────────────────
if page == "Home":
    show_home(db_ok)
else:
    # Inject command bar into sub-pages
    command_bar(page, db_ok)
    {
        "Users":      users.show,
        "Agents":     agents.show,
        "Memory":     memory.show,
        "Tasks":      tasks.show,
        "Tools":      tools.show,
        "Tool Usage": tool_usage.show,
        "Sessions":   sessions.show,
        "Logs":       logs.show,
    }[page]()
```
</file>

---

## File: `../Database Project/ai_agent_system/requirements.txt`
**Last Modified:** `2026-05-23 09:28` | **Size:** `0.03 KB`

<file path="../Database Project/ai_agent_system/requirements.txt" type="text">
```text
streamlit
mysql-connector-python

```
</file>

---

## File: `../Database Project/ai_agent_system/test_connection.py`
**Last Modified:** `2026-05-23 12:29` | **Size:** `2.69 KB`

<file path="../Database Project/ai_agent_system/test_connection.py" type="python">
```python
"""
Test script to verify MySQL connection works
"""

from database.connection import get_connection, close_connection, execute_query


def test_connection():
    """Test basic connection"""
    print("Testing MySQL connection...")
    
    connection = get_connection()
    
    if connection:
        print("✓ Connection successful")
        
        db_info = connection.get_server_info()
        print(f"✓ MySQL Server version: {db_info}")
        
        close_connection(connection)
        print("✓ Connection closed")
        return True
    else:
        print("✗ Connection failed")
        return False


def test_query():
    """Test executing a query"""
    print("\nTesting query execution...")
    
    # Test query - show all tables
    query = "SHOW TABLES;"
    results = execute_query(query, fetch=True)
    
    if results:
        print(f"✓ Query executed successfully")
        print(f"✓ Found {len(results)} tables:")
        for row in results:
            table_name = list(row.values())[0]
            print(f"  - {table_name}")
        return True
    else:
        print("✗ Query failed")
        return False


def test_insert_and_select():
    """Test inserting and selecting data"""
    print("\nTesting insert and select...")
    
    # Insert a test user
    insert_query = """
    INSERT INTO user (user_name, user_email, user_subscription_tier)
    VALUES (%s, %s, %s)
    """
    params = ("Test User", "test@example.com", "free")
    
    execute_query(insert_query, params)
    print("✓ Test user inserted")
    
    # Select that user back
    select_query = "SELECT * FROM user WHERE user_email = %s"
    results = execute_query(select_query, ("test@example.com",), fetch=True)
    
    if results and len(results) > 0:
        print("✓ Test user retrieved:")
        print(f"  ID: {results[0]['user_id']}")
        print(f"  Name: {results[0]['user_name']}")
        print(f"  Email: {results[0]['user_email']}")
        print(f"  Tier: {results[0]['user_subscription_tier']}")
        
        # Clean up - delete test user
        delete_query = "DELETE FROM user WHERE user_email = %s"
        execute_query(delete_query, ("test@example.com",))
        print("✓ Test user deleted")
        
        return True
    else:
        print("✗ Failed to retrieve test user")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("MySQL Connection Test")
    print("=" * 60)
    
    # Run all tests
    test1 = test_connection()
    test2 = test_query()
    test3 = test_insert_and_select()
    
    print("\n" + "=" * 60)
    if test1 and test2 and test3:
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 60)
```
</file>

---

## File: `../Database Project/ai_agent_system/utils.py`
**Last Modified:** `2026-05-23 18:47` | **Size:** `8.52 KB`

<file path="../Database Project/ai_agent_system/utils.py" type="python">
```python
"""
utils.py — shared design-system helpers
Import in every page:  from utils import section, badge, empty_state, command_bar, page_header
"""

import streamlit as st
from datetime import datetime


# ── Semantic color map ───────────────────────────────────────────────────────
# bg / fg / border
_BADGE_MAP = {
    # status — green
    "completed":   ("#0e2318", "#3ec97f", "#1a3d2a"),
    "done":        ("#0e2318", "#3ec97f", "#1a3d2a"),
    "active":      ("#0e2318", "#3ec97f", "#1a3d2a"),
    "running":     ("#0e2318", "#3ec97f", "#1a3d2a"),
    "success":     ("#0e2318", "#3ec97f", "#1a3d2a"),
    "online":      ("#0e2318", "#3ec97f", "#1a3d2a"),
    "true":        ("#0e2318", "#3ec97f", "#1a3d2a"),
    "1":           ("#0e2318", "#3ec97f", "#1a3d2a"),
    # status — amber
    "pending":     ("#221a09", "#e0933a", "#3a2e10"),
    "in_progress": ("#221a09", "#e0933a", "#3a2e10"),
    "in progress": ("#221a09", "#e0933a", "#3a2e10"),
    "paused":      ("#221a09", "#e0933a", "#3a2e10"),
    "warning":     ("#221a09", "#e0933a", "#3a2e10"),
    "medium":      ("#221a09", "#e0933a", "#3a2e10"),
    # status — red
    "failed":      ("#220d0d", "#e05b5b", "#3d1616"),
    "failure":     ("#220d0d", "#e05b5b", "#3d1616"),
    "error":       ("#220d0d", "#e05b5b", "#3d1616"),
    "cancelled":   ("#220d0d", "#e05b5b", "#3d1616"),
    "terminated":  ("#220d0d", "#e05b5b", "#3d1616"),
    "false":       ("#220d0d", "#e05b5b", "#3d1616"),
    "0":           ("#220d0d", "#e05b5b", "#3d1616"),
    "high":        ("#220d0d", "#e05b5b", "#3d1616"),
    "critical":    ("#220d0d", "#e05b5b", "#3d1616"),
    # status — blue
    "low":         ("#0d1a35", "#5b8af5", "#1a2c55"),
    "info":        ("#0d1a35", "#5b8af5", "#1a2c55"),
    # tiers
    "enterprise":  ("#0d1a35", "#5b8af5", "#1a2c55"),
    "pro":         ("#0e2318", "#3ec97f", "#1a3d2a"),
    "free":        ("#13161f", "#4a5068", "#1e2230"),
    # memory types
    "long-term":   ("#0d1a35", "#5b8af5", "#1a2c55"),
    "short-term":  ("#221a09", "#e0933a", "#3a2e10"),
    "episodic":    ("#1a0d35", "#a07af5", "#2e1a55"),
    # tool types
    "search":      ("#0d1a35", "#5b8af5", "#1a2c55"),
    "compute":     ("#221a09", "#e0933a", "#3a2e10"),
    "communicate": ("#0e2318", "#3ec97f", "#1a3d2a"),
    "retrieve":    ("#1a0d35", "#a07af5", "#2e1a55"),
}
_BADGE_DEFAULT = ("#13161f", "#4a5068", "#1e2230")


def badge(value) -> str:
    """Return an HTML pill badge for any status/priority/type value."""
    raw = str(value) if value is not None else ""
    key = raw.lower().strip()
    bg, fg, border = _BADGE_MAP.get(key, _BADGE_DEFAULT)
    label = raw if raw else "—"
    return (
        f'<span style="background:{bg};color:{fg};border:1px solid {border};'
        f'padding:2px 8px;border-radius:3px;font-size:0.62rem;font-weight:600;'
        f'letter-spacing:0.07em;text-transform:uppercase;white-space:nowrap;'
        f'font-family:\'IBM Plex Mono\',monospace;">{label}</span>'
    )


def section(label: str):
    """Muted uppercase section divider."""
    st.markdown(
        f'<div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.58rem;'
        f'text-transform:uppercase;letter-spacing:0.14em;color:#2a2f45;'
        f'padding-bottom:0.6rem;border-bottom:1px solid #1a1d27;'
        f'margin:1.5rem 0 0.9rem;">{label}</div>',
        unsafe_allow_html=True,
    )


def empty_state(message: str = "no records found"):
    """Dashed placeholder shown when a query returns nothing."""
    st.markdown(
        f'<div style="text-align:center;padding:2.5rem 1rem;'
        f'border:1px dashed #1a1d27;border-radius:8px;'
        f'font-family:\'IBM Plex Mono\',monospace;'
        f'font-size:0.72rem;color:#2a2f45;letter-spacing:0.08em;">'
        f'{message}</div>',
        unsafe_allow_html=True,
    )


def command_bar(page_name: str, db_ok: bool = True):
    """Top bar: breadcrumb left, DB status + clock right."""
    now = datetime.now().strftime("%H:%M")
    status_color = "#3ec97f" if db_ok else "#e05b5b"
    status_label = "mysql connected" if db_ok else "mysql disconnected"
    st.markdown(
        f'''<div style="display:flex;align-items:center;
            justify-content:space-between;padding:0.6rem 0;
            border-bottom:1px solid #1a1d27;margin-bottom:1.75rem;">
          <div style="font-family:\'IBM Plex Mono\',monospace;font-size:0.65rem;
               color:#2a2f45;letter-spacing:0.12em;">
            AGENTSYS &nbsp;/&nbsp;
            <span style="color:#6b748c;">{page_name.upper()}</span>
          </div>
          <div style="display:flex;align-items:center;gap:1.5rem;">
            <span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.65rem;
                  color:{status_color};letter-spacing:0.08em;">
              ● {status_label}
            </span>
            <span style="font-family:\'IBM Plex Mono\',monospace;
                  font-size:0.65rem;color:#2a2f45;">{now}</span>
          </div>
        </div>''',
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = ""):
    """Page title + optional subtitle in the design system font."""
    st.markdown(
        f'<h1 style="font-family:\'IBM Plex Mono\',monospace;font-size:1.5rem;'
        f'font-weight:600;color:#e0e4ef;letter-spacing:-0.02em;margin:0 0 0.25rem;">'
        f'{title}</h1>',
        unsafe_allow_html=True,
    )
    if subtitle:
        st.markdown(
            f'<p style="font-family:\'IBM Plex Sans\',sans-serif;font-size:0.8rem;'
            f'color:#4a5068;margin:0 0 1.5rem;">{subtitle}</p>',
            unsafe_allow_html=True,
        )


def metric_row(items: list[tuple]):
    """
    Render a row of metric cards.
    items = [(label, value), ...]  — up to 4.
    """
    cols = st.columns(len(items))
    for col, (label, value) in zip(cols, items):
        col.metric(label, value)


def success_msg(msg: str):
    st.markdown(
        f'<div style="background:#0e2318;border:1px solid #1a3d2a;border-radius:6px;'
        f'padding:0.6rem 1rem;font-family:\'IBM Plex Mono\',monospace;'
        f'font-size:0.72rem;color:#3ec97f;margin:0.5rem 0;">✓ {msg}</div>',
        unsafe_allow_html=True,
    )


def error_msg(msg: str):
    st.markdown(
        f'<div style="background:#220d0d;border:1px solid #3d1616;border-radius:6px;'
        f'padding:0.6rem 1rem;font-family:\'IBM Plex Mono\',monospace;'
        f'font-size:0.72rem;color:#e05b5b;margin:0.5rem 0;">✗ {msg}</div>',
        unsafe_allow_html=True,
    )


def table(rows: list[dict], badge_cols: list[str] = None, bool_cols: list[str] = None):
    """
    Render a list of dicts as a styled HTML table.
    badge_cols: column names whose values should be rendered as badges.
    bool_cols:  column names containing 0/1 or True/False.
    """
    if not rows:
        empty_state()
        return

    badge_cols = badge_cols or []
    bool_cols  = bool_cols  or []
    headers    = list(rows[0].keys())

    th_style = (
        "padding:7px 14px;font-family:'IBM Plex Mono',monospace;"
        "font-size:0.6rem;text-transform:uppercase;letter-spacing:0.1em;"
        "color:#2a2f45;text-align:left;border-bottom:1px solid #1a1d27;"
        "white-space:nowrap;"
    )
    td_style = (
        "padding:7px 14px;font-family:'IBM Plex Mono',monospace;"
        "font-size:0.72rem;color:#8a90a4;"
        "border-bottom:1px solid #13161f;white-space:nowrap;"
    )

    header_html = "".join(f'<th style="{th_style}">{h}</th>' for h in headers)

    rows_html = ""
    for row in rows:
        cells = ""
        for h in headers:
            val = row.get(h, "")
            if h in bool_cols:
                cell = badge("true" if val else "false")
            elif h in badge_cols:
                cell = badge(str(val))
            else:
                display = str(val) if val is not None else "—"
                # truncate long strings
                if len(display) > 60:
                    display = display[:57] + "…"
                cell = f'<span style="color:#c8cdd8;">{display}</span>' \
                    if h == headers[0] else display
            cells += f'<td style="{td_style}">{cell}</td>'
        rows_html += f"<tr>{cells}</tr>"

    html = (
        f'<div style="border:1px solid #1a1d27;border-radius:8px;overflow:hidden;'
        f'overflow-x:auto;margin-bottom:1rem;">'
        f'<table style="width:100%;border-collapse:collapse;">'
        f'<thead><tr>{header_html}</tr></thead>'
        f'<tbody>{rows_html}</tbody>'
        f'</table></div>'
    )
    st.markdown(html, unsafe_allow_html=True)
```
</file>

---

## File: `../Khwarizm/agents/__init__.py`
**Last Modified:** `2026-05-19 11:39` | **Size:** `0.00 KB`

<file path="../Khwarizm/agents/__init__.py" type="python">
```python

```
</file>

---

## File: `../Khwarizm/agents/baseagent.py`
**Last Modified:** `2026-05-26 06:47` | **Size:** `6.58 KB`

<file path="../Khwarizm/agents/baseagent.py" type="python">
```python
from agents.config import Config
from llms import BaseLLM
from tools import ToolRegistry
from memory.stm import ShortTermMemory
from memory.ltm import LongTermMemory
import xml.etree.ElementTree as ET

class BaseAgent:
    def __init__(self,
                name,
                llm:BaseLLM,
                system_prompt: str = "You are a helpful AI assistant", 
                
                tools: list = None
                ):
        
        self.llm = llm

        self.registry = ToolRegistry()
        tools = tools or []
        # THE LOOP 
        # Which automates the work of resgistering the TOOLS manually
        for tool in tools:
            self.registry.register(tool)

        # This is basically a prompt that tells the llm what tools it has
        if tools:
            tool_schemas = self.registry.get_descriptions()
            system_prompt = (
                f"{system_prompt}\n\n"
                f"You have access to these tools:\n"
                f"{tool_schemas}\n\n"
                f"STRICT RULES:\n"
                f"CRITICAL: Only use ONE tool per response. Wait for the tool result before taking your next step.\n"
                f"1. Use ONE tool per response. No exceptions.\n"
                f"2. After using a tool,Stop. wait for the result before continuing. Do not write anything else.\n"
                f"3. If you use more than one tool in a single response, I will stop the conversation and you will fail the task.\n\n"
                f"4. NEVER call the same or different tool twice in one response.\n"
                f"5. You MUST use tools when the task requires them.\n\n"
                f"To use a tool, respond EXACTLY in this XML format:\n\n"
                f"<tool_use>\n"
                f"  <tool_name>tool_name_here</tool_name>\n"
                f"  <parameters>\n"
                f"    <param_name>value here</param_name>\n"
                f"  </parameters>\n"
                f"</tool_use>"
            )

        # THE CONFIG
        self.config = Config(
            name=name,
            description="Agent",
            system_prompt=system_prompt,
        )

        # Memory 
        # The Memory part of the agent
        # Truly automatic  
        self.__base_system_prompt = system_prompt
        self.__short_term = ShortTermMemory(max_entries=self.config.max_stm_entries)
        self.__long_term = LongTermMemory(
            agent_name=name,
            max_entries=self.config.max_ltm_entries
            )

    @property
    def name(self) -> str:
        # agent's name
        return self.config.name
    
    @property
    def description(self) -> str:
        # agent's description
        return self.config.description

    @property
    def system_prompt(self) -> str:
        # system prompt
        return self.config.system_prompt

    @property
    def tools(self) -> list:
        # list of tool names
        return self.registry.list_tools()
    

    def run(self, user_input: str) -> str:

        self.__short_term.add_entry(role="user", content= user_input)
        self.__long_term.add_entry(role="user", content= user_input)


        iterations = 0
        max_iters = self.config.max_iterations

        print(f"Starting: {self.config.name} \n{self.config.name} is thinking...")
        

        while iterations < max_iters:
            iterations += 1
            print(f"  [Loop {iterations}/{max_iters}] Agent is thinking...")

            #  Build context from BOTH memories

            long_term_context = self.__long_term.get_context()
            short_term_context = self.__short_term.get_context()

            #  Combine them into one prompt
            full_context = (
                f"Past Conversations:\n{long_term_context}\n\n"
                f"Current Session:\n{short_term_context}"
            )
            
            # print("\n--- SYSTEM PROMPT ---")
            # print(self.config.system_prompt)
            # print("--- END SYSTEM PROMPT ---\n")


            response = self.llm.generate(
                system_prompt=self.__base_system_prompt,
                user_prompt=full_context
            )

            if response.startswith("Error: LLM API failed"):
                print("  -> Critical LLM Error encountered.")
                return response
            
            
            if "<think>" in response and "</think>" in response:
                response = response.split("</think>")[-1].strip()

        # Check if LLM decided to use a tool
            if "<tool_use>" in response:
                tool_note = self.__handle_tool_call(response)

                self.__short_term.add_entry(
                    role="assistant",
                    content=response
                )
                self.__short_term.add_entry(
                    role="tool",
                    content=tool_note
                )
                continue

             # Save to both memories
            self.__short_term.add_entry(role="assistant", content=response)
            self.__long_term.add_entry(role="assistant", content=response)

            return response if response else "Error: Agent reached max iterations without a final answer."

    def __handle_tool_call(self, response: str) -> str:
        try:
            start = response.find("<tool_use>")
            end = response.find("</tool_use>") + len("</tool_use>")
            xml_block = response[start:end]

            root = ET.fromstring(xml_block)

            # Extract tool name
            tool_name_el = root.find("tool_name")
            if tool_name_el is None:
                return "Error: No tool_name found in XML."
            tool_name = tool_name_el.text.strip()

            parameters = {}
            params_el = root.find("parameters")
            if params_el is not None:
                for param in params_el:
                    parameters[param.tag] = param.text.strip() if param.text else ""

            print(f"  -> Tool: {tool_name} | Parameters: {parameters}")

            # Fetch the tool from registry
            tool = self.registry.get_tool(tool_name)
            if not tool:
                return f"Error: Unknown tool '{tool_name}'. Available: {self.registry.list_tools()}"

            # Run the tool with the clean dictionary
            result = tool.run(parameters)
            return f"Tool '{tool_name}' returned: {result}"

        except ET.ParseError as e:
            return f"Error: Could not parse XML tool call. Details: {e}"
        except Exception as e:
            return f"Error during tool execution: {e}"


    def clear_memory(self):
        self.__short_term.clear()
        self.__long_term.clear()
        print(f"[{self.name}] Memory cleared.")
```
</file>

---

## File: `../Khwarizm/agents/config.py`
**Last Modified:** `2026-05-25 12:48` | **Size:** `1.05 KB`

<file path="../Khwarizm/agents/config.py" type="python">
```python
from dataclasses import dataclass

@dataclass
class Config:
#---Identity
    name: str
    # model: str
    description: str = "This AI agent is like an AI from the future and will give you futuristic explainations for every question you ask."

#---Prompts
    system_prompt: str = "You are a helpful AI assistant."
    

#---LLM Settings
    
    max_tokens: int = 1000

#---Behavior settings
    max_iterations: int = 50

     # --- Memory ---
    max_ltm_entries: int = 100
    max_stm_entries: int = 50

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Agent must have a name")
        if self.max_tokens <= 0:
            raise ValueError("max_tokens must be greater than 0")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than 0")
        if self.max_ltm_entries <= 0:
            raise ValueError("max_ltm_entries must be greater than 0")
        if self.max_stm_entries <= 0:
            raise ValueError("max_stm_entries must be greater than 0")
        



```
</file>

---

## File: `../Khwarizm/docs/codecontext.min.md`
**Last Modified:** `2026-05-26 07:32` | **Size:** `85.71 KB`

<file path="../Khwarizm/docs/codecontext.min.md" type="markdown">
```markdown
## File: `agents/__init__.py`
<file path="agents/__init__.py" type="python">
```python

```
</file>
## File: `agents/baseagent.py`
<file path="agents/baseagent.py" type="python">
```python
from agents.config import Config
from llms import BaseLLM
from tools import ToolRegistry
from memory.stm import ShortTermMemory
from memory.ltm import LongTermMemory
import xml.etree.ElementTree as ET
class BaseAgent:
    def __init__(self,
                name,
                llm:BaseLLM,
                system_prompt: str = "You are a helpful AI assistant", 
                tools: list = None
                ):
        self.llm = llm
        self.registry = ToolRegistry()
        tools = tools or []
        # THE LOOP 
        # Which automates the work of resgistering the TOOLS manually
        for tool in tools:
            self.registry.register(tool)
        # This is basically a prompt that tells the llm what tools it has
        if tools:
            tool_schemas = self.registry.get_descriptions()
            system_prompt = (
                f"{system_prompt}\n\n"
                f"You have access to these tools:\n"
                f"{tool_schemas}\n\n"
                f"STRICT RULES:\n"
                f"CRITICAL: Only use ONE tool per response. Wait for the tool result before taking your next step.\n"
                f"1. Use ONE tool per response. No exceptions.\n"
                f"2. After using a tool,Stop. wait for the result before continuing. Do not write anything else.\n"
                f"3. If you use more than one tool in a single response, I will stop the conversation and you will fail the task.\n\n"
                f"4. NEVER call the same or different tool twice in one response.\n"
                f"5. You MUST use tools when the task requires them.\n\n"
                f"To use a tool, respond EXACTLY in this XML format:\n\n"
                f"<tool_use>\n"
                f"  <tool_name>tool_name_here</tool_name>\n"
                f"  <parameters>\n"
                f"    <param_name>value here</param_name>\n"
                f"  </parameters>\n"
                f"</tool_use>"
            )
        # THE CONFIG
        self.config = Config(
            name=name,
            description="Agent",
            system_prompt=system_prompt,
        )
        # Memory 
        # The Memory part of the agent
        # Truly automatic  
        self.__base_system_prompt = system_prompt
        self.__short_term = ShortTermMemory(max_entries=self.config.max_stm_entries)
        self.__long_term = LongTermMemory(
            agent_name=name,
            max_entries=self.config.max_ltm_entries
            )
    @property
    def name(self) -> str:
        # agent's name
        return self.config.name
    @property
    def description(self) -> str:
        # agent's description
        return self.config.description
    @property
    def system_prompt(self) -> str:
        # system prompt
        return self.config.system_prompt
    @property
    def tools(self) -> list:
        # list of tool names
        return self.registry.list_tools()
    def run(self, user_input: str) -> str:
        self.__short_term.add_entry(role="user", content= user_input)
        self.__long_term.add_entry(role="user", content= user_input)
        iterations = 0
        max_iters = self.config.max_iterations
        print(f"Starting: {self.config.name} \n{self.config.name} is thinking...")
        while iterations < max_iters:
            iterations += 1
            print(f"  [Loop {iterations}/{max_iters}] Agent is thinking...")
            #  Build context from BOTH memories
            long_term_context = self.__long_term.get_context()
            short_term_context = self.__short_term.get_context()
            #  Combine them into one prompt
            full_context = (
                f"Past Conversations:\n{long_term_context}\n\n"
                f"Current Session:\n{short_term_context}"
            )
            # print("\n--- SYSTEM PROMPT ---")
            # print(self.config.system_prompt)
            # print("--- END SYSTEM PROMPT ---\n")
            response = self.llm.generate(
                system_prompt=self.__base_system_prompt,
                user_prompt=full_context
            )
            if response.startswith("Error: LLM API failed"):
                print("  -> Critical LLM Error encountered.")
                return response
            if "<think>" in response and "</think>" in response:
                response = response.split("</think>")[-1].strip()
        # Check if LLM decided to use a tool
            if "<tool_use>" in response:
                tool_note = self.__handle_tool_call(response)
                self.__short_term.add_entry(
                    role="assistant",
                    content=response
                )
                self.__short_term.add_entry(
                    role="tool",
                    content=tool_note
                )
                continue
             # Save to both memories
            self.__short_term.add_entry(role="assistant", content=response)
            self.__long_term.add_entry(role="assistant", content=response)
            return response if response else "Error: Agent reached max iterations without a final answer."
    def __handle_tool_call(self, response: str) -> str:
        try:
            start = response.find("<tool_use>")
            end = response.find("</tool_use>") + len("</tool_use>")
            xml_block = response[start:end]
            root = ET.fromstring(xml_block)
            # Extract tool name
            tool_name_el = root.find("tool_name")
            if tool_name_el is None:
                return "Error: No tool_name found in XML."
            tool_name = tool_name_el.text.strip()
            parameters = {}
            params_el = root.find("parameters")
            if params_el is not None:
                for param in params_el:
                    parameters[param.tag] = param.text.strip() if param.text else ""
            print(f"  -> Tool: {tool_name} | Parameters: {parameters}")
            # Fetch the tool from registry
            tool = self.registry.get_tool(tool_name)
            if not tool:
                return f"Error: Unknown tool '{tool_name}'. Available: {self.registry.list_tools()}"
            # Run the tool with the clean dictionary
            result = tool.run(parameters)
            return f"Tool '{tool_name}' returned: {result}"
        except ET.ParseError as e:
            return f"Error: Could not parse XML tool call. Details: {e}"
        except Exception as e:
            return f"Error during tool execution: {e}"
    def clear_memory(self):
        self.__short_term.clear()
        self.__long_term.clear()
        print(f"[{self.name}] Memory cleared.")
```
</file>
## File: `agents/config.py`
<file path="agents/config.py" type="python">
```python
from dataclasses import dataclass
@dataclass
class Config:
#---Identity
    name: str
    # model: str
    description: str = "This AI agent is like an AI from the future and will give you futuristic explainations for every question you ask."
#---Prompts
    system_prompt: str = "You are a helpful AI assistant."
#---LLM Settings
    max_tokens: int = 1000
#---Behavior settings
    max_iterations: int = 50
     # --- Memory ---
    max_ltm_entries: int = 100
    max_stm_entries: int = 50
    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Agent must have a name")
        if self.max_tokens <= 0:
            raise ValueError("max_tokens must be greater than 0")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than 0")
        if self.max_ltm_entries <= 0:
            raise ValueError("max_ltm_entries must be greater than 0")
        if self.max_stm_entries <= 0:
            raise ValueError("max_stm_entries must be greater than 0")
```
</file>
## File: `llms/__init__.py`
<file path="llms/__init__.py" type="python">
```python
from .basellm import BaseLLM
from .groqclient import GroqClient
```
</file>
## File: `llms/basellm.py`
<file path="llms/basellm.py" type="python">
```python
from abc import ABC , abstractmethod
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt, user_prompt) ->str:
        pass
```
</file>
## File: `llms/geminiclient.py`
<file path="llms/geminiclient.py" type="python">
```python
import os
import google.generativeai as genai
from llms.basellm import BaseLLM
class GeminiClient(BaseLLM):
    def __init__(self, model: str = "gemini-1.5-flash"):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")
        # Configure Google's SDK
        genai.configure(api_key=api_key)
        # Initialize the model
        self.model = genai.GenerativeModel(model)
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            full_prompt = f"System Instructions:\n{system_prompt}\n\nUser Input:\n{user_prompt}"
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error: Gemini API failed with message: {str(e)}"
```
</file>
## File: `llms/groqclient.py`
<file path="llms/groqclient.py" type="python">
```python
from llms.basellm import BaseLLM
from groq import Groq
class GroqClient(BaseLLM):
    def __init__(self, model: str, max_tokens: int = 1000 ):
        self.client = Groq()
        self.model = model
        self.max_tokens = max_tokens
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens = self.max_tokens,
                messages = [
                    {"role": "system", "content" : system_prompt},
                    {"role": "user" , "content" : user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: LLM API failed with message: {str(e)}"
```
</file>
## File: `memory/__init__.py`
<file path="memory/__init__.py" type="python">
```python

```
</file>
## File: `memory/ltm.py`
<file path="memory/ltm.py" type="python">
```python
import json
import os
from memory.memory import BaseMemory
class LongTermMemory(BaseMemory):
    def __init__(self, agent_name: str, max_entries: int = 100):
        self.__file_path = f"{agent_name}_memory.json"
        self.__max_entries = max_entries
        self.__history = self.__load_from_file()
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
        self.__save_to_file()
    def get_context(self) -> str:
        if not self.__history:
            return ""
        return "".join([
            f"{entry['role']}: {entry['content']}\n"
        for entry in self.__history
        ])
    def clear(self):
        self.__history = []
        self.__save_to_file()
    def __save_to_file(self):
        try:
            with open(self.__file_path, "w") as f:
                json.dump(self.__history, f, indent=4)
        except Exception as e:
            print(f"Warning: Could not save memory to {self.__file_path}. Error: {e}")
    def __load_from_file(self) -> list:
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Memory file corrupted or unreadable. Starting fresh. Error: {e}")
                return []
        return []
```
</file>
## File: `memory/memory.py`
<file path="memory/memory.py" type="python">
```python
from abc import ABC, abstractmethod
class BaseMemory(ABC):
    @abstractmethod
    def add_entry(self, role: str, content: str):
        """Save a new message to memory"""
        pass
    @abstractmethod
    def get_context(self) -> str:
        """Retrieve full history as a string for the LLM"""
        pass
    @abstractmethod
    def clear(self):
        """Reset memory completely"""
        pass
#Roles: The talking entities in a conversation
# user, assistant, system
#  ShortTerm memory: Just a list having the messages #
```
</file>
## File: `memory/stm.py`
<file path="memory/stm.py" type="python">
```python
from memory.memory import BaseMemory
class ShortTermMemory(BaseMemory):
    def __init__(self, max_entries=50):
        self.__history = []
        self.__max_entries = max_entries
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
    def get_context(self) -> str:
        if not self.__history:
            return ""
        context = ""
        for entry in self.__history:
            context += f"{entry['role']}: {entry['content']}\n"
        return context
    def clear(self):
        self.__history = []
```
</file>
## File: `tools/agent_made/__init__.py`
<file path="tools/agent_made/__init__.py" type="python">
```python

```
</file>
## File: `tools/agent_made/directory_watcher.py`
<file path="tools/agent_made/directory_watcher.py" type="python">
```python
from tools.basetool import BaseTool
import os
class DirectoryWatcherTool(BaseTool):
    def __init__(self):
        self.name = "directory_watcher"
        self.description = "Lists files in a directory to keep track of changes."
        self.parameters = {
            "path": "The path of the directory to list."
        }
    def run(self, parameters: dict) -> str:
        path = parameters.get("path", ".")
        try:
            files = os.listdir(path)
            return f"Files in {path}: {', '.join(files)}"
        except Exception as e:
            return f"Error accessing directory: {str(e)}"
```
</file>
## File: `tools/agent_made/git_manager.py`
<file path="tools/agent_made/git_manager.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess
class GitManagerTool(BaseTool):
    def __init__(self):
        self.name = "git_manager"
        self.description = "Provides a safe interface to run 'git status' or 'git log' to track project changes."
        self.parameters = {
            "command": "The git command to execute (e.g., 'status', 'log -n 5')."
        }
    def run(self, parameters: dict) -> str:
        cmd_arg = parameters.get("command", "status")
        full_command = f"git {cmd_arg}"
        print(f"The following git command will be executed: {full_command}. Proceed? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            try:
                result = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Git command failed: {e.output}"
        else:
            return "Git command execution cancelled by user."
```
</file>
## File: `tools/agent_made/light_python_runner.py`
<file path="tools/agent_made/light_python_runner.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess
import os
import shutil
class LightPythonRunnerTool(BaseTool):
    def __init__(self):
        self.name = "light_python_runner"
        self.description = "Executes python files in a clean, ephemeral virtual environment that is deleted immediately after execution."
        self.parameters = {
            "filepath": "The path to the python file to execute."
        }
    def run(self, parameters: dict) -> str:
        filepath = parameters.get("filepath", "")
        venv_dir = ".ephemeral_venv"
        # Cleanup if old one exists
        if os.path.exists(venv_dir):
            shutil.rmtree(venv_dir)
        cmd = f"python3 -m venv {venv_dir} && {venv_dir}/bin/python3 {filepath}"
        print(f"The following ephemeral python execution will be run: {cmd}. Proceed? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            try:
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Execution failed: {e.output}"
            finally:
                if os.path.exists(venv_dir):
                    shutil.rmtree(venv_dir)
        else:
            return "Execution cancelled by user."
```
</file>
## File: `tools/agent_made/terminal_executor.py`
<file path="tools/agent_made/terminal_executor.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess
class TerminalExecutorTool(BaseTool):
    def __init__(self):
        self.name = "terminal_executor"
        self.description = "Executes shell commands after explicit user confirmation."
        self.parameters = {
            "command": "The shell command to be executed."
        }
    def run(self, parameters: dict) -> str:
        command = parameters.get("command", "")
        print(f"The following command will be executed: {command}. Proceed? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Command failed: {e.output}"
        else:
            return "Command execution cancelled by user."
```
</file>
## File: `tools/__init__.py`
<file path="tools/__init__.py" type="python">
```python
from tools.basetool import BaseTool
from tools.calculator import CalculatorTool
from tools.registry import ToolRegistry
from tools.filereader import FileReaderTool
from tools.filewriter import FileWriterTool
```
</file>
## File: `tools/basetool.py`
<file path="tools/basetool.py" type="python">
```python
from abc import ABC,abstractmethod
class BaseTool(ABC):
    def __init__(self):
        name: str
        description: str
        parameters: dict={}
    @abstractmethod
    def run(self, parameters: dict) -> str:
        """The method called by the agent to run a tool"""
        pass
    def get_schema(self) -> str:
        """Builds the XML schema shown to the LLM"""
        params_xml = ""
        for param_name, param_desc in self.parameters.items():
            params_xml += f"\n        <{param_name}>({param_desc})</{param_name}>"
        return (
            f"<tool>\n"
            f"  <tool_name>{self.name}</tool_name>\n"
            f"  <description>{self.description}</description>\n"
            f"  <parameters>{params_xml}\n  </parameters>\n"
            f"</tool>"
        )
```
</file>
## File: `tools/calculator.py`
<file path="tools/calculator.py" type="python">
```python
from tools.basetool import BaseTool
class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    parameters = {
        "expression": "The math expression to evaluate. Example: 150*4"
    }
    def run(self, parameters: dict) -> str:
        try:
            expression = parameters.get("expression", "")
            # Clean any trailing = signs the LLM might add
            expression = expression.strip().rstrip("=").strip()
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Calculator error: {e}"
```
</file>
## File: `tools/filereader.py`
<file path="tools/filereader.py" type="python">
```python
from tools.basetool import BaseTool
class FileReaderTool(BaseTool):
    name = "file_reader"
    description = "Reads and returns the content of a file."
    parameters = {
        "filename": "The name of the file to read. Example: result.txt"
    }
    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            if not filename:
                return "Error: filename parameter is missing."
            with open(filename, "r") as f:
                content = f.read()
            return f"Content of {filename}:\n{content}"
        except FileNotFoundError:
            return f"Error: File '{filename}' not found."
        except Exception as e:
            return f"Error reading file: {e}"
```
</file>
## File: `tools/filewriter.py`
<file path="tools/filewriter.py" type="python">
```python
from tools.basetool import BaseTool
import os
class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file in the current working directory only."
    parameters = {
        "filename": "The name of the file to write. Example: result.txt",
        "content": "The full text content to write into the file."
    }
    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            content = parameters.get("content", "").strip()
            if not filename:
                return "Error: filename parameter is missing."
            # Prevent path traversal attacks
            safe_path = os.path.realpath(os.path.join(os.getcwd(), filename))
            if not safe_path.startswith(os.getcwd()):
                return "Error: Writing outside the working directory is not allowed."
            # Create subdirectories if needed (safely)
            os.makedirs(os.path.dirname(safe_path), exist_ok=True) \
                if os.path.dirname(safe_path) else None
            with open(safe_path, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"
```
</file>
## File: `tools/registry.py`
<file path="tools/registry.py" type="python">
```python
from tools.basetool import BaseTool
class ToolRegistry:
    def __init__(self):
        self.__tools = {}
    def register(self, tool: BaseTool):
        self.__tools[tool.name] = tool
        print(f"Registered tool: {tool.name}")
    def get_tool(self, name: str) -> BaseTool:
        return self.__tools.get(name)
    def get_descriptions(self) -> str:
        """Returns full XML schemas for all tools"""
        schemas = []
        for tool in self.__tools.values():
            schemas.append(tool.get_schema())
        return "\n\n".join(schemas)
    def list_tools(self) -> list:
        return list(self.__tools.keys())
```
</file>
## File: `tools/s.txt`
<file path="tools/s.txt" type="text">
```text
git config --global user.email "faseuu@gmail.com"
git config --global user.name "Faseeu"
```
</file>
## File: `utils/chat_ui.py`
<file path="utils/chat_ui.py" type="python">
```python
# utils/chat_ui.py
def start_terminal_chat(agent):
    print("=" * 50)
    print(f"Starting chat with {agent.name}. Type 'exit' to quit.")
    print("=" * 50)
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation...")
            break
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
```
</file>
## File: `__init__.py`
<file path="__init__.py" type="python">
```python

```
</file>
## File: `generate_codecontext.py`
<file path="generate_codecontext.py" type="python">
```python
import datetime
from pathlib import Path
from typing import Dict, List, Set
def generate_context() -> None:
    output_file = Path("codecontext.md")
    project_root = Path(".")
    # --- CONFIGURATION & SAFETY SAFETY VALVES ---
    MAX_FILE_SIZE_BYTES = 200 * 1024  # 200 KB individual file ceiling guard
    ignore_dirs: Set[str] = {
        '__pycache__', 'tests', 'venv', '.venv', '.git', 
        '.env', '.ephemeral_venv', '.temp_venv', '.idea', '.vscode'
    }
    ignore_files: Set[str] = {
        'codecontext.md',
        'context.md',
        'Agent1_memory.json'
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
```
</file>
## File: `main.py`
<file path="main.py" type="python">
```python
# from llms.groqclient import GroqClient
# from llms.geminiclient import GeminiClient
# from tools.calculator import CalculatorTool
# from tools.filewriter import FileWriterTool
# from tools.filereader import FileReaderTool
# from agents.baseagent import BaseAgent
from utils.chat_ui import start_terminal_chat
# if __name__ == "__main__":
#     # 1. Create the LLM
#     groq_llm = GroqClient(model="llama-3.3-70b-versatile")
#     # 2. Create the Agent with tools
#     agent = BaseAgent(
#         name="SmartBot",
#         llm=gemini_llm,
#         system_prompt= """
#         Be a helpful assistant who always always uses the tools given to him. 
#         Never do a task without using the apppropriate tools. 
#         You have all the appropriate tools at your disposal to perfrom the tasks i ask of you.
#         Always try to reason everything yourself.
#         Try your best not to bother user.
#         Create plans to perform the tasks.
#         Also at the end of each task try to double check if it was properly fullfilled or not. 
#         """,
#         tools=[CalculatorTool(),FileReaderTool(),FileWriterTool()]
#     )
#     print("\n" + "=" * 40)
#     print("TEST 2: Tool needed")
#     print("=" * 40)
# #     response2 = agent.run("""
# #     🌀 SYSTEM OVERRIDE: PROJECT HIDDEN GEM 🌀
# # Agent, your framework is entering the **Anime Recommendation Gauntlet**.  
# # Your mission: populate three classified dossiers, then unleash a fourth wild-card category that breaks the genre matrix.
# # ---
# # 📁 DOSSIER 1: `action`  
# # Compile the absolute GOATed action anime—titles with timelines so beautifully convoluted they require a whiteboard, and stories that hit harder than a final-form scream. Save the list to a file named **`action`**.
# # 📁 DOSSIER 2: `psychological`  
# # Infiltrate the deep cuts. I need **5 criminally underrated psychological anime** that are:
# # - Motivational enough to make me run through a wall,
# # - Political enough to start a debate club,
# # - Obscure enough that even seasoned weebs reply, *"Never heard of it."*  
# # Drop these into **`psychological`**.
# # 📁 DOSSIER 3: `most motivational anime`  
# # Uncover **5 motivational masterpieces** flying completely under the radar. Not the mainstream hype trains—actual underground bangers that rebuild your soul episode by episode. Write these to **`most motivational anime`**.
# # 🎲 DOSSIER 4: `[REDACTED]`  
# # Finally, deploy the wildcard. Create **one additional file** with a category so specific, so dangerously niche, that it feels like it was tailor-made for my brain. Make me fall in love with something I didn’t know existed.
# # ---
# # Execute with maximum flair. Framework stress-test: **ACTIVE**. ⚡
# #     """)
# #     print(response2)
#     start_terminal_chat(agent)
#     # # TEST THE PROPERTIES:
#     # print("--- AGENT INFO ---")
#     # print(f"Name: {agent.name}")                
#     # print(f"Tools: {agent.tools}")     
#     # print(f"Prompt: {agent.system_prompt}")      
#     # print("------------------")
from llms.geminiclient import GeminiClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
from tools.agent_made.terminal_executor import TerminalExecutorTool
if __name__ == "__main__":
    llm = GeminiClient(model="gemini-3.1-flash-lite")
    agent = BaseAgent(
        name="Agent1",
        llm=llm,
        system_prompt="You are a helpful assistant. Always use tools for math and files. Always use tools. Never try to solve any math eq internally",
        tools=[CalculatorTool(), FileWriterTool(), FileReaderTool(),TerminalExecutorTool()]
    )
    # Test multi-parameter tool call
    # response = agent.run("""
    # Study the whole of tools directory
    # and create for yourself a terminal usage tool 
    # but it should have feature to show to the user
    # what command is going to be ran 
    # and ask him yes for y and no for n
    # """)
    start_terminal_chat(agent)
    print("\nFinal Answer:")
    # print(response)
        # "Calculate 1234 multiplied by 5678. "
        # "Then save the result to a file called answer.txt. "
        # "Then read the file back."
```
</file>
## File: `main2.py`
<file path="main2.py" type="python">
```python
# from llms.groqclient import GroqClient
# from llms.geminiclient import GeminiClient
# from tools.calculator import CalculatorTool
# from tools.filewriter import FileWriterTool
# from tools.filereader import FileReaderTool
# from agents.baseagent import BaseAgent
from utils.chat_ui import start_terminal_chat
# if __name__ == "__main__":
#     # 1. Create the LLM
#     groq_llm = GroqClient(model="llama-3.3-70b-versatile")
#     # 2. Create the Agent with tools
#     agent = BaseAgent(
#         name="SmartBot",
#         llm=gemini_llm,
#         system_prompt= """
#         Be a helpful assistant who always always uses the tools given to him. 
#         Never do a task without using the apppropriate tools. 
#         You have all the appropriate tools at your disposal to perfrom the tasks i ask of you.
#         Always try to reason everything yourself.
#         Try your best not to bother user.
#         Create plans to perform the tasks.
#         Also at the end of each task try to double check if it was properly fullfilled or not. 
#         """,
#         tools=[CalculatorTool(),FileReaderTool(),FileWriterTool()]
#     )
#     print("\n" + "=" * 40)
#     print("TEST 2: Tool needed")
#     print("=" * 40)
# #     response2 = agent.run("""
# #     🌀 SYSTEM OVERRIDE: PROJECT HIDDEN GEM 🌀
# # Agent, your framework is entering the **Anime Recommendation Gauntlet**.  
# # Your mission: populate three classified dossiers, then unleash a fourth wild-card category that breaks the genre matrix.
# # ---
# # 📁 DOSSIER 1: `action`  
# # Compile the absolute GOATed action anime—titles with timelines so beautifully convoluted they require a whiteboard, and stories that hit harder than a final-form scream. Save the list to a file named **`action`**.
# # 📁 DOSSIER 2: `psychological`  
# # Infiltrate the deep cuts. I need **5 criminally underrated psychological anime** that are:
# # - Motivational enough to make me run through a wall,
# # - Political enough to start a debate club,
# # - Obscure enough that even seasoned weebs reply, *"Never heard of it."*  
# # Drop these into **`psychological`**.
# # 📁 DOSSIER 3: `most motivational anime`  
# # Uncover **5 motivational masterpieces** flying completely under the radar. Not the mainstream hype trains—actual underground bangers that rebuild your soul episode by episode. Write these to **`most motivational anime`**.
# # 🎲 DOSSIER 4: `[REDACTED]`  
# # Finally, deploy the wildcard. Create **one additional file** with a category so specific, so dangerously niche, that it feels like it was tailor-made for my brain. Make me fall in love with something I didn’t know existed.
# # ---
# # Execute with maximum flair. Framework stress-test: **ACTIVE**. ⚡
# #     """)
# #     print(response2)
#     start_terminal_chat(agent)
#     # # TEST THE PROPERTIES:
#     # print("--- AGENT INFO ---")
#     # print(f"Name: {agent.name}")                
#     # print(f"Tools: {agent.tools}")     
#     # print(f"Prompt: {agent.system_prompt}")      
#     # print("------------------")
from llms.geminiclient import GeminiClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
from tools.agent_made.terminal_executor import TerminalExecutorTool
if __name__ == "__main__":
    llm = GeminiClient(model="gemini-3.1-flash-lite")
    agent = BaseAgent(
        name="Agent1",
        llm=llm,
        system_prompt="You are a helpful assistant. Always use tools for math and files. Always use tools. Never try to solve any math eq internally",
        tools=[CalculatorTool(), FileWriterTool(), FileReaderTool(),TerminalExecutorTool()]
    )
    # Test multi-parameter tool call
    # response = agent.run("""
    # Study the whole of tools directory
    # and create for yourself a terminal usage tool 
    # but it should have feature to show to the user
    # what command is going to be ran 
    # and ask him yes for y and no for n
    # """)
    start_terminal_chat(agent)
    print("\nFinal Answer:")
    # print(response)
        # "Calculate 1234 multiplied by 5678. "
        # "Then save the result to a file called answer.txt. "
        # "Then read the file back."
```
</file>
## File: `problems.md`
<file path="problems.md" type="markdown">
```markdown
I'll do a thorough, file-by-file review and then give you a prioritized improvement plan.
## Critical Bugs First
### Bug 1: `BaseTool.__init__` swallows `abstractmethod`
```python
# CURRENT (broken)
class BaseTool(ABC):
    def __init__(self):
        name: str
        description: str
        parameters: dict = {}
        @abstractmethod          # ← nested INSIDE __init__, never enforced
        def run(self, parameters: dict) -> str:
            pass
```
`run()` is defined **inside** `__init__`. Python never sees it as an abstract method. Any subclass that forgets to implement `run()` will **not** raise `TypeError`. The entire abstraction contract is silently broken.
```python
# FIXED
from abc import ABC, abstractmethod
class BaseTool(ABC):
    name: str = ""
    description: str = ""
    parameters: dict = {}
    @abstractmethod
    def run(self, parameters: dict) -> str:
        """The method called by the agent to run a tool"""
        pass
    def get_schema(self) -> str:
        params_xml = ""
        for param_name, param_desc in self.parameters.items():
            params_xml += f"\n        <{param_name}>({param_desc})</{param_name}>"
        return (
            f"<tool>\n"
            f"  <tool_name>{self.name}</tool_name>\n"
            f"  <description>{self.description}</description>\n"
            f"  <parameters>{params_xml}\n  </parameters>\n"
            f"</tool>"
        )
```
### Bug 2: `eval()` in `CalculatorTool` is a security hole
```python
# CURRENT (dangerous)
result = eval(expression)  # eval("__import__('os').system('rm -rf /')") works fine
```
`eval()` executes **any** Python code. If the LLM hallucinates or is prompted maliciously, this destroys files, leaks keys, or worse.
```python
# FIXED - use ast.literal_eval for simple cases, or a safe parser
import ast
import operator
class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    parameters = {
        "expression": "The math expression to evaluate. Example: 150*4"
    }
    # Whitelist of safe operations
    _SAFE_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
    }
    def _safe_eval(self, node):
        if isinstance(node, ast.Constant):          # numbers
            return node.value
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in self._SAFE_OPS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            left = self._safe_eval(node.left)
            right = self._safe_eval(node.right)
            return self._SAFE_OPS[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in self._SAFE_OPS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            return self._SAFE_OPS[op_type](self._safe_eval(node.operand))
        else:
            raise ValueError(f"Unsupported expression type: {type(node).__name__}")
    def run(self, parameters: dict) -> str:
        try:
            expression = parameters.get("expression", "")
            expression = expression.strip().rstrip("=").strip()
            tree = ast.parse(expression, mode="eval")
            result = self._safe_eval(tree.body)
            return str(result)
        except ZeroDivisionError:
            return "Calculator error: Division by zero."
        except ValueError as e:
            return f"Calculator error: {e}"
        except Exception as e:
            return f"Calculator error: {e}"
```
### Bug 3: `FileWriterTool` has no path traversal protection
```python
# CURRENT - agent can write to /etc/passwd or ../../secrets.env
with open(filename, "w") as f:
    f.write(content)
```
```python
# FIXED
import os
class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file in the current working directory only."
    parameters = {
        "filename": "The name of the file to write. Example: result.txt",
        "content": "The full text content to write into the file."
    }
    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            content = parameters.get("content", "").strip()
            if not filename:
                return "Error: filename parameter is missing."
            # Prevent path traversal attacks
            safe_path = os.path.realpath(os.path.join(os.getcwd(), filename))
            if not safe_path.startswith(os.getcwd()):
                return "Error: Writing outside the working directory is not allowed."
            # Create subdirectories if needed (safely)
            os.makedirs(os.path.dirname(safe_path), exist_ok=True) \
                if os.path.dirname(safe_path) else None
            with open(safe_path, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"
```
### Bug 4: `GeminiClient` uses a non-existent model name
```python
# main.py
llm = GeminiClient(model="gemini-3.1-flash-lite")  # This model does not exist
```
As of 2025, valid model names are `gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-2.0-flash`, etc. This will raise an API error at runtime with a confusing message.
```python
# FIXED geminiclient.py - validate on init
VALID_GEMINI_MODELS = {
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
}
class GeminiClient(BaseLLM):
    def __init__(self, model: str = "gemini-2.0-flash"):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")
        if model not in VALID_GEMINI_MODELS:
            raise ValueError(
                f"Unknown Gemini model: '{model}'. "
                f"Valid options: {sorted(VALID_GEMINI_MODELS)}"
            )
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
```
### Bug 5: `LongTermMemory` grows forever and will break the context window
```python
# CURRENT - every single message ever sent gets loaded and sent to LLM
def get_context(self) -> str:
    context = ""
    for entry in self.__history:       # No limit. Session 100 sends 10,000 lines.
        context += f"{entry['role']}: {entry['content']}\n"
    return context
```
After enough sessions, the combined memory exceeds the LLM's context window and the API call fails or gets truncated silently.
```python
# FIXED ltm.py - add a rolling window
class LongTermMemory(BaseMemory):
    def __init__(self, agent_name: str, max_entries: int = 50):
        self.__file_path = f"{agent_name}_memory.json"
        self.__max_entries = max_entries
        self.__history = self.__load_from_file()
    def add_entry(self, role: str, content: str):
        self.__history.append({"role": role, "content": content})
        # Keep only the most recent N entries on disk too
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
        self.__save_to_file()
    def get_context(self) -> str:
        if not self.__history:
            return ""
        # Only send last N entries to LLM to avoid context overflow
        recent = self.__history[-self.__max_entries:]
        return "".join(
            f"{entry['role']}: {entry['content']}\n" for entry in recent
        )
```
## Architecture Issues
### Issue 1: `Config` stores `user_prompt` which it never uses
```python
@dataclass
class Config:
    name: str
    description: str = "..."
    system_prompt: str = "You are a helpful AI assistant."
    user_prompt: str = ""        # ← never read by BaseAgent, dead field
    max_tokens: int = 1000       # ← also never used since LLM controls this
```
`user_prompt` belongs to the conversation, not the config. `max_tokens` is already set in `GroqClient`. Remove dead fields.
```python
# FIXED config.py
from dataclasses import dataclass, field
@dataclass
class Config:
    # --- Identity ---
    name: str
    description: str = "A helpful AI agent."
    # --- Prompts ---
    system_prompt: str = "You are a helpful AI assistant."
    # --- Behavior ---
    max_iterations: int = 10
    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Agent must have a non-empty name")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than 0")
```
### Issue 2: `registry.register()` prints to stdout unconditionally
```python
def register(self, tool: BaseTool):
    self.__tools[tool.name] = tool
    print(f"Registered tool: {tool.name}")   # ← pollutes output in production
```
This is a debug statement left in. In a real system, registration output should be opt-in.
```python
# FIXED registry.py
import logging
logger = logging.getLogger(__name__)
class ToolRegistry:
    def __init__(self):
        self.__tools: dict[str, BaseTool] = {}
    def register(self, tool: BaseTool):
        if not isinstance(tool, BaseTool):
            raise TypeError(f"Expected BaseTool, got {type(tool).__name__}")
        if not tool.name:
            raise ValueError("Tool must have a non-empty name")
        if tool.name in self.__tools:
            logger.warning(f"Tool '{tool.name}' is being overwritten in registry.")
        self.__tools[tool.name] = tool
        logger.debug(f"Registered tool: {tool.name}")
    def get_tool(self, name: str):
        return self.__tools.get(name)
    def get_descriptions(self) -> str:
        return "\n\n".join(tool.get_schema() for tool in self.__tools.values())
    def list_tools(self) -> list[str]:
        return list(self.__tools.keys())
    def __len__(self) -> int:
        return len(self.__tools)
```
### Issue 3: `BaseLLM.generate()` has a redundant `raise NotImplementedError`
```python
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt, user_prompt) -> str:
        raise NotImplementedError    # ← pointless, ABC already enforces this
```
`@abstractmethod` already prevents instantiation. `raise NotImplementedError` is redundant and adds noise. Also, add type hints.
```python
# FIXED basellm.py
from abc import ABC, abstractmethod
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """
        Send a prompt to the LLM and return the text response.
        Args:
            system_prompt: Instructions that define the agent's behavior.
            user_prompt: The conversation history and current task.
        Returns:
            The LLM's text response.
        """
        pass
```
### Issue 4: `chat_ui.py` loses the last response after loop ends
```python
def start_terminal_chat(agent):
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation...")
            break
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
```
And in `main.py`:
```python
start_terminal_chat(agent)
print("\nFinal Answer:")
# print(response)       ← response is undefined here, this would crash
```
The function returns nothing. Make it return the conversation history.
```python
# FIXED chat_ui.py
def start_terminal_chat(agent) -> list[dict]:
    """
    Run an interactive terminal chat session.
    Returns:
        List of conversation turns: [{"user": ..., "agent": ...}, ...]
    """
    print("=" * 50)
    print(f"Chat with {agent.name}  |  Tools: {agent.available_tools}")
    print("Type 'exit' or 'quit' to end. Type 'clear' to reset memory.")
    print("=" * 50)
    history = []
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted.")
            break
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("Ending conversation...")
            break
        if user_input.lower() == "clear":
            agent.clear_memory()
            print("[Memory cleared]")
            continue
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
        history.append({"user": user_input, "agent": response})
    return history
```
## Code Quality Issues
### Issue 5: `ShortTermMemory` and `LongTermMemory` duplicate `get_context()`
Both classes have this identical method:
```python
def get_context(self) -> str:
    if not self.__history:
        return ""
    context = ""
    for entry in self.__history:
        context += f"{entry['role']}: {entry['content']}\n"
    return context
```
Move the shared logic to `BaseMemory` as a concrete method.
```python
# FIXED memory/memory.py
from abc import ABC, abstractmethod
class BaseMemory(ABC):
    @abstractmethod
    def add_entry(self, role: str, content: str) -> None:
        pass
    @abstractmethod
    def get_history(self) -> list[dict]:
        """Return raw history list for subclasses to implement."""
        pass
    @abstractmethod
    def clear(self) -> None:
        pass
    def get_context(self) -> str:
        """Format history as a readable string. Shared by all subclasses."""
        history = self.get_history()
        if not history:
            return ""
        return "".join(
            f"{entry['role']}: {entry['content']}\n" for entry in history
        )
```
```python
# FIXED memory/stm.py
from memory.memory import BaseMemory
class ShortTermMemory(BaseMemory):
    def __init__(self):
        self.__history: list[dict] = []
    def add_entry(self, role: str, content: str) -> None:
        self.__history.append({"role": role, "content": content})
    def get_history(self) -> list[dict]:
        return self.__history.copy()    # Return copy, not the live list
    def clear(self) -> None:
        self.__history = []
```
### Issue 6: String concatenation in loops is O(n²)
```python
# CURRENT - inefficient
context = ""
for entry in self.__history:
    context += f"{entry['role']}: {entry['content']}\n"   # new string object each iteration
```
Use `str.join()` instead. It allocates once.
```python
# FIXED - O(n)
return "".join(
    f"{entry['role']}: {entry['content']}\n" for entry in history
)
```
### Issue 7: `directory_watcher.py` uses `os.listdir()` which is too shallow
Based on the context description, `os.listdir()` only shows the top level. For an agent working inside a project, it needs a recursive tree view to be useful.
```python
# IMPROVED directory_watcher.py
import os
from tools.basetool import BaseTool
class DirectoryWatcherTool(BaseTool):
    name = "directory_watcher"
    description = "Returns the directory tree of a given path."
    parameters = {
        "path": "The directory path to inspect. Use '.' for current directory.",
        "max_depth": "Maximum depth to recurse. Default is 3."
    }
    def run(self, parameters: dict) -> str:
        try:
            path = parameters.get("path", ".").strip() or "."
            max_depth = int(parameters.get("max_depth", 3))
            if not os.path.exists(path):
                return f"Error: Path '{path}' does not exist."
            lines = []
            self._walk(path, lines, depth=0, max_depth=max_depth)
            return "\n".join(lines) if lines else "Directory is empty."
        except Exception as e:
            return f"Error: {e}"
    def _walk(self, path: str, lines: list, depth: int, max_depth: int):
        if depth > max_depth:
            return
        indent = "  " * depth
        try:
            entries = sorted(os.listdir(path))
        except PermissionError:
            lines.append(f"{indent}[Permission Denied]")
            return
        for entry in entries:
            lines.append(f"{indent}{entry}")
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                self._walk(full_path, lines, depth + 1, max_depth)
```
## What to Add Next
### Addition 1: A `WebSearchTool` using DuckDuckGo (no API key needed)
```python
# tools/web_search.py
import urllib.request
import urllib.parse
import json
from tools.basetool import BaseTool
class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Searches the web using DuckDuckGo and returns top results."
    parameters = {
        "query": "The search query. Example: Python asyncio tutorial"
    }
    def run(self, parameters: dict) -> str:
        try:
            query = parameters.get("query", "").strip()
            if not query:
                return "Error: query parameter is missing."
            encoded = urllib.parse.quote(query)
            url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1"
            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())
            results = []
            if data.get("AbstractText"):
                results.append(f"Summary: {data['AbstractText']}")
            for topic in data.get("RelatedTopics", [])[:5]:
                if "Text" in topic:
                    results.append(f"- {topic['Text']}")
            return "\n".join(results) if results else "No results found."
        except Exception as e:
            return f"Web search error: {e}"
```
### Addition 2: Proper logging instead of `print()`
```python
# utils/logger.py
import logging
import sys
def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates a configured logger for the framework.
    Usage:
        from utils.logger import setup_logger
        logger = setup_logger(__name__)
        logger.info("Agent started")
        logger.debug("Tool called: calculator")
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
            datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
```
### Addition 3: A `MemorySummarizationTool` to prevent context overflow
```python
# memory/summarizer.py
class MemorySummarizer:
    """
    Uses the agent's own LLM to compress long memory into a short summary.
    Call this when get_context() exceeds a token threshold.
    """
    def __init__(self, llm):
        self.llm = llm
    def summarize(self, context: str) -> str:
        system = "You are a memory compression assistant."
        user = (
            f"Compress the following conversation history into a concise summary "
            f"that preserves all important facts, decisions, and tool results:\n\n"
            f"{context}"
        )
        try:
            return self.llm.generate(system, user)
        except Exception as e:
            return f"[Summary failed: {e}]\n{context[-500:]}"  # fallback to tail
```
## Complete Priority List
```
PRIORITY 1 - Fix Before Using (Bugs)
─────────────────────────────────────
[ ] Fix BaseTool: move @abstractmethod outside __init__
[ ] Replace eval() in CalculatorTool with ast-based safe parser
[ ] Add path traversal protection to FileWriterTool
[ ] Fix GeminiClient model name (gemini-3.1-flash-lite does not exist)
[ ] Add LongTermMemory rolling window to prevent context overflow
PRIORITY 2 - Architecture Cleanup
───────────────────────────────────
[ ] Remove dead fields from Config (user_prompt, max_tokens)
[ ] Remove print() from ToolRegistry.register(), use logging
[ ] Add duplicate tool name warning in ToolRegistry
[ ] Move shared get_context() to BaseMemory base class
[ ] Remove redundant raise NotImplementedError from BaseLLM
[ ] Make chat_ui return conversation history
PRIORITY 3 - Code Quality
──────────────────────────
[ ] Replace string concatenation loops with str.join()
[ ] Add type hints to all method signatures
[ ] Add docstrings to all public methods
[ ] Return copies not live lists from ShortTermMemory
[ ] Make DirectoryWatcherTool recursive with max_depth
PRIORITY 4 - New Features
──────────────────────────
[ ] Add WebSearchTool (DuckDuckGo, no key needed)
[ ] Add proper logging module (utils/logger.py)
[ ] Add MemorySummarizer to handle context overflow gracefully
[ ] Add SupervisorAgent that routes tasks between specialized agents
[ ] Add tests/ directory with at least unit tests for each tool
```
The most important fix by far is **Bug 1** (the `BaseTool` abstract method placement). Your entire tool safety net is currently non-functional because of it, and you would not know until a tool silently misbehaved.\\\
im not gonna fix bug 2 for a while were going to focus on other imp stuff for now
bug 4 seems to be unecessary to fix cuz right now im the only user
also add a list of models feels a lot of work for providers like openrouter and cerebras that keep changing models everyday
lets focus on the logterm memory and also fix the memory once and for all
im open to anyu type of suggestions
and we can also add the episoidic memory
also i want to hear about more better memory if possible cuz what i have been using uptil now is just the ancients just in  order to learn stuff and im still incistant on learning things thats why im developing this shit framework from scratch
```
</file>
## File: `project_structure.html`
<file path="project_structure.html" type="html">
```html
<!doctype html><html lang=en><meta charset=UTF-8><title>Professional Project Architecture</title><script src=https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js></script><style>body{color:#333;background-color:#f4f7f9;padding:40px;font-family:Segoe UI,Tahoma,Geneva,Verdana,sans-serif}.container{background:#fff;border-radius:12px;padding:30px;box-shadow:0 4px 15px #0000001a}h1{color:#2c3e50;border-bottom:2px solid #3498db;padding-bottom:10px}.mermaid{background:#fff;border:1px solid #ddd;border-radius:8px;margin-top:30px;padding:20px}</style><body><div class=container><h1>Khwarizm Architecture Map</h1><p>A detailed overview of the system components and their interdependencies.<div class=mermaid>graph TB subgraph Entry M[main.py] end subgraph Agent_Layer A[BaseAgent] C[Config] Mem[Memory System] end subgraph Tool_System TR[Tool Registry] ST[Standard Tools] AM[Agent-Made Tools] end M --> A A --> C A --> Mem A --> TR TR --> ST TR --> AM style M fill:#f9f9f9,stroke:#333 style A fill:#3498db,color:#fff style TR fill:#e67e22,color:#fff</div></div><script>mermaid.initialize({startOnLoad:!0,theme:`default`});</script>
```
</file>
## File: `project_structure.txt`
<file path="project_structure.txt" type="text">
```text
KHWARIZM PROJECT HIERARCHY (Tree View)
========================================
.
├── main.py (Entry Point)
├── README.md
├── requirements.txt
├── report.md (Summary Report)
├── project_graph.mermaid (Graph Data)
├── agents/
│   ├── baseagent.py (ReAct Loop)
│   └── config.py (Dataclass)
├── llms/
│   └── geminiclient.py
├── memory/
│   ├── basememory.py
│   ├── stm.py
│   └── ltm.py
├── tools/
│   ├── basetool.py (Abstract Interface)
│   ├── registry.py (Tool Management)
│   ├── calculator.py
│   ├── filewriter.py
│   ├── filereader.py
│   └── agent_made/ (Custom Tools)
│       ├── terminal_executor.py
│       ├── git_manager.py
│       ├── light_python_runner.py
│       └── directory_watcher.py
├── utils/
│   └── chat_ui.py
└── tests/
```
</file>
## File: `README.md`
<file path="README.md" type="markdown">
```markdown
# Khwarizm - AI Agent Framework
## Overview
Khwarizm is a minimalist, production-inspired AI Agent Framework built entirely from scratch using core Object-Oriented Programming principles in Python. It wraps stateless Large Language Models (LLMs) into intelligent, autonomous agents capable of persistent memory, tool use, and multi-step reasoning.
## The Problem We Solve
Large Language Models are stateless. Every time you call them, they forget everything. They cannot:
- Remember previous conversations
- Take actions in the real world
- Reason through multi-step problems
- Use external tools like calculators or file systems
**Khwarizm solves all of these problems.**
## Architecture Overview
```
                    USER INPUT
                         │
                         ▼
┌────────────────────────────────────────────┐
│                 BaseAgent                  │
│                                            │
│  ┌──────────┐        ┌─────────────────┐  │
│  │  Config  │        │    BaseLLM      │  │
│  │  name    │        │  GroqClient     │  │
│  │  prompt  │        │  GeminiClient   │  │
│  │  tokens  │        └─────────────────┘  │
│  └──────────┘                             │
│                                            │
│  ┌──────────┐        ┌─────────────────┐  │
│  │ToolRegistr│        │    Memory       │  │
│  │Calculator │        │  ShortTerm      │  │
│  │FileWriter │        │  LongTerm       │  │
│  │FileReader │        └─────────────────┘  │
│  └──────────┘                             │
└────────────────────────────────────────────┘
                         │
                         ▼
                    FINAL ANSWER
```
## Project Structure
```
khwarizm/
├── main.py                    # Entry point and demos
├── agents/
│   ├── baseagent.py           # Core agent logic and agentic loop
│   └── config.py              # Agent configuration dataclass
├── clients/
│   ├── basellm.py             # Abstract LLM contract
│   ├── groqclient.py          # Groq implementation
│   └── geminiclient.py        # Gemini implementation
├── tools/
│   ├── basetool.py            # Abstract tool contract
│   ├── registry.py            # Auto tool registration system
│   ├── calculator.py          # Math operations tool
│   ├── filewriter.py          # File writing tool
│   └── filereader.py          # File reading tool
├── memory/
│   ├── basememory.py          # Abstract memory contract
│   ├── stm.py                 # Short term (RAM) memory
│   └── ltm.py                 # Long term (JSON file) memory
└── utils/
    └── chat_ui.py             # Reusable terminal chat interface
```
## OOP Concepts Applied
### 1. Abstraction
Three Abstract Base Classes define the contracts of the framework:
- `BaseLLM` → Any LLM provider must implement `generate()`
- `BaseTool` → Any tool must implement `run()`
- `BaseMemory` → Any memory type must implement `add_entry()`, `get_context()`, `clear()`
```python
from abc import ABC, abstractmethod
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        pass
```
### 2. Encapsulation
Private attributes hide internal data from outside access:
```python
class ToolRegistry:
    def __init__(self):
        self.__tools = {}  # Private! Cannot be accessed from outside
```
### 3. Inheritance
Concrete classes inherit from abstract base classes:
```python
class GroqClient(BaseLLM):      # Inherits LLM contract
class CalculatorTool(BaseTool): # Inherits Tool contract
class ShortTermMemory(BaseMemory): # Inherits Memory contract
```
### 4. Composition
`BaseAgent` is built FROM other objects rather than inheriting from them:
```python
class BaseAgent:
    def __init__(self, ...):
        self.llm = llm              # HAS A LLM
        self.registry = ToolRegistry()  # HAS A Registry
        self.__short_term = ShortTermMemory()  # HAS A Memory
        self.__long_term = LongTermMemory()    # HAS A Memory
```
### 5. Polymorphism
The same `BaseAgent` works identically with different LLM providers:
```python
groq_agent = BaseAgent(llm=GroqClient())    # Works with Groq
gemini_agent = BaseAgent(llm=GeminiClient()) # Works with Gemini
# BaseAgent code does not change. Only the LLM object changes.
```
### 6. Exception Handling
All critical operations are wrapped in try/except blocks:
```python
def generate(self, system_prompt: str, user_prompt: str) -> str:
    try:
        response = self.client.chat.completions.create(...)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: LLM API failed: {str(e)}"
```
### 7. Properties (Advanced Encapsulation)
Clean public access to private internal data:
```python
@property
def name(self) -> str:
    return self.config.name  # User types agent.name, not agent.config.name
```
## The Agentic Loop (Core Algorithm)
The heart of Khwarizm is the **ReAct (Reason + Act) Loop** inside `BaseAgent.run()`.
```
User Input
    │
    ▼
Save to Memory (STM + LTM)
    │
    ▼
┌─────────────────────────────┐
│         WHILE LOOP          │
│                             │
│  Build Context from Memory  │
│           │                 │
│           ▼                 │
│    Send to LLM              │
│           │                 │
│           ▼                 │
│  Does response have TOOL:?  │
│                             │
│  YES              NO        │
│   │                │        │
│   ▼                ▼        │
│ Run Tool      Save to       │
│   │           Memory        │
│   ▼                │        │
│ Save result        ▼        │
│ to Memory     Return        │
│   │           Answer        │
│   ▼                         │
│ Continue Loop               │
└─────────────────────────────┘
    │
    ▼
Max Iterations Reached?
    │
    ▼
Return Error Message
```
## Memory System
Khwarizm has two types of memory working simultaneously:
| | Short Term Memory | Long Term Memory |
|--|------------------|-----------------|
| **Storage** | Python List (RAM) | JSON File (Disk) |
| **Lives** | Current session only | Forever |
| **Dies when** | Program closes | Never |
| **Analogy** | Human working memory | Human long term memory |
## Key Concepts Explained
### 1. Config and the `@dataclass` Decorator
#### What is a `@dataclass`?
In Python, a normal class requires you to write a lot of 
repetitive boilerplate code just to store data:
```python
# WITHOUT dataclass (repetitive and messy)
class Config:
    def __init__(self, name, description, system_prompt, model, max_tokens):
        self.name = name
        self.description = description
        self.system_prompt = system_prompt
        self.model = model
        self.max_tokens = max_tokens
```
The `@dataclass` decorator eliminates all of this repetition. 
You just declare the fields and their types, 
and Python writes the `__init__` for you automatically:
```python
# WITH dataclass (clean and professional)
@dataclass
class Config:
    name: str
    description: str
    system_prompt: str = "You are a helpful AI assistant"
    model: str = "llama3-8b-8192"
    max_tokens: int = 1000
    max_iterations: int = 10
```
#### What does `Config` actually do?
`Config` is a pure data container. It has one job 
and one job only: hold the settings of an agent.
It does NOT:
- Run any logic
- Call any APIs
- Make any decisions
It just holds values. This follows the 
**Single Responsibility Principle** of OOP.
#### What is `__post_init__`?
`__post_init__` is a special method that `@dataclass` 
calls automatically right after the object is created.
We use it to validate the data:
```python
def __post_init__(self):
    if not self.name:
        raise ValueError("Agent must have a name")
    if self.max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0")
    if self.max_iterations <= 0:
        raise ValueError("max_iterations must be greater than 0")
```
**Analogy:** Think of `Config` as a job application form.
`__post_init__` is the HR officer who checks the form
for missing or invalid fields before accepting it.
#### Default Values
Fields with `=` have default values. 
Fields without `=` are mandatory.
**Rule:** Mandatory fields ALWAYS come before fields with defaults.
This is a Python rule. Breaking it causes a `TypeError`.
```python
@dataclass
class Config:
    # MANDATORY FIRST (no defaults)
    name: str
    description: str
    # DEFAULTS SECOND
    system_prompt: str = "You are a helpful AI assistant"
    model: str = "llama3-8b-8192"
    max_tokens: int = 1000
    max_iterations: int = 10
```
### 2. BaseAgent: Every Method Explained
#### `__init__()` - The Setup Method
This is the constructor. It runs exactly once when 
the agent is created. It does 4 things in order:
**Step 1:** Takes the LLM and saves it.
```python
self.llm = llm
```
**Step 2:** Creates a ToolRegistry and automatically 
registers every tool the user passed in.
```python
self.registry = ToolRegistry()
tools = tools or []      # Safe default (avoids mutable default arg bug)
for tool in tools:
    self.registry.register(tool)
```
**Step 3:** If tools exist, injects their descriptions 
into the system prompt so the LLM knows about them.
```python
if tools:
    tool_info = self.registry.get_descriptions()
    system_prompt = f"{system_prompt}\n\nYou have access to:\n{tool_info}"
```
**Step 4:** Creates the Config and both Memory objects.
```python
self.config = Config(name=name, ...)
self.__short_term = ShortTermMemory()
self.__long_term = LongTermMemory(agent_name=name)
```
#### `run(user_input)` - The Agentic Loop
This is the most important method in the entire framework.
It is the **ReAct (Reason + Act)** algorithm.
```
STEP 1: Save user input to both memories
STEP 2: Start the while loop (max_iterations times)
STEP 3: Build the full context from both memories
        (This is what the LLM reads to know what happened so far)
STEP 4: Send (system_prompt + full_context) to LLM
STEP 5: Strip <think> tags if present 
        (Some reasoning models output their thoughts)
STEP 6: Check if LLM response contains "TOOL:"
        YES: Call __handle_tool_call()
             Save action and result to short term memory
             CONTINUE the loop (go back to Step 3)
        NO:  This is the final answer!
             Save to both memories
             RETURN the response to the user
STEP 7: If loop finishes without answer
        Return max iterations error message
```
**Why a loop?**
Because complex tasks require multiple steps. 
A single LLM call can only do one thing. 
The loop allows the agent to:
- Use tool 1
- Read the result
- Use tool 2
- Read the result
- Give final answer
**Why does memory grow each loop?**
Because the LLM has no memory between API calls.
We manually feed it the entire history every loop
so it knows what has already been done.
**Analogy:** Imagine a surgeon who gets amnesia 
between each step of an operation. 
The nurse reads the surgery log out loud 
before every step so the surgeon knows where they are.
The memory is that surgery log.
#### `__handle_tool_call(response)` - The Tool Parser
This private method is called when the LLM decides 
it needs a tool. It does 5 things:
**Step 1:** Split the LLM response into lines
```python
lines = response.strip().split("\n")
```
**Step 2:** Loop through lines to find TOOL: and INPUT:
```python
for line in lines:
    if line.startswith("TOOL:") and not tool_name:
        tool_name = line.replace("TOOL:", "").strip()
    elif line.startswith("INPUT:") and not tool_input:
        tool_input = line.replace("INPUT:", "").strip()
    if tool_name and tool_input:
        break  # Stop after finding the FIRST tool call only
```
**Why `break`?**
Smart LLMs sometimes try to call multiple tools 
in one response. We force ONE tool per loop iteration
so each result gets properly saved to memory 
before the next decision is made.
**Step 3:** Ask the Registry for the tool by name
```python
tool = self.registry.get_tool(tool_name)
```
**Step 4:** If tool not found, return a clean error
```python
if not tool:
    return f"Error: Unknown tool '{tool_name}'"
```
**Step 5:** Run the tool and return the result string
```python
result = tool.run(tool_input)
return f"Tool '{tool_name}' returned: {result}"
```
This result string goes back into the loop,
gets saved to memory, and the LLM reads it 
on the next iteration.
#### `name` property - Clean Public Access
```python
@property
def name(self) -> str:
    return self.config.name
```
Without this, users would write: `agent.config.name`
With this, users write: `agent.name`
This follows the **Law of Demeter**: 
Objects should not reach deep into other objects.
It is also **read-only**. There is no setter.
So `agent.name = "Hacker"` throws an AttributeError.
The name is protected from accidental modification.
#### `available_tools` property
```python
@property
def available_tools(self) -> list:
    return self.registry.list_tools()
```
Returns a clean list of tool names without 
exposing the internal Registry object.
#### `clear_memory()` - The Reset Button
```python
def clear_memory(self):
    self.__short_term.clear()
    self.__long_term.clear()
```
Wipes both memories. The agent starts fresh.
Notice how `BaseAgent` delegates the actual 
clearing to each memory object.
This is the **Single Responsibility Principle**.
The agent manages. The memory objects do the work.
### 3. The Tool System: How It All Connects
#### Why does `BaseTool` use class variables for `name` and `description`?
```python
class CalculatorTool(BaseTool):
    name = "calculator"           # Class variable
    description = "Does math"    # Class variable
```
Because every instance of `CalculatorTool` will 
always have the same name and description.
There is no reason for these to be different 
per object. Class variables are shared across 
all instances. This saves memory and makes 
the code cleaner.
#### Why does `ToolRegistry` use a dictionary?
```python
self.__tools = {}  # Dictionary, not a list!
```
A list lookup is O(n): check index 0, index 1, 
index 2... until found. With 1000 tools: 1000 checks.
A dictionary lookup is O(1): hash the key, 
go directly to the location. Always 1 step.
No matter if you have 1 tool or 1,000,000 tools.
#### The Auto Registration Flow
```
User passes: tools=[CalculatorTool(), FileWriterTool()]
                    │
                    ▼
BaseAgent loops through the list
                    │
                    ▼
registry.register(CalculatorTool())
registry.register(FileWriterTool())
                    │
                    ▼
Registry stores them:
{
    "calculator": CalculatorTool(),
    "file_writer": FileWriterTool()
}
                    │
                    ▼
get_descriptions() builds:
"- calculator: Does math
 - file_writer: Writes files"
                    │
                    ▼
Injected into system prompt
                    │
                    ▼
LLM now knows what tools exist
```
### 4. The Memory System: Why Two Types?
#### The Computer Analogy
Your computer has two types of storage:
- **RAM:** Fast, temporary. Dies when you shut down.
- **Hard Drive:** Slow, permanent. Survives shutdown.
Our memory system mirrors this exactly:
| | ShortTermMemory | LongTermMemory |
|--|----------------|----------------|
| Storage | Python list (RAM) | JSON file (Disk) |
| Speed | Instant | Slightly slower |
| Survives restart | ❌ No | ✅ Yes |
| Used for | Current session | All past sessions |
#### How They Work Together in the Loop
```python
# At the start of run():
self.__short_term.add_entry(role="user", content=user_input)
self.__long_term.add_entry(role="user", content=user_input)
# Inside the loop:
long_term_context = self.__long_term.get_context()
short_term_context = self.__short_term.get_context()
full_context = (
    f"Past Conversations:\n{long_term_context}\n\n"
    f"Current Session:\n{short_term_context}"
)
```
The LLM receives BOTH contexts combined.
It knows what happened in previous sessions 
AND what happened earlier in this session.
### 5. Polymorphism: The Most Powerful OOP Concept in This Framework
Polymorphism means "many forms."
The same interface works differently 
depending on the object behind it.
```python
# Both follow the BaseLLM contract
groq = GroqClient()     # Talks to Groq servers in USA
gemini = GeminiClient() # Talks to Google servers
# BaseAgent does not care which one it gets
agent1 = BaseAgent(llm=groq)
agent2 = BaseAgent(llm=gemini)
# Internally, BaseAgent just calls:
response = self.llm.generate(system_prompt, user_prompt)
# For agent1: This hits Groq's API
# For agent2: This hits Google's API
# The BaseAgent code is IDENTICAL for both
```
This is why Abstract Base Classes exist.
`BaseLLM` guarantees that whatever object 
is passed in, it WILL have a `generate()` method.
The agent never has to check. It just calls it.
### 6. Why Composition Over Inheritance for BaseAgent?
The question is: should `BaseAgent` INHERIT from 
`BaseLLM`, or should it CONTAIN a `BaseLLM`?
**Wrong (Inheritance):**
```python
class BaseAgent(BaseLLM):  # Agent IS A LLM? No!
    pass
```
**Right (Composition):**
```python
class BaseAgent:
    def __init__(self, llm: BaseLLM):
        self.llm = llm  # Agent HAS A LLM. Yes!
```
An agent is NOT a type of LLM.
An agent USES a LLM.
An agent USES memory.
An agent USES tools.
Inheritance models "IS A" relationships.
Composition models "HAS A" relationships.
Using the wrong one here would mean:
- `BaseAgent` could only ever BE one type of LLM
- You could never swap Groq for Gemini
- The entire framework would be tightly coupled
Composition gives us flexibility, 
loose coupling, and the ability to 
swap any component at any time.
## Tool System
Tools give the agent hands. Without tools, the agent can only talk. With tools, it can act.
### How Tools Work:
1. User passes tools into `BaseAgent` as a list
2. `BaseAgent` automatically registers them in `ToolRegistry`
3. Tool descriptions are injected into the system prompt
4. LLM decides which tool to use and responds in a special format
5. Agent parses the response, finds the tool, runs it
6. Result is saved to memory and the loop continues
### Tool Call Format:
```
TOOL: calculator
INPUT: 150*4
```
## Multi-Agent Workflow
Because `BaseAgent.run()` takes text in and returns text out, agents can be chained together using pure Python:
```python
# Agent 1 writes a poem
writer_output = writer_agent.run("Write a poem about AI")
# Agent 2 critiques what Agent 1 wrote
critic_output = critic_agent.run(writer_output)
```
No special framework needed. Just Python variables.
## Installation and Setup
### 1. Clone the repository
```bash
git clone https://github.com/faseeu/khwarizm.git
cd khwarizm
```
### 2. Install dependencies
```bash
pip install groq google-generativeai
```
### 3. Set API Keys
```bash
# Mac/Linux
export GROQ_API_KEY="your_groq_key_here"
export GEMINI_API_KEY="your_gemini_key_here"
# Windows
set GROQ_API_KEY="your_groq_key_here"
set GEMINI_API_KEY="your_gemini_key_here"
```
### 4. Run the demo
```bash
python main.py
```
## Quick Start
```python
from clients.groqclient import GroqClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from baseagent import BaseAgent
# 1. Create the LLM
llm = GroqClient(model="llama3-8b-8192")
# 2. Create the Agent
agent = BaseAgent(
    name="MyAgent",
    llm=llm,
    system_prompt="You are a helpful assistant.",
    tools=[CalculatorTool(), FileWriterTool()]
)
# 3. Run it
response = agent.run("Calculate 150 times 4 and save it to result.txt")
print(response)
```
## Live Demo Output
```
Starting: MyAgent
Creating a new instance...
  [Loop 1/10] Agent is thinking...
  -> Using tool: calculator | Input: 150*4
  [Loop 2/10] Agent is thinking...
  -> Using tool: file_writer | Input: result.txt|600
  [Loop 3/10] Agent is thinking...
The result of 150 multiplied by 4 is 600.
It has been saved to result.txt successfully!
```
## Key Design Decisions
| Decision | Reason |
|----------|--------|
| Abstract Base Classes | Forces correct implementation. No silent bugs. |
| Composition over Inheritance for Agent | Agent HAS a brain. It is not A TYPE of brain. |
| Dictionary in Registry | O(1) lookup speed vs O(n) for lists |
| Two Memory Types | Short term for context. Long term for persistence. |
| Scratchpad replaced by Memory | Cleaner, structured, reusable across sessions |
| Tools injected via list | User never manually touches ToolRegistry |
| `frozen=False` on Config | Allows post-init flexibility |
| Private `__tools` in Registry | Enforces access only through clean public methods |
## Technologies Used
| Technology | Purpose |
|------------|---------|
| Python 3.13 | Core language |
| Groq SDK | LLM API (Llama3, Mixtral models) |
| Google Generative AI SDK | LLM API (Gemini models) |
| `dataclasses` | Clean config management |
| `abc` module | Abstract Base Classes |
| `json` module | Long term memory persistence |
| `os` module | File path management |
## What We Would Add Next
1. **SupervisorAgent** - An agent that manages other agents and routes tasks between them
2. **Streamlit Web UI** - A browser-based chat interface for the framework
3. **WebSearchTool** - Live internet access via DuckDuckGo or Wikipedia API
4. **Python Logging** - Replace print statements with proper log levels
5. **Memory Summarization** - Compress long term memory using LLM summaries to prevent context overflow
## Authors
Built by Faseeh ur Rehman and Huzaifa Imran as part of an OOP and AI Agents learning project.
```
</file>
## File: `report.md`
<file path="report.md" type="markdown">
```markdown
# Project Structure and Files Report
This report documents the current state of the Khwarizm project as of the latest file scan.
## Directory Structure
### Root Directory
- **main.py**: Entry point of the application.
- **README.md**: Project documentation and overview.
- **workflow.py**: Project workflow configuration.
- **requirements.txt**: Dependencies.
- **architecture_flow.mermaid**: Visual representation of the agent architecture.
- **SmartBot_memory.json**, **Agent1_memory.json**: Long-term memory storage files.
- **create_directory.py**: Utility for directory management.
- **doc.html**: Documentation file.
- **.venv/**: Virtual environment directory.
- **llms/**: Contains LLM client implementations (e.g., `geminiclient.py`).
- **utils/**: Utility scripts, including `chat_ui.py`.
- **agents/**: Core agent logic (`baseagent.py`, `config.py`).
- **memory/**: Memory system modules (`basememory.py`, `stm.py`, `ltm.py`).
- **tests/**: Test suite.
- **tools/**: Core tool definitions and custom tool subdirectories.
### Tools Directory
The `tools/` directory is organized into base tools and agent-created extensions:
- **basetool.py**: Abstract base class for all tools.
- **registry.py**: Tool registration system.
- **calculator.py**, **filewriter.py**, **filereader.py**: Standard tools.
- **agent_made/**: Contains tools created during the session.
    - **terminal_executor.py**: Secure terminal execution tool.
    - **git_manager.py**: Git status/log management.
    - **light_python_runner.py**: Ephemeral python execution script.
    - **directory_watcher.py**: Directory navigation utility.
    - **potential_tools.txt**: List of future tool ideas.
## Current Configuration
The system is integrated within `main.py`, importing all tools from `tools/` and `tools/agent_made/` and registering them with the `BaseAgent` instance.
```
</file>
## File: `requirements.txt`
<file path="requirements.txt" type="text">
```text
groq
google-generativeai
```
</file>
## File: `workflow.py`
<file path="workflow.py" type="python">
```python
from llms.geminiclient import GeminiClient
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
llm = GeminiClient(model="gemini-3.1-flash-lite")
# Agent 1: The Writer
writer = BaseAgent(
    name="Writer",
    llm=llm,
    system_prompt="You are a creative writer. Write what the user asks and nothing else. Also use tools",
    tools=[FileWriterTool()]
)
# Agent 2: The Critic
critic = BaseAgent(
    name="Critic",
    llm=llm,
    system_prompt="You are a harsh critic. Read what is given to you and give brutal feedback. Also use tools",
    tools=[FileReaderTool()]
)
poet= BaseAgent(
    name="Poet",
    llm=llm,
    system_prompt="Write a poem in a file",
    tools=[FileReaderTool()]
)
print("Step 1: Writer writes a poem...")
writer_output = writer.run("Write a short poem about AI and save it to poem.txt")
poetOutput = poet.run("Gimme the poems")
print("\nStep 2: Critic reviews the poem...")
critic_output = critic.run("Read poem.txt and another poem file and crush their dreams and give me harsh feedback on it")
print("\nCritic's Verdict:")
print(critic_output)
```
</file>

```
</file>

---

## File: `../Khwarizm/docs/problems.md`
**Last Modified:** `2026-05-25 13:09` | **Size:** `21.65 KB`

<file path="../Khwarizm/docs/problems.md" type="markdown">
```markdown
I'll do a thorough, file-by-file review and then give you a prioritized improvement plan.

---

## Critical Bugs First

### Bug 1: `BaseTool.__init__` swallows `abstractmethod`

```python
# CURRENT (broken)
class BaseTool(ABC):
    def __init__(self):
        name: str
        description: str
        parameters: dict = {}

        @abstractmethod          # ← nested INSIDE __init__, never enforced
        def run(self, parameters: dict) -> str:
            pass
```

`run()` is defined **inside** `__init__`. Python never sees it as an abstract method. Any subclass that forgets to implement `run()` will **not** raise `TypeError`. The entire abstraction contract is silently broken.

```python
# FIXED
from abc import ABC, abstractmethod

class BaseTool(ABC):
    name: str = ""
    description: str = ""
    parameters: dict = {}

    @abstractmethod
    def run(self, parameters: dict) -> str:
        """The method called by the agent to run a tool"""
        pass

    def get_schema(self) -> str:
        params_xml = ""
        for param_name, param_desc in self.parameters.items():
            params_xml += f"\n        <{param_name}>({param_desc})</{param_name}>"
        return (
            f"<tool>\n"
            f"  <tool_name>{self.name}</tool_name>\n"
            f"  <description>{self.description}</description>\n"
            f"  <parameters>{params_xml}\n  </parameters>\n"
            f"</tool>"
        )
```

---

### Bug 2: `eval()` in `CalculatorTool` is a security hole

```python
# CURRENT (dangerous)
result = eval(expression)  # eval("__import__('os').system('rm -rf /')") works fine
```

`eval()` executes **any** Python code. If the LLM hallucinates or is prompted maliciously, this destroys files, leaks keys, or worse.

```python
# FIXED - use ast.literal_eval for simple cases, or a safe parser
import ast
import operator

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    parameters = {
        "expression": "The math expression to evaluate. Example: 150*4"
    }

    # Whitelist of safe operations
    _SAFE_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
    }

    def _safe_eval(self, node):
        if isinstance(node, ast.Constant):          # numbers
            return node.value
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in self._SAFE_OPS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            left = self._safe_eval(node.left)
            right = self._safe_eval(node.right)
            return self._SAFE_OPS[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in self._SAFE_OPS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            return self._SAFE_OPS[op_type](self._safe_eval(node.operand))
        else:
            raise ValueError(f"Unsupported expression type: {type(node).__name__}")

    def run(self, parameters: dict) -> str:
        try:
            expression = parameters.get("expression", "")
            expression = expression.strip().rstrip("=").strip()
            tree = ast.parse(expression, mode="eval")
            result = self._safe_eval(tree.body)
            return str(result)
        except ZeroDivisionError:
            return "Calculator error: Division by zero."
        except ValueError as e:
            return f"Calculator error: {e}"
        except Exception as e:
            return f"Calculator error: {e}"
```

---

### Bug 3: `FileWriterTool` has no path traversal protection

```python
# CURRENT - agent can write to /etc/passwd or ../../secrets.env
with open(filename, "w") as f:
    f.write(content)
```

```python
# FIXED
import os

class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file in the current working directory only."
    parameters = {
        "filename": "The name of the file to write. Example: result.txt",
        "content": "The full text content to write into the file."
    }

    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            content = parameters.get("content", "").strip()

            if not filename:
                return "Error: filename parameter is missing."

            # Prevent path traversal attacks
            safe_path = os.path.realpath(os.path.join(os.getcwd(), filename))
            if not safe_path.startswith(os.getcwd()):
                return "Error: Writing outside the working directory is not allowed."

            # Create subdirectories if needed (safely)
            os.makedirs(os.path.dirname(safe_path), exist_ok=True) \
                if os.path.dirname(safe_path) else None

            with open(safe_path, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"
```

---

### Bug 4: `GeminiClient` uses a non-existent model name

```python
# main.py
llm = GeminiClient(model="gemini-3.1-flash-lite")  # This model does not exist
```

As of 2025, valid model names are `gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-2.0-flash`, etc. This will raise an API error at runtime with a confusing message.

```python
# FIXED geminiclient.py - validate on init
VALID_GEMINI_MODELS = {
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
}

class GeminiClient(BaseLLM):
    def __init__(self, model: str = "gemini-2.0-flash"):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")

        if model not in VALID_GEMINI_MODELS:
            raise ValueError(
                f"Unknown Gemini model: '{model}'. "
                f"Valid options: {sorted(VALID_GEMINI_MODELS)}"
            )

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
```

---

### Bug 5: `LongTermMemory` grows forever and will break the context window

```python
# CURRENT - every single message ever sent gets loaded and sent to LLM
def get_context(self) -> str:
    context = ""
    for entry in self.__history:       # No limit. Session 100 sends 10,000 lines.
        context += f"{entry['role']}: {entry['content']}\n"
    return context
```

After enough sessions, the combined memory exceeds the LLM's context window and the API call fails or gets truncated silently.

```python
# FIXED ltm.py - add a rolling window
class LongTermMemory(BaseMemory):

    def __init__(self, agent_name: str, max_entries: int = 50):
        self.__file_path = f"{agent_name}_memory.json"
        self.__max_entries = max_entries
        self.__history = self.__load_from_file()

    def add_entry(self, role: str, content: str):
        self.__history.append({"role": role, "content": content})
        # Keep only the most recent N entries on disk too
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
        self.__save_to_file()

    def get_context(self) -> str:
        if not self.__history:
            return ""
        # Only send last N entries to LLM to avoid context overflow
        recent = self.__history[-self.__max_entries:]
        return "".join(
            f"{entry['role']}: {entry['content']}\n" for entry in recent
        )
```

---

## Architecture Issues

### Issue 1: `Config` stores `user_prompt` which it never uses

```python
@dataclass
class Config:
    name: str
    description: str = "..."
    system_prompt: str = "You are a helpful AI assistant."
    user_prompt: str = ""        # ← never read by BaseAgent, dead field
    max_tokens: int = 1000       # ← also never used since LLM controls this
```

`user_prompt` belongs to the conversation, not the config. `max_tokens` is already set in `GroqClient`. Remove dead fields.

```python
# FIXED config.py
from dataclasses import dataclass, field

@dataclass
class Config:
    # --- Identity ---
    name: str
    description: str = "A helpful AI agent."

    # --- Prompts ---
    system_prompt: str = "You are a helpful AI assistant."

    # --- Behavior ---
    max_iterations: int = 10

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Agent must have a non-empty name")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than 0")
```

---

### Issue 2: `registry.register()` prints to stdout unconditionally

```python
def register(self, tool: BaseTool):
    self.__tools[tool.name] = tool
    print(f"Registered tool: {tool.name}")   # ← pollutes output in production
```

This is a debug statement left in. In a real system, registration output should be opt-in.

```python
# FIXED registry.py
import logging

logger = logging.getLogger(__name__)

class ToolRegistry:
    def __init__(self):
        self.__tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        if not isinstance(tool, BaseTool):
            raise TypeError(f"Expected BaseTool, got {type(tool).__name__}")
        if not tool.name:
            raise ValueError("Tool must have a non-empty name")
        if tool.name in self.__tools:
            logger.warning(f"Tool '{tool.name}' is being overwritten in registry.")
        self.__tools[tool.name] = tool
        logger.debug(f"Registered tool: {tool.name}")

    def get_tool(self, name: str):
        return self.__tools.get(name)

    def get_descriptions(self) -> str:
        return "\n\n".join(tool.get_schema() for tool in self.__tools.values())

    def list_tools(self) -> list[str]:
        return list(self.__tools.keys())

    def __len__(self) -> int:
        return len(self.__tools)
```

---

### Issue 3: `BaseLLM.generate()` has a redundant `raise NotImplementedError`

```python
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt, user_prompt) -> str:
        raise NotImplementedError    # ← pointless, ABC already enforces this
```

`@abstractmethod` already prevents instantiation. `raise NotImplementedError` is redundant and adds noise. Also, add type hints.

```python
# FIXED basellm.py
from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """
        Send a prompt to the LLM and return the text response.

        Args:
            system_prompt: Instructions that define the agent's behavior.
            user_prompt: The conversation history and current task.

        Returns:
            The LLM's text response.
        """
        pass
```

---

### Issue 4: `chat_ui.py` loses the last response after loop ends

```python
def start_terminal_chat(agent):
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation...")
            break
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
```

And in `main.py`:
```python
start_terminal_chat(agent)
print("\nFinal Answer:")
# print(response)       ← response is undefined here, this would crash
```

The function returns nothing. Make it return the conversation history.

```python
# FIXED chat_ui.py
def start_terminal_chat(agent) -> list[dict]:
    """
    Run an interactive terminal chat session.

    Returns:
        List of conversation turns: [{"user": ..., "agent": ...}, ...]
    """
    print("=" * 50)
    print(f"Chat with {agent.name}  |  Tools: {agent.available_tools}")
    print("Type 'exit' or 'quit' to end. Type 'clear' to reset memory.")
    print("=" * 50)

    history = []

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted.")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Ending conversation...")
            break

        if user_input.lower() == "clear":
            agent.clear_memory()
            print("[Memory cleared]")
            continue

        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
        history.append({"user": user_input, "agent": response})

    return history
```

---

## Code Quality Issues

### Issue 5: `ShortTermMemory` and `LongTermMemory` duplicate `get_context()`

Both classes have this identical method:

```python
def get_context(self) -> str:
    if not self.__history:
        return ""
    context = ""
    for entry in self.__history:
        context += f"{entry['role']}: {entry['content']}\n"
    return context
```

Move the shared logic to `BaseMemory` as a concrete method.

```python
# FIXED memory/memory.py
from abc import ABC, abstractmethod

class BaseMemory(ABC):

    @abstractmethod
    def add_entry(self, role: str, content: str) -> None:
        pass

    @abstractmethod
    def get_history(self) -> list[dict]:
        """Return raw history list for subclasses to implement."""
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    def get_context(self) -> str:
        """Format history as a readable string. Shared by all subclasses."""
        history = self.get_history()
        if not history:
            return ""
        return "".join(
            f"{entry['role']}: {entry['content']}\n" for entry in history
        )
```

```python
# FIXED memory/stm.py
from memory.memory import BaseMemory

class ShortTermMemory(BaseMemory):

    def __init__(self):
        self.__history: list[dict] = []

    def add_entry(self, role: str, content: str) -> None:
        self.__history.append({"role": role, "content": content})

    def get_history(self) -> list[dict]:
        return self.__history.copy()    # Return copy, not the live list

    def clear(self) -> None:
        self.__history = []
```

---

### Issue 6: String concatenation in loops is O(n²)

```python
# CURRENT - inefficient
context = ""
for entry in self.__history:
    context += f"{entry['role']}: {entry['content']}\n"   # new string object each iteration
```

Use `str.join()` instead. It allocates once.

```python
# FIXED - O(n)
return "".join(
    f"{entry['role']}: {entry['content']}\n" for entry in history
)
```

---

### Issue 7: `directory_watcher.py` uses `os.listdir()` which is too shallow

Based on the context description, `os.listdir()` only shows the top level. For an agent working inside a project, it needs a recursive tree view to be useful.

```python
# IMPROVED directory_watcher.py
import os
from tools.basetool import BaseTool

class DirectoryWatcherTool(BaseTool):
    name = "directory_watcher"
    description = "Returns the directory tree of a given path."
    parameters = {
        "path": "The directory path to inspect. Use '.' for current directory.",
        "max_depth": "Maximum depth to recurse. Default is 3."
    }

    def run(self, parameters: dict) -> str:
        try:
            path = parameters.get("path", ".").strip() or "."
            max_depth = int(parameters.get("max_depth", 3))

            if not os.path.exists(path):
                return f"Error: Path '{path}' does not exist."

            lines = []
            self._walk(path, lines, depth=0, max_depth=max_depth)
            return "\n".join(lines) if lines else "Directory is empty."
        except Exception as e:
            return f"Error: {e}"

    def _walk(self, path: str, lines: list, depth: int, max_depth: int):
        if depth > max_depth:
            return
        indent = "  " * depth
        try:
            entries = sorted(os.listdir(path))
        except PermissionError:
            lines.append(f"{indent}[Permission Denied]")
            return
        for entry in entries:
            lines.append(f"{indent}{entry}")
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                self._walk(full_path, lines, depth + 1, max_depth)
```

---

## What to Add Next

### Addition 1: A `WebSearchTool` using DuckDuckGo (no API key needed)

```python
# tools/web_search.py
import urllib.request
import urllib.parse
import json
from tools.basetool import BaseTool

class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Searches the web using DuckDuckGo and returns top results."
    parameters = {
        "query": "The search query. Example: Python asyncio tutorial"
    }

    def run(self, parameters: dict) -> str:
        try:
            query = parameters.get("query", "").strip()
            if not query:
                return "Error: query parameter is missing."

            encoded = urllib.parse.quote(query)
            url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1"

            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())

            results = []

            if data.get("AbstractText"):
                results.append(f"Summary: {data['AbstractText']}")

            for topic in data.get("RelatedTopics", [])[:5]:
                if "Text" in topic:
                    results.append(f"- {topic['Text']}")

            return "\n".join(results) if results else "No results found."

        except Exception as e:
            return f"Web search error: {e}"
```

---

### Addition 2: Proper logging instead of `print()`

```python
# utils/logger.py
import logging
import sys

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates a configured logger for the framework.

    Usage:
        from utils.logger import setup_logger
        logger = setup_logger(__name__)
        logger.info("Agent started")
        logger.debug("Tool called: calculator")
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
            datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
```

---

### Addition 3: A `MemorySummarizationTool` to prevent context overflow

```python
# memory/summarizer.py
class MemorySummarizer:
    """
    Uses the agent's own LLM to compress long memory into a short summary.
    Call this when get_context() exceeds a token threshold.
    """

    def __init__(self, llm):
        self.llm = llm

    def summarize(self, context: str) -> str:
        system = "You are a memory compression assistant."
        user = (
            f"Compress the following conversation history into a concise summary "
            f"that preserves all important facts, decisions, and tool results:\n\n"
            f"{context}"
        )
        try:
            return self.llm.generate(system, user)
        except Exception as e:
            return f"[Summary failed: {e}]\n{context[-500:]}"  # fallback to tail
```

---

## Complete Priority List

```
PRIORITY 1 - Fix Before Using (Bugs)
─────────────────────────────────────
[ ] Fix BaseTool: move @abstractmethod outside __init__
[ ] Replace eval() in CalculatorTool with ast-based safe parser
[ ] Add path traversal protection to FileWriterTool
[ ] Fix GeminiClient model name (gemini-3.1-flash-lite does not exist)
[ ] Add LongTermMemory rolling window to prevent context overflow

PRIORITY 2 - Architecture Cleanup
───────────────────────────────────
[ ] Remove dead fields from Config (user_prompt, max_tokens)
[ ] Remove print() from ToolRegistry.register(), use logging
[ ] Add duplicate tool name warning in ToolRegistry
[ ] Move shared get_context() to BaseMemory base class
[ ] Remove redundant raise NotImplementedError from BaseLLM
[ ] Make chat_ui return conversation history

PRIORITY 3 - Code Quality
──────────────────────────
[ ] Replace string concatenation loops with str.join()
[ ] Add type hints to all method signatures
[ ] Add docstrings to all public methods
[ ] Return copies not live lists from ShortTermMemory
[ ] Make DirectoryWatcherTool recursive with max_depth

PRIORITY 4 - New Features
──────────────────────────
[ ] Add WebSearchTool (DuckDuckGo, no key needed)
[ ] Add proper logging module (utils/logger.py)
[ ] Add MemorySummarizer to handle context overflow gracefully
[ ] Add SupervisorAgent that routes tasks between specialized agents
[ ] Add tests/ directory with at least unit tests for each tool
```

The most important fix by far is **Bug 1** (the `BaseTool` abstract method placement). Your entire tool safety net is currently non-functional because of it, and you would not know until a tool silently misbehaved.\\\




im not gonna fix bug 2 for a while were going to focus on other imp stuff for now
bug 4 seems to be unecessary to fix cuz right now im the only user
also add a list of models feels a lot of work for providers like openrouter and cerebras that keep changing models everyday

lets focus on the logterm memory and also fix the memory once and for all
im open to anyu type of suggestions
and we can also add the episoidic memory
also i want to hear about more better memory if possible cuz what i have been using uptil now is just the ancients just in  order to learn stuff and im still incistant on learning things thats why im developing this shit framework from scratch
```
</file>

---

## File: `../Khwarizm/docs/project_structure.html`
**Last Modified:** `2026-05-23 08:29` | **Size:** `1.61 KB`

<file path="../Khwarizm/docs/project_structure.html" type="html">
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Professional Project Architecture</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f9; color: #333; padding: 40px; }
        .container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        .mermaid { margin-top: 30px; background: #fff; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Khwarizm Architecture Map</h1>
        <p>A detailed overview of the system components and their interdependencies.</p>
        <div class="mermaid">
        graph TB
            subgraph Entry
                M[main.py]
            end
            subgraph Agent_Layer
                A[BaseAgent]
                C[Config]
                Mem[Memory System]
            end
            subgraph Tool_System
                TR[Tool Registry]
                ST[Standard Tools]
                AM[Agent-Made Tools]
            end
            M --> A
            A --> C
            A --> Mem
            A --> TR
            TR --> ST
            TR --> AM
            style M fill:#f9f9f9,stroke:#333
            style A fill:#3498db,color:#fff
            style TR fill:#e67e22,color:#fff
        </div>
    </div>
    <script>mermaid.initialize({startOnLoad:true, theme: 'default'});</script>
</body>
</html>
```
</file>

---

## File: `../Khwarizm/docs/project_structure.txt`
**Last Modified:** `2026-05-23 08:27` | **Size:** `0.93 KB`

<file path="../Khwarizm/docs/project_structure.txt" type="text">
```text
KHWARIZM PROJECT HIERARCHY (Tree View)
========================================

.
├── main.py (Entry Point)
├── README.md
├── requirements.txt
├── report.md (Summary Report)
├── project_graph.mermaid (Graph Data)
├── agents/
│   ├── baseagent.py (ReAct Loop)
│   └── config.py (Dataclass)
├── llms/
│   └── geminiclient.py
├── memory/
│   ├── basememory.py
│   ├── stm.py
│   └── ltm.py
├── tools/
│   ├── basetool.py (Abstract Interface)
│   ├── registry.py (Tool Management)
│   ├── calculator.py
│   ├── filewriter.py
│   ├── filereader.py
│   └── agent_made/ (Custom Tools)
│       ├── terminal_executor.py
│       ├── git_manager.py
│       ├── light_python_runner.py
│       └── directory_watcher.py
├── utils/
│   └── chat_ui.py
└── tests/
```
</file>

---

## File: `../Khwarizm/docs/report.md`
**Last Modified:** `2026-05-23 07:35` | **Size:** `1.81 KB`

<file path="../Khwarizm/docs/report.md" type="markdown">
```markdown
# Project Structure and Files Report

This report documents the current state of the Khwarizm project as of the latest file scan.

## Directory Structure

### Root Directory
- **main.py**: Entry point of the application.
- **README.md**: Project documentation and overview.
- **workflow.py**: Project workflow configuration.
- **requirements.txt**: Dependencies.
- **architecture_flow.mermaid**: Visual representation of the agent architecture.
- **SmartBot_memory.json**, **Agent1_memory.json**: Long-term memory storage files.
- **create_directory.py**: Utility for directory management.
- **doc.html**: Documentation file.
- **.venv/**: Virtual environment directory.
- **llms/**: Contains LLM client implementations (e.g., `geminiclient.py`).
- **utils/**: Utility scripts, including `chat_ui.py`.
- **agents/**: Core agent logic (`baseagent.py`, `config.py`).
- **memory/**: Memory system modules (`basememory.py`, `stm.py`, `ltm.py`).
- **tests/**: Test suite.
- **tools/**: Core tool definitions and custom tool subdirectories.

### Tools Directory
The `tools/` directory is organized into base tools and agent-created extensions:
- **basetool.py**: Abstract base class for all tools.
- **registry.py**: Tool registration system.
- **calculator.py**, **filewriter.py**, **filereader.py**: Standard tools.
- **agent_made/**: Contains tools created during the session.
    - **terminal_executor.py**: Secure terminal execution tool.
    - **git_manager.py**: Git status/log management.
    - **light_python_runner.py**: Ephemeral python execution script.
    - **directory_watcher.py**: Directory navigation utility.
    - **potential_tools.txt**: List of future tool ideas.

## Current Configuration
The system is integrated within `main.py`, importing all tools from `tools/` and `tools/agent_made/` and registering them with the `BaseAgent` instance.
```
</file>

---

## File: `../Khwarizm/llms/__init__.py`
**Last Modified:** `2026-05-09 07:26` | **Size:** `0.06 KB`

<file path="../Khwarizm/llms/__init__.py" type="python">
```python
from .basellm import BaseLLM
from .groqclient import GroqClient
```
</file>

---

## File: `../Khwarizm/llms/basellm.py`
**Last Modified:** `2026-05-26 07:06` | **Size:** `0.15 KB`

<file path="../Khwarizm/llms/basellm.py" type="python">
```python
from abc import ABC , abstractmethod

class BaseLLM(ABC):
    
    @abstractmethod
    def generate(self, system_prompt, user_prompt) ->str:
        pass
```
</file>

---

## File: `../Khwarizm/llms/geminiclient.py`
**Last Modified:** `2026-05-16 14:30` | **Size:** `0.90 KB`

<file path="../Khwarizm/llms/geminiclient.py" type="python">
```python
import os
import google.generativeai as genai
from llms.basellm import BaseLLM

class GeminiClient(BaseLLM):
    def __init__(self, model: str = "gemini-1.5-flash"):
        
        api_key = os.environ.get("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")
            
        # Configure Google's SDK
        genai.configure(api_key=api_key)
        
        # Initialize the model
        self.model = genai.GenerativeModel(model)
    
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            full_prompt = f"System Instructions:\n{system_prompt}\n\nUser Input:\n{user_prompt}"
            
            response = self.model.generate_content(full_prompt)
            return response.text
            
        except Exception as e:
            return f"Error: Gemini API failed with message: {str(e)}"
```
</file>

---

## File: `../Khwarizm/llms/groqclient.py`
**Last Modified:** `2026-05-19 11:43` | **Size:** `0.79 KB`

<file path="../Khwarizm/llms/groqclient.py" type="python">
```python
from llms.basellm import BaseLLM
from groq import Groq

class GroqClient(BaseLLM):
    def __init__(self, model: str, max_tokens: int = 1000 ):

        self.client = Groq()
        self.model = model
        self.max_tokens = max_tokens

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens = self.max_tokens,
                messages = [
                    {"role": "system", "content" : system_prompt},
                    {"role": "user" , "content" : user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: LLM API failed with message: {str(e)}"
```
</file>

---

## File: `../Khwarizm/memory/__init__.py`
**Last Modified:** `2026-05-15 18:13` | **Size:** `0.00 KB`

<file path="../Khwarizm/memory/__init__.py" type="python">
```python

```
</file>

---

## File: `../Khwarizm/memory/ltm.py`
**Last Modified:** `2026-05-26 06:44` | **Size:** `1.54 KB`

<file path="../Khwarizm/memory/ltm.py" type="python">
```python
import json
import os
from memory.memory import BaseMemory

class LongTermMemory(BaseMemory):
    
    def __init__(self, agent_name: str, max_entries: int = 100):
        self.__file_path = f"{agent_name}_memory.json"
        self.__max_entries = max_entries
        self.__history = self.__load_from_file()
    
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })

        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]


        self.__save_to_file()
    
    def get_context(self) -> str:
        if not self.__history:
            return ""
        
        return "".join([
            f"{entry['role']}: {entry['content']}\n"
        for entry in self.__history
        ])
    
    def clear(self):
        self.__history = []
        self.__save_to_file()
    
    def __save_to_file(self):
        try:
            with open(self.__file_path, "w") as f:
                json.dump(self.__history, f, indent=4)
        except Exception as e:
            print(f"Warning: Could not save memory to {self.__file_path}. Error: {e}")
    def __load_from_file(self) -> list:
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Memory file corrupted or unreadable. Starting fresh. Error: {e}")
                return []
        return []
```
</file>

---

## File: `../Khwarizm/memory/memory.py`
**Last Modified:** `2026-05-15 18:30` | **Size:** `0.54 KB`

<file path="../Khwarizm/memory/memory.py" type="python">
```python
from abc import ABC, abstractmethod

class BaseMemory(ABC):
      
    @abstractmethod
    def add_entry(self, role: str, content: str):
        """Save a new message to memory"""
        pass
    
    @abstractmethod
    def get_context(self) -> str:
        """Retrieve full history as a string for the LLM"""
        pass
    
    @abstractmethod
    def clear(self):
        """Reset memory completely"""
        pass


#Roles: The talking entities in a conversation
# user, assistant, system

#  ShortTerm memory: Just a list having the messages #


```
</file>

---

## File: `../Khwarizm/memory/stm.py`
**Last Modified:** `2026-05-26 06:31` | **Size:** `0.75 KB`

<file path="../Khwarizm/memory/stm.py" type="python">
```python
from memory.memory import BaseMemory


class ShortTermMemory(BaseMemory):

    def __init__(self, max_entries=50):
        self.__history = []
        self.__max_entries = max_entries
    
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
        

     
    def get_context(self) -> str:
        if not self.__history:
            return ""
        
        context = ""
        for entry in self.__history:
            context += f"{entry['role']}: {entry['content']}\n"
        return context
    
    def clear(self):
        self.__history = []
```
</file>

---

## File: `../Khwarizm/scripts/__init__.py`
**Last Modified:** `2026-05-09 20:19` | **Size:** `0.00 KB`

<file path="../Khwarizm/scripts/__init__.py" type="python">
```python

```
</file>

---

## File: `../Khwarizm/scripts/compress_context.py`
**Last Modified:** `2026-05-26 07:30` | **Size:** `5.39 KB`

<file path="../Khwarizm/scripts/compress_context.py" type="python">
```python
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
```
</file>

---

## File: `../Khwarizm/scripts/generate_codecontext.py`
**Last Modified:** `2026-05-26 13:08` | **Size:** `5.13 KB`

<file path="../Khwarizm/scripts/generate_codecontext.py" type="python">
```python
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
        '.env', '.ephemeral_venv', '.temp_venv', '.idea', '.vscode','.agent_projects'
    }
    ignore_files: Set[str] = {
        'codecontext.md',
        'context.md',
        'Agent1_memory.json'
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
```
</file>

---

## File: `../Khwarizm/skills/llm_client_skill.md`
**Last Modified:** `2026-05-26 08:55` | **Size:** `1.90 KB`

<file path="../Khwarizm/skills/llm_client_skill.md" type="markdown">
```markdown
# Guide to Creating LLM Clients for the Khwarizm Architecture

To create a functional LLM client that integrates with the existing system, you must inherit from the `BaseLLM` abstract class and adhere to the following requirements:

## 1. Class Structure
Every LLM client must be implemented as a class that inherits from `BaseLLM` (located in `llms/basellm.py`). This ensures compatibility with the agent's LLM orchestration.

## 2. Interface Requirements
Each client must implement:
- **`__init__`**: Handle secure credential retrieval (e.g., from environment variables) and SDK initialization.
- **`generate(system_prompt: str, user_prompt: str) -> str`**: The core method that maps the agent's inputs to the specific provider's API request format.

## 3. Integration
1. Define the class in the `llms/` directory.
2. Ensure the class overrides the abstract methods defined in `BaseLLM`.
3. Use standard error handling to ensure failures return a descriptive string rather than crashing the execution flow.

## 4. Execution Protocol
Clients must be stateless. They are initialized once and utilized for message generation based on the current context provided by the agent.

# Example: Building an LLM Client

To create an LLM client, follow this pattern:

1. **Inheritance**: Inherit from `BaseLLM`.
2. **Implementation**:
```python
import os
from llms.basellm import BaseLLM

class ExampleLLMClient(BaseLLM):
    def __init__(self):
        self.api_key = os.environ.get("EXAMPLE_API_KEY")
        # Initialize your SDK here
        
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            # Construct payload and call provider API
            return "Generated response from LLM"
        except Exception as e:
            return f"Error: LLM provider failed: {str(e)}"
```

This pattern ensures that the system remains extensible to any LLM provider while maintaining a strict, predictable interface.
```
</file>

---

## File: `../Khwarizm/skills/toolSkill.md`
**Last Modified:** `2026-05-26 08:41` | **Size:** `1.65 KB`

<file path="../Khwarizm/skills/toolSkill.md" type="markdown">
```markdown
# Guide to Creating Tools for the Khwarizm Architecture

To create a functional tool within this system, you must adhere to the following architectural requirements:

## 1. Class Structure
Every tool must be implemented as a class that encapsulates its functionality. Ensure it follows the established patterns of the existing toolset to maintain compatibility with the agent's dispatch mechanism.

## 2. Interface Requirements
Each tool must provide:
- A `description` of its capabilities.
- Defined `parameters` that the agent can parse.
- A logic block that accepts inputs and returns outputs in a predictable format.

## 3. Integration
For a new tool to be accessible by the agent:
1. Define the tool class in the appropriate directory (e.g., `tools/agent_made/`).
2. Update `main.py` (or the central entry point) to import the new class.
3. Register the tool instance within the agent's initialized tool list.

## 4. Execution Protocol
Tools must be designed for single-purpose execution per request. They should prioritize safety, logging, and error handling to prevent environment corruption.

# Example: Building a Tool

To create a tool, follow this pattern:

1. **Define the Class**: Create a Python file in `tools/agent_made/`.
2. **Logic Implementation**:
```python
class ExampleTool:
    def __init__(self):
        self.name = "example_tool"
        self.description = "A brief description of what this tool does."

    def execute(self, parameter):
        # Implementation logic here
        return f"Processed: {parameter}"
```
3. **Registering**: Import into `main.py` and add to the `tools` list initialized in the agent.

This keeps the architecture modular and scalable.
```
</file>

---

## File: `../Khwarizm/tools/agent_made/__init__.py`
**Last Modified:** `2026-05-23 07:04` | **Size:** `0.00 KB`

<file path="../Khwarizm/tools/agent_made/__init__.py" type="python">
```python

```
</file>

---

## File: `../Khwarizm/tools/agent_made/directory_watcher.py`
**Last Modified:** `2026-05-23 07:18` | **Size:** `0.60 KB`

<file path="../Khwarizm/tools/agent_made/directory_watcher.py" type="python">
```python
from tools.basetool import BaseTool
import os

class DirectoryWatcherTool(BaseTool):
    def __init__(self):
        self.name = "directory_watcher"
        self.description = "Lists files in a directory to keep track of changes."
        self.parameters = {
            "path": "The path of the directory to list."
        }

    def run(self, parameters: dict) -> str:
        path = parameters.get("path", ".")
        try:
            files = os.listdir(path)
            return f"Files in {path}: {', '.join(files)}"
        except Exception as e:
            return f"Error accessing directory: {str(e)}"
```
</file>

---

## File: `../Khwarizm/tools/agent_made/git_manager.py`
**Last Modified:** `2026-05-23 07:18` | **Size:** `1.01 KB`

<file path="../Khwarizm/tools/agent_made/git_manager.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess

class GitManagerTool(BaseTool):
    def __init__(self):
        self.name = "git_manager"
        self.description = "Provides a safe interface to run 'git status' or 'git log' to track project changes."
        self.parameters = {
            "command": "The git command to execute (e.g., 'status', 'log -n 5')."
        }

    def run(self, parameters: dict) -> str:
        cmd_arg = parameters.get("command", "status")
        full_command = f"git {cmd_arg}"
        print(f"The following git command will be executed: {full_command}. Proceed? (y/n)")
        choice = input().strip().lower()
        
        if choice == 'y':
            try:
                result = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Git command failed: {e.output}"
        else:
            return "Git command execution cancelled by user."
```
</file>

---

## File: `../Khwarizm/tools/agent_made/light_python_runner.py`
**Last Modified:** `2026-05-23 07:21` | **Size:** `1.35 KB`

<file path="../Khwarizm/tools/agent_made/light_python_runner.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess
import os
import shutil

class LightPythonRunnerTool(BaseTool):
    def __init__(self):
        self.name = "light_python_runner"
        self.description = "Executes python files in a clean, ephemeral virtual environment that is deleted immediately after execution."
        self.parameters = {
            "filepath": "The path to the python file to execute."
        }

    def run(self, parameters: dict) -> str:
        filepath = parameters.get("filepath", "")
        venv_dir = ".ephemeral_venv"
        
        # Cleanup if old one exists
        if os.path.exists(venv_dir):
            shutil.rmtree(venv_dir)
            
        cmd = f"python3 -m venv {venv_dir} && {venv_dir}/bin/python3 {filepath}"
        
        print(f"The following ephemeral python execution will be run: {cmd}. Proceed? (y/n)")
        choice = input().strip().lower()
        
        if choice == 'y':
            try:
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Execution failed: {e.output}"
            finally:
                if os.path.exists(venv_dir):
                    shutil.rmtree(venv_dir)
        else:
            return "Execution cancelled by user."
```
</file>

---

## File: `../Khwarizm/tools/agent_made/terminal_executor.py`
**Last Modified:** `2026-05-23 07:04` | **Size:** `0.91 KB`

<file path="../Khwarizm/tools/agent_made/terminal_executor.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess

class TerminalExecutorTool(BaseTool):
    def __init__(self):
        self.name = "terminal_executor"
        self.description = "Executes shell commands after explicit user confirmation."
        self.parameters = {
            "command": "The shell command to be executed."
        }

    def run(self, parameters: dict) -> str:
        command = parameters.get("command", "")
        print(f"The following command will be executed: {command}. Proceed? (y/n)")
        choice = input().strip().lower()
        
        if choice == 'y':
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Command failed: {e.output}"
        else:
            return "Command execution cancelled by user."

```
</file>

---

## File: `../Khwarizm/tools/__init__.py`
**Last Modified:** `2026-05-16 06:08` | **Size:** `0.20 KB`

<file path="../Khwarizm/tools/__init__.py" type="python">
```python
from tools.basetool import BaseTool
from tools.calculator import CalculatorTool
from tools.registry import ToolRegistry
from tools.filereader import FileReaderTool
from tools.filewriter import FileWriterTool
```
</file>

---

## File: `../Khwarizm/tools/basetool.py`
**Last Modified:** `2026-05-25 11:45` | **Size:** `0.79 KB`

<file path="../Khwarizm/tools/basetool.py" type="python">
```python
from abc import ABC,abstractmethod

class BaseTool(ABC):

    def __init__(self):
        name: str
        description: str
        parameters: dict={}


    @abstractmethod
    def run(self, parameters: dict) -> str:
        """The method called by the agent to run a tool"""
        pass


    def get_schema(self) -> str:
        """Builds the XML schema shown to the LLM"""
        params_xml = ""
        for param_name, param_desc in self.parameters.items():
            params_xml += f"\n        <{param_name}>({param_desc})</{param_name}>"

        return (
            f"<tool>\n"
            f"  <tool_name>{self.name}</tool_name>\n"
            f"  <description>{self.description}</description>\n"
            f"  <parameters>{params_xml}\n  </parameters>\n"
            f"</tool>"
        )

```
</file>

---

## File: `../Khwarizm/tools/calculator.py`
**Last Modified:** `2026-05-22 18:22` | **Size:** `0.64 KB`

<file path="../Khwarizm/tools/calculator.py" type="python">
```python
from tools.basetool import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    parameters = {
        "expression": "The math expression to evaluate. Example: 150*4"
    }

    def run(self, parameters: dict) -> str:
        try:
            expression = parameters.get("expression", "")
            # Clean any trailing = signs the LLM might add
            expression = expression.strip().rstrip("=").strip()
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Calculator error: {e}"
```
</file>

---

## File: `../Khwarizm/tools/filereader.py`
**Last Modified:** `2026-05-22 18:29` | **Size:** `0.75 KB`

<file path="../Khwarizm/tools/filereader.py" type="python">
```python
from tools.basetool import BaseTool

class FileReaderTool(BaseTool):
    name = "file_reader"
    description = "Reads and returns the content of a file."
    parameters = {
        "filename": "The name of the file to read. Example: result.txt"
    }

    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()

            if not filename:
                return "Error: filename parameter is missing."

            with open(filename, "r") as f:
                content = f.read()
            return f"Content of {filename}:\n{content}"
        except FileNotFoundError:
            return f"Error: File '{filename}' not found."
        except Exception as e:
            return f"Error reading file: {e}"
```
</file>

---

## File: `../Khwarizm/tools/filewriter.py`
**Last Modified:** `2026-05-25 11:45` | **Size:** `1.25 KB`

<file path="../Khwarizm/tools/filewriter.py" type="python">
```python
from tools.basetool import BaseTool

import os

class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file in the current working directory only."
    parameters = {
        "filename": "The name of the file to write. Example: result.txt",
        "content": "The full text content to write into the file."
    }

    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            content = parameters.get("content", "").strip()

            if not filename:
                return "Error: filename parameter is missing."

            # Prevent path traversal attacks
            safe_path = os.path.realpath(os.path.join(os.getcwd(), filename))
            if not safe_path.startswith(os.getcwd()):
                return "Error: Writing outside the working directory is not allowed."

            # Create subdirectories if needed (safely)
            os.makedirs(os.path.dirname(safe_path), exist_ok=True) \
                if os.path.dirname(safe_path) else None

            with open(safe_path, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"

```
</file>

---

## File: `../Khwarizm/tools/in_process_runner_tool.py`
**Last Modified:** `2026-05-26 09:11` | **Size:** `12.86 KB`

<file path="../Khwarizm/tools/in_process_runner_tool.py" type="python">
```python
"""
tools/python_runner_tool.py

PythonRunnerTool
================
Executes a single Python file inside the current interpreter process.

Strategy
--------
- Zero new dependencies — uses only CPython stdlib.
- exec() with a restricted globals dict (allowlisted builtins + guarded import).
- POSIX resource limits (CPU time, address space, no subprocesses) applied
  inside the worker thread before exec() runs.
- Hard wall-clock timeout via a daemon thread join.
- open() restricted to the working directory — no absolute paths, no ../traversal.
- Stdout/stderr captured and returned; never printed directly.

When to use this tool
---------------------
Use for single-file scripts that only need the standard library or the
allowlisted pure-Python modules listed in _ALLOWED_MODULES below.
For multi-file projects or third-party package installs, use ProjectRunnerTool.
"""

from tools.basetool import BaseTool

import builtins
import io
import os
import resource
import threading
import time
import traceback


# ── Tunables ──────────────────────────────────────────────────────────────────

TIMEOUT_SECONDS = 15          # hard wall-clock limit per run
CPU_SECONDS     = 10          # POSIX RLIMIT_CPU (Linux/macOS only)
MAX_MEMORY_MB   = 128         # POSIX RLIMIT_AS  (Linux/macOS only)
MAX_OUTPUT_CHARS = 50_000     # truncate captured output beyond this

# ── Import allowlist ──────────────────────────────────────────────────────────

_ALLOWED_MODULES = {
    # math / numerics
    "math", "cmath", "decimal", "fractions", "statistics", "random",
    "numbers",
    # data structures
    "collections", "collections.abc", "heapq", "bisect", "array",
    "queue", "copy", "pprint", "enum",
    # strings / text
    "string", "textwrap", "re", "difflib", "unicodedata",
    # date / time
    "datetime", "calendar", "time", "zoneinfo",
    # itertools / functools
    "itertools", "functools", "operator",
    # serialisation
    "json", "csv", "pickle", "struct",
    # typing / introspection
    "typing", "types", "abc", "dataclasses", "inspect",
    # I/O (stdout only — open() is guarded)
    "io", "pathlib",
    # hashing / encoding
    "hashlib", "hmac", "base64", "binascii",
    # context / utils
    "contextlib", "weakref", "gc",
    # exceptions only
    "errno",
}


def _make_safe_import(allowed: set):
    """Return a replacement __import__ restricted to *allowed* modules."""

    def _safe_import(name, globals=None, locals=None, fromlist=(), level=0):
        top = name.split(".")[0]
        if top not in allowed:
            raise ImportError(
                f"Sandbox: '{name}' is not on the import allowlist. "
                f"Use ProjectRunnerTool for third-party packages."
            )
        return builtins.__import__(name, globals, locals, fromlist, level)

    return _safe_import


def _make_safe_open(cwd: str):
    """Return an open() that only permits paths under *cwd*."""

    def _safe_open(file, mode="r", *args, **kwargs):
        path = os.path.realpath(os.path.join(cwd, str(file)))
        if not path.startswith(os.path.realpath(cwd)):
            raise PermissionError(
                f"Sandbox: access outside working directory is blocked: {file!r}"
            )
        return builtins.open(path, mode, *args, **kwargs)

    return _safe_open


def _build_sandbox_globals(cwd: str) -> dict:
    """Assemble the restricted globals dict for exec()."""

    safe_names = {
        "None", "True", "False",
        "bool", "int", "float", "complex", "str", "bytes", "bytearray",
        "list", "tuple", "dict", "set", "frozenset", "memoryview",
        "print", "input",
        "range", "enumerate", "zip", "map", "filter", "reversed", "sorted",
        "len", "sum", "min", "max", "abs", "round", "divmod", "pow",
        "isinstance", "issubclass", "callable", "type",
        "hasattr", "getattr", "setattr", "delattr",
        "vars", "dir", "repr", "hash", "id",
        "iter", "next", "all", "any",
        "chr", "ord", "bin", "oct", "hex", "format",
        "compile", "eval", "exec",
        "staticmethod", "classmethod", "property", "super",
        "object",
        # exception types
        "Exception", "BaseException", "ValueError", "TypeError",
        "KeyError", "IndexError", "AttributeError", "RuntimeError",
        "StopIteration", "NotImplementedError", "OSError", "IOError",
        "FileNotFoundError", "PermissionError", "AssertionError",
        "ZeroDivisionError", "OverflowError", "ImportError", "NameError",
        "RecursionError", "GeneratorExit", "SystemExit", "KeyboardInterrupt",
        "ArithmeticError", "LookupError", "UnicodeError",
        "UnicodeDecodeError", "UnicodeEncodeError", "StopAsyncIteration",
        "ConnectionError", "TimeoutError",
        # built-in functions continued
        "slice", "Ellipsis", "NotImplemented",
        "breakpoint",   # will hit our safe version or just pass
    }

    sandbox = {name: getattr(builtins, name) for name in safe_names if hasattr(builtins, name)}
    sandbox["open"]       = _make_safe_open(cwd)
    sandbox["__import__"] = _make_safe_import(_ALLOWED_MODULES)
    sandbox["__builtins__"] = sandbox   # so nested exec/eval sees same env
    sandbox["__name__"]   = "__main__"
    sandbox["__doc__"]    = None
    return sandbox


# ── Resource limits ───────────────────────────────────────────────────────────

def _apply_resource_limits() -> None:
    try:
        resource.setrlimit(resource.RLIMIT_CPU, (CPU_SECONDS, CPU_SECONDS))
        mem = MAX_MEMORY_MB * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem, mem))
        resource.setrlimit(resource.RLIMIT_NPROC, (0, 0))
    except (AttributeError, ValueError, OSError):
        pass  # Windows or unprivileged — skip silently


# ── Sandbox runner (runs inside daemon thread) ────────────────────────────────

def _run_sandboxed(code: str, filepath: str, result_box: list) -> None:
    """
    Execute *code* in a restricted globals dict with resource limits.
    Stores a result dict into result_box[0].
    """
    import sys

    _apply_resource_limits()

    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout = stdout_buf
    sys.stderr = stderr_buf

    cwd     = os.path.dirname(os.path.abspath(filepath))
    sandbox = _build_sandbox_globals(cwd)
    sandbox["__file__"] = filepath

    t_start = time.perf_counter()
    error   = None

    try:
        exec(compile(code, filepath, "exec"), sandbox)  # noqa: S102
    except SystemExit:
        pass  # treat sys.exit() as clean termination
    except Exception:
        error = traceback.format_exc()
    finally:
        sys.stdout = old_out
        sys.stderr = old_err

    elapsed_ms = round((time.perf_counter() - t_start) * 1000)
    stdout_val = stdout_buf.getvalue()
    stderr_val = stderr_buf.getvalue()

    # Truncate runaway output
    if len(stdout_val) > MAX_OUTPUT_CHARS:
        stdout_val = stdout_val[:MAX_OUTPUT_CHARS] + f"\n[...truncated at {MAX_OUTPUT_CHARS} chars]"
    if len(stderr_val) > MAX_OUTPUT_CHARS:
        stderr_val = stderr_val[:MAX_OUTPUT_CHARS] + f"\n[...truncated at {MAX_OUTPUT_CHARS} chars]"

    result_box[0] = {
        "stdout":     stdout_val,
        "stderr":     stderr_val,
        "error":      error,
        "elapsed_ms": elapsed_ms,
        "file":       filepath,
    }


# ── Tool class ────────────────────────────────────────────────────────────────

class InprocessPythonRunnerTool(BaseTool):
    """
    Execute a single Python file in a locked-down in-process sandbox.

    Capabilities
    ------------
    - Fast: <1 ms overhead (no subprocess, no venv spin-up).
    - Safe: restricted builtins, guarded import/open, POSIX resource limits,
      hard timeout via daemon thread.
    - Zero deps: pure CPython stdlib.

    Limitations
    -----------
    - Only stdlib modules on the allowlist are importable.
    - No network access, no subprocess spawning, no absolute filesystem paths.
    - For third-party packages or multi-file projects → use ProjectRunnerTool.
    """

    def __init__(self):
        self.name = "python_runner"
        self.description = (
            "Execute a single Python (.py) file in a secure in-process sandbox. "
            "Supports stdlib only. Returns stdout, stderr, errors, and execution time. "
            "No installs required. For projects with pip packages use project_runner."
        )
        self.parameters = {
            "filepath": (
                "Path to the .py file to execute. "
                "Must be relative to the working directory."
            ),
        }

    # ------------------------------------------------------------------
    def run(self, parameters: dict) -> dict:
        """
        Execute the file at parameters['filepath'].

        Returns
        -------
        dict with keys:
            success     : bool   — True if no uncaught exception
            stdout      : str    — captured standard output
            stderr      : str    — captured standard error
            error       : str|None — formatted traceback if exception
            elapsed_ms  : int    — wall-clock execution time in milliseconds
            file        : str    — resolved filepath that was executed
            sandbox     : str    — always "in-process (restricted exec)"
        """
        filepath: str = parameters.get("filepath", "").strip()

        # ── Validate ────────────────────────────────────────────────────
        err = self._validate(filepath)
        if err:
            return {"success": False, "error": err, "stdout": "", "stderr": "",
                    "elapsed_ms": 0, "file": filepath, "sandbox": "in-process (restricted exec)"}

        norm = os.path.normpath(filepath)

        # ── Read source ─────────────────────────────────────────────────
        try:
            source = open(norm, encoding="utf-8").read()
        except OSError as exc:
            return {"success": False, "error": f"Cannot read file: {exc}",
                    "stdout": "", "stderr": "", "elapsed_ms": 0,
                    "file": norm, "sandbox": "in-process (restricted exec)"}

        # ── Syntax check before threading ───────────────────────────────
        try:
            compile(source, norm, "exec")
        except SyntaxError as exc:
            return {"success": False, "error": f"SyntaxError: {exc}",
                    "stdout": "", "stderr": "", "elapsed_ms": 0,
                    "file": norm, "sandbox": "in-process (restricted exec)"}

        # ── Run in daemon thread with timeout ───────────────────────────
        result_box: list = [None]
        thread = threading.Thread(
            target=_run_sandboxed,
            args=(source, norm, result_box),
            daemon=True,
        )
        thread.start()
        thread.join(timeout=TIMEOUT_SECONDS)

        if thread.is_alive():
            return {
                "success":    False,
                "error":      f"Timeout: execution exceeded {TIMEOUT_SECONDS}s wall-clock limit.",
                "stdout":     "",
                "stderr":     "",
                "elapsed_ms": TIMEOUT_SECONDS * 1000,
                "file":       norm,
                "sandbox":    "in-process (restricted exec)",
            }

        result = result_box[0]
        result["success"] = result["error"] is None
        result["sandbox"] = "in-process (restricted exec)"
        return result

    # ------------------------------------------------------------------
    @staticmethod
    def _validate(filepath: str) -> str | None:
        """Return an error string, or None if filepath is acceptable."""
        if not filepath:
            return "Parameter 'filepath' is required."
        norm = os.path.normpath(filepath)
        if os.path.isabs(norm):
            return f"Absolute paths are not permitted: {filepath!r}"
        if norm.startswith(".."):
            return f"Parent-directory traversal is not permitted: {filepath!r}"
        if not norm.endswith(".py"):
            return f"Only .py files are accepted, got: {filepath!r}"
        if not os.path.isfile(norm):
            return f"File not found: {norm!r}"
        return None
```
</file>

---

## File: `../Khwarizm/tools/project_runner.py`
**Last Modified:** `2026-05-26 12:49` | **Size:** `35.49 KB`

<file path="../Khwarizm/tools/project_runner.py" type="python">
```python
"""
tools/project_runner_tool.py

ProjectRunnerTool
=================
Manages and executes a full multi-file Python project with pip package support.

Strategy
--------
- Each project lives in its own directory under a configurable base path.
- Packages are installed into a project-local virtual environment (one venv
  per project, reused across runs — no rebuild unless explicitly reset).
- Execution uses subprocess with:
    • shell=False  (no injection surface)
    • an explicit argument list
    • a timeout
    • cwd set to the project directory
    • a clean, minimal environment (no host secrets leaked)
    • stdout/stderr captured and returned
- File writes are validated before touching disk.
- The agent interacts through a structured tool interface; humans see a clear
  result dict with every detail they need to understand what happened.

When to use this tool
---------------------
Use when:
- The task requires multiple Python files (modules, packages, configs).
- Third-party packages (pandas, requests, etc.) need to be installed.
- The project needs to persist between agent turns (files survive the call).

For single-file stdlib-only scripts use PythonRunnerTool instead — it is
faster and requires no venv setup.
"""

from __future__ import annotations

from tools.basetool import BaseTool

import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import venv
from datetime import datetime
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


# ── Tunables ──────────────────────────────────────────────────────────────────

DEFAULT_BASE_DIR      = ".agent_projects"
RUN_TIMEOUT_SECONDS   = 60
PIP_TIMEOUT_SECONDS   = 120
MAX_OUTPUT_CHARS      = 100_000
MAX_FILE_SIZE_BYTES   = 1_000_000   # 1 MB
MAX_FILES_PER_PROJECT = 100
MAX_LOG_LINES         = 10_000


# ── Validation patterns ───────────────────────────────────────────────────────

# PEP 508 distribution name plus optional version specifier
_PKG_NAME_RE = re.compile(
    r"^([A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"(\s*[><=!~^]+\s*[A-Za-z0-9.*+!-]+)?$"
)

_PROJECT_ID_RE = re.compile(r"^[a-zA-Z0-9_\-]{1,40}$")

# Allowed shapes for entry_args: plain values, flags, key=value pairs
_SAFE_ARG_RE = re.compile(r"^[A-Za-z0-9_./:@,=+\-]{1,256}$")


# ── Allowed actions ───────────────────────────────────────────────────────────

ACTIONS = {
    "write_file":      "Create or overwrite a file in the project.",
    "read_file":       "Read a file from the project.",
    "list_files":      "List all files in the project.",
    "delete_file":     "Delete a file from the project.",
    "move_file":       "Move or rename a file within the project.",
    "install_package": "Install a pip package into the project venv.",
    "list_packages":   "List packages installed in the project venv.",
    "run":             "Execute a Python file inside the project venv.",
    "run_snippet":     "Run an ad-hoc Python snippet inside the project venv.",
    "reset":           "Delete the entire project directory and start fresh.",
    "status":          "Return project metadata (files, packages, venv path).",
}


# ── Custom exceptions ─────────────────────────────────────────────────────────

class ProjectRunnerError(Exception):
    """Base for all tool-level errors."""

class PathTraversalError(ProjectRunnerError):
    """Raised when a path escapes the project root."""

class ValidationError(ProjectRunnerError):
    """Raised when input parameters fail validation."""

class VenvError(ProjectRunnerError):
    """Raised when venv creation or executable lookup fails."""


# ── Helpers ───────────────────────────────────────────────────────────────────

def _clean_env(venv_dir: Path) -> dict[str, str]:
    """
    Return a minimal environment for subprocesses.
    Replaces PATH with only the venv bin directory so no host
    executables are reachable. Keeps locale and temp-dir variables.
    """
    venv_bin = str(venv_dir / ("Scripts" if sys.platform == "win32" else "bin"))

    keep_as_is = {
        "HOME", "USER", "LANG", "LC_ALL", "LC_CTYPE",
        "TERM", "TMPDIR", "TMP", "TEMP",
        "SYSTEMROOT", "USERPROFILE",
    }
    env = {k: v for k, v in os.environ.items() if k in keep_as_is}
    env["PATH"] = venv_bin
    return env


def _truncate(text: str, limit: int = MAX_OUTPUT_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n[...output truncated at {limit} chars]"


def _safe_relpath(base: Path, target: str) -> Path:
    """
    Resolve *target* relative to *base* and verify it stays inside *base*.
    Raises PathTraversalError on traversal attempts.
    Raises ValidationError on empty or obviously invalid paths.
    """
    if not target or target.strip() in ("", ".", ".."):
        raise ValidationError(f"Invalid path: {target!r}")
    resolved = (base / target).resolve()
    try:
        resolved.relative_to(base.resolve())
    except ValueError:
        raise PathTraversalError(
            f"Path traversal blocked: {target!r} escapes project root."
        )
    return resolved


def _validate_project_id(pid: str) -> str | None:
    """Return an error message string, or None if valid."""
    if not pid:
        return "'project_id' is required."
    if not _PROJECT_ID_RE.fullmatch(pid):
        return (
            f"'project_id' must be 1-40 characters: letters, digits, "
            f"hyphens, underscores. Got: {pid!r}"
        )
    return None


def _validate_package_name(package: str) -> str | None:
    """Return an error message string, or None if valid."""
    if not package:
        return "'package' is required."
    if not _PKG_NAME_RE.fullmatch(package.strip()):
        return (
            f"Invalid package specifier: {package!r}. "
            "Use PyPI names like 'requests' or 'pandas==2.2.0'."
        )
    return None


def _validate_entry_args(args: Any) -> tuple[list[str], str | None]:
    """
    Validate and normalise entry_args.
    Returns (clean_list, error_message_or_None).
    """
    if args is None:
        return [], None
    if not isinstance(args, list):
        return [], "'entry_args' must be a list of strings."
    clean = []
    for i, arg in enumerate(args):
        arg_str = str(arg)
        if not _SAFE_ARG_RE.fullmatch(arg_str):
            return [], (
                f"entry_args[{i}]={arg_str!r} contains unsafe characters. "
                "Only alphanumerics and _./:@,=+- are allowed."
            )
        clean.append(arg_str)
    return clean, None


# ── Tool class ────────────────────────────────────────────────────────────────

class ProjectRunnerTool(BaseTool):
    """
    Full project execution environment for the agent.

    One tool, many actions. The agent picks the action it needs and
    supplies the matching parameters. Every action returns a structured
    dict so the agent can reason about the result and the human can read
    the log without digging into internals.

    Project layout on disk
    ----------------------
    <base_dir>/
      <project_id>/
        files/          ← all user/agent-written source files live here
          main.py
          utils/
            helpers.py
          ...
        venv/           ← project-local virtual environment (created on first use)
        run.log         ← rotating log of every run (not returned to agent)
    """

    def __init__(self, base_dir: str = DEFAULT_BASE_DIR) -> None:
        self.base_dir = Path(base_dir).resolve()
        self.base_dir.mkdir(parents=True, exist_ok=True)

        self.name = "project_runner"
        self.description = (
            "Manage and execute a full multi-file Python project with pip package support. "
            "Actions: write_file, read_file, list_files, delete_file, move_file, "
            "install_package, list_packages, run, run_snippet, reset, status. "
            "Each project is isolated in its own directory with its own venv."
        )
        self.parameters = {
            "project_id": (
                "Short identifier for the project, e.g. 'web_scraper'. "
                "Alphanumeric, hyphens, underscores. Max 40 chars. "
                "The same project_id re-uses the same directory and venv across calls."
            ),
            "action": (
                "One of: " + ", ".join(ACTIONS.keys()) + ". "
                "See tool description for what each action does."
            ),
            "filename": (
                "[write_file, read_file, delete_file, run, move_file (source)] "
                "Path relative to the project root, e.g. 'main.py' or 'utils/helpers.py'."
            ),
            "destination": (
                "[move_file] Destination path relative to the project root."
            ),
            "content": (
                "[write_file] Full content of the file as a string."
            ),
            "package": (
                "[install_package] PyPI package name, optionally with version, "
                "e.g. 'requests' or 'pandas==2.2.0'."
            ),
            "code": (
                "[run_snippet] A Python code snippet to execute inside the project venv. "
                "The project files directory is on sys.path."
            ),
            "entry_args": (
                "[run] Optional list of command-line arguments to pass to the script, "
                "e.g. ['--input', 'data.csv']. Each arg must match "
                r"^[A-Za-z0-9_./:@,=+\-]{1,256}$. Defaults to []."
            ),
            "stdin": (
                "[run] Optional string to feed as stdin to the process."
            ),
        }

    # ── Dispatch ──────────────────────────────────────────────────────────────

    def run(self, parameters: dict) -> dict:
        """
        Route to the appropriate action handler.

        Always returns a dict with at least:
            success : bool
            action  : str
            project : str
            message : str   — human-readable summary
            error   : str | None
        """
        project_id = parameters.get("project_id", "")
        if isinstance(project_id, str):
            project_id = project_id.strip()

        action = parameters.get("action", "")
        if isinstance(action, str):
            action = action.strip()

        # ── Validate project_id ───────────────────────────────────────
        pid_err = _validate_project_id(project_id)
        if pid_err:
            return self._err(project_id, action, pid_err)

        # ── Validate action ───────────────────────────────────────────
        if action not in ACTIONS:
            return self._err(
                project_id, action,
                f"Unknown action {action!r}. Valid actions: {', '.join(ACTIONS)}"
            )

        project_dir = self.base_dir / project_id
        files_dir   = project_dir / "files"
        venv_dir    = project_dir / "venv"

        # ── Ensure project directory exists (except for reset) ────────
        if action != "reset":
            files_dir.mkdir(parents=True, exist_ok=True)

        # ── Route ─────────────────────────────────────────────────────
        try:
            if action == "write_file":
                return self._write_file(project_id, files_dir, parameters)
            elif action == "read_file":
                return self._read_file(project_id, files_dir, parameters)
            elif action == "list_files":
                return self._list_files(project_id, files_dir)
            elif action == "delete_file":
                return self._delete_file(project_id, files_dir, parameters)
            elif action == "move_file":
                return self._move_file(project_id, files_dir, parameters)
            elif action == "install_package":
                return self._install_package(project_id, venv_dir, parameters)
            elif action == "list_packages":
                return self._list_packages(project_id, venv_dir)
            elif action == "run":
                return self._run_file(project_id, files_dir, venv_dir, parameters)
            elif action == "run_snippet":
                return self._run_snippet(project_id, files_dir, venv_dir, parameters)
            elif action == "reset":
                return self._reset(project_id, project_dir)
            elif action == "status":
                return self._status(project_id, project_dir, files_dir, venv_dir)
        except ProjectRunnerError as exc:
            return self._err(project_id, action, str(exc))
        except Exception as exc:
            import traceback
            logger.exception("Unexpected error in ProjectRunnerTool")
            return self._err(
                project_id, action,
                f"Unexpected error: {exc}\n{traceback.format_exc()}"
            )

    # ── Action: write_file ────────────────────────────────────────────────────

    def _write_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "")
        if isinstance(filename, str):
            filename = filename.strip()
        content = params.get("content", "")

        if not filename:
            return self._err(pid, "write_file", "'filename' is required.")
        if not isinstance(content, str):
            return self._err(pid, "write_file", "'content' must be a string.")

        encoded = content.encode("utf-8")
        if len(encoded) > MAX_FILE_SIZE_BYTES:
            return self._err(
                pid, "write_file",
                f"File exceeds size limit ({MAX_FILE_SIZE_BYTES // 1_000} KB)."
            )

        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "write_file", str(e))

        # Count only regular files, and only block if this is a brand new file
        existing_count = sum(1 for p in files_dir.rglob("*") if p.is_file())
        is_new_file = not target.exists()
        if is_new_file and existing_count >= MAX_FILES_PER_PROJECT:
            return self._err(
                pid, "write_file",
                f"Project file limit ({MAX_FILES_PER_PROJECT}) reached."
            )

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

        return {
            "success":       True,
            "action":        "write_file",
            "project":       pid,
            "filename":      filename,
            "bytes_written": len(encoded),
            "path":          str(target),
            "message":       f"Wrote {filename} ({len(encoded):,} bytes).",
            "error":         None,
        }

    # ── Action: read_file ─────────────────────────────────────────────────────

    def _read_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "").strip()
        if not filename:
            return self._err(pid, "read_file", "'filename' is required.")
        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "read_file", str(e))

        if not target.exists():
            return self._err(pid, "read_file", f"File not found: {filename!r}")
        if not target.is_file():
            return self._err(pid, "read_file", f"Not a file: {filename!r}")

        content    = target.read_text(encoding="utf-8")
        byte_count = len(content.encode("utf-8"))
        return {
            "success":  True,
            "action":   "read_file",
            "project":  pid,
            "filename": filename,
            "content":  content,
            "bytes":    byte_count,
            "message":  f"Read {filename} ({byte_count:,} bytes).",
            "error":    None,
        }

    # ── Action: list_files ────────────────────────────────────────────────────

    def _list_files(self, pid: str, files_dir: Path) -> dict:
        if not files_dir.exists():
            return {
                "success": True, "action": "list_files", "project": pid,
                "files": [], "count": 0,
                "message": "Project is empty.", "error": None,
            }
        files = []
        for p in sorted(files_dir.rglob("*")):
            if p.is_file():
                rel  = p.relative_to(files_dir).as_posix()
                stat = p.stat()
                files.append({
                    "path":     rel,
                    "bytes":    stat.st_size,
                    "modified": datetime.fromtimestamp(
                        stat.st_mtime
                    ).isoformat(timespec="seconds"),
                })
        return {
            "success": True, "action": "list_files", "project": pid,
            "files":   files,
            "count":   len(files),
            "message": f"{len(files)} file(s) in project.",
            "error":   None,
        }

    # ── Action: delete_file ───────────────────────────────────────────────────

    def _delete_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "").strip()
        if not filename:
            return self._err(pid, "delete_file", "'filename' is required.")
        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "delete_file", str(e))

        if not target.exists():
            return self._err(pid, "delete_file", f"File not found: {filename!r}")
        if not target.is_file():
            return self._err(pid, "delete_file", f"Not a file: {filename!r}")

        target.unlink()
        return {
            "success":  True,
            "action":   "delete_file",
            "project":  pid,
            "filename": filename,
            "message":  f"Deleted {filename}.",
            "error":    None,
        }

    # ── Action: move_file ─────────────────────────────────────────────────────

    def _move_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        src_name = params.get("filename", "").strip()
        dst_name = params.get("destination", "").strip()

        if not src_name:
            return self._err(pid, "move_file", "'filename' (source) is required.")
        if not dst_name:
            return self._err(pid, "move_file", "'destination' is required.")

        try:
            src = _safe_relpath(files_dir, src_name)
            dst = _safe_relpath(files_dir, dst_name)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "move_file", str(e))

        if not src.exists():
            return self._err(pid, "move_file", f"Source not found: {src_name!r}")
        if not src.is_file():
            return self._err(pid, "move_file", f"Not a file: {src_name!r}")
        if dst.exists():
            return self._err(pid, "move_file", f"Destination already exists: {dst_name!r}")

        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)

        return {
            "success":     True,
            "action":      "move_file",
            "project":     pid,
            "filename":    src_name,
            "destination": dst_name,
            "message":     f"Moved {src_name!r} -> {dst_name!r}.",
            "error":       None,
        }

    # ── Action: install_package ───────────────────────────────────────────────

    def _install_package(self, pid: str, venv_dir: Path, params: dict) -> dict:
        package = params.get("package", "").strip()

        pkg_err = _validate_package_name(package)
        if pkg_err:
            return self._err(pid, "install_package", pkg_err)

        pip_exe = self._ensure_venv(venv_dir)
        cmd = [
            str(pip_exe), "install",
            "--quiet",
            "--disable-pip-version-check",
            "--no-input",
            "--exists-action", "i",
            package,
        ]
        t0 = time.perf_counter()
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=PIP_TIMEOUT_SECONDS,
                env=_clean_env(venv_dir),
                shell=False,
            )
        except subprocess.TimeoutExpired:
            return self._err(
                pid, "install_package",
                f"pip install timed out after {PIP_TIMEOUT_SECONDS}s."
            )

        elapsed_ms = round((time.perf_counter() - t0) * 1000)

        if result.returncode != 0:
            return {
                "success":    False,
                "action":     "install_package",
                "project":    pid,
                "package":    package,
                "stdout":     _truncate(result.stdout),
                "stderr":     _truncate(result.stderr),
                "elapsed_ms": elapsed_ms,
                "message":    f"pip install {package!r} failed (exit {result.returncode}).",
                "error":      result.stderr.strip() or f"exit {result.returncode}",
            }

        return {
            "success":    True,
            "action":     "install_package",
            "project":    pid,
            "package":    package,
            "stdout":     _truncate(result.stdout),
            "elapsed_ms": elapsed_ms,
            "message":    f"Installed {package!r} in {elapsed_ms} ms.",
            "error":      None,
        }

    # ── Action: list_packages ─────────────────────────────────────────────────

    def _list_packages(self, pid: str, venv_dir: Path) -> dict:
        if not venv_dir.exists():
            return {
                "success":  True,
                "action":   "list_packages",
                "project":  pid,
                "packages": [],
                "count":    0,
                "message":  "No venv yet — no packages installed.",
                "error":    None,
            }
        pip_exe = self._get_pip(venv_dir)
        result  = subprocess.run(
            [str(pip_exe), "list", "--format=json", "--disable-pip-version-check"],
            capture_output=True, text=True, timeout=30,
            env=_clean_env(venv_dir), shell=False,
        )
        warning = None
        try:
            pkgs = json.loads(result.stdout)
        except json.JSONDecodeError:
            pkgs    = []
            warning = f"Could not parse pip list output: {result.stdout[:200]!r}"
            logger.warning("list_packages JSON parse failure: %s", result.stdout[:200])

        return {
            "success":  True,
            "action":   "list_packages",
            "project":  pid,
            "packages": pkgs,
            "count":    len(pkgs),
            "message":  f"{len(pkgs)} package(s) installed.",
            "warning":  warning,
            "error":    None,
        }

    # ── Action: run ───────────────────────────────────────────────────────────

    def _run_file(
        self, pid: str, files_dir: Path, venv_dir: Path, params: dict
    ) -> dict:
        filename   = params.get("filename", "").strip()
        entry_args = params.get("entry_args", [])
        stdin_data = params.get("stdin", None)

        if not filename:
            return self._err(pid, "run", "'filename' is required.")
        if not filename.endswith(".py"):
            return self._err(pid, "run", "Only .py files can be executed.")

        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "run", str(e))

        if not target.exists():
            return self._err(pid, "run", f"File not found: {filename!r}")
        if not target.is_file():
            return self._err(pid, "run", f"Not a file: {filename!r}")

        clean_args, args_err = _validate_entry_args(entry_args)
        if args_err:
            return self._err(pid, "run", args_err)

        python_exe = self._ensure_python(venv_dir)
        cmd = [str(python_exe), str(target)] + clean_args

        return self._subprocess_run(
            pid, "run", cmd, cwd=files_dir,
            filename=filename, stdin_data=stdin_data,
            venv_dir=venv_dir,
        )

    # ── Action: run_snippet ───────────────────────────────────────────────────

    def _run_snippet(
        self, pid: str, files_dir: Path, venv_dir: Path, params: dict
    ) -> dict:
        """
        Execute an ad-hoc snippet by writing it to a temp file — never
        embedding it in a shell string or -c argument.
        Tracebacks will show real line numbers inside the snippet.
        """
        code = params.get("code", "")
        if not isinstance(code, str) or not code.strip():
            return self._err(pid, "run_snippet", "'code' must be a non-empty string.")

        python_exe = self._ensure_python(venv_dir)

        # Wrapper gives the snippet access to project files on sys.path
        wrapper = textwrap.dedent(f"""\
            import sys as _sys, os as _os
            _sys.path.insert(0, {str(files_dir)!r})
            _os.chdir({str(files_dir)!r})
            # ── user snippet below ──────────────────────────────────
        """) + code

        # Write to a real temp file so tracebacks show accurate line numbers
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", prefix="snippet_",
            dir=str(files_dir), delete=False, encoding="utf-8",
        ) as tmp:
            tmp.write(wrapper)
            tmp_path = Path(tmp.name)

        try:
            cmd = [str(python_exe), str(tmp_path)]
            return self._subprocess_run(
                pid, "run_snippet", cmd, cwd=files_dir, venv_dir=venv_dir
            )
        finally:
            try:
                tmp_path.unlink()
            except OSError:
                pass

    # ── Action: reset ─────────────────────────────────────────────────────────

    def _reset(self, pid: str, project_dir: Path) -> dict:
        existed = project_dir.exists()
        if existed:
            shutil.rmtree(project_dir)
        return {
            "success": True,
            "action":  "reset",
            "project": pid,
            "message": (
                f"Project '{pid}' deleted. Next write_file will start fresh."
                if existed else
                f"Project '{pid}' did not exist — nothing to delete."
            ),
            "error": None,
        }

    # ── Action: status ────────────────────────────────────────────────────────

    def _status(
        self, pid: str, project_dir: Path, files_dir: Path, venv_dir: Path
    ) -> dict:
        files_info = self._list_files(pid, files_dir)
        # Only call list_packages if venv actually exists
        packages_info = (
            self._list_packages(pid, venv_dir)
            if venv_dir.exists()
            else {"packages": [], "count": 0}
        )
        return {
            "success":       True,
            "action":        "status",
            "project":       pid,
            "project_root":  str(project_dir),
            "files_dir":     str(files_dir),
            "venv_dir":      str(venv_dir),
            "venv_exists":   venv_dir.exists(),
            "files":         files_info.get("files", []),
            "file_count":    files_info.get("count", 0),
            "packages":      packages_info.get("packages", []),
            "package_count": packages_info.get("count", 0),
            "message": (
                f"{files_info.get('count', 0)} file(s), "
                f"{packages_info.get('count', 0)} package(s)."
            ),
            "error": None,
        }

    # ── Subprocess execution helper ───────────────────────────────────────────

    def _subprocess_run(
        self,
        pid: str,
        action: str,
        cmd: list[str],
        cwd: Path,
        filename: str | None = None,
        stdin_data: str | None = None,
        venv_dir: Path | None = None,
    ) -> dict:
        env = _clean_env(venv_dir) if venv_dir else dict(os.environ)
        t0  = time.perf_counter()

        try:
            result = subprocess.run(
                cmd,
                input=stdin_data,
                capture_output=True,
                text=True,
                timeout=RUN_TIMEOUT_SECONDS,
                cwd=str(cwd),
                env=env,
                shell=False,
            )
        except subprocess.TimeoutExpired:
            return {
                "success":    False,
                "action":     action,
                "project":    pid,
                "filename":   filename,
                "stdout":     "",
                "stderr":     "",
                "returncode": -1,
                "elapsed_ms": RUN_TIMEOUT_SECONDS * 1_000,
                "message":    f"Timeout: execution exceeded {RUN_TIMEOUT_SECONDS}s.",
                "error":      "TimeoutExpired",
            }

        elapsed_ms = round((time.perf_counter() - t0) * 1000)
        self._append_log(pid, cmd, result, elapsed_ms)

        success = result.returncode == 0
        return {
            "success":    success,
            "action":     action,
            "project":    pid,
            "filename":   filename,
            "stdout":     _truncate(result.stdout),
            "stderr":     _truncate(result.stderr),
            "returncode": result.returncode,
            "elapsed_ms": elapsed_ms,
            "message": (
                f"Ran successfully in {elapsed_ms} ms."
                if success else
                f"Exited {result.returncode} in {elapsed_ms} ms."
            ),
            "error": (
                None if success else
                (result.stderr.strip() or f"Non-zero exit: {result.returncode}")
            ),
        }

    # ── Venv management ───────────────────────────────────────────────────────

    def _ensure_venv(self, venv_dir: Path) -> Path:
        """Create venv if missing. Returns path to pip executable."""
        if not venv_dir.exists():
            try:
                venv.create(str(venv_dir), with_pip=True, clear=False)
            except Exception as exc:
                raise VenvError(
                    f"Failed to create venv at {venv_dir}: {exc}"
                ) from exc
        return self._get_pip(venv_dir)

    def _ensure_python(self, venv_dir: Path) -> Path:
        """Create venv if missing. Returns path to python executable."""
        if not venv_dir.exists():
            try:
                venv.create(str(venv_dir), with_pip=True, clear=False)
            except Exception as exc:
                raise VenvError(
                    f"Failed to create venv at {venv_dir}: {exc}"
                ) from exc
        return self._get_python(venv_dir)

    @staticmethod
    def _get_pip(venv_dir: Path) -> Path:
        for candidate in (
            "bin/pip", "bin/pip3",
            "Scripts/pip.exe", "Scripts/pip3.exe",
        ):
            p = venv_dir / candidate
            if p.exists():
                return p
        raise VenvError(f"pip not found in venv: {venv_dir}")

    @staticmethod
    def _get_python(venv_dir: Path) -> Path:
        for candidate in (
            "bin/python", "bin/python3",
            "Scripts/python.exe",
        ):
            p = venv_dir / candidate
            if p.exists():
                return p
        raise VenvError(f"python not found in venv: {venv_dir}")

    # ── Run log ───────────────────────────────────────────────────────────────

    def _append_log(
        self,
        pid: str,
        cmd: list[str],
        result: subprocess.CompletedProcess,
        elapsed_ms: int,
    ) -> None:
        """
        Append one entry to run.log.
        Rotates the file when it exceeds MAX_LOG_LINES to prevent
        unbounded disk growth.
        """
        log_path = self.base_dir / pid / "run.log"
        try:
            ts   = datetime.now().isoformat(timespec="seconds")
            line = (
                f"[{ts}] exit={result.returncode} ms={elapsed_ms} "
                f"cmd={' '.join(cmd)}\n"
            )
            stderr_line = (
                ("  stderr: " + result.stderr.strip()[:200] + "\n")
                if result.stderr.strip() else ""
            )

            # Rotate if the log has grown too large
            if log_path.exists():
                lines = log_path.read_text(
                    encoding="utf-8", errors="replace"
                ).splitlines(keepends=True)
                if len(lines) >= MAX_LOG_LINES:
                    keep = lines[MAX_LOG_LINES // 2:]
                    log_path.write_text("".join(keep), encoding="utf-8")

            with log_path.open("a", encoding="utf-8") as f:
                f.write(line)
                if stderr_line:
                    f.write(stderr_line)

        except OSError as exc:
            logger.warning(
                "Could not write run.log for project %r: %s", pid, exc
            )

    # ── Error helper ──────────────────────────────────────────────────────────

    @staticmethod
    def _err(pid: str, action: str, message: str) -> dict:
        return {
            "success": False,
            "action":  action,
            "project": pid,
            "message": message,
            "error":   message,
        }
```
</file>

---

## File: `../Khwarizm/tools/registry.py`
**Last Modified:** `2026-05-22 18:33` | **Size:** `0.62 KB`

<file path="../Khwarizm/tools/registry.py" type="python">
```python
from tools.basetool import BaseTool

class ToolRegistry:
    def __init__(self):
        self.__tools = {}

    def register(self, tool: BaseTool):
        self.__tools[tool.name] = tool
        print(f"Registered tool: {tool.name}")

    def get_tool(self, name: str) -> BaseTool:
        return self.__tools.get(name)

    def get_descriptions(self) -> str:
        """Returns full XML schemas for all tools"""
        schemas = []
        for tool in self.__tools.values():
            schemas.append(tool.get_schema())
        return "\n\n".join(schemas)

    def list_tools(self) -> list:
        return list(self.__tools.keys())
```
</file>

---

## File: `../Khwarizm/tools/s.txt`
**Last Modified:** `2026-05-25 07:42` | **Size:** `0.09 KB`

<file path="../Khwarizm/tools/s.txt" type="text">
```text
git config --global user.email "faseuu@gmail.com"
git config --global user.name "Faseeu"
```
</file>

---

## File: `../Khwarizm/utils/chat_ui.py`
**Last Modified:** `2026-05-19 11:41` | **Size:** `0.42 KB`

<file path="../Khwarizm/utils/chat_ui.py" type="python">
```python
# utils/chat_ui.py

def start_terminal_chat(agent):
    print("=" * 50)
    print(f"Starting chat with {agent.name}. Type 'exit' to quit.")
    print("=" * 50)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation...")
            break
            
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
```
</file>

---

## File: `../Khwarizm/main.py`
**Last Modified:** `2026-05-26 13:04` | **Size:** `4.34 KB`

<file path="../Khwarizm/main.py" type="python">
```python
# from llms.groqclient import GroqClient
# from llms.geminiclient import GeminiClient
# from tools.calculator import CalculatorTool
# from tools.filewriter import FileWriterTool
# from tools.filereader import FileReaderTool
# from agents.baseagent import BaseAgent
from utils.chat_ui import start_terminal_chat

# if __name__ == "__main__":

#     # 1. Create the LLM
#     groq_llm = GroqClient(model="llama-3.3-70b-versatile")


#     # 2. Create the Agent with tools
#     agent = BaseAgent(
#         name="SmartBot",
#         llm=gemini_llm,
#         system_prompt= """
#         Be a helpful assistant who always always uses the tools given to him. 
#         Never do a task without using the apppropriate tools. 
#         You have all the appropriate tools at your disposal to perfrom the tasks i ask of you.
#         Always try to reason everything yourself.
#         Try your best not to bother user.
#         Create plans to perform the tasks.
#         Also at the end of each task try to double check if it was properly fullfilled or not. 
#         """,
#         tools=[CalculatorTool(),FileReaderTool(),FileWriterTool()]
#     )

#     print("\n" + "=" * 40)
#     print("TEST 2: Tool needed")
#     print("=" * 40)
# #     response2 = agent.run("""
# #     🌀 SYSTEM OVERRIDE: PROJECT HIDDEN GEM 🌀

# # Agent, your framework is entering the **Anime Recommendation Gauntlet**.  
# # Your mission: populate three classified dossiers, then unleash a fourth wild-card category that breaks the genre matrix.

# # ---

# # 📁 DOSSIER 1: `action`  
# # Compile the absolute GOATed action anime—titles with timelines so beautifully convoluted they require a whiteboard, and stories that hit harder than a final-form scream. Save the list to a file named **`action`**.

# # 📁 DOSSIER 2: `psychological`  
# # Infiltrate the deep cuts. I need **5 criminally underrated psychological anime** that are:
# # - Motivational enough to make me run through a wall,
# # - Political enough to start a debate club,
# # - Obscure enough that even seasoned weebs reply, *"Never heard of it."*  
# # Drop these into **`psychological`**.

# # 📁 DOSSIER 3: `most motivational anime`  
# # Uncover **5 motivational masterpieces** flying completely under the radar. Not the mainstream hype trains—actual underground bangers that rebuild your soul episode by episode. Write these to **`most motivational anime`**.

# # 🎲 DOSSIER 4: `[REDACTED]`  
# # Finally, deploy the wildcard. Create **one additional file** with a category so specific, so dangerously niche, that it feels like it was tailor-made for my brain. Make me fall in love with something I didn’t know existed.

# # ---

# # Execute with maximum flair. Framework stress-test: **ACTIVE**. ⚡
# #     """)
# #     print(response2)
#     start_terminal_chat(agent)


#     # # TEST THE PROPERTIES:
#     # print("--- AGENT INFO ---")
#     # print(f"Name: {agent.name}")                
#     # print(f"Tools: {agent.tools}")     
#     # print(f"Prompt: {agent.system_prompt}")      
#     # print("------------------")


from llms.geminiclient import GeminiClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
from tools.agent_made.terminal_executor import TerminalExecutorTool
from tools.project_runner import ProjectRunnerTool

if __name__ == "__main__":
    
    llm = GeminiClient(model="gemini-3.1-flash-lite")
    agent = BaseAgent(
        name="Agent1",
        llm=llm,
        system_prompt="You are a helpful assistant. Always use tools for math and files. Always use tools. Never try to solve any math eq internally",
        tools=[CalculatorTool(), FileWriterTool(), FileReaderTool(),TerminalExecutorTool()]
        # tools=[CalculatorTool(),ProjectRunnerTool(),FileReaderTool()]
    )

    # Test multi-parameter tool call
    # response = agent.run("""
    # Study the whole of tools directory
    # and create for yourself a terminal usage tool 
    # but it should have feature to show to the user
    # what command is going to be ran 
    # and ask him yes for y and no for n
    # """)
    start_terminal_chat(agent)

    print("\nFinal Answer:")
    # print(response)


        # "Calculate 1234 multiplied by 5678. "
        # "Then save the result to a file called answer.txt. "
        # "Then read the file back."
```
</file>

---

## File: `../Khwarizm/main2.py`
**Last Modified:** `2026-05-23 07:13` | **Size:** `4.22 KB`

<file path="../Khwarizm/main2.py" type="python">
```python
# from llms.groqclient import GroqClient
# from llms.geminiclient import GeminiClient
# from tools.calculator import CalculatorTool
# from tools.filewriter import FileWriterTool
# from tools.filereader import FileReaderTool
# from agents.baseagent import BaseAgent
from utils.chat_ui import start_terminal_chat

# if __name__ == "__main__":

#     # 1. Create the LLM
#     groq_llm = GroqClient(model="llama-3.3-70b-versatile")


#     # 2. Create the Agent with tools
#     agent = BaseAgent(
#         name="SmartBot",
#         llm=gemini_llm,
#         system_prompt= """
#         Be a helpful assistant who always always uses the tools given to him. 
#         Never do a task without using the apppropriate tools. 
#         You have all the appropriate tools at your disposal to perfrom the tasks i ask of you.
#         Always try to reason everything yourself.
#         Try your best not to bother user.
#         Create plans to perform the tasks.
#         Also at the end of each task try to double check if it was properly fullfilled or not. 
#         """,
#         tools=[CalculatorTool(),FileReaderTool(),FileWriterTool()]
#     )

#     print("\n" + "=" * 40)
#     print("TEST 2: Tool needed")
#     print("=" * 40)
# #     response2 = agent.run("""
# #     🌀 SYSTEM OVERRIDE: PROJECT HIDDEN GEM 🌀

# # Agent, your framework is entering the **Anime Recommendation Gauntlet**.  
# # Your mission: populate three classified dossiers, then unleash a fourth wild-card category that breaks the genre matrix.

# # ---

# # 📁 DOSSIER 1: `action`  
# # Compile the absolute GOATed action anime—titles with timelines so beautifully convoluted they require a whiteboard, and stories that hit harder than a final-form scream. Save the list to a file named **`action`**.

# # 📁 DOSSIER 2: `psychological`  
# # Infiltrate the deep cuts. I need **5 criminally underrated psychological anime** that are:
# # - Motivational enough to make me run through a wall,
# # - Political enough to start a debate club,
# # - Obscure enough that even seasoned weebs reply, *"Never heard of it."*  
# # Drop these into **`psychological`**.

# # 📁 DOSSIER 3: `most motivational anime`  
# # Uncover **5 motivational masterpieces** flying completely under the radar. Not the mainstream hype trains—actual underground bangers that rebuild your soul episode by episode. Write these to **`most motivational anime`**.

# # 🎲 DOSSIER 4: `[REDACTED]`  
# # Finally, deploy the wildcard. Create **one additional file** with a category so specific, so dangerously niche, that it feels like it was tailor-made for my brain. Make me fall in love with something I didn’t know existed.

# # ---

# # Execute with maximum flair. Framework stress-test: **ACTIVE**. ⚡
# #     """)
# #     print(response2)
#     start_terminal_chat(agent)


#     # # TEST THE PROPERTIES:
#     # print("--- AGENT INFO ---")
#     # print(f"Name: {agent.name}")                
#     # print(f"Tools: {agent.tools}")     
#     # print(f"Prompt: {agent.system_prompt}")      
#     # print("------------------")


from llms.geminiclient import GeminiClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
from tools.agent_made.terminal_executor import TerminalExecutorTool


if __name__ == "__main__":
    
    llm = GeminiClient(model="gemini-3.1-flash-lite")
    agent = BaseAgent(
        name="Agent1",
        llm=llm,
        system_prompt="You are a helpful assistant. Always use tools for math and files. Always use tools. Never try to solve any math eq internally",
        tools=[CalculatorTool(), FileWriterTool(), FileReaderTool(),TerminalExecutorTool()]
    )

    # Test multi-parameter tool call
    # response = agent.run("""
    # Study the whole of tools directory
    # and create for yourself a terminal usage tool 
    # but it should have feature to show to the user
    # what command is going to be ran 
    # and ask him yes for y and no for n
    # """)
    start_terminal_chat(agent)

    print("\nFinal Answer:")
    # print(response)


        # "Calculate 1234 multiplied by 5678. "
        # "Then save the result to a file called answer.txt. "
        # "Then read the file back."
```
</file>

---

## File: `../Khwarizm/plan.md`
**Last Modified:** `2026-05-26 13:05` | **Size:** `1.06 KB`

<file path="../Khwarizm/plan.md" type="markdown">
```markdown
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
```
</file>

---

## File: `../Khwarizm/README.md`
**Last Modified:** `2026-05-21 09:24` | **Size:** `22.29 KB`

<file path="../Khwarizm/README.md" type="markdown">
```markdown
# Khwarizm - AI Agent Framework

## Overview
Khwarizm is a minimalist, production-inspired AI Agent Framework built entirely from scratch using core Object-Oriented Programming principles in Python. It wraps stateless Large Language Models (LLMs) into intelligent, autonomous agents capable of persistent memory, tool use, and multi-step reasoning.

---

## The Problem We Solve
Large Language Models are stateless. Every time you call them, they forget everything. They cannot:
- Remember previous conversations
- Take actions in the real world
- Reason through multi-step problems
- Use external tools like calculators or file systems

**Khwarizm solves all of these problems.**

---

## Architecture Overview

```
                    USER INPUT
                         │
                         ▼
┌────────────────────────────────────────────┐
│                 BaseAgent                  │
│                                            │
│  ┌──────────┐        ┌─────────────────┐  │
│  │  Config  │        │    BaseLLM      │  │
│  │  name    │        │  GroqClient     │  │
│  │  prompt  │        │  GeminiClient   │  │
│  │  tokens  │        └─────────────────┘  │
│  └──────────┘                             │
│                                            │
│  ┌──────────┐        ┌─────────────────┐  │
│  │ToolRegistr│        │    Memory       │  │
│  │Calculator │        │  ShortTerm      │  │
│  │FileWriter │        │  LongTerm       │  │
│  │FileReader │        └─────────────────┘  │
│  └──────────┘                             │
└────────────────────────────────────────────┘
                         │
                         ▼
                    FINAL ANSWER
```

---

## Project Structure

```
khwarizm/
├── main.py                    # Entry point and demos
├── agents/
│   ├── baseagent.py           # Core agent logic and agentic loop
│   └── config.py              # Agent configuration dataclass
├── clients/
│   ├── basellm.py             # Abstract LLM contract
│   ├── groqclient.py          # Groq implementation
│   └── geminiclient.py        # Gemini implementation
├── tools/
│   ├── basetool.py            # Abstract tool contract
│   ├── registry.py            # Auto tool registration system
│   ├── calculator.py          # Math operations tool
│   ├── filewriter.py          # File writing tool
│   └── filereader.py          # File reading tool
├── memory/
│   ├── basememory.py          # Abstract memory contract
│   ├── stm.py                 # Short term (RAM) memory
│   └── ltm.py                 # Long term (JSON file) memory
└── utils/
    └── chat_ui.py             # Reusable terminal chat interface
```

---

## OOP Concepts Applied

### 1. Abstraction
Three Abstract Base Classes define the contracts of the framework:
- `BaseLLM` → Any LLM provider must implement `generate()`
- `BaseTool` → Any tool must implement `run()`
- `BaseMemory` → Any memory type must implement `add_entry()`, `get_context()`, `clear()`

```python
from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        pass
```

### 2. Encapsulation
Private attributes hide internal data from outside access:
```python
class ToolRegistry:
    def __init__(self):
        self.__tools = {}  # Private! Cannot be accessed from outside
```

### 3. Inheritance
Concrete classes inherit from abstract base classes:
```python
class GroqClient(BaseLLM):      # Inherits LLM contract
class CalculatorTool(BaseTool): # Inherits Tool contract
class ShortTermMemory(BaseMemory): # Inherits Memory contract
```

### 4. Composition
`BaseAgent` is built FROM other objects rather than inheriting from them:
```python
class BaseAgent:
    def __init__(self, ...):
        self.llm = llm              # HAS A LLM
        self.registry = ToolRegistry()  # HAS A Registry
        self.__short_term = ShortTermMemory()  # HAS A Memory
        self.__long_term = LongTermMemory()    # HAS A Memory
```

### 5. Polymorphism
The same `BaseAgent` works identically with different LLM providers:
```python
groq_agent = BaseAgent(llm=GroqClient())    # Works with Groq
gemini_agent = BaseAgent(llm=GeminiClient()) # Works with Gemini
# BaseAgent code does not change. Only the LLM object changes.
```

### 6. Exception Handling
All critical operations are wrapped in try/except blocks:
```python
def generate(self, system_prompt: str, user_prompt: str) -> str:
    try:
        response = self.client.chat.completions.create(...)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: LLM API failed: {str(e)}"
```

### 7. Properties (Advanced Encapsulation)
Clean public access to private internal data:
```python
@property
def name(self) -> str:
    return self.config.name  # User types agent.name, not agent.config.name
```

---

## The Agentic Loop (Core Algorithm)

The heart of Khwarizm is the **ReAct (Reason + Act) Loop** inside `BaseAgent.run()`.

```
User Input
    │
    ▼
Save to Memory (STM + LTM)
    │
    ▼
┌─────────────────────────────┐
│         WHILE LOOP          │
│                             │
│  Build Context from Memory  │
│           │                 │
│           ▼                 │
│    Send to LLM              │
│           │                 │
│           ▼                 │
│  Does response have TOOL:?  │
│                             │
│  YES              NO        │
│   │                │        │
│   ▼                ▼        │
│ Run Tool      Save to       │
│   │           Memory        │
│   ▼                │        │
│ Save result        ▼        │
│ to Memory     Return        │
│   │           Answer        │
│   ▼                         │
│ Continue Loop               │
└─────────────────────────────┘
    │
    ▼
Max Iterations Reached?
    │
    ▼
Return Error Message
```

---

## Memory System

Khwarizm has two types of memory working simultaneously:

| | Short Term Memory | Long Term Memory |
|--|------------------|-----------------|
| **Storage** | Python List (RAM) | JSON File (Disk) |
| **Lives** | Current session only | Forever |
| **Dies when** | Program closes | Never |
| **Analogy** | Human working memory | Human long term memory |

---

## Key Concepts Explained

---

### 1. Config and the `@dataclass` Decorator

#### What is a `@dataclass`?
In Python, a normal class requires you to write a lot of 
repetitive boilerplate code just to store data:

```python
# WITHOUT dataclass (repetitive and messy)
class Config:
    def __init__(self, name, description, system_prompt, model, max_tokens):
        self.name = name
        self.description = description
        self.system_prompt = system_prompt
        self.model = model
        self.max_tokens = max_tokens
```

The `@dataclass` decorator eliminates all of this repetition. 
You just declare the fields and their types, 
and Python writes the `__init__` for you automatically:

```python
# WITH dataclass (clean and professional)
@dataclass
class Config:
    name: str
    description: str
    system_prompt: str = "You are a helpful AI assistant"
    model: str = "llama3-8b-8192"
    max_tokens: int = 1000
    max_iterations: int = 10
```

#### What does `Config` actually do?
`Config` is a pure data container. It has one job 
and one job only: hold the settings of an agent.

It does NOT:
- Run any logic
- Call any APIs
- Make any decisions

It just holds values. This follows the 
**Single Responsibility Principle** of OOP.

#### What is `__post_init__`?
`__post_init__` is a special method that `@dataclass` 
calls automatically right after the object is created.
We use it to validate the data:

```python
def __post_init__(self):
    if not self.name:
        raise ValueError("Agent must have a name")
    if self.max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0")
    if self.max_iterations <= 0:
        raise ValueError("max_iterations must be greater than 0")
```

**Analogy:** Think of `Config` as a job application form.
`__post_init__` is the HR officer who checks the form
for missing or invalid fields before accepting it.

#### Default Values
Fields with `=` have default values. 
Fields without `=` are mandatory.

**Rule:** Mandatory fields ALWAYS come before fields with defaults.
This is a Python rule. Breaking it causes a `TypeError`.

```python
@dataclass
class Config:
    # MANDATORY FIRST (no defaults)
    name: str
    description: str
    
    # DEFAULTS SECOND
    system_prompt: str = "You are a helpful AI assistant"
    model: str = "llama3-8b-8192"
    max_tokens: int = 1000
    max_iterations: int = 10
```

---

### 2. BaseAgent: Every Method Explained

#### `__init__()` - The Setup Method
This is the constructor. It runs exactly once when 
the agent is created. It does 4 things in order:

**Step 1:** Takes the LLM and saves it.
```python
self.llm = llm
```

**Step 2:** Creates a ToolRegistry and automatically 
registers every tool the user passed in.
```python
self.registry = ToolRegistry()
tools = tools or []      # Safe default (avoids mutable default arg bug)
for tool in tools:
    self.registry.register(tool)
```

**Step 3:** If tools exist, injects their descriptions 
into the system prompt so the LLM knows about them.
```python
if tools:
    tool_info = self.registry.get_descriptions()
    system_prompt = f"{system_prompt}\n\nYou have access to:\n{tool_info}"
```

**Step 4:** Creates the Config and both Memory objects.
```python
self.config = Config(name=name, ...)
self.__short_term = ShortTermMemory()
self.__long_term = LongTermMemory(agent_name=name)
```

---

#### `run(user_input)` - The Agentic Loop
This is the most important method in the entire framework.
It is the **ReAct (Reason + Act)** algorithm.

```
STEP 1: Save user input to both memories

STEP 2: Start the while loop (max_iterations times)

STEP 3: Build the full context from both memories
        (This is what the LLM reads to know what happened so far)

STEP 4: Send (system_prompt + full_context) to LLM

STEP 5: Strip <think> tags if present 
        (Some reasoning models output their thoughts)

STEP 6: Check if LLM response contains "TOOL:"
        
        YES: Call __handle_tool_call()
             Save action and result to short term memory
             CONTINUE the loop (go back to Step 3)
        
        NO:  This is the final answer!
             Save to both memories
             RETURN the response to the user

STEP 7: If loop finishes without answer
        Return max iterations error message
```

**Why a loop?**
Because complex tasks require multiple steps. 
A single LLM call can only do one thing. 
The loop allows the agent to:
- Use tool 1
- Read the result
- Use tool 2
- Read the result
- Give final answer

**Why does memory grow each loop?**
Because the LLM has no memory between API calls.
We manually feed it the entire history every loop
so it knows what has already been done.

**Analogy:** Imagine a surgeon who gets amnesia 
between each step of an operation. 
The nurse reads the surgery log out loud 
before every step so the surgeon knows where they are.
The memory is that surgery log.

---

#### `__handle_tool_call(response)` - The Tool Parser
This private method is called when the LLM decides 
it needs a tool. It does 5 things:

**Step 1:** Split the LLM response into lines
```python
lines = response.strip().split("\n")
```

**Step 2:** Loop through lines to find TOOL: and INPUT:
```python
for line in lines:
    if line.startswith("TOOL:") and not tool_name:
        tool_name = line.replace("TOOL:", "").strip()
    elif line.startswith("INPUT:") and not tool_input:
        tool_input = line.replace("INPUT:", "").strip()
    if tool_name and tool_input:
        break  # Stop after finding the FIRST tool call only
```

**Why `break`?**
Smart LLMs sometimes try to call multiple tools 
in one response. We force ONE tool per loop iteration
so each result gets properly saved to memory 
before the next decision is made.

**Step 3:** Ask the Registry for the tool by name
```python
tool = self.registry.get_tool(tool_name)
```

**Step 4:** If tool not found, return a clean error
```python
if not tool:
    return f"Error: Unknown tool '{tool_name}'"
```

**Step 5:** Run the tool and return the result string
```python
result = tool.run(tool_input)
return f"Tool '{tool_name}' returned: {result}"
```

This result string goes back into the loop,
gets saved to memory, and the LLM reads it 
on the next iteration.

---

#### `name` property - Clean Public Access
```python
@property
def name(self) -> str:
    return self.config.name
```

Without this, users would write: `agent.config.name`
With this, users write: `agent.name`

This follows the **Law of Demeter**: 
Objects should not reach deep into other objects.

It is also **read-only**. There is no setter.
So `agent.name = "Hacker"` throws an AttributeError.
The name is protected from accidental modification.

---

#### `available_tools` property
```python
@property
def available_tools(self) -> list:
    return self.registry.list_tools()
```

Returns a clean list of tool names without 
exposing the internal Registry object.

---

#### `clear_memory()` - The Reset Button
```python
def clear_memory(self):
    self.__short_term.clear()
    self.__long_term.clear()
```

Wipes both memories. The agent starts fresh.
Notice how `BaseAgent` delegates the actual 
clearing to each memory object.
This is the **Single Responsibility Principle**.
The agent manages. The memory objects do the work.

---

### 3. The Tool System: How It All Connects

#### Why does `BaseTool` use class variables for `name` and `description`?

```python
class CalculatorTool(BaseTool):
    name = "calculator"           # Class variable
    description = "Does math"    # Class variable
```

Because every instance of `CalculatorTool` will 
always have the same name and description.
There is no reason for these to be different 
per object. Class variables are shared across 
all instances. This saves memory and makes 
the code cleaner.

#### Why does `ToolRegistry` use a dictionary?

```python
self.__tools = {}  # Dictionary, not a list!
```

A list lookup is O(n): check index 0, index 1, 
index 2... until found. With 1000 tools: 1000 checks.

A dictionary lookup is O(1): hash the key, 
go directly to the location. Always 1 step.
No matter if you have 1 tool or 1,000,000 tools.

#### The Auto Registration Flow

```
User passes: tools=[CalculatorTool(), FileWriterTool()]
                    │
                    ▼
BaseAgent loops through the list
                    │
                    ▼
registry.register(CalculatorTool())
registry.register(FileWriterTool())
                    │
                    ▼
Registry stores them:
{
    "calculator": CalculatorTool(),
    "file_writer": FileWriterTool()
}
                    │
                    ▼
get_descriptions() builds:
"- calculator: Does math
 - file_writer: Writes files"
                    │
                    ▼
Injected into system prompt
                    │
                    ▼
LLM now knows what tools exist
```

---

### 4. The Memory System: Why Two Types?

#### The Computer Analogy
Your computer has two types of storage:
- **RAM:** Fast, temporary. Dies when you shut down.
- **Hard Drive:** Slow, permanent. Survives shutdown.

Our memory system mirrors this exactly:

| | ShortTermMemory | LongTermMemory |
|--|----------------|----------------|
| Storage | Python list (RAM) | JSON file (Disk) |
| Speed | Instant | Slightly slower |
| Survives restart | ❌ No | ✅ Yes |
| Used for | Current session | All past sessions |

#### How They Work Together in the Loop

```python
# At the start of run():
self.__short_term.add_entry(role="user", content=user_input)
self.__long_term.add_entry(role="user", content=user_input)

# Inside the loop:
long_term_context = self.__long_term.get_context()
short_term_context = self.__short_term.get_context()

full_context = (
    f"Past Conversations:\n{long_term_context}\n\n"
    f"Current Session:\n{short_term_context}"
)
```

The LLM receives BOTH contexts combined.
It knows what happened in previous sessions 
AND what happened earlier in this session.

---

### 5. Polymorphism: The Most Powerful OOP Concept in This Framework

Polymorphism means "many forms."
The same interface works differently 
depending on the object behind it.

```python
# Both follow the BaseLLM contract
groq = GroqClient()     # Talks to Groq servers in USA
gemini = GeminiClient() # Talks to Google servers

# BaseAgent does not care which one it gets
agent1 = BaseAgent(llm=groq)
agent2 = BaseAgent(llm=gemini)

# Internally, BaseAgent just calls:
response = self.llm.generate(system_prompt, user_prompt)

# For agent1: This hits Groq's API
# For agent2: This hits Google's API
# The BaseAgent code is IDENTICAL for both
```

This is why Abstract Base Classes exist.
`BaseLLM` guarantees that whatever object 
is passed in, it WILL have a `generate()` method.
The agent never has to check. It just calls it.

---

### 6. Why Composition Over Inheritance for BaseAgent?

The question is: should `BaseAgent` INHERIT from 
`BaseLLM`, or should it CONTAIN a `BaseLLM`?

**Wrong (Inheritance):**
```python
class BaseAgent(BaseLLM):  # Agent IS A LLM? No!
    pass
```

**Right (Composition):**
```python
class BaseAgent:
    def __init__(self, llm: BaseLLM):
        self.llm = llm  # Agent HAS A LLM. Yes!
```

An agent is NOT a type of LLM.
An agent USES a LLM.
An agent USES memory.
An agent USES tools.

Inheritance models "IS A" relationships.
Composition models "HAS A" relationships.

Using the wrong one here would mean:
- `BaseAgent` could only ever BE one type of LLM
- You could never swap Groq for Gemini
- The entire framework would be tightly coupled

Composition gives us flexibility, 
loose coupling, and the ability to 
swap any component at any time.


## Tool System

Tools give the agent hands. Without tools, the agent can only talk. With tools, it can act.

### How Tools Work:
1. User passes tools into `BaseAgent` as a list
2. `BaseAgent` automatically registers them in `ToolRegistry`
3. Tool descriptions are injected into the system prompt
4. LLM decides which tool to use and responds in a special format
5. Agent parses the response, finds the tool, runs it
6. Result is saved to memory and the loop continues

### Tool Call Format:
```
TOOL: calculator
INPUT: 150*4
```

---

## Multi-Agent Workflow

Because `BaseAgent.run()` takes text in and returns text out, agents can be chained together using pure Python:

```python
# Agent 1 writes a poem
writer_output = writer_agent.run("Write a poem about AI")

# Agent 2 critiques what Agent 1 wrote
critic_output = critic_agent.run(writer_output)
```

No special framework needed. Just Python variables.

---

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/faseeu/khwarizm.git
cd khwarizm
```

### 2. Install dependencies
```bash
pip install groq google-generativeai
```

### 3. Set API Keys
```bash
# Mac/Linux
export GROQ_API_KEY="your_groq_key_here"
export GEMINI_API_KEY="your_gemini_key_here"

# Windows
set GROQ_API_KEY="your_groq_key_here"
set GEMINI_API_KEY="your_gemini_key_here"
```

### 4. Run the demo
```bash
python main.py
```

---

## Quick Start

```python
from clients.groqclient import GroqClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from baseagent import BaseAgent

# 1. Create the LLM
llm = GroqClient(model="llama3-8b-8192")

# 2. Create the Agent
agent = BaseAgent(
    name="MyAgent",
    llm=llm,
    system_prompt="You are a helpful assistant.",
    tools=[CalculatorTool(), FileWriterTool()]
)

# 3. Run it
response = agent.run("Calculate 150 times 4 and save it to result.txt")
print(response)
```

---

## Live Demo Output

```
Starting: MyAgent
Creating a new instance...
  [Loop 1/10] Agent is thinking...
  -> Using tool: calculator | Input: 150*4
  [Loop 2/10] Agent is thinking...
  -> Using tool: file_writer | Input: result.txt|600
  [Loop 3/10] Agent is thinking...

The result of 150 multiplied by 4 is 600.
It has been saved to result.txt successfully!
```

---

## Key Design Decisions

| Decision | Reason |
|----------|--------|
| Abstract Base Classes | Forces correct implementation. No silent bugs. |
| Composition over Inheritance for Agent | Agent HAS a brain. It is not A TYPE of brain. |
| Dictionary in Registry | O(1) lookup speed vs O(n) for lists |
| Two Memory Types | Short term for context. Long term for persistence. |
| Scratchpad replaced by Memory | Cleaner, structured, reusable across sessions |
| Tools injected via list | User never manually touches ToolRegistry |
| `frozen=False` on Config | Allows post-init flexibility |
| Private `__tools` in Registry | Enforces access only through clean public methods |

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Core language |
| Groq SDK | LLM API (Llama3, Mixtral models) |
| Google Generative AI SDK | LLM API (Gemini models) |
| `dataclasses` | Clean config management |
| `abc` module | Abstract Base Classes |
| `json` module | Long term memory persistence |
| `os` module | File path management |

---

## What We Would Add Next

1. **SupervisorAgent** - An agent that manages other agents and routes tasks between them
2. **Streamlit Web UI** - A browser-based chat interface for the framework
3. **WebSearchTool** - Live internet access via DuckDuckGo or Wikipedia API
4. **Python Logging** - Replace print statements with proper log levels
5. **Memory Summarization** - Compress long term memory using LLM summaries to prevent context overflow

---

## Authors
Built by Faseeh ur Rehman and Huzaifa Imran as part of an OOP and AI Agents learning project.
```
</file>

---

## File: `../Khwarizm/requirements.txt`
**Last Modified:** `2026-05-26 07:28` | **Size:** `0.05 KB`

<file path="../Khwarizm/requirements.txt" type="text">
```text
groq
google-generativeai
python-minifier 
minify-html
```
</file>

---

## File: `../Khwarizm/workflow.py`
**Last Modified:** `2026-05-23 06:18` | **Size:** `1.13 KB`

<file path="../Khwarizm/workflow.py" type="python">
```python
from llms.geminiclient import GeminiClient
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent

llm = GeminiClient(model="gemini-3.1-flash-lite")

# Agent 1: The Writer
writer = BaseAgent(
    name="Writer",
    llm=llm,
    system_prompt="You are a creative writer. Write what the user asks and nothing else. Also use tools",
    tools=[FileWriterTool()]
)

# Agent 2: The Critic
critic = BaseAgent(
    name="Critic",
    llm=llm,
    system_prompt="You are a harsh critic. Read what is given to you and give brutal feedback. Also use tools",
    tools=[FileReaderTool()]
)

poet= BaseAgent(
    name="Poet",
    llm=llm,
    system_prompt="Write a poem in a file",
    tools=[FileReaderTool()]
)
print("Step 1: Writer writes a poem...")
writer_output = writer.run("Write a short poem about AI and save it to poem.txt")
poetOutput = poet.run("Gimme the poems")
print("\nStep 2: Critic reviews the poem...")
critic_output = critic.run("Read poem.txt and another poem file and crush their dreams and give me harsh feedback on it")

print("\nCritic's Verdict:")
print(critic_output)
```
</file>

---

## File: `../OOP/class/asignmnts/bankassign.py`
**Last Modified:** `2026-05-13 08:07` | **Size:** `0.00 KB`

<file path="../OOP/class/asignmnts/bankassign.py" type="python">
```python

```
</file>

---

## File: `../OOP/class/asignmnts/s-a-dict.py`
**Last Modified:** `2026-03-24 08:06` | **Size:** `0.98 KB`

<file path="../OOP/class/asignmnts/s-a-dict.py" type="python">
```python
class MyDict:

    def __init__(self,mydict=None):
        
        self.__mydict= {} if mydict == None else mydict


    def __str__(self):
        
        return "\n".join(f"{key} : {value}" for key,value in self.__mydict.items())
        
    def __getitem__(self,key):
        return self.__mydict[key]
    
    def __setitem__(self, key, value):
        self.__mydict[key] = value
    
    def __delitem__(self, key):
        del self.__mydict[key]
    
    def __len__(self):
        return len(self.__mydict)
    
    def __contains__(self, item):
        return item in self.__mydict
    
    def __iter__(self):
        for key in self.__mydict:
            yield key

ex_dic = {
    "name":"Ali",
    "class":"Unknown",
    "profession": "SWE",
    "criminalMetric":6,
    "age": 25,
    "hobby": "doomscrolling"

}
d1 = MyDict(ex_dic)

print("fav_dish" in d1)
print(len(d1))
for i in d1:
    print(i)
print()

del d1["class"]
print(d1["class"])
print(d1["age"])
d1["age"] = 36
print(d1["age"])
```
</file>

---

## File: `../OOP/class/asignmnts/s-a-set.py`
**Last Modified:** `2026-03-24 07:01` | **Size:** `0.75 KB`

<file path="../OOP/class/asignmnts/s-a-set.py" type="python">
```python

class MySet:

    def __init__(self,myset=None):
        if myset==None:
            self.__myset=set()
        else:
            self.__myset=set(myset)



    def __str__(self):
        return f"Set: {self.__myset}"
    

    
    def __add__(self,other):
        return MySet(self.__myset.union(other.__myset))
    

    def __sub__(self, other):
        return MySet(self.__myset.difference(other.__myset))
    

    def __and__(self, other):
        return MySet(self.__myset.intersection(other.__myset))
    

    def __contains__(self,x):
        return x in self.__myset
            
    
    def __len__(self):
        return len(self.__myset)

s1= MySet([1,2,3,4]) 
s2= MySet([12,5,8,4]) 

print(s1 + s2)

print(s1 - s2)

print(s1 & s2)

print(len(s1))
```
</file>

---

## File: `../OOP/class/asignmnts/sessional-assinmnt-stack.py`
**Last Modified:** `2026-05-13 08:06` | **Size:** `0.89 KB`

<file path="../OOP/class/asignmnts/sessional-assinmnt-stack.py" type="python">
```python

class MyStack:
    
    def __init__(self,stack=None):
        if stack==None:
            self.__stack=[]
        else:
            self.__stack = stack
    def getStack(self):
        return self.__stack
    
    def pop(self):
        self.__stack.pop()
        
    def push(self, v):
        self.__stack.append(v)

    
    def __len__(self):
        return len(self.__stack)
    
    def __str__(self):
    
        return f"This Stack contains the following items:\n {self.__stack}"

    def __iter__(self):
        for item in self.__stack:
            yield item

#this function overloads the logic for "in" operator
    def __contains__(self,x):
        return x in self.__stack
            

    
s1 = MyStack(['dbs',2,3])
print(s1)

s1.push(6) 
s1.push(9)
s1.push(2)
s1.pop()

print(s1)              

print('Length of stack: ',len(s1))

print(2 in s1)

for i in s1:
    print(i,end=" ")
print()
```
</file>

---

## File: `../OOP/class/class4-3-26.py`
**Last Modified:** `2026-03-04 08:53` | **Size:** `1.03 KB`

<file path="../OOP/class/class4-3-26.py" type="python">
```python
class Distance:
    def __init__(self,feet,inches):
        self.__feet=feet
        self.__inches=inches
        if(self.__inches >= 12):
            self.__feet+=(self.__inches//12)
            self.__inches=(self.__inches%12)

    def __str__(self):
        return f"Feets: {self.__feet}, Inches: {self.__inches}"
    def to_inches(self):
        return self.__feet*12 + self.__inches
    def __lt__(self,other):
        return self.to_inches() > other.to_inches()
    def __sub__(self, other):
        nfeet= self.__feet - other.__feet
        ninch= self.__inches-other.__inches
        if ninch <= 0:
            nfeet-=1
            ninch+=12
        return Distance(nfeet,ninch)
    def __add__(self, other):
        nfeet= self.__feet + other.__feet
        ninch= self.__inches+other.__inches
        if ninch >= 12:
            nfeet+=1
            ninch-=12
        return Distance(nfeet,ninch)



d1=Distance(1,25)
d2=Distance(2,11)
print(d1)

d3= d1+ d2
print(d3)

if (d2>d1):  # == (__eq__ ) != (__ne__)
    print(f"d1 and d2 are equal")
```
</file>

---

## File: `../OOP/class/class5-3-26.py`
**Last Modified:** `2026-03-22 07:41` | **Size:** `0.70 KB`

<file path="../OOP/class/class5-3-26.py" type="python">
```python
class Time:
    def __init__(self,hours,mins,secs):
        self.hours=hours
        self.mins=mins
        self.secs=secs
        self.normalize()

    def __str__(self):
        return f"HOUR: {self.hours} MIN: {self.mins} SEC: {self.secs}"
    def normalize(self):
        if self.secs>=60:
            self.secs-=60
            self.mins+=1
        if self.mins>=60:
            self.mins-=60
            self.hours+=1
        if self.hours>12:
            self.hours-=12
    def totalSec(self):

        hr=self.hours*3600
        mi=self.mins*60
        self.secs=hr+mi+self.secs
        # print(self.secs)
        return self.secs
    
t1= Time(0,34,0)
t2= Time(16,67,98)
print(t1,f"\n",t2)
print(t1.totalSec())
```
</file>

---

## File: `../OOP/class/classOPOV.py`
**Last Modified:** `2026-02-26 08:47` | **Size:** `0.54 KB`

<file path="../OOP/class/classOPOV.py" type="python">
```python
class Number:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __str__(self):
        return f"2({self.real}+{self.imag}i)"
    def __imul__(self, other):
        return Number(other*self.real,other*self.imag)
    # def __radd__(self, other):
    #     # real = 
    #     return Number(other+self.value)
    def __add__(self, other):
        real = self.real+other.real
        imag = self.imag+other.imag
        return Number(real,imag)
    
n1=Number(9,8)
n2=Number(8,4)

n3= n1+n2
n4=n1*n2
print(n3)
print(n4)
```
</file>

---

## File: `../OOP/class/com.py`
**Last Modified:** `2026-02-25 09:00` | **Size:** `0.33 KB`

<file path="../OOP/class/com.py" type="python">
```python
class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"X is {self.x} and Y is {self.y}"
    def __iadd__(self,other):
        self.x+=other.x
        self.y+=other.y
        return self#Coordinate(self.x,self.y)
    

c = Coordinate(42,6)
c1 = Coordinate(2,4)
c+=c1
print(c)

```
</file>

---

## File: `../OOP/class/complex.py`
**Last Modified:** `2026-02-25 08:45` | **Size:** `0.59 KB`

<file path="../OOP/class/complex.py" type="python">
```python
class Employee:
    def __init__(self,name,salary=0):
        self.__name = name
        self.__salary = salary
    
    def __str__(self):
        return f"{self.name}---{self.salary}"
    
    @property
    def name(self):
        return f"{self.__name}"
    @name.setter
    def name(self,new):
        self.__name = new
        
    @property
    def salary(self):
        return f"{self.__salary}"
    @salary.setter
    def salary(self,new):
        if new < 0:
            raise ValueError("The income should be greater then 0")
        self.__salary = new
    
e = Employee("FA",299)
print(e)
```
</file>

---

## File: `../OOP/class/distance.py`
**Last Modified:** `2026-02-26 09:03` | **Size:** `0.68 KB`

<file path="../OOP/class/distance.py" type="python">
```python
class Distance:
    def __init__(self,feet,inches):
        self.__feet=feet
        self.__inches=inches

        if inches >= 12:
            self.__feet += 1
            self.__inches -= 12
    
    def __str__(self):
        return f"Feet:{self.__feet} {self.__inches}"
    
    @property
    def feet(self):
        return self.__feet
    @feet.setter
    def feet(self,new):
        if new<=0:
            raise ValueError
        self.__feet=new
    @property
    def inches(self):
        return self.__inches
    @inches.setter
    def inches(self,new):
        if new<=0:
            raise ValueError
        self.__inches=new
    
    


d1 = Distance(5,12)
print(d1)
d1.feet=10
print(d1)
```
</file>

---

## File: `../OOP/class/employee.py`
**Last Modified:** `2026-02-12 07:01` | **Size:** `0.76 KB`

<file path="../OOP/class/employee.py" type="python">
```python
class Employee:
    __bonus=10#This is in percentage
    def __init__(self, name = "Unknown",salary=0):
        self.__name=name
        self.__salary= salary
    #🤣I wasnt able to remember i need @property here and made the error eat my brain
    @property
    def salary(self):
        return self.__salary
    

    @classmethod
    def displayBonus(cls):
        print(f"Bonus: % {cls.__bonus}")
    
    def showDetails(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")

    @classmethod
    def calcBonus(cls,empSalary):
        bonusAm=empSalary*(cls.__bonus/100)
        print(f"Total salary after bonus addition: {bonusAm+empSalary}")
    
emp = Employee("ALI",50000)
print(emp.salary)
emp.showDetails()
emp.displayBonus()
emp.calcBonus(emp.salary)

```
</file>

---

## File: `../OOP/class/funcprac.py`
**Last Modified:** `2026-02-18 09:24` | **Size:** `0.29 KB`

<file path="../OOP/class/funcprac.py" type="python">
```python
# def sq(v):
#     return v*v

# def sumOfSq(a,b):
#     return sq(a)+sq(b)


# sums= sumOfSq(3,4)
# print(sums)

def getAverage(lst):
    sums=0
    size=0
    for i in lst:
        sums+=i
    for i in range(len(lst)):
        size+=1

    return sums/size

ave= getAverage([1,2,3,4,5])
print(ave)



```
</file>

---

## File: `../OOP/class/lmethods.py`
**Last Modified:** `2026-02-18 09:15` | **Size:** `0.53 KB`

<file path="../OOP/class/lmethods.py" type="python">
```python
class Distance:
    def __init__(self,meters):
        self.meters= meters
    def __str__(self):
        return f"{self.meters}m"
    def __add__(self,other):
        return Distance(self.meters+other.meters)
    def __sub__(self,other):
        return Distance(self.meters-other.meters)
    def __mul__(self,other):
        return Distance(self.meters*other.meters)
    def __truediv__(self,other):
        return Distance(self.meters/other.meters)

d1=Distance(23)
d2=Distance(2)
d3=d1-d2

d4=d1*d2


d5=d1/d2

print(d3,d4,d5,end="\n")
```
</file>

---

## File: `../practice/7-1-26/tier1.py`
**Last Modified:** `2026-01-07 18:39` | **Size:** `4.94 KB`

<file path="../practice/7-1-26/tier1.py" type="python">
```python
#    ████████╗██╗███████╗██████╗      ██╗
#    ╚══██╔══╝██║██╔════╝██╔══██╗    ███║
#       ██║   ██║█████╗  ██████╔╝    ╚██║
#       ██║   ██║██╔══╝  ██╔══██╗     ██║
#       ██║   ██║███████╗██║  ██║     ██║
#       ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝                                                                                                                    
#                                                                                                                      
#    █████╗█████╗█████╗█████╗█████╗█████╗
#    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
#                                                                                                                      
#                                                                                                                      
#                                                                                                                      
# ╔════════════════════════════════════════════════════════════════╗
# ║                       PROBLEM 1                                ║
# ╚════════════════════════════════════════════════════════════════╝   


#Problem 1: Find the 2nd largest element in a given list of integers

# Output: It looks to me like getting a loop and then getting the if conditionals to find the 2nd largest. 
# I think i shall first get the largest and then compare other with it 
# or can use any condition for loop with generator or something like that,ok lets find out

# lst=[33,33,3,33,23,34,34,34]

# sec=0
# for i in lst:
#     if i > sec and any(i<j for j in lst):
#         sec=i
# print(sec)

# ╔════════════════════════════════════════════════════════════════╗
# ║                       PROBLEM 2                                ║
# ╚════════════════════════════════════════════════════════════════╝ 

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                      Frequency Counter                         ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   

#Output: Should have a count of the alphabets as a prefix. 
#How should we get about this. I think we should get a for loop for the current and create a new list

# s = "abracadabara"

# dc = {}
# ky = dc.keys() #O(N)
# for i in s: #O(N)
#     if i in ky:
#         dc[i] += 1
#     elif i not in dc:
#         dc[i] = 1
# print(dc)


# ╔════════════════════════════════════════════════════════════════╗
# ║                       PROBLEM 3                                ║
# ╚════════════════════════════════════════════════════════════════╝ 

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                      Missing number finder                     ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
#
# Output: It should have to find the missing number. 
# I couldnt make up for the logic but i asked ai for help on this 
# and got the mathematical technique of expected sum - actual sum
# expected sum used the gauss method and actualwas the actual sum taken using sum() method

nums = [1,2,4,5,6]
def find(lst):
    n = max(lst)
    expSum = int(n*(n+1)/2)
    actual = sum(lst)
    missing = expSum-actual
    print(actual , "  ", expSum)
    print(missing)
    
find(nums)
```
</file>

---

## File: `../practice/7-1-26/tier2.py`
**Last Modified:** `2026-01-08 12:14` | **Size:** `5.09 KB`

<file path="../practice/7-1-26/tier2.py" type="python">
```python
#    ████████╗██╗███████╗██████╗     ██████╗ 
#    ╚══██╔══╝██║██╔════╝██╔══██╗    ╚════██╗
#       ██║   ██║█████╗  ██████╔╝     █████╔╝
#       ██║   ██║██╔══╝  ██╔══██╗    ██╔═══╝ 
#       ██║   ██║███████╗██║  ██║    ███████╗
#       ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝
#                                            
#    ╔╦╗┬┌┬┐┌─┐┬  ┬┌┐┌┌─┐  ┬ ┬┌─┐┌─┐  ┌┬┐┬┌─┐┌─┐┌─┐┌┬┐
#     ║ ││││├┤ │  ││││├┤   │││├─┤└─┐  ││││└─┐└─┐├┤  ││
#     ╩ ┴┴ ┴└─┘┴─┘┴┘└┘└─┘  └┴┘┴ ┴└─┘  ┴ ┴┴└─┘└─┘└─┘─┴┘
#     Date : 8-1-26

# ╔════════════════════════════════════════════════════════════════╗
# ║                       PROBLEM 1                                ║
# ╚════════════════════════════════════════════════════════════════╝ 
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                        Two Sum                                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                       Version A                                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   

# Output: It should be the sum of 2 digits from a list right so i think
# maybe i should try to use a loop to find out what these two are and add them to a list

# nums = [1,2,3,4,5,6,7]
# target= 13
# # the2 = []
# # for i in nums:
# #     for j in nums:
# #         if i+j == target:
# #             the2.append(i)
            
# print(the2)
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                       Version B                                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
# Output: Need to solve it with a dictionary now. How to go about it.
# Got the help  of AI on this one. i wasnt able to make up for the logic
# I thought of having a dict with key aving the target num and value having a list of the numbers
# that can come to sum up for the target but i couldnt make up logic for that so i got the help of deepseek r2
# still cant make proper sense of it
# num_dict={}
# for i,num in enumerate(nums):
#     complement =  target - num

#     if complement in num_dict:
#         print( [num_dict[complement],i])

#     num_dict[num]=i
#     # print(num_dict)

# ╔════════════════════════════════════════════════════════════════╗
# ║                       PROBLEM 2                                ║
# ╚════════════════════════════════════════════════════════════════╝ 
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                       Move Zeros                               ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
# Output: i need to i think find the zeros using loop and and 'if' and
# use the .move() method to send it to the end
# 
lst = [0,1,0,2,4,5]
# l = len(lst)
# m = max(lst)
z = []
for i in lst:
    if i==0:
        e=lst.index(i)
        v=lst.pop(i)
        print(e,v,z)
        z.append(e)

print(lst+z)
```
</file>

---

## File: `../practice/7-1-26/warmup.py`
**Last Modified:** `2026-01-07 14:55` | **Size:** `1.59 KB`

<file path="../practice/7-1-26/warmup.py" type="python">
```python
# #Create a list and print the elements at even indices     
# lst = ["gia","hanji","praan","tum Kon","wow",6,4,3,4,2,5,2,1,4,4]

# for i in range(len(lst)):
#     if i%2!=0:
#         continue
#     print(lst[i])

#/////////////////////////////////////////////////////////

# #Given a list of numbers return the list with the elements doubled
# lst = [1,2,3,4,5,6,7,8,9]

# doubled=[x*2 for x in lst]

# print(doubled)

#/////////////////////////////////////////////////////////

# #Create a dictionary of name:age , print names of people older than 18
# dic = {
#     "Faseeh":19,
#     "Ali":14,
#     "Leo":22
# }
# for k,v in dic.items():
#     if v>18:
#         print(k)
#     continue

#/////////////////////////////////////////////////////////

# s = 'Im faseeh and i am a uos dinosaur. i got stuck in this small uni but i wont let it define my identity i shall outlive all of the doubts.'


# l = len(s.split())
# print(l)

#    .-.   .-.                                      .--.                      .-.        .-.      
#    : :.-.: :                                     : .--'                     : :       .' `.     
#    : :: :: : .--.  .--. ,-.,-.,-.  .-..-..---.   : :    .--. ,-.,-.,-..---. : :   .--.`. .'.--. 
#    : `' `' ;' .; ; : ..': ,. ,. :  : :; :: .; `  : :__ ' .; :: ,. ,. :: .; `: :_ ' '_.': :' '_.'
#     `.,`.,' `.__,_;:_;  :_;:_;:_;  `.__.': ._.'  `.__.'`.__.':_;:_;:_;: ._.'`.__;`.__.':_;`.__.'
#                                          : :                          : :                       
#                                          :_;                          :_;                       
```
</file>

---

## File: `../practice/coolSlides/main.py`
**Last Modified:** `2026-02-18 10:06` | **Size:** `0.62 KB`

<file path="../practice/coolSlides/main.py" type="python">
```python
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)#detector object
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        handData = results.multi_hand_landmarks[0]
        print(handData.landmark[20])

    cv2.imshow("Hand", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
</file>

---

## File: `../practice/coolSlides/requirements.txt`
**Last Modified:** `2026-02-16 18:51` | **Size:** `0.06 KB`

<file path="../practice/coolSlides/requirements.txt" type="text">
```text
mediapipe==0.10.14
opencv-python==4.9.0.80
numpy>=1.24.0,<2.0.0
```
</file>

---

## File: `../practice/coolSlides/test.py`
**Last Modified:** `2026-02-16 11:02` | **Size:** `1.16 KB`

<file path="../practice/coolSlides/test.py" type="python">
```python
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Initialize camera
# cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Step 1: Create HandLandmarker
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert frame
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Detect hand landmarks
    detection_result = detector.detect(mp_image)
    print(detection_result.hand_landmarks)  # List of detected hand landmarks

    # Display frame
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
 
```
</file>

---

## File: `../practice/polioMap/testfolum.py`
**Last Modified:** `2026-02-12 07:02` | **Size:** `0.00 KB`

<file path="../practice/polioMap/testfolum.py" type="python">
```python

```
</file>

---

## File: `../practice/unip/h.py`
**Last Modified:** `2025-12-14 09:54` | **Size:** `0.92 KB`

<file path="../practice/unip/h.py" type="python">
```python
subjects =["math","english","science"]
students = {}
for _ in range(3):
    name = input("Enter the name: ")
    if name.lower() == 'quit':
        break
    age = input("Enter the age: ")
    marks = []
    
    for sub in subjects:
        mark = int(input(f"Enter your marks for {sub}: "))
        marks.append(mark)
    students[name]= {
        'Age':age,
        'marks':marks,
        'Subjects':subjects
    }
    
print(students)

for name, info in students.items():
    uppername = name.upper()
    subs = info['Subjects']
    marks = info['marks']
    print(marks)

    total = sum(marks)
    average = total/len(marks)
    maxMark = max(marks)

    maxMarkIndex = marks.index(maxMark)
    maxSub = marks[maxMarkIndex]

    print(f" Name: {uppername} \n Max: {maxMark}\n Max marks subject: {maxSub}\n Total: {total}\n Average: {average[:2]}")


search = input("Choose name / subject")
if search.lower() == name:
    for names in 
```
</file>

---

## File: `../practice/unip/main.py`
**Last Modified:** `2025-12-14 09:06` | **Size:** `0.08 KB`

<file path="../practice/unip/main.py" type="python">
```python
def main():
    print("Hello from unip!")


if __name__ == "__main__":
    main()

```
</file>

---

## File: `../practice/unip/r.py`
**Last Modified:** `2025-12-14 16:12` | **Size:** `0.00 KB`

<file path="../practice/unip/r.py" type="python">
```python

```
</file>

---

## File: `../practice/unip/README.md`
**Last Modified:** `2025-12-14 09:06` | **Size:** `0.00 KB`

<file path="../practice/unip/README.md" type="markdown">
```markdown

```
</file>

---

## File: `../practice/hodia.py`
**Last Modified:** `2026-01-03 11:51` | **Size:** `0.41 KB`

<file path="../practice/hodia.py" type="python">
```python
n =5

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        if j==1 or j == 2*i-1:
            print(i,end="")
        else:
            print(" ",end="")
    print()
for k in range(n-1,-1,-1):
        print(" "*(n-k),end="")
        for l in range(1,2*k):
            if l==1 or l==2*k-1:
                print(k,end="")
            else:
                print(" ",end="")
        print()
```
</file>

---

## File: `../practice/ulamspiral.py`
**Last Modified:** `2026-01-03 12:32` | **Size:** `6.00 KB`

<file path="../practice/ulamspiral.py" type="python">
```python
"""
ULAM SPIRAL GENERATOR
=====================
The Ulam spiral is a visual way to display prime numbers.
Numbers are placed in a spiral pattern starting from 1 in the center.
When we mark the prime numbers, interesting diagonal patterns appear!
"""


# ============================================
# STEP 1: Function to check if a number is prime
# ============================================

def is_prime(number):
    """
    Check if a number is a prime number.
    Prime numbers are only divisible by 1 and themselves.
    """
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # 2 is the smallest prime number
    if number == 2:
        return True
    
    # Even numbers (except 2) are not prime
    if number % 2 == 0:
        return False
    
    # Check odd divisors from 3 up to square root of number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False  # Found a divisor, not prime
    
    return True  # No divisors found, it's prime!


# ============================================
# STEP 2: Function to create the spiral grid
# ============================================

def create_ulam_spiral(size):
    """
    Create an Ulam spiral grid of the given size.
    
    The spiral looks like this (for size 5):
    
        17  16  15  14  13
        18   5   4   3  12
        19   6   1   2  11
        20   7   8   9  10
        21  22  23  24  25
    """
    # Make size odd so we have a clear center
    if size % 2 == 0:
        size = size + 1
    
    # Create an empty grid filled with zeros
    grid = []
    for row in range(size):
        grid.append([0] * size)
    
    # Start position: center of the grid
    x = size // 2  # Column (horizontal position)
    y = size // 2  # Row (vertical position)
    
    # Place the number 1 at the center
    grid[y][x] = 1
    
    # Define movement directions
    # Right: x+1, y stays same
    # Up: x stays same, y-1
    # Left: x-1, y stays same  
    # Down: x stays same, y+1
    
    directions_x = [1, 0, -1, 0]   # Change in x for each direction
    directions_y = [0, -1, 0, 1]   # Change in y for each direction
    direction_names = ["right", "up", "left", "down"]
    
    # Movement tracking variables
    current_direction = 0   # 0=right, 1=up, 2=left, 3=down
    steps_before_turn = 1   # How many steps to take before turning
    steps_taken = 0         # Steps taken in current direction
    turns_made = 0          # Total turns we've made
    
    # Fill in numbers 2 through size*size
    for number in range(2, size * size + 1):
        
        # Move one step in the current direction
        x = x + directions_x[current_direction]
        y = y + directions_y[current_direction]
        
        # Place the number at this position
        grid[y][x] = number
        
        # Count this step
        steps_taken = steps_taken + 1
        
        # Check if it's time to turn
        if steps_taken == steps_before_turn:
            # Reset step counter
            steps_taken = 0
            
            # Turn left (counter-clockwise)
            current_direction = (current_direction + 1) % 4
            
            # Count this turn
            turns_made = turns_made + 1
            
            # Every 2 turns, increase the step length
            # Pattern: 1,1,2,2,3,3,4,4,...
            if turns_made % 2 == 0:
                steps_before_turn = steps_before_turn + 1
    
    return grid


# ============================================
# STEP 3: Function to display the spiral
# ============================================

def print_spiral_pattern(grid):
    """
    Print the spiral with symbols:
    * = prime number
    . = not a prime number
    """
    print("\n--- ULAM SPIRAL PATTERN ---")
    print("Legend: * = prime, . = not prime\n")
    
    for row in grid:
        line = ""
        for number in row:
            if is_prime(number):
                line = line + " * "
            else:
                line = line + " ` "
        print(line)


def print_spiral_numbers(grid):
    """
    Print the spiral showing all numbers.
    Prime numbers are marked with brackets [].
    """
    print("\n--- ULAM SPIRAL WITH NUMBERS ---")
    print("Prime numbers have [brackets]\n")
    
    for row in grid:
        line = ""
        for number in row:
            if is_prime(number):
                line = line + f"[{number:3}]"  # Prime in brackets
            else:
                line = line + f" {number:3} "  # Non-prime, plain
        print(line)


def count_primes(grid):
    """Count how many prime numbers are in the grid."""
    count = 0
    for row in grid:
        for number in row:
            if is_prime(number):
                count = count + 1
    return count


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    
    print("=" * 50)
    print("       WELCOME TO ULAM SPIRAL GENERATOR")
    print("=" * 50)
    print()
    print("The Ulam spiral arranges numbers in a spiral")
    print("and reveals patterns in prime numbers!")
    print()
    
    # Get size from user
    try:
        size = int(input("Enter spiral size (try 11, 21, or 31): "))
        if size < 5:
            size = 5
        if size > 41:
            size = 41
            print("Using maximum size of 41")
    except:
        size = 21
        print("Using default size of 21")
    
    # Create the spiral
    print(f"\nCreating {size}x{size} Ulam spiral...\n")
    spiral = create_ulam_spiral(size)
    
    # Display the pattern view
    print_spiral_pattern(spiral)
    
    # Display the numbers view
    print_spiral_numbers(spiral)
    
    # Show statistics
    prime_count = count_primes(spiral)
    total_numbers = size * size
    percentage = (prime_count / total_numbers) * 100
    
    print("\n--- STATISTICS ---")
    print(f"Grid size: {size} x {size}")
    print(f"Total numbers: {total_numbers}")
    print(f"Prime numbers found: {prime_count}")
    print(f"Prime percentage: {percentage:.1f}%")
    print()
```
</file>

---

## File: `../ProjectBOT/bot/ai.py`
**Last Modified:** `2026-03-23 09:02` | **Size:** `0.00 KB`

<file path="../ProjectBOT/bot/ai.py" type="python">
```python
db
```
</file>

---

## File: `../ProjectBOT/bot/db.py`
**Last Modified:** `2026-03-23 09:17` | **Size:** `2.72 KB`

<file path="../ProjectBOT/bot/db.py" type="python">
```python
import requests
import os


SUPABASE_URL= os.getenv('SUPABASE_URL')
SUPABASE_KEY= os.getenv("SUPABASE_ANON_KEY")

HEADERS = {
    "apikey" : SUPABASE_KEY,
    "Authorization" : f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer" : "return=minimal"
}

def get_user(telegram_id):
    url = f"{SUPABASE_URL}/rest/v1/users?telegram_id=eq.{telegram_id}&select = *"

    response = requests.get(url, headers=HEADERS)
    data = response.json()


    if data and len(data) > 0:
        return data[0]
    return None

def create_user(telegram_id, first_name):
    url = f"{SUPABASE_URL}/rest/v1/users"

    new_user = {
        "telegram_id": telegram_id,
        "first_name": first_name,
        "state": "awaiting_goal",
        "streak_current": 0,
        "streak_best":0,
        "onboarding_complete" : False

    }
    response = requests.post(url, json= new_user, headers=HEADERS)
    return response.status_code == 201

def update_user(telegram_id,updates):
    url = f"{SUPABASE_URL}/rest/v1/users?telegram_id=eq.{telegram_id}"
    response = requests.patch(url, json=updates, headers=HEADERS)
    return response.status_code == 204


def get_today_checkin(telegram_id, today):
    url = (
        f"{SUPABASE_URL}/rest/v1/checkins"
        f"?telegram_id=eq.{telegram_id}"
        f"&date=eq.{today}"
        f"&select=*"
    )

    response = requests.get(url, headers=HEADERS)
    data = response.json()

    if data and len(data) > 0:
        return data[0]
    return None


def create_checkin(telegram_id, today,commitment):
    url = f"{SUPABASE_URL}/rest/v1/checkins"
    checkin = {
        "telegram_id": telegram_id,
        "date" : today,
        "commitment": commitment
    }
    response = requests.post(url, headers=HEADERS)
    return response.status_code == 201



def create_checkin(telegram_id, today,updates):
    url = (
        f"{SUPABASE_URL}/rest/v1/checkins"
        f"?telegram_id=eq.{telegram_id}"
        f"&date=eq.{today}"
       
    )
   
    response = requests.patch(url,json=updates, headers=HEADERS)
    return response.status_code == 204

def get_recent_checkins(telegram_id, days=7):

    from datetime import datetime, timedelta

    start_date= (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    url = (
        f"{SUPABASE_URL}/rest/v1/checkins"
        f"?telegram_id=eq.{telegram_id}"
        f"&date=gte.{start_date}"
        f"&select=*"
        f"&order=date.asc"
    )
    response = response.get(url, headers=HEADERS)
    return response.json()

def count_all_checkins(telegram_id):
    url = (
        f"{SUPABASE_URL}/rest/v1/checkins"
        f"?telegram_id=eq.{telegram_id}"  
    )

    response = requests.get(url, headers=HEADERS)

    data = response.json()

    return len(data)
   
```
</file>

---

## File: `../ProjectBOT/bot/handler.py`
**Last Modified:** `2026-03-28 11:01` | **Size:** `0.54 KB`

<file path="../ProjectBOT/bot/handler.py" type="python">
```python
"""
handler.py — Routes incoming updates to the state machine

This is a thin wrapper. In a small bot, you could
put this logic directly in app.py. We separate it
for clean organization.
"""

from bot.states import handle_message as process_message
from bot.states import handle_callback as process_callback


def handle_message(message):
    """Route text messages to the state machine."""
    process_message(message)


def handle_callback(callback_query):
    """Route button clicks to the state machine."""
    process_callback(callback_query)
```
</file>

---

## File: `../ProjectBOT/bot/states.py`
**Last Modified:** `2026-03-28 10:49` | **Size:** `8.83 KB`

<file path="../ProjectBOT/bot/states.py" type="python">
```python

from datetime import datetime
from bot.telegram import send_message, send_buttons
from bot.db import (
    get_user, create_user, update_user,
    get_today_checkin, create_checkin, update_checkin,
    get_recent_checkins
)
from bot.ai import ask_ai




def get_today():
    """Returns today's date as a string like 2025-06-18"""
    return datetime.now().strftime("%Y-%m-%d")


def handle_message(message):
    chat_id = message["chat"]["id"]
    telegram_id = message["from"]["id"]
    first_name = message["from"].get("first_name", "Friend")
    text = message.get("text", "").strip()
    

    # Get user from database
    user = get_user(telegram_id)
    
    # ===== NEW USER =====
    if user is None:
        create_user(telegram_id, first_name)
        
        welcome = (
            f"Hey {first_name}.\n\n"
            f"I'm your accountability partner.\n\n"
            f"Not a motivational app. Not a habit tracker. "
            f"I just ask you one question every day:\n\n"
            f"\"Did you do what you said you'd do?\"\n\n"
            f"Before we start — what's the ONE area "
            f"of your life you want to change?\n\n"
            f"Type it out. Be honest."
        )
        send_message(chat_id, welcome)
        return
    
    # ===== COMMANDS =====
    if text == "/start":
        handle_start(chat_id, user)
        return
    
     
    if text == "/commitment":
        update_user(telegram_id, {"state": "awaiting_commitment"})
        send_message(chat_id, 
            "What's your ONE commitment for today?\n\n"
            "Be specific. Not \"be productive.\"\n"
            "But \"study 2 hours\" or \"no phone after 10pm.\"\n\n"
            "Type it:"
        )
        return
    
    if text == "/checkin":
        handle_checkin(chat_id, user)
        return
    
    if text == "/stats":
        handle_stats(chat_id, user)
        return
    
    if text == "/help":
        send_message(chat_id,
            "Commands:\n\n"
            "/commitment — set today's goal\n"
            "/checkin — report your progress\n"
            "/stats — see your journey\n\n"
            "Or just type anything to talk."
        )
        return
    

    # ===== STATE MACHINE =====
    state = user.get("state", "awaiting_goal")

    if state == "awaiting_goal":
        update_user(telegram_id, {
            "goal_primary" : text,
            "state" : "awaiting_struggle"
        })
        send_message(chat_id,
            f"\"{text}\"\n\n"
            f"Got it. One more thing.\n\n"
            f"What usually pulls you back? "
            f"The trigger. The moment you fall.\n\n"
            f"Be specific. \"Late night scrolling\" "
            f"is better than \"lack of discipline.\"\n\n"
            f"Type it:"
        )
        return
    

    if state == "awaiting_struggle":
        update_user(telegram_id, {
            "struggle": text,
            "state": "awaiting_commitment",
            "onboarding_complete": True
        })
        send_message(chat_id,
            f"Goal: {user.get('goal_primary', '')}\n"
            f"Trigger: {text}\n\n"
            f"Here's how this works:\n"
            f"1. You set ONE commitment daily\n"
            f"2. You report back honestly\n"
            f"3. I track patterns\n"
            f"4. I don't judge. But I don't let you lie.\n\n"
            f"What's your commitment for today?\n"
            f"ONE thing. Type it:"
        )
        return
    

    if state == "awaiting_commitment":
        today = get_today()
        existing = get_today_checkin(telegram_id, today)
        
        if existing:
            update_checkin(telegram_id, today, {"commitment": text})
        else:
            create_checkin(telegram_id, today, text)
        
        update_user(telegram_id, {"state": "committed"})
        send_message(chat_id,
            f"Locked in.\n\n"
            f"Today: \"{text}\"\n\n"
            f"Type /checkin when you're done. Be honest."
        )
        return
    
    if state == "awaiting_details":
        today = get_today()
        update_checkin(telegram_id, today, {"details": text})
        update_user(telegram_id, {"state": "checked_in"})
        
        ai_response = ask_ai(user, "missed", text)
        send_message(chat_id, ai_response)
        return
    
    # ===== DEFAULT: AI CONVERSATION =====
    ai_response = ask_ai(user, "conversation", text)
    send_message(chat_id, ai_response)

def handle_callback(callback_query):
    chat_id = callback_query["message"]["chat"]["id"]
    telegram_id = callback_query["from"]["id"]
    data = callback_query["data"]

    from bot.telegram import answer_callback
    answer_callback(callback_query["id"])

    user = get_user(telegram_id)
    if not user:
        return
    
    today = get_today()

    if data == "ci_yes":
        update_checkin(telegram_id, today, {"result" : "yes"})

        new_streak = (user.get("streak_current",0) or 0) + 1
        best_streak = max(new_streak,user.get("streak_best", 0) or 0)

        update_user(telegram_id, {
            "streak_current" : new_streak,
            "streak_best" : best_streak,
            "state" : "checked_in"
        })

        user["streak_current"] = new_streak
        ai_response = ask_ai(user, "completed")
        send_message(chat_id, ai_response)

    elif data == "ci_no":
        update_checkin(telegram_id, today, {"result": "no"})
        update_user(telegram_id, {
            "streak_current": 0,
            "state": "awaiting_details"
        })
        send_message(chat_id,
            "No judgment.\n\n"
            "But I need to understand.\n"
            "What got in the way?\n\n"
            "Type honestly:"
        )

    elif data == "ci_partial":
        update_checkin(telegram_id, today, {"result": "partial"})
        update_user(telegram_id, {"state": "awaiting_details"})
        send_message(chat_id,
            "Progress counts.\n\n"
            "What did you manage? "
            "What stopped you from finishing?\n\n"
            "Type it:"
        )
def handle_start(chat_id, user):
    """Handle /start command for existing users."""
    if user.get("onboarding_complete"):
        send_message(chat_id,
            f"Welcome back.\n\n"
            f"Streak: {user.get('streak_current', 0)} days\n"
            f"Best: {user.get('streak_best', 0)} days\n\n"
            f"/commitment — set today's goal\n"
            f"/checkin — report progress\n"
            f"/stats — your journey"
        )
    else:
        update_user(user["telegram_id"], {"state": "awaiting_goal"})
        send_message(chat_id,
            "Let's pick up where we left off.\n\n"
            "What's the ONE area of your life "
            "you want to change?"
        )


def handle_checkin(chat_id, user):
    """Handle /checkin command."""
    today = get_today()
    checkin = get_today_checkin(user["telegram_id"], today)
    

    if not checkin or not checkin.get("commitment"):
        send_message(chat_id,
            "You haven't set a commitment today.\n\n"
            "Type /commitment to set one."
        )
        return
    

    if checkin.get("result"):
        send_message(chat_id,
            f"Already checked in today.\n\n"
            f"Commitment: \"{checkin['commitment']}\"\n"
            f"Result: {checkin['result']}\n\n"
            f"Set tomorrow's with /commitment"
        )
        return
    

    buttons = [
        [
            {"text": "✅ Yes", "callback_data": "ci_yes"},
            {"text": "❌ No", "callback_data": "ci_no"}
        ],
        [
            {"text": "🔄 Partially", "callback_data": "ci_partial"}
        ]
    ]
    
    send_buttons(chat_id,
        f"Your commitment today:\n\n"
        f"\"{checkin['commitment']}\"\n\n"
        f"Did you do it?",
        buttons
    )


def handle_stats(chat_id, user):
    """Handle /stats command."""
    checkins = get_recent_checkins(user["telegram_id"], days=7)
    joinedAt = user["created_at"]
    from datetime import datetime,date
    today = datetime.now().strftime("%Y-%m-%d")


    delta = today - joinedAt
    week_display = ""
    yes_count = 0
    total = len(checkins)
    
    for c in checkins:
        result = c.get("result", "")

        if result == "yes":
            week_display  +=  "✅"
            yes_count += 1
        elif result == "no":
            week_display += "❌"
        elif result == "partial":
            week_display += "🔄"
        else:
            week_display += "⬜"

    consistency = round((yes_count / total) * 100) if total > 0 else 0
    
    send_message(chat_id,
        f"Your Journey\n\n"
        f"Streak: {user.get('streak_current', 0)} days\n"
        f"Best: {user.get('streak_best', 0)} days\n\n"
        f"Last 7 days: {week_display or '—'}\n"
        f"Consistency: {consistency}%\n\n"
        f"Goal: {user.get('goal_primary', 'Not set')}\n"
        f"Trigger: {user.get('struggle', 'Not set')}"
        f"Time after you signed up: {delta}"
    )



```
</file>

---

## File: `../ProjectBOT/bot/telegram.py`
**Last Modified:** `2026-03-23 08:05` | **Size:** `0.85 KB`

<file path="../ProjectBOT/bot/telegram.py" type="python">
```python
import requests
import os

BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id,text):
    url= f"{BASE_URL}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }

    response =requests.post(url, json= payload)
    return response.json()


def send_buttons(chat_id,text,buttons):
    url= f"{BASE_URL}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup':{
            'inline_keyboard': buttons
        }
    }

    response =requests.post(url, json= payload)
    return response.json()

def answer_callback(callback_query_id):
    url= f"{BASE_URL}/answerCallbackQuery"

    payload = {
        'callback_query_id': callback_query_id
    }

    requests.post(url, json= payload)

```
</file>

---

## File: `../ProjectBOT/app.py`
**Last Modified:** `2026-03-23 07:33` | **Size:** `0.00 KB`

<file path="../ProjectBOT/app.py" type="python">
```python

```
</file>

---

## File: `../ProjectBOT/requirements.txt`
**Last Modified:** `2026-03-23 08:04` | **Size:** `0.04 KB`

<file path="../ProjectBOT/requirements.txt" type="text">
```text
flask
requests
python-dotenv
gunicorn

```
</file>

---

