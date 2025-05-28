# CTSGen3

Python package with:
- documentation
- testing
- API interface for host machines running python to interface with EVKs
- API reference for host MCUs to implement communication protocols.

## Install

```
poetry update
```

## Documentation

```
poetry run mkdocs servce
```

## Testing

To be implemented

```
poetry run pytest -rA -s tests/test_spi.py
```

## Static analysis

Before making changes, run these commands and fix their errors

```
poetry run black ctsplayer.py gen3_outputs.py
poetry run ruff check ctsplayer.py gen3_outputs.py
poetry run mypy --strict ctsplayer.py gen3_outputs.py
```
