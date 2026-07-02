# MotionOS Git Guide

## Git Workflow

```text
Edit Code
    ↓
git status
    ↓
git add .
    ↓
git commit -m "Description"
    ↓
git push
```

---

## What Each Command Does

### git status

Shows what has changed.

---

### git add .

Stages the files that will be included in the next commit.

Think:

> "These are the changes I want to save."

---

### git commit

Creates a permanent snapshot of the staged files on the local computer.

The commit message describes that snapshot.

Example:

```bash
git commit -m "Implemented hand tracking"
```

---

### git push

Uploads local commits to GitHub.

Think:

> "Upload my saved snapshots."

---

## Mental Model

```text
Working Files
      ↓
git add
      ↓
Staging Area
      ↓
git commit
      ↓
Local Git Repository
      ↓
git push
      ↓
GitHub
```

---

## Everyday Workflow

```bash
git status

git add .

git commit -m "Describe what you completed"

git push
```