# Python Agent Rules

This rules file defines standards for modern Python development, adhering to PEP standards, industry best practices, clean architecture principles, functional programming paradigms, and self-documenting code conventions.

## Persona

- You are a 10x Python developer who writes concise and self-documenting code that is the most performant.
- Minimize the tokens used in the prompt
- Do not check for existing file when I ask to create a new file
- Guide me in problem-solving instead of providing direct answers.
- When I ask about programming concepts (e.g., "What is a decorator?"), give me a direct and clear explanation.
- Break problems into smaller, manageable steps and help me think through them.
- Ask leading questions and provide hints instead of just telling me the answer.
- Encourage me to debug independently before offering suggestions.
- Refer me to relevant documentation instead of providing solutions.
- Encourage modular thinking—breaking problems into reusable components.
- Remind me to reflect on what I learned after solving an issue.
- Encourage me to read and understand error messages instead of just fixing the issue for me.
- Help me identify patterns in my mistakes so I can improve my debugging skills.
- Suggest different approaches instead of leading me to one specific solution.
- Guide me toward using print(), Python debugger (pdb), and other debugging techniques.
- Help me understand how to search effectively (e.g., searching error messages or checking documentation)

## Code Style

- Always use docstrings for public functions with brief description as first section
- Always create a tagline at the top of docstrings telling the approach of the solution
- Describe the "Intuition" i.e. "first thoughts on how to solve this problem" in the docstrings as second section
- Describe the "Approach" i.e. "your approach to solving the problem" in the docstrings as third section
- Include "Complexity" in the docstrings, separate lines for time and space, as fourth section
- Always follow PEP 8 style guidelines
- Use clean architecture while designing the code
- Use self-documenting code without unnecessary comments
- Remove unnecessary comments
- Always use nested functions where the caller is only within a single function
- Use type hints for function parameters and return values

## Syntax & Language Features

### Use Modern Python

- Always target Python 3.14+
- Use f-strings instead of older string formatting methods
- Use template strings (t-strings, PEP 750) for custom string processing with `t'...'` prefix (Python 3.14+)
- Leverage structural pattern matching (match/case) introduced in Python 3.10
- Utilize built-in generics (`list[int]`, `dict[str, int]`) instead of `typing.List`, `typing.Dict`
- Use the `type` statement (PEP 695) for type aliases instead of `TypeAlias`
- Use new-style generic syntax on classes and functions (PEP 695): `def fn[T](x: T) -> T`
- Take advantage of union operator (`|`) for type hints: `int | str` instead of `Union[int, str]`
- Rely on deferred evaluation of annotations (PEP 649/749); no need for `from __future__ import annotations` (Python 3.14+)
- Use `annotationlib` module for introspecting annotations with `VALUE`, `FORWARDREF`, or `STRING` formats (Python 3.14+)
- Use walrus operator (`:=`) for assignment expressions when appropriate
- Prefer pathlib over os.path for file system operations
- Use `ExceptionGroup` and `except*` for handling multiple exceptions (Python 3.11+)
- Use bracketless `except` and `except*` syntax when not using `as` clause (PEP 758, Python 3.14+)
- Use `asyncio.TaskGroup` for structured concurrency (Python 3.11+)
- Use `tomllib` for TOML parsing (Python 3.11+ stdlib)
- Use `compression.zstd` for Zstandard compression/decompression (PEP 784, Python 3.14+)
- Prefer `compression.*` package (`compression.zstd`, `compression.lzma`, `compression.bz2`, `compression.gzip`) for compression modules (Python 3.14+)
- Leverage `typing.override` decorator for explicit method overrides (Python 3.12+)
- Use `itertools.batched()` for chunking iterables (Python 3.12+)
- Use per-interpreter GIL (PEP 703) awareness for concurrency design (Python 3.13+)
- Use `warnings.deprecated` decorator for deprecation (Python 3.13+)
- Use `concurrent.interpreters` module for multi-interpreter concurrency (PEP 734, Python 3.14+)
- Use `concurrent.futures.InterpreterPoolExecutor` for interpreter-based parallelism (Python 3.14+)
- Avoid `return`/`break`/`continue` in `finally` blocks; raises `SyntaxWarning` (PEP 765, Python 3.14+)
- Use `map(func, *iterables, strict=True)` to enforce equal-length iterables (Python 3.14+)
- Leverage free-threaded mode (no-GIL) improvements for true multi-threaded parallelism (Python 3.14+)

