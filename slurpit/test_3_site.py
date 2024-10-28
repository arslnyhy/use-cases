import slurpit  # Import the slurpit library, which is assumed to contain API client functionalities.
import pytest
import asyncio
from slurpit.models.site import Site

# Configuration setup: update these values to your actual API connection settings.
host = "http://portal_test"  # Specify the API host address.
api_key = "1234567890abcdefghijklmnopqrstuvwxqz"  # Provide the API key.

# Initialize an API client instance with the configured host and API key.
api = slurpit.api(host, api_key)  

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope='module')
def shared_data():
    data = {}  # Initialize an empty dictionary to store data
    yield data  # This will be passed to each test function that requests this fixture

@pytest.mark.asyncio
async def test_create_site(shared_data):
    new_data = {
        "sitename": "The Simpsons",
        "status": "1",
        "description": "The Simpsons family home",
        "street": "742 Evergreen Terrace",
        "number": "",
        "zipcode": "",
        "country": "USA",
        "phonenumber": ""
    }
    new_site = await api.site.create_site(new_data)
    shared_data.update(vars(new_site))
    assert isinstance(new_site, Site)

# Retrieve sites
@pytest.mark.asyncio
async def test_get_sites():
    sites = await api.site.get_sites()
    assert all(isinstance(site, Site) for site in sites)

@pytest.mark.asyncio
async def test_save_csv():
    sites_csvdata = await api.site.get_sites(export_csv=True)
    result = api.site.save_csv_bytes(sites_csvdata, "csv/sites.csv")
    assert result == True, "Failed to save csv file"

# Updating a site's details.
@pytest.mark.asyncio
async def test_update_site(shared_data):
    update_data = {
        "sitename": "The White House",
        "status": "1",
        "description": "",
        "street": "1600 Pennsylvania Avenue",
        "number": "",
        "zipcode": "20500",
        "country": "USA",
        "phonenumber": "",
    }
    updated_site = await api.site.update_site(shared_data['id'], update_data)
    shared_data.update(vars(updated_site))
    assert isinstance(updated_site, Site)

# Fetching a specific site by its ID.
@pytest.mark.asyncio
async def test_get_site(shared_data):
    site = await api.site.get_site(shared_data['id'])
    assert isinstance(site, Site)

# Deleting a site by its ID.
@pytest.mark.asyncio
async def test_delete_site(shared_data):
    deleted_site = await api.site.delete_site(shared_data['id'])
    assert isinstance(deleted_site, Site)