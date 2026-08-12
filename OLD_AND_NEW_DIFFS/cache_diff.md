# cache — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `cache` |
| **Old file** | `cache/old/ballerina_cache.bal.txt` |
| **New file** | `cache/new/ballerina_cache.bal.txt` |
| **Old lines** | 78 |
| **New lines** | 180 |
| **Lines added** | 104 |
| **Lines removed** | 2 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 3 | 3 |

### Declarations added (11)

- `class Cache`
- `function capacity`
- `function get`
- `function hasKey`
- `function init`
- `function invalidate`
- `function invalidateAll`
- `function keys`
- `function put`
- `function size`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 48–53 | 48–86 | Types | +33 | −0 |
| 2 | 55–70 | 88–107 | Types | +4 | −0 |
| 3 | 73–78 | 110–180 | Types | +67 | −2 |

---

## Unified diff

`````diff
--- cache/old/ballerina_cache.bal.txt	2026-08-12 23:21:51
+++ cache/new/ballerina_cache.bal.txt	2026-08-12 23:23:51
@@ -48,6 +48,39 @@
 # The `cache:AbstractCache` object is used for custom implementations of the Ballerina cache.
 # Any custom cache implementation should be object-wise similar.
 class AbstractCache {
+
+    # Adds the given key value pair to the cache. If the cache previously contained a value associated with the key, the
+    # old value is replaced by the new value.
+    # 
+    function put(string key, any value, decimal maxAge = -1) returns Error|();
+
+    # Returns the cached value associated with the provided key.
+    # 
+    function get(string key) returns any|Error;
+
+    # Discards a cached value from the cache.
+    # 
+    function invalidate(string key) returns Error|();
+
+    # Discards all the cached values from the cache.
+    # 
+    function invalidateAll() returns Error|();
+
+    # Checks whether the given key has an associated cache value.
+    # 
+    function hasKey(string key) returns boolean;
+
+    # Returns all keys from the cache.
+    # 
+    function keys() returns string[];
+
+    # Returns the current size of the cache.
+    # 
+    function size() returns int;
+
+    # Returns the capacity of the cache.
+    # 
+    function capacity() returns int;
 }
 
 # Represents configurations for the `cache:Cache` object.
@@ -55,16 +88,20 @@
 
 type CacheConfig record {
     # Maximum number of entries allowed in the cache
+    @constraint:Int { minValue: 1 }
     int capacity?;
     # The factor by which the entries will be evicted once the cache is full
+    @constraint:Float { minValueExclusive: 0, maxValue: 1 }
     float evictionFactor?;
     # The policy which is used to evict entries once the cache is full
     EvictionPolicy evictionPolicy?;
     # The max-age in seconds which all the cache entries are valid. '-1' means, the entries are
 valid forever. This will be overwritten by the `maxAge` property set when inserting item into
 the cache
+    @constraint:Number { minValue: -1 }
     decimal defaultMaxAge?;
     # Interval (in seconds) of the timer task, which will clean up the cache
+    @constraint:Number { minValueExclusive: 0 }
     decimal cleanupInterval?;
 };
 
@@ -73,6 +110,71 @@
     LRU
 }
 
-// Unknown type: Error
+# Represents Cache related errors. This will be returned if an error occurred while doing any of the cache operations.
+type Error error;
 
-// Unknown type: Cache
+# Initializes new `cache:Cache` instance.
+# ```ballerina
+# cache:Cache cache = new(capacity = 10, evictionFactor = 0.2);
+# ```
+# 
+class Cache {
+    function init(int capacity = 100, float evictionFactor = 0.25, EvictionPolicy evictionPolicy = LRU, decimal defaultMaxAge = -1, decimal cleanupInterval = 0.0d, CacheConfig cacheConfig) returns ();
+
+    # Adds the given key value pair to the cache. If the cache previously contained a value associated with the
+    # provided key, the old value will be replaced by the newly-provided value.
+    # ```ballerina
+    # check cache.put("Hello", "Ballerina");
+    # ```
+    # 
+    function put(string key, any value, decimal maxAge = 0.0d) returns Error|();
+
+    # Returns the cached value associated with the provided key.
+    # ```ballerina
+    # any value = check cache.get(key);
+    # ```
+    # 
+    function get(string key) returns any|Error;
+
+    # Discards a cached value from the cache.
+    # ```ballerina
+    # check cache.invalidate(key);
+    # ```
+    # 
+    function invalidate(string key) returns Error|();
+
+    # Discards all the cached values from the cache.
+    # ```ballerina
+    # check cache.invalidateAll();
+    # ```
+    # 
+    function invalidateAll() returns Error|();
+
+    # Checks whether the given key has an associated cached value.
+    # ```ballerina
+    # boolean result = cache.hasKey(key);
+    # ```
+    # 
+    function hasKey(string key) returns boolean;
+
+    # Returns a list of all the keys from the cache.
+    # ```ballerina
+    # string[] keys = cache.keys();
+    # ```
+    # 
+    function keys() returns string[];
+
+    # Returns the size of the cache.
+    # ```ballerina
+    # int result = cache.size();
+    # ```
+    # 
+    function size() returns int;
+
+    # Returns the capacity of the cache.
+    # ```ballerina
+    # int result = cache.capacity();
+    # ```
+    # 
+    function capacity() returns int;
+}
`````
