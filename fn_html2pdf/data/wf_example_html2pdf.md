<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Example: HTML2PDF

## Function - HTML to PDF

### API Name
`fn_html2pdf`

### Output Name
`pdf`

### Message Destination
`fn_html2pdf`

### Pre-Processing Script
```python
None
```

### Post-Processing Script
```python
# results in base64. see output property 'content':
# results.content
# or use workflow properties, such as 'pdf', when using this function with another function such as utilities: base64 to attachment:
# inputs.base64content = workflow.properties.pdf.content
```

---

