<p>
  <img src="docs/images/doc-writer-logo.png" alt="doc-writer black-and-white notebook and pen logo" width="64" height="64">
</p>

# doc-writer

**English** | [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An Agent Skill that writes and checks Chinese technical documents from project evidence, covering 12 types including PRDs, designs, APIs, ADRs, and READMEs.

You provide material and a goal. The assistant picks a document type and variant, reads the matching rules, checks facts against code, configuration, and execution logs, drafts the text, and then reviews structure, evidence, and wording item by item. The skill follows the [Agent Skills](https://agentskills.io) specification, so any agent that can read files can use it. It activates only when you explicitly ask to write or review a technical document, not for code changes or everyday questions. Saving files, running operations described in a document, and committing code each need your separate permission. The skill's rules, templates, and guides are written in Chinese.

<a id="安装"></a>

## Installation

Copy the `skills/doc-writer/` directory from this repository into your agent's skills directory and keep the directory name `doc-writer` (it must match `name` in `SKILL.md`). For example, Claude Code's project-level directory:

```bash
tmp=$(mktemp -d) &&
  git clone --depth 1 https://github.com/blankhoney/doc-writer.git "$tmp" &&
  mkdir -p .claude/skills &&
  cp -r "$tmp/skills/doc-writer" .claude/skills/ &&
  rm -rf "$tmp"
```

For other agents, see their documentation for the skills directory. Reopen the session and check that the agent lists `doc-writer`.

To use it in all your projects, copy it into the agent's personal skills directory (for Claude Code, `~/.claude/skills/doc-writer/`). If that directory already exists, compare versions before updating and keep your local customizations.

The candidate scanner needs Python 3.9 or later and uses only the standard library. Without Python, the assistant still writes and checks the document, and notes in its delivery summary that the scan did not run.

## Quick start

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

Describe the task in plain language, or name the type in your request. See the [template index](skills/doc-writer/assets/templates/_index.md) (Chinese) for each type's variants and style requirements.

## How it keeps quality up

- **Rules before writing.** Each stage (preparation, research, writing, verification) reads its rules in full, and the selected template is read completely.
- **Facts from the project.** Code, configuration, recorded decisions, and execution logs back their respective claims; missing information is reported as a gap, not invented.
- **Conclusion first.** Decision documents open with the conclusion, and sections follow a pyramid structure.
- **The model judges, the script locates.** The model checks scope, evidence, terminology, and usability; the scanner only marks candidate boilerplate, vague modifiers, and Chinese formatting issues.
- **Examples with provenance.** The 8 external examples bundled with the templates are pinned to source commits with their licenses, and serve only as writing models.

See [architecture and writing methods](docs/guide/architecture.md) (Chinese) for the full mechanism.

## When not to use it

- You are writing English documents. The rules, word lists, and scanner target Chinese.
- Your agent cannot read local files. Rules and templates are read from disk on demand.
- You want it to commit or publish on its own. Committing and publishing stay your decision.

## Documentation

The guides below are in Chinese.

| Document | Contents |
|---|---|
| [Documentation entry point](docs/guide/README.md) | Installation layout, first use, and navigation |
| [Usage guide](docs/guide/usage.md) | Supplying material, saving, revising, reviewing only, running the scanner standalone |
| [Architecture and writing methods](docs/guide/architecture.md) | How rules, templates, the model, and the scanner divide the work |
| [Extending templates](docs/guide/templates.md) | Adding types, variants, or modules |

## Contributing

Issues and pull requests are welcome. Before changing rules, templates, or the scanner, read the [contributing guide](CONTRIBUTING.md) (Chinese), which covers the test command and example registration.

## Star history

<a href="https://www.star-history.com/#blankhoney/doc-writer&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=blankhoney/doc-writer&type=Date" />
  </picture>
</a>

## License

The project's code, rules, and documentation are licensed under the [MIT License](LICENSE). Example excerpts from Requests, Backstage, Django, Kubernetes enhancements, ripgrep, and uv keep their respective licenses and attribution; the PEP 380 excerpt keeps Gregory Ewing's public-domain dedication. See the [source registry](skills/doc-writer/assets/examples/SOURCES.md) and [assets/examples/licenses/](skills/doc-writer/assets/examples/licenses/).