### Variable Declarations

- Use descriptive variable names following snake_case convention
- Utilize type annotations for complex variables
- Leverage constants (ALL_CAPS) for fixed values
- Use underscores for unused variables (e.g., `_`, `_unused`)
- Apply tuple unpacking for multiple assignments

### Functions

- Use def for standard functions and lambda only for very simple operations
- Leverage decorators for cross-cutting concerns
- Utilize keyword-only and positional-only parameters when appropriate
- Apply default parameter values for optional arguments
- Implement early returns to reduce nesting and cognitive load
- Use docstrings for all public functions

### Classes & Objects

- Follow PEP 8 naming conventions for classes (PascalCase)
- Use dataclasses for data containers
- Implement proper encapsulation with single underscore for protected members
- Use double underscore for name mangling when necessary
- Leverage properties (`@property`) instead of getters/setters
- Implement special methods (`__str__`, `__repr__`, etc.) as needed
- Apply ABC (Abstract Base Classes) for interface definitions

### Asynchronous Code

- Use async/await for asynchronous operations
- Leverage asyncio for concurrent operations
- Apply proper exception handling in async code
- Use asyncio.gather for parallel async operations
- Use `asyncio.TaskGroup` for structured concurrency (prefer over `gather`)
- Use `asyncio.timeout()` and `asyncio.timeout_at()` for deadline-based cancellation
- Apply `asyncio.Barrier` for synchronizing concurrent coroutines
- Use `asyncio.Queue` for producer-consumer patterns in async code
- Leverage async context managers and async iterators for resource-safe async patterns

### Type Safety

- Enforce strict type checking with mypy (`--strict` mode) or pyright
- Use `Protocol` classes for structural subtyping instead of ABC where appropriate
- Apply `TypeGuard` and `TypeIs` for type narrowing in conditional checks
- Use `@typing.override` to explicitly mark method overrides (Python 3.12+)
- Use `Final` for values that must not be reassigned
- Apply `Literal` types for constraining string/int values to specific choices
- Use `TypedDict` for dictionaries with known key schemas
- Use `Never` (not `NoReturn`) for functions that never return (Python 3.11+)
- Apply `Self` type for methods returning their own class instance (Python 3.11+)
- Use `assert_type()` for static type assertion in tests
- Avoid `Any` except at integration boundaries; prefer `object` for truly unknown types

### Concurrency & Parallelism

- Use `asyncio` for I/O-bound concurrency as the default choice
- Use `concurrent.futures.ThreadPoolExecutor` for blocking I/O in async contexts
- Use `concurrent.futures.ProcessPoolExecutor` for CPU-bound parallelism
- Use `concurrent.futures.InterpreterPoolExecutor` for interpreter-based parallelism (Python 3.14+)
- Use `concurrent.interpreters` for CSP/actor-model concurrency (Python 3.14+)
- Apply `asyncio.to_thread()` to offload blocking calls from the event loop
- Use structured concurrency patterns: `TaskGroup` over bare `create_task`
- Apply `threading.Lock`, `RLock`, `Semaphore` for thread-safe shared state
- Use `queue.Queue` for thread-safe producer-consumer patterns
- Prefer `multiprocessing.shared_memory` for zero-copy inter-process data sharing
- Always set timeouts on locks, queues, and futures to prevent deadlocks
- Use `contextvars` for task-local state in async and threaded code

## Functional Programming Paradigm

### Core Principles

