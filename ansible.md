cat vars
```
openshift:
 - name: lab
   admins:
     - rajlabA
     - tomtomlabA
     - hulolabA
   viewers:
     - rajlabV
     - tomlabV
 - name: prod
   #admins:
   viewers:
      - rajprodV
      - tomprodV
```      


cat test.yaml
```
- hosts: localhost
  tasks:
    - include_vars: vars
    - debug: msg="envirnment is {{ item.0.name }} and uer is {{ item.1  }}"
      with_subelements:
        - "{{ openshift }}"
        - admins
        - flags:
          skip_missing: true
```
**OR**

cat test.yaml
```
- hosts: localhost
  tasks:
    - include_vars: vars
    - debug: msg="envirnment is {{ item.0.name }} and uer is {{ item.1  }}"
      loop: "{{ q('subelements', openshift, 'admins', {'skip_missing': True}) }}"
```



