# Tg-Truth-Dare

# Examples
## Installing Package
```
$ sh pip3 install -U TruthDarePy
```

# Truth In English
```python3
from TruthDarePy import TD
love = TD()
print(love.truth["question"])
```
## Truth In Bangala
```python3
from TruthDarePy import TD
love = TD()
print(love.truth["bangala"])
```

# Dare In English
```python3
from TruthDarePy import TD
love = TD()
print(love.dare["question"])
```

## Dare In Bangala
```python3
from TruthDarePy import TD
love = TD()
print(love.dare["bn"])
```

# Get Available Languages
```python3
from TruthDarePy import TD
love = TD()
print(love.languages())
```

# Output
```
• English - question
• বাংলা (Bengali) - bn
• Deutsch (German) - de
• Español (Spanish) - ea
• Français (French) - fr
• हिंदी (Hindi) - hi
• Tagalog (Filipino) - tl
```
