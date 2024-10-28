import slurpit
import pytest
import asyncio
import json
from slurpit.models.site import Site 

host = "https://sandbox.slurpit.io/"
api_key = "4DTIz5axkWqOuxUGm6gobN4JAaB4l5Cg16589a08019c20"

# Initialize an API client instance with the configured host and API key
api = slurpit.api(host, api_key)

@pytest.mark.asyncio
async def test_get_sites():
    sites = await api.site.get_sites()
    
    sites_data = [site.__dict__ for site in sites]
    print("Retrieved sites:")
    print(json.dumps(sites_data, indent=2))

if __name__ == "__main__":
    asyncio.run(test_get_sites())
