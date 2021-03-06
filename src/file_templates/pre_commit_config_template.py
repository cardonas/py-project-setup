pre_commit_config_template = """repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
      - id: check-yaml
      - id: requirements-txt-fixer
        files: ^requirements*.txt$
      - id: check-toml
      - id: pretty-format-json
        name: format-json
        args: [--autofix, --no-sort-keys]
      - id: check-json
  - repo: https://github.com/psf/black
    rev: 22.6.0
    hooks:
      - id: black
  - repo: https://github.com/asottile/reorder_python_imports
    rev: v3.3.0
    hooks:
      - id: reorder-python-imports
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.14
    hooks:
      - id: mdformat
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: 'v0.961'
    hooks:
      - id: mypy
        additional_dependencies: [ types-all ]
        exclude: ^tests/
  - repo: https://github.com/asottile/setup-cfg-fmt
    rev: v1.20.1
    hooks:
      - id: setup-cfg-fmt"""
