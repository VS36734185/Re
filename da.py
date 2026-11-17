import requests as req
def compare_heroes(id1, id2):
    token = "cc66b250623cfeb0c5fcd1d841b0cc3"
    url = f'https://superheroapi.com/api/{token}/{{}}'

    def get_data(h_id):
        response = req.get(url.format(h_id))
        d = response.json() if response.status_code == 200 else {}
        return d if d.get('response') == 'success' else None

    h1, h2 = get_data(id1), get_data(id2)
    print(h1,h2)
    if not h1 or not h2: return

    print(f" {h1['name']} VS {h2['name']}\n")

    keys = (h1['powerstats']) | set(h2['powerstats'])
    for k in keys:
        v1 = h1['powerstats'].get(k, 'N/A')
        v2 = h2['powerstats'].get(k, 'N/A')
        v1 = v1 if v1.isdigit() else 'N/A'
        v2 = v2 if v2.isdigit() else 'N/A'
compare_heroes('1','2')
       