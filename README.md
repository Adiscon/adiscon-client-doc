# Adiscon Documentation

The Adiscon documentation project is a unified Sphinx-based knowledge base for
multiple Adiscon products. It contains the authoritative product manuals,
concepts, and how-to guides generated from reStructuredText (`.rst`) sources and
built into HTML, PDF, and CHM formats.

## Products Covered
- WinSyslog
- WinSyslog-J
- Rsyslog
- MonitorWare Agent (MWAgent)
- EventReporter
- SyslogViewer

## Getting Started
- **Read online:** [https://adiscon.github.io/adiscon-client-doc/master/](https://adiscon.github.io/adiscon-client-doc/master/)
- **Build locally:** follow the environment setup instructions in
  [BUILDING.md](BUILDING.md) and the Makefile usage guide in
  [README.MAKEFILE.md](README.MAKEFILE.md).

The consolidated Makefile replaces the legacy `build-*.sh` scripts and exposes
consistent targets across all products (`make help` lists the available
commands).

## Quality Assurance
The repository provides automated checks for link validation, spelling, and RST
style. Run the following before opening a pull request:

```bash
make linkcheck
make spelling
make validate-rst
```

See the [CHANGELOG](CHANGELOG.md) for project-wide updates and the
[DOC_STRUCTURE](DOC_STRUCTURE.md) notes for deeper architectural context.

## License
Documentation content and supporting build scripts are licensed under the
[Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for copyright details and
third-party acknowledgements.
