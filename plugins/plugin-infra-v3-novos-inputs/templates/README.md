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
- bucket.bucket_requerido_object.selected: {{ bucket.bucket_requerido_object.selected }} 
- bucket.bucket_requerido_object.type: {{ bucket.bucket_requerido_object.type }} 
-----
{% endfor %}
```

## Required Connection
- bucket_requerido_raiz.selected
```
{{ bucket_requerido_raiz.selected }}
```

- bucket_requerido_raiz.type
```
{{ bucket_requerido_raiz.type }}
```

# Required Connection (deploy only)
- bucket_requerido_raiz.connection
```
{{ bucket_requerido_raiz.connection }}
```

- bucket_requerido_raiz.connection.arn
```
{{ bucket_requerido_raiz.connection.arn }}
```
- bucket_requerido_raiz.connection.name
```
{{ bucket_requerido_raiz.connection.name }}
```