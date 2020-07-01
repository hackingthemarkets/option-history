## Capture option price history to SQLite using Tradier API

### Run every minute

```
* * * * * /Users/larry/Projects/venv/bin/python /Users/larry/Projects/scheduling/snapshot.py >> snapshot.log 2>&1
```

### Run every 10 minutes

```
*/10 * * * * 
```
