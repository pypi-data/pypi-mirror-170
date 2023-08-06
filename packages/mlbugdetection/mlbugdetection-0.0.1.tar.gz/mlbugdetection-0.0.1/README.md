# MLBugDetection

# Functions



1. Monotonic:

    `from mlbugdetection import monotonic`

    Usage:
    
    `check_monotonicity(feature, min, max, sample, model, steps=100)`

2. Critical Values:

    `from mlbugdetection import critical_values`
    
    Usage:
    
    `find_critical_values(model, sample, feature, limit, border, step=100)`


3. Calibration:
    
    `from mlbugdetection import calibration`
    
    Usage:    
    `calibration_check(target_col, model, df)`

4. Sanity:

    `from mlbugdetection import sanity`

    Usage:

    `sanity_check(model, examples, target_column)`


---

## Virtual Environment with Jupyter Notebook

```bash
python3 -m virtualenv venv 
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```