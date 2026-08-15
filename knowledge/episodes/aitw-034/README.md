# Git Worktrees for AI Coding Agents

Status: curated from the existing upstream transcript. The transcript is timestamped and speaker labeled, but its origin and cleanup history are not recorded upstream.

Source episode: [`2025-12-09-git-worktrees`](../../../2025-12-09-git-worktrees)

## Purpose, audience, and message

Purpose: Explain Git worktrees through live agent coding examples and show where separate working directories help or hurt parallel work.

Audience: Developers who use coding agents and want to keep several tasks or candidate implementations isolated without cloning the repository for each one.

Message: Use worktrees as named views of branches that share one Git object database. Automate setup and cleanup, keep parallel work bounded, and standardize agent checkpoints so humans can compare and combine results.

## How the workflow works

Each agent gets a branch checked out at its own path. The worktrees share Git history, branches, and remote configuration, while tracked files and installed dependencies remain separate in each directory. A main working directory can inspect or merge commits from the agent branches. The episode also demonstrates a manager process that watches branches, merges new commits, and uses `tmux` to inspect other agent terminals.

## Tactical practices

- Use worktrees when separate branches must be active at the same time. A branch alone gives only one checked out view, while separate clones do not share local commits. See 08:58 to 14:14.
- Give the repository one setup command, then wrap worktree creation so it copies required ignored configuration and installs dependencies. Clean up the new worktree if setup fails. See 15:12 to 17:33.
- Keep the number of active agents small unless the work and review process support more. Dexter says his usual maximum is two and often uses worktrees to preserve resumable tasks rather than to run many agents at once. See 19:24 to 20:21.
- Let agents commit small increments, then inspect or merge those commits from a main branch. Add tests or other checks before automatic merging. See 21:46 to 24:04.
- Name worktrees by feature, issue, model, or another stable convention so their purpose is visible. See 32:21 to 33:01 and 38:15 to 38:56.
- Remove a worktree after its branch is merged. Do not delete in bulk until unfinished work has been identified. See 38:56 to 40:00 and 45:38 to 46:37.
- Standardize parallel outputs, such as research documents or plans with the same shape, so the human comparison point is predictable. See 43:51 to 45:38.
- Create development worktrees after research and planning are settled when those documents do not need branch isolation. If parallel document variants are the goal, worktrees can still provide useful side by side candidates. See 46:30 to 50:46.

## Failure modes and limits

- Untracked and ignored files do not appear automatically. Environment files, local agent settings, dependencies, and linked document stores need explicit setup.
- Dependencies stored inside the repository are duplicated for every worktree and can consume substantial disk space.
- Git prevents the same branch from being checked out in two worktrees, which avoids conflicting writes but can surprise new users.
- Unnamed or abandoned worktrees become hard to distinguish. Automatic deletion is unsafe when some branches contain unfinished work.
- More parallel agents create more review and context reconstruction work. Automation can increase output while reducing alignment with the intended result.
- Automatic merge agents still need checks and conflict handling. The episode demonstrates the pattern but does not verify the generated language ports or measure their correctness.
- Worktrees isolate files, not all machine resources. Build caches, ports, databases, credentials, and external services may still conflict.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2025-12-09-git-worktrees/transcript.md), [episode metadata](../../../2025-12-09-git-worktrees/meta.md), and [source README](../../../2025-12-09-git-worktrees/README.md).

Supporting links include the official [Git worktree documentation](https://git-scm.com/docs/git-worktree), the [Git objects chapter](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects), and the [MultiClaude repository](https://github.com/dexhorthy/multiclaude). The README embeds remote whiteboards and a workflow diagram, but they were not copied into this packet. Its thumbnail URL points to episode 35's video ID even though its video link and metadata agree on episode 34's ID. Exact recording start, transcript model, and transcript cleanup history remain unknown.
