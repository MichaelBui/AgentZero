# Unit Test Culture & Requirements

Standards for writing unit tests across all Agent Zero skills.

## Stack

- **Framework**: pytest (not `unittest.TestCase`)
- **Subtests**: `pytest-subtests` plugin for BDD scenario display
- **Coverage**: `pytest-cov` with `--cov=<module>` flag
- **Mocking**: `unittest.mock.patch` / `unittest.mock.MagicMock`

## Pattern: BDD Test Tables

Every public function/method gets **one test function** containing a **test table** of scenarios.

```python
def test_compute_discount(subtests):
    cases = [
        ("When cart total < 50 then no discount",
         49.99, 0.0),
        ("When cart total >= 50 and < 100 then 10% discount",
         75.00, 7.50),
        ("When cart total >= 100 then 20% discount",
         150.00, 30.00),
    ]
    for scenario, cart_total, expected_discount in cases:
        with subtests.test(msg=scenario):
            assert compute_discount(cart_total) == expected_discount
```

### Rules

| Rule | Why |
|---|---|
| Scenario string starts with "When" | BDD convention: stimulus -> response |
| Test table is a list of tuples | Reader sees all inputs/outputs at a glance |
| One test function per public method | Prevents test explosion; internals can change freely |
| Use `subtests.test(msg=scenario)` | Shows `SUBPASSED[When ...]` in verbose output |
| Assert with `assert` not `self.assertEqual` | Pytest-native; better failure messages |
| Use `pytest.raises(X)` not `self.assertRaises` | Pytest-native context manager |

### What Makes a Good Test Table

A test table must show the **reader** at minimum: scenario description, input, and expected output.

```python
# GOOD - input and output visible in the tuple
cases = [
    ("When node is None then returns empty string", None, ""),
    ("When node is text type then returns text value",
     {"type": "text", "text": "hello"}, "hello"),
]
```

```python
# BAD - scattered assertions, no table structure
with self.subTest(scenario="When upserting same content then returns False"):
    result = self.db.upsert_atomic("jira", "K-1", "K-1", "A", "C", "2026-01-01", "2026-01-01")
    self.assertFalse(result)
```

### Stateful Test Tables

When tests require setup before each scenario (e.g., DB operations), use setup lambdas:

```python
def test_needs_resummarize(subtests):
    cases = [
        ("When no summary exists then returns True",
         lambda d: d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01"),
         True),
        ("When summary is up-to-date then returns False",
         lambda d: (d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01"),
                    d.upsert_summary("K-1", "jira", "T", "S")),
         False),
    ]
    for scenario, setup, expected in cases:
        with subtests.test(msg=scenario):
            db = create_fresh_db()
            setup(db)
            assert db.needs_resummarize("K-1") == expected
            cleanup(db)
```

## Fixtures

Use `@pytest.fixture` for shared setup/teardown instead of `setUp/tearDown`:

```python
@pytest.fixture
def db():
    d, path = create_temp_db()
    yield d
    cleanup(d, path)

def test_something(subtests, db):
    # db is automatically created and cleaned up
    ...
```

Use `tmp_path` (built-in pytest fixture) for temporary directories.

## Coverage Requirements

| Metric | Target |
|---|---|
| Line coverage | >= 95% |
| Each public method | At least 1 test function |
| Edge cases | Empty input, None, error paths, boundary values |

Run coverage:
```bash
make coverage     # term-missing report
make coverage-html  # HTML report
```

## Makefile Targets

Every skill with tests must have a `Makefile` with these targets:

```makefile
test:          # quick run, quiet output
test-verbose:  # verbose with SUBPASSED scenario display
coverage:      # term-missing coverage report
clean:         # remove .coverage, htmlcov, __pycache__, .pytest_cache
```

## What NOT to Do

| Anti-pattern | Why it fails |
|---|---|
| `unittest.TestCase` with `self.subTest` | Scenarios don't show PASS/FAIL individually in pytest |
| One assertion per test function | Test explosion; harder to maintain |
| Testing private methods directly | Breaks when implementation changes |
| `make scenarios` that extracts strings with regex | Faked output; doesn't prove tests actually run |
| Hardcoding dates that expire | Use relative dates or `--days 365` in tests |
| Mocking too deep | Test behavior, not implementation details |

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Test file | `test_<module>.py` | `test_jira.py` |
| Test function | `test_<public_method>` | `test_compute_mention_type` |
| Scenario string | `"When {condition} then {behavior}"` | `"When user is assignee then returns 'direct'"` |
| Fixture | lowercase descriptive noun | `db`, `tmp_path`, `mock_api` |

## Dependencies

Install before running tests:
```bash
pip install pytest pytest-subtests pytest-cov
```
