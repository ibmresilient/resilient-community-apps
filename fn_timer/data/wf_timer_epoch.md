<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Timer: Epoch

## Function - Timer

### API Name
`fn_timer`

### Output Name
`None`

### Message Destination
`fn_timer`

### Pre-Processing Script
```python
# Get the input date/time for timer end from the rule activity field
inputs.timer_epoch = rule.properties.timer_end_time
```

### Post-Processing Script
```python
None
```

---

