resource "cloudflare_record" "terraform_managed_resource_132799f6599e6375bb28bff6b9ce40e3" {
  name    = "terraform"
  proxied = true
  ttl     = 1
  type    = "A"
  value   = "192.0.2.1"
  zone_id = "9806ceb9d6d2303f90e5435ab8bcb4a2"
}