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
{% if ips is defined and ips[0] is defined %}
{{ ips[0] }}
{% endif %}
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
{% if firewall_rule is defined %}
{{ firewall_rule.cidr }}
{% endif %}
```
- firewall_rule.port: 
```
{% if firewall_rule is defined %}
{{ firewall_rule.port }}
{% endif %}
```

## List Object
- buckets: 
```
{{ buckets }}
```
- buckets[0]:
```
{% if firewall_rule is defined %}
{{ buckets[0] }}
{% endif %}
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
{% if bucket_requerido_raiz is defined %}
{{ bucket_requerido_raiz.selected }}
{% endif %}
```

- bucket_requerido_raiz.type
```
{% if bucket_requerido_raiz is defined %}
{{ bucket_requerido_raiz.type }}
{% endif %}
```

# Required Connection (deploy only)
- bucket_requerido_raiz.connection
```
{% if bucket_requerido_raiz is defined %}
{{ bucket_requerido_raiz.connection }}
{% endif %}
```

- bucket_requerido_raiz.connection.arn
```
{% if bucket_requerido_raiz is defined %}
{{ bucket_requerido_raiz.connection.arn }}
{% endif %}
```
- bucket_requerido_raiz.connection.name
```
{% if bucket_requerido_raiz is defined %}
{{ bucket_requerido_raiz.connection.name }}
{% endif %}
```