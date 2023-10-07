import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('dictojson.json', 'w', encoding='utf-8') as f:
    json.dump(person,f,ensure_ascii=False, indent=4)
