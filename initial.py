
import gzip
with gzip.open('weather.json.gz', 'rb') as f:
    file_content = f.read()

my_bytes = file_content.decode('utf8').split('\n')
for data in my_bytes:

