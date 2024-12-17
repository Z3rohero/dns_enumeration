import dns.resolver

#Definidmo el nombre de dominio 
target_domain = "udemy.com"
record_types=["A","AAA","CNAME","MX","NS","SOA","TXT"]

#Creamos un DNS resolver 
resolver = dns.resolver.Resolver()

for record_type in record_types:
    try:
        answer = resolver.resolve(target_domain,record_type)

    except dns.resolver.NoAnswer:
        continue

    print(f"{record_type} registros para {target_domain}") 
    for data in answer:
        print(f"{data}")