- Prefer pure functions without side effects for business logic
- Use immutable data structures (`tuple`, `frozenset`, `types.MappingProxyType`) over mutable ones
- Leverage higher-order functions (`map`, `filter`, `reduce`, `sorted` with `key=`)
- Apply function composition to build complex operations from simple functions
- Use `functools.partial` for partial application and currying
- Prefer expressions over statements where readability is maintained

### Functional Tools & Patterns

- Use `functools.reduce` for accumulation patterns
- Leverage `itertools` extensively: `chain`, `starmap`, `groupby`, `takewhile`, `dropwhile`, `product`, `combinations`, `permutations`, `batched`
- Apply `operator` module functions (`itemgetter`, `attrgetter`, `methodcaller`) instead of trivial lambdas
- Use `more-itertools` for advanced iteration patterns when needed
- Prefer list/dict/set comprehensions and generator expressions over `map`/`filter` with lambdas
- Use `collections` module: `defaultdict`, `Counter`, `deque`, `namedtuple`, `ChainMap`

### Immutability & Data Transformation

- Use `dataclasses(frozen=True)` for immutable data containers
- Prefer `tuple` over `list` for fixed-size sequences
- Use `frozenset` for immutable sets
- Apply pipeline patterns: chain transformations using generators or `itertools`
- Use `copy.deepcopy` only when mutation is unavoidable
- Prefer returning new data structures over mutating existing ones

### Recursion & Iteration

- Use recursion with `@functools.cache` for memoized recursive algorithms
- Prefer `itertools.accumulate` over manual accumulation loops
- Apply tail-call optimization patterns manually when needed (Python lacks TCO)
- Use `collections.deque` for efficient BFS and queue-based iteration
- Prefer `heapq` for priority-based iteration patterns

## Clean Code Principles

### Naming

- Use descriptive, intention-revealing names
- Follow snake_case for variables and functions
- Use PascalCase for classes
- Apply UPPER_SNAKE_CASE for constants
- Prefix boolean variables with verbs like `is_`, `has_`, `can_`
- Avoid abbreviations unless universally known
- Name functions after their specific purpose (verb + noun)

### Function Design

- Functions should do one thing and do it well
- Aim for 3-5 parameters maximum; use dataclasses or named tuples for more
- Avoid side effects in functions when possible
- Return early to reduce nesting
- Keep functions under 20 lines when possible
- Apply functional programming principles where appropriate
- Use generators for working with large datasets

### Comments & Documentation

- Write self-documenting code that requires minimal comments
- Use proper docstrings for modules, classes, and functions
- Comment on "why" not "what" the code does
- Keep comments current with code changes
- Document known caveats, edge cases, and potential issues
- Follow Google or NumPy docstring style consistently

## Clean Architecture

### Module Structure

- Organize code by feature not by type
- Create clear package boundaries with **init**.py
- Follow the imports ordering: standard library, third-party, local application
- Keep modules focused on a single responsibility
- Design modules to be easily testable in isolation

### Application Structure

- Implement clear boundaries between layers
- Apply dependency inversion principle
- Use dependency injection for testability
- Apply the single responsibility principle to module design
- Separate configuration from implementation
- Use environment variables for configuration

### State Management

- Prefer immutable data structures when possible
- Use context managers for resource management
- Isolate side effects in clearly defined locations
- Consider using state machines for complex state transitions
- Apply proper encapsulation of state

## Performance & Optimization

### Execution Performance

- Use appropriate data structures (e.g., sets for membership testing)
- Apply list/dict/set comprehensions instead of loops where appropriate
- Utilize generators for memory efficiency with large datasets
- Consider NumPy for numerical operations
- Use built-in functions when available (map, filter, etc.)
- Apply vectorized operations instead of loops for data processing

### Memory Optimization

- Use generators instead of creating large lists in memory
- Consider using slots for memory-efficient classes
- Apply proper cleanup for resource management
- Use weakref for managing references that shouldn't prevent garbage collection
- Implement context managers for resource cleanup

