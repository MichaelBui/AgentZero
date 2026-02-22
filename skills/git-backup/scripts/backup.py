#!/usr/bin/env python3
"""
Git Backup Script

Backs up specified paths to their configured git remotes.
Prioritizes local changes over remote while preserving remote history.
"""

import subprocess
import argparse
import sys
from datetime import datetime
from pathlib import Path

# ============================================================================
# CONFIGURATION - Edit this list to change backup paths
# ============================================================================
BACKUP_PATHS = [
    "/a0/usr",
]
# ============================================================================


def run_command(cmd, cwd, dry_run=False, check=True):
    """Run a shell command and return the result."""
    if dry_run:
        print(f"  [DRY-RUN] Would run: {' '.join(cmd)}")
        return subprocess.CompletedProcess(cmd, 0, b"", b"")
    
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(
            result.returncode, cmd, result.stdout, result.stderr
        )
    
    return result


def is_git_repo(path):
    """Check if a directory is a git repository."""
    git_dir = Path(path) / ".git"
    return git_dir.exists()


def get_current_branch(path, dry_run=False):
    """Get the current branch name."""
    result = run_command(
        ["git", "branch", "--show-current"],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    branch = result.stdout.strip()
    if not branch:
        # Detached HEAD or other issue, try to get from ref
        result = run_command(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=path,
            dry_run=dry_run,
            check=False
        )
        branch = result.stdout.strip()
    return branch or "main"


def has_remote(path, dry_run=False):
    """Check if the repository has a remote origin configured."""
    result = run_command(
        ["git", "remote", "get-url", "origin"],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    return result.returncode == 0


def has_staged_changes(path, dry_run=False):
    """Check if there are staged changes ready to commit."""
    result = run_command(
        ["git", "diff", "--cached", "--quiet"],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    # Returns 0 if no changes, 1 if there are changes
    return result.returncode != 0


def has_any_changes(path, dry_run=False):
    """Check if there are any changes (staged or unstaged)."""
    result = run_command(
        ["git", "status", "--porcelain"],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    return bool(result.stdout.strip())


def is_ahead_of_remote(path, branch, dry_run=False):
    """Check if local is ahead of remote."""
    result = run_command(
        ["git", "rev-list", "--count", f"origin/{branch}..HEAD"],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    try:
        count = int(result.stdout.strip())
        return count > 0
    except (ValueError, AttributeError):
        return False


def backup_path(path, custom_message=None, dry_run=False):
    """
    Backup a single path to its git remote.
    
    Git Strategy:
    1. Stage all changes (git add -A)
    2. Commit locally with timestamp (if there are changes)
    3. Fetch remote
    4. Merge with -X ours (local changes priority, remote preserved in history)
    5. Push to remote (if there's something to push)
    """
    print(f"\n{'='*60}")
    print(f"Backing up: {path}")
    print(f"{'='*60}")
    
    path_obj = Path(path)
    
    # Validate path exists
    if not path_obj.exists():
        print(f"  ❌ Error: Path does not exist: {path}")
        return False
    
    # Validate git repository
    if not is_git_repo(path):
        print(f"  ❌ Error: Not a git repository: {path}")
        print(f"     Run: git init && git remote add origin <url>")
        return False
    
    # Validate remote exists
    if not has_remote(path, dry_run):
        print(f"  ❌ Error: No remote origin configured for: {path}")
        print(f"     Run: git remote add origin <url>")
        return False
    
    branch = get_current_branch(path, dry_run)
    print(f"  📋 Branch: {branch}")
    
    # Check for any changes
    has_changes = has_any_changes(path, dry_run)
    
    if not has_changes:
        print(f"  ℹ️  No local changes detected")
        
        # Still try to fetch and sync with remote
        print(f"  🔄 Fetching remote...")
        try:
            run_command(["git", "fetch", "origin"], cwd=path, dry_run=dry_run, check=False)
        except subprocess.CalledProcessError as e:
            print(f"  ⚠️  Warning: Could not fetch remote: {e.stderr}")
        
        # Check if we need to pull (local behind remote)
        result = run_command(
            ["git", "rev-list", "--count", f"HEAD..origin/{branch}"],
            cwd=path,
            dry_run=dry_run,
            check=False
        )
        
        try:
            behind_count = int(result.stdout.strip()) if result.stdout.strip() else 0
        except ValueError:
            behind_count = 0
        
        if behind_count > 0:
            print(f"  📥 Local is behind remote by {behind_count} commits, pulling...")
            try:
                run_command(["git", "pull", "origin", branch], cwd=path, dry_run=dry_run, check=False)
                print(f"  ✅ Synced with remote")
            except subprocess.CalledProcessError as e:
                print(f"  ⚠️  Warning: Could not pull: {e.stderr}")
        else:
            print(f"  ✅ Already in sync with remote - nothing to backup")
        
        return True
    
    # Step 1: Stage all changes
    print(f"  📦 Staging changes...")
    try:
        run_command(["git", "add", "-A"], cwd=path, dry_run=dry_run)
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to stage changes: {e.stderr}")
        return False
    
    # Check if staging resulted in anything to commit
    if not has_staged_changes(path, dry_run) and not dry_run:
        print(f"  ℹ️  No changes to commit after staging")
        return True
    
    # Step 2: Commit locally
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if custom_message:
        commit_message = f"{custom_message} [{timestamp}]"
    else:
        commit_message = f"Backup [{timestamp}]"
    
    print(f"  💾 Committing: {commit_message}")
    result = run_command(
        ["git", "commit", "-m", commit_message],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    
    if result.returncode != 0:
        # Check if it's just "nothing to commit"
        if "nothing to commit" in result.stdout.lower() or "nothing to commit" in result.stderr.lower():
            print(f"  ℹ️  Nothing to commit - working tree clean")
        else:
            print(f"  ⚠️  Commit warning: {result.stderr}")
            # Continue anyway, might still have unpushed commits
    
    # Step 3: Fetch remote
    print(f"  🔄 Fetching remote...")
    try:
        run_command(["git", "fetch", "origin"], cwd=path, dry_run=dry_run, check=False)
    except subprocess.CalledProcessError as e:
        print(f"  ⚠️  Warning: Could not fetch remote: {e.stderr}")
    
    # Step 4: Merge with local priority (-X ours)
    print(f"  🔀 Checking remote state...")
    
    # Check if remote branch exists
    result = run_command(
        ["git", "rev-parse", f"origin/{branch}"],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    
    remote_exists = result.returncode == 0
    
    if remote_exists:
        # Check if we need to merge (remote has commits we don't have)
        result = run_command(
            ["git", "rev-list", "--count", f"HEAD..origin/{branch}"],
            cwd=path,
            dry_run=dry_run,
            check=False
        )
        
        try:
            commits_behind = int(result.stdout.strip()) if result.stdout.strip() else 0
        except ValueError:
            commits_behind = 0
        
        if commits_behind > 0:
            print(f"  🔀 Merging {commits_behind} remote commits with local priority...")
            result = run_command(
                ["git", "merge", f"origin/{branch}", "-X", "ours", "-m", f"Merge remote with local priority [{timestamp}]"],
                cwd=path,
                dry_run=dry_run,
                check=False
            )
            
            if result.returncode != 0:
                if "Already up to date" in result.stdout or "Already up to date" in result.stderr:
                    print(f"  ℹ️  Already up to date with remote")
                else:
                    print(f"  ⚠️  Merge warning: {result.stderr}")
                    # Continue to try push anyway
            else:
                print(f"  ✅ Merged with local priority")
        else:
            print(f"  ℹ️  No remote commits to merge")
    else:
        print(f"  ℹ️  No remote branch yet, will create on push")
    
    # Step 5: Check if there's anything to push
    if not is_ahead_of_remote(path, branch, dry_run):
        print(f"  ℹ️  Nothing to push - already in sync with remote")
        return True
    
    # Step 6: Push to remote
    print(f"  📤 Pushing to remote...")
    result = run_command(
        ["git", "push", "origin", branch],
        cwd=path,
        dry_run=dry_run,
        check=False
    )
    
    if result.returncode != 0:
        # Check if it's "no upstream branch" error
        if "no upstream branch" in result.stderr.lower() or "has no upstream" in result.stderr.lower():
            print(f"  📤 Setting upstream and pushing...")
            result = run_command(
                ["git", "push", "-u", "origin", branch],
                cwd=path,
                dry_run=dry_run,
                check=False
            )
        
        if result.returncode != 0:
            # Check if it's "everything up-to-date"
            if "everything up-to-date" in result.stdout.lower() or "everything up-to-date" in result.stderr.lower():
                print(f"  ✅ Already up to date with remote")
                return True
            else:
                print(f"  ❌ Failed to push: {result.stderr}")
                return False
        else:
            print(f"  ✅ Successfully pushed to origin/{branch}")
    else:
        print(f"  ✅ Successfully pushed to origin/{branch}")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Git backup script - backs up paths to git remotes with local priority"
    )
    parser.add_argument(
        "--message", "-m",
        help="Custom commit message prefix",
        default=None
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without executing"
    )
    parser.add_argument(
        "--paths",
        nargs="+",
        help="Override configured backup paths",
        default=None
    )
    
    args = parser.parse_args()
    
    paths = args.paths if args.paths else BACKUP_PATHS
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
    
    print(f"\n📋 Backup paths configured: {len(paths)}")
    for p in paths:
        print(f"   - {p}")
    
    success_count = 0
    fail_count = 0
    
    for path in paths:
        if backup_path(path, args.message, args.dry_run):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n{'='*60}")
    print(f"Backup Summary")
    print(f"{'='*60}")
    print(f"  ✅ Successful: {success_count}")
    print(f"  ❌ Failed: {fail_count}")
    
    if fail_count > 0:
        sys.exit(1)
    
    print(f"\n🎉 Backup completed successfully!")


if __name__ == "__main__":
    main()
