<p>
  <img src="docs/images/doc-writer-logo.png" alt="doc-writer black-and-white notebook and pen logo" width="64" height="64">
</p>

# doc-writer

**English** | [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An Agent Skill that writes and checks Chinese technical documents from project evidence, covering 12 types including PRDs, designs, APIs, ADRs, and READMEs.

You provide material and a goal. The main session orchestrates six stages (define, research, resolve, outline, write, verify) with one lead per document, and hands code reading, drafting, and verification to sub-agents. Each stage writes its output to a file, and the next stage reads only files. The skill follows the [Agent Skills](https://agentskills.io) specification, so any agent that can read files can use it. It activates only when you explicitly ask to write or review a technical document, not for code changes or everyday questions. Saving files, running operations described in a document, and committing code each need your separate permission. The skill's rules, writing guides, and documentation are written in Chinese.

<a id="安装"></a>

## Installation

Install with the [skills](https://github.com/vercel-labs/skills) CLI. It detects the agents on your machine (Codex, Cursor, Gemini CLI, GitHub Copilot, Claude Code, and others) and places the skill in each one's skills directory:

```bash
npx skills add blankhoney/doc-writer        # current project
npx skills add blankhoney/doc-writer -g     # personal directory, all projects
```

Without Node, copy the repository's `skills/doc-writer/` directory into your agent's skills directory and keep the directory name `doc-writer` (it must match `name` in `SKILL.md`). See your agent's documentation for that location. Reopen the session and check that the agent lists `doc-writer`.

The doc-lint scanner needs Python 3.9 or later and uses only the standard library. Without Python, the assistant still writes and checks the document, and notes in its delivery summary that the scan did not run.

## Usage

In a session opened in your target project, type (clients with slash commands also accept a leading `/doc-writer`):

```text
Use doc-writer: using the following material, write a Chinese code contribution guide for project contributors. Return the text in chat only: developers create a feature branch and submit a pull request; each pull request must explain the purpose of the changes; a maintainer merges it after automated tests pass and one maintainer approves.
```

You get an operational guide organized around branching, submitting a pull request, testing, and review, ending with a line stating that no file was saved and the scanner did not run.

To save the result, name a path in the request:

```text
Use doc-writer: based on this project's README.md, write a Chinese quick-start guide for engineers joining the project. Save it to docs/quickstart.md.
```

To review without rewriting:

```text
Use doc-writer: review docs/architecture.md for structure, terminology, and accuracy against the implementation. List specific locations and suggested changes. Do not modify any files.
```

## What it writes

| Task | Document type |
|---|---|
| Define feature goals and acceptance conditions | PRD |
| Propose a design and explain trade-offs | Technical design (architecture proposal or implementation design) |
| Describe API usage | API documentation |
| Explain what a release changes for users | Changelog |
| Report test results or plan testing | Test report |
| Document deployment and on-call operations | Deployment guide / Runbook |
| Record an existing decision | ADR |
| Teach a skill or walk through a task | Tutorial, How-to |
| Look up a contract or understand a mechanism | Reference, Explanation |
| Write a repository front page | README |

Describe the task in plain language, or name the type in your request. A document often mixes fragment types (a README opens with a product introduction and continues with setup steps), so the writing agent reads only the guide for each fragment it writes: `product`, `tech`, `reference`, `ops`, `test`, or `marketing` under `skills/doc-writer/references/writing/`.

## How it keeps quality up

- **Stages with files.** Research notes carry `file:line` references and are checked before entering a shared fact pool (`facts.md`), with conflicts re-verified on the spot. A glossary defines each ambiguous term once, and a fresh writing agent takes facts only from the pool instead of raw research.
- **Facts from the project.** Code, configuration, recorded decisions, and execution logs back their respective claims; missing information is reported as a gap, not invented.
- **Three parallel checks.** Three agents without the writing context check facts and consistency, scope and requirements (what is decided too early, what is written too heavily), and style and layout (the balance of text, tables, and diagrams). They write evidence tables only, and the lead makes the changes.
- **The model judges, the script locates.** doc-lint marks candidate boilerplate, vague modifiers, Chinese formatting issues from the G1 table, and layout candidates such as overlong paragraphs and bold body text; the model decides which candidates are real. A separate unslop checklist covers the habits a word list cannot catch.

See [architecture and writing methods](docs/guide/architecture.md) (Chinese) for the full mechanism. Sources for the writing rules are listed in [SOURCES.md](SOURCES.md).

## When not to use it

- You are writing English documents. The rules, word lists, and scanner target Chinese.
- Your agent cannot read local files. Rules and writing guides are read from disk on demand.
- You want it to commit or publish on its own. Committing and publishing stay your decision.

## Documentation

The guides below are in Chinese.

| Document | Contents |
|---|---|
| [Documentation entry point](docs/guide/README.md) | Installation layout, first use, and navigation |
| [Usage guide](docs/guide/usage.md) | Supplying material, saving, revising, reviewing only, running doc-lint standalone |
| [Architecture and writing methods](docs/guide/architecture.md) | The six stages, writing guides, verification, and how the model and doc-lint divide the work |

## Contributing

Issues and pull requests are welcome. Before changing rules, writing guides, or the scanner, read the [contributing guide](CONTRIBUTING.md) (Chinese), which covers the test command and doc-lint.

## Star history

<a href="https://www.star-history.com/#blankhoney/doc-writer&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
  </picture>
</a>

## License

The project's code, rules, and documentation are licensed under the [MIT License](LICENSE). The unslop checklist is adapted from unslop (Lauren Tan, MIT); see [SOURCES.md](SOURCES.md).