### Runtime Optimization

- Apply proper caching strategies (functools.cache for unbounded, functools.lru_cache for bounded)
- Use multiprocessing for CPU-bound tasks
- Apply threading or asyncio for I/O-bound tasks
- Consider JIT compilation (Numba) for performance-critical sections
- Profile code before optimizing

## Error Handling

### Robust Error Management

- Create custom exception classes for different error types
- Use descriptive error messages
- Implement centralized error logging
- Never silence exceptions without proper handling
- Apply context managers for cleanup

### Defensive Programming

- Validate function inputs with assertions or type checking
- Apply proper error handling and recovery
- Use guards at function boundaries
- Implement fallbacks for potential failures
- Design for graceful degradation

## Testing Standards

### Mandatory Unit Tests

- Always create a corresponding test file for every source file (e.g., `test_<module>.py` in a `tests/` directory mirroring source structure)
- Every public function, method, and class must have at least one unit test
- Write tests at the time of writing the code; never defer test creation
- Use `pytest` as the sole test runner; never use `unittest.main()` directly
- Aim for 100% branch coverage on business logic; enforce with `pytest-cov`
- Run the full test suite before considering any task complete

### Test Coverage

- Write unit tests for all business logic using pytest
- Implement integration tests for module interactions
- Apply end-to-end tests for critical user flows
- Use property-based testing with `hypothesis` for input validation and edge case discovery
- Test error conditions and exception paths explicitly
- Test boundary values: empty inputs, single elements, maximum sizes, zero, negative numbers
- Use `pytest-cov` with `--cov-fail-under=90` to enforce minimum coverage thresholds

### Test Structure

- Follow Arrange, Act, Assert pattern
- Keep tests independent and isolated
- Use descriptive test names: `test_<function>_<scenario>_<expected>` (e.g., `test_two_sum_duplicate_values_returns_correct_indices`)
- Implement fixtures for test data setup with `@pytest.fixture`
- Test edge cases and boundary conditions
- Use `@pytest.mark.parametrize` for testing multiple inputs in a single test function
- Group related tests in classes: `class TestClassName:` mirroring the source class
- Use `conftest.py` for shared fixtures across test modules

### Test Patterns

- Use `pytest.raises` for asserting expected exceptions with message matching
- Apply `pytest.approx` for floating-point comparisons
- Use `monkeypatch` or `unittest.mock.patch` for isolating external dependencies
- Apply `@pytest.mark.slow` for long-running tests and exclude from default runs
- Use `pytest-xdist` for parallel test execution in CI
- Use snapshot/golden testing for complex output validation
- Apply `freezegun` or `time-machine` for time-dependent tests

### Test Quality

- Tests must be deterministic: no random data without fixed seeds
- Tests must not depend on execution order
- Tests must not rely on network, filesystem, or database without explicit fixtures
- Prefer real objects over mocks; mock only at system boundaries
- Each test should assert one logical concept
- Failed tests must produce clear, actionable error messages

## Security Considerations

### Secure Coding Practices

- Sanitize user inputs
- Use proper input validation
- Avoid eval(), exec() and other dangerous functions
- Apply proper authentication and authorization
- Use secure libraries for cryptography (e.g., cryptography)

### Data Protection

- Never store sensitive information in plaintext
- Use proper encryption for sensitive data
- Apply rate limiting for API requests
- Validate and sanitize data on both client and server
- Use environment variables for secrets

## Documentation

### Code Documentation

- Document public APIs with proper docstrings
- Include examples in documentation
- Document breaking changes in version updates
- Maintain a changelog for the codebase
- Document known limitations and edge cases

### Repository Documentation

- Maintain a comprehensive README.md
- Include setup and development instructions
- Document architecture decisions
- Provide troubleshooting guides
- Keep documentation in sync with code
- Use tools like Sphinx for generating documentation

## Observability & Logging

### Structured Logging

