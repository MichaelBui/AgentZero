# Git Backup Skill

## Description
Automated git backup skill that commits and pushes local paths to a remote git repository. Prioritizes local changes over remote changes while preserving remote content in git history for easy recovery.

## Features
- **Configurable backup paths**: Define multiple directories/files to backup
- **Conflict resolution**: Prioritizes local changes using `-X ours` merge strategy
- **History preservation**: Remote content is preserved in git history for recovery
- **Automatic staging**: Handles new files, modifications, and deletions
- **Error handling**: Comprehensive error messages and status reporting

## Configuration

### Backup Paths
Edit the `BACKUP_PATHS` list at the top of the script:

```python
BACKUP_PATHS = [
    "/a0/usr",
    # Add more paths as needed
]
```

### Remote Repository
The script expects each backup path to be a git repository with a configured remote.

```bash
cd /your/backup/path
git remote add origin <your-repo-url>
```

## Usage

### Basic Usage
```bash
python /a0/usr/skills/git-backup/scripts/backup.py
```

### With Custom Commit Message
```bash
python /a0/usr/skills/git-backup/scripts/backup.py --message "Manual backup before changes"
```

### Dry Run (Preview Changes)
```bash
python /a0/usr/skills/git-backup/scripts/backup.py --dry-run
```

## Git Strategy

The script uses a strategy that **prioritizes local changes** while **preserving remote history**:

1. **Stage all changes**: `git add -A` (includes new, modified, and deleted files)
2. **Commit locally**: Creates a timestamped commit with all local changes
3. **Fetch remote**: Gets the latest remote state without merging
4. **Merge with local priority**: `git merge origin/<branch> -X ours`
   - The `-X ours` flag resolves conflicts by preferring local changes
   - Remote content is preserved in the merge commit history
5. **Push to remote**: Uploads the merged result

### Recovery
If the script overwrites something important from remote:
1. Check `git log` to find the commit before the merge
2. Use `git show <commit>:<file>` to view the old content
3. Restore with `git checkout <commit> -- <file>` or cherry-pick

## Requirements
- Git installed and configured
- Python 3.x
- Git repositories initialized in backup paths
- Remote origin configured for each repository

## Files
- `scripts/backup.py` - Main backup script
