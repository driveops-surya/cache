# GitHub Actions Caching Demo

This repository demonstrates various caching concepts and strategies in GitHub Actions.

## Caching Examples Included

### 1. Basic Dependency Caching
- Caches `node_modules` based on `package-lock.json`
- Shows cache hit/miss behavior
- Demonstrates time savings

### 2. Multi-Path Caching  
- Caches multiple directories in a single action
- Useful for complex build processes
- Includes build artifacts and dependencies

### 3. Matrix Strategy Caching
- Shows caching across different Node.js versions
- Demonstrates cache key strategies for matrix builds
- Uses fallback keys for better cache utilization

### 4. Cross-Language Caching
- Python pip cache example
- Model/data file caching
- Custom cache paths

### 5. Performance Testing
- Compares build times with and without cache
- Measures cache effectiveness
- Demonstrates cache hit benefits

## Key Caching Concepts

### Cache Keys
```yaml
key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```
- Should be unique for different cache contents
- Use file hashes for dependency-based caching
- Include OS and relevant environment variables

### Restore Keys
```yaml
restore-keys: |
  ${{ runner.os }}-node-
  ${{ runner.os }}-
```
- Fallback when exact key match fails
- Enables partial cache reuse
- Order matters (most specific first)

### Cache Paths
```yaml
path: |
  node_modules
  dist
  ~/.cache
```
- Can specify single path or multiple paths
- Use absolute or relative paths
- Consider cache size limits (10GB per repository)

## Best Practices

1. **Use specific cache keys** - Include file hashes for dependencies
2. **Implement fallback keys** - Enable partial cache reuse
3. **Cache early in workflow** - Before expensive operations
4. **Monitor cache hit rates** - Optimize key strategies
5. **Clean up regularly** - Manage cache storage limits

## Running the Demo

1. Fork this repository
2. Push changes to trigger workflows
3. Check Actions tab for cache behavior
4. Compare run times between cache hits and misses

## Cache Locations by Technology

| Technology | Typical Cache Paths |
|-----------|-------------------|
| Node.js | `node_modules`, `~/.npm` |
| Python | `~/.cache/pip`, `__pycache__` |
| Java | `~/.m2`, `~/.gradle` |
| Go | `~/go/pkg/mod` |
| Rust | `~/.cargo`, `target/` |

## Monitoring Cache Performance

Use workflow outputs to track:
- Cache hit/miss rates
- Build time improvements
- Cache size growth
- Storage usage patterns

## Workflow Structure

The demo includes two main workflows:

1. **caching-demo.yml** - Main demonstration with 5 different caching scenarios
2. **cache-cleanup.yml** - Shows cache management and cleanup strategies

Each job in the workflow demonstrates different aspects of caching:

- **dependency-caching**: Basic npm dependency caching
- **multi-path-caching**: Caching multiple directories at once
- **conditional-caching**: Matrix builds with version-specific caches
- **custom-cache-demo**: Python dependencies and model file caching
- **cache-performance-test**: Performance comparison with timing

## Files in This Demo

- `.github/workflows/caching-demo.yml` - Main caching demonstration workflow
- `.github/workflows/cache-cleanup.yml` - Cache management workflow
- `package.json` - Node.js dependencies for caching demos
- `requirements.txt` - Python dependencies for pip caching
- `scripts/download-models.py` - Simulates downloading large files/models
- `README.md` - This documentation

## Advanced Caching Strategies

### 1. Hierarchical Cache Keys
```yaml
key: ${{ runner.os }}-${{ matrix.node-version }}-${{ hashFiles('package-lock.json') }}
restore-keys: |
  ${{ runner.os }}-${{ matrix.node-version }}-
  ${{ runner.os }}-
```

### 2. Branch-Specific Caching
```yaml
key: ${{ github.ref }}-${{ hashFiles('**/*.js') }}
```

### 3. Time-Based Cache Invalidation
```yaml
key: ${{ runner.os }}-weekly-${{ github.run_number }}
```

### 4. Conditional Cache Usage
```yaml
- name: Cache dependencies
  if: github.event_name != 'schedule'
  uses: actions/cache@v3
```

This comprehensive demo provides practical examples of how to implement effective caching strategies in your GitHub Actions workflows, helping reduce build times and improve CI/CD efficiency.