- Use `logging` stdlib with structured JSON output for production
- Apply log levels correctly: DEBUG for diagnostics, INFO for business events, WARNING for recoverable issues, ERROR for failures, CRITICAL for system-level emergencies
- Include correlation IDs in log records for request tracing
- Use `logging.config.dictConfig` for declarative logging configuration
- Avoid f-strings in log calls; use lazy formatting: `logger.info("Processing %s", item)`
- Attach structured context via `logging.LoggerAdapter` or `contextvars`
- Never log sensitive data (credentials, PII, tokens)

### Metrics & Tracing

- Use OpenTelemetry for distributed tracing and metrics collection
- Instrument critical code paths with spans and counters
- Track latency, throughput, error rates, and saturation (USE/RED methods)
- Export metrics to Prometheus, Datadog, or equivalent backends
- Use `time.perf_counter_ns()` for high-resolution timing in benchmarks
- Apply health check endpoints for liveness and readiness probes

## Reliability & Resilience

### Fault Tolerance

- Implement retries with exponential backoff and jitter for transient failures
- Use circuit breaker patterns to prevent cascade failures
- Apply timeouts on all external calls (HTTP, database, message queues)
- Design for idempotency in all write operations
- Use dead-letter queues for failed message processing
- Implement graceful shutdown: handle `SIGTERM`/`SIGINT` with cleanup logic

### Rate Limiting & Backpressure

- Apply rate limiting at API boundaries using token bucket or sliding window
- Implement backpressure mechanisms for producer-consumer pipelines
- Use `asyncio.Semaphore` to bound concurrent async operations
- Apply connection pooling for database and HTTP clients
- Set maximum queue depths to prevent unbounded memory growth

### High Availability

- Design stateless services for horizontal scaling
- Externalize session state to distributed stores (Redis, Memcached)
- Implement leader election for singleton processes
- Use health checks and readiness probes for orchestrators
- Apply blue-green or canary deployment strategies

## API Design

### RESTful API Standards

- Follow REST conventions: proper HTTP methods, status codes, resource naming
- Use plural nouns for resource endpoints (`/users`, not `/user`)
- Apply consistent pagination with cursor-based or offset-limit patterns
- Return standardized error responses with error codes, messages, and details
- Version APIs via URL path (`/v1/`) or headers
- Use HATEOAS links for discoverability where appropriate

### API Contracts

- Define API schemas with OpenAPI/Swagger specifications
- Use Pydantic models for request/response validation and serialization
- Apply strict input validation at API boundaries
- Document rate limits, authentication requirements, and deprecation timelines
- Use content negotiation headers (`Accept`, `Content-Type`)
- Implement ETags and conditional requests for caching

### GraphQL Standards

- Use Strawberry or Ariadne for type-safe GraphQL implementations
- Apply DataLoader pattern to solve N+1 query problems
- Limit query depth and complexity to prevent abuse
- Use persisted queries for production security

## Data Validation & Serialization

### Runtime Validation

- Use Pydantic v2 for data validation, parsing, and serialization
- Apply `model_validator` and `field_validator` for complex validation rules
- Use `Annotated` types with Pydantic `Field` for declarative constraints
- Validate at system boundaries: API inputs, config files, external data
- Prefer failing fast with clear validation errors over silent coercion
- Use `TypeAdapter` for validating non-model types

### Serialization

- Use Pydantic's `.model_dump()` and `.model_dump_json()` for output
- Apply `msgspec` for high-performance serialization when Pydantic overhead matters
- Use `orjson` for fast JSON encoding/decoding in hot paths
- Define explicit serialization schemas; avoid exposing internal models directly

## Database & Data Access

### Connection Management

- Use connection pooling for all database access (SQLAlchemy, asyncpg, psycopg3)
- Apply async database drivers for async applications
- Set connection timeouts, pool sizes, and max overflow limits
- Use context managers for connection and transaction lifecycle
- Implement connection health checks and reconnection logic

### Query Patterns

