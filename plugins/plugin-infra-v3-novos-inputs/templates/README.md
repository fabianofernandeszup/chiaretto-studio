## StackSpot Plugin

## Jinja

You can use jinja to make a template-data folder more dynamic.

complete documentation of jinja: https://jinja.palletsprojects.com/en/3.0.x/templates/

### Example Inputs:
- Resource: {{ resource }}
- Method: {{ method }}

## List
- ips: 
```
{{ ips }}
```
- ips[0]:
```
{{ ips[0] }}
```
- for ip in ips
```
{% for ip in ips %}
- ip: {{ ip }} 
{% endfor %}
```

## Object
- firewall_rule: 
```
{{ firewall_rule }}
```
- firewall_rule.cidr: 
```
{{ firewall_rule.cidr }}
```
- firewall_rule.port: 
```
{{ firewall_rule.port }}
```

## List Object
- buckets: 
```
{{ buckets }}
```
- buckets[0]:
```
{{ buckets[0] }}
```
- for bucket in buckets
```
{% for bucket in buckets %}
- bucket.description: {{ bucket.description }} 
- bucket.number: {{ bucket.number }} 
- bucket.encrypted: {{ bucket.encrypted }} 
- bucket.region: {{ bucket.region }} 
- bucket.region_bkp: {{ bucket.region_bkp }} 
- bucket.bucket-requerido-raiz.selected: {{ bucket.bucket-requerido-raiz.selected }} 
- bucket.bucket-requerido-raiz.type: {{ bucket.bucket-requerido-raiz.type }} 
-----
{% endfor %}
```

## Required Connection
- bucket-requerido-raiz.selected
```
{{ bucket-requerido-raiz.selected }}
```

- bucket-requerido-raiz.type
```
{{ bucket-requerido-raiz.type }}
```

# Required Connection (deploy only)
- bucket-requerido-raiz.connection.arn
```
{{ bucket-requerido-raiz.connection.arn }}
```
- bucket-requerido-raiz.connection.name
```
{{ bucket-requerido-raiz.connection.name }}
```