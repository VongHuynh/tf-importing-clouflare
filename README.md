# Install cf-terraforming for importing
```
brew tap cloudflare/cloudflare
brew install cloudflare/cloudflare/cf-terraforming
```
refer document: https://developers.cloudflare.com/terraform/advanced-topics/import-cloudflare-resources/

# if using API Token
```
export CLOUDFLARE_API_TOKEN='Hzsq3Vub-7Y-hSTlAaLH3Jq_YfTUOCcgf22_Fs-j'
```

# if using API Key
```
export CLOUDFLARE_EMAIL='user@example.com'
export CLOUDFLARE_API_KEY='1150bed3f45247b99f7db9696fffa17cbx9'
```
# specify zone ID
```
export CLOUDFLARE_ZONE_ID='81b06ss3228f488fh84e5e993c2dc17'
```
# now call cf-terraforming, e.g.
```
cf-terraforming generate \
  --resource-type "cloudflare_record" \
  --zone $CLOUDFLARE_ZONE_ID
```
## OR
```
cf-terraforming generate --email $CLOUDFLARE_EMAIL --token $CLOUDFLARE_API_TOKEN -z 9806ceb9d6d2303f90e5435ab8bcb4a2 --resource-type cloudflare_record > importing-example.tf
```

## OR
```
cf-terraforming generate --email $CLOUDFLARE_EMAIL --token $CLOUDFLARE_API_TOKEN -z 9806ceb9d6d2303f90e5435ab8bcb4a2 --resource-type cloudflare_record > importing-example.tf
```
#### and
```
python3 import.py
```