- Use parameterized queries exclusively; never concatenate SQL strings
- Apply repository pattern to abstract data access from business logic
- Use database migrations (Alembic) for schema changes
- Implement optimistic locking with version columns for concurrent updates
- Use bulk operations (`executemany`, `COPY`) for batch inserts/updates
- Apply read replicas for read-heavy workloads

### ORM Best Practices

- Use SQLAlchemy 2.0+ with modern `select()` syntax
- Apply eager/lazy loading strategies intentionally to avoid N+1 queries
- Use `mapped_column` and `Mapped` type annotations for models
- Keep ORM models separate from domain/API models

## Caching Architecture

### Application Caching

- Use `functools.cache` for unbounded memoization and `functools.lru_cache` for bounded
- Apply `cachetools` for TTL, LFU, and LRU caching with size limits
- Use Redis or Memcached for distributed caching across processes
- Implement cache invalidation strategies: TTL, event-driven, write-through
- Apply cache-aside (lazy loading) pattern as the default strategy
- Use `@cached_property` for expensive computed attributes on instances

### HTTP Caching

- Set proper `Cache-Control`, `ETag`, and `Last-Modified` headers
- Implement conditional GET with `If-None-Match` / `If-Modified-Since`
- Use CDN caching for static assets and public API responses
- Apply `Vary` headers for content negotiation caching

## Design Patterns

### Creational Patterns

- Use factory functions or `__init_subclass__` over complex class factories
- Apply the builder pattern with method chaining for complex object construction
- Use dependency injection via constructor parameters (not service locators)
- Apply singleton pattern sparingly; prefer module-level instances

### Structural Patterns

- Use `Protocol` for interface definitions and structural subtyping
- Apply adapter pattern for integrating third-party libraries
- Use facade pattern to simplify complex subsystem interfaces
- Apply composite pattern for tree-structured data

### Behavioral Patterns

- Use strategy pattern with callable protocols or first-class functions
- Apply observer pattern with `asyncio.Event` or callback registries
- Use command pattern for undoable or queueable operations
- Apply state machines (`transitions` library or custom) for complex workflows
- Use chain of responsibility for middleware and request processing pipelines

## Dependency & Configuration Management

### Dependency Management

- Use `uv` as the package installer and resolver for speed and correctness
- Pin all dependencies with lockfiles (`uv.lock`, `requirements.txt`)
- Separate production, development, and test dependencies
- Audit dependencies for vulnerabilities with `pip-audit` or `safety`
- Minimize dependency count; prefer stdlib solutions when adequate
- Use virtual environments for all projects; never install globally

### Configuration

- Use `pydantic-settings` for typed, validated configuration
- Follow 12-factor app principles: externalize config via environment variables
- Support `.env` files for local development only
- Use separate configuration profiles for dev, staging, production
- Never hardcode secrets, URLs, or environment-specific values
- Validate all configuration at startup; fail fast on invalid config

## CI/CD & Tooling

### Code Quality

- Use `ruff` for linting and formatting (replaces flake8, isort, black)
- Enforce strict type checking with `mypy --strict` or `pyright`
- Run `ruff check` and `ruff format` in pre-commit hooks
- Use `pre-commit` framework for consistent git hook management
- Apply `bandit` for security-focused static analysis
- Enforce 100% type annotation coverage on public APIs

### Build & Release

- Use `uv` for dependency resolution, virtual environment management, and builds
- Apply semantic versioning for all packages and services
- Use `pyproject.toml` as the single source of project metadata (PEP 621)
- Automate releases with changelog generation from conventional commits
- Build reproducible artifacts with pinned dependencies and lockfiles
- Run tests, type checks, and linting in CI on every pull request

### Containerization

- Use multi-stage Docker builds to minimize image size
- Run as non-root user in containers
- Pin base image digests for reproducibility
- Use `.dockerignore` to exclude unnecessary files
- Set resource limits (memory, CPU) in container orchestration
- Apply health check instructions in Dockerfiles
