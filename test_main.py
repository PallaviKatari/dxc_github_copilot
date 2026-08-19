import pytest
from fastapi.testclient import TestClient
from app.main import app, COUNTRIES


@pytest.fixture
def client():
    """Fixture to create a TestClient for the FastAPI app"""
    return TestClient(app)


class TestReadRoot:
    """Test suite for the root endpoint"""
    
    def test_read_root_status_code(self, client):
        """Test that the root endpoint returns status code 200"""
        response = client.get("/")
        assert response.status_code == 200
    
    def test_read_root_response_content(self, client):
        """Test that the root endpoint returns the expected message"""
        response = client.get("/")
        data = response.json()
        assert data == {"message": "Countries API is running"}
    
    def test_read_root_response_type(self, client):
        """Test that the root endpoint returns a dictionary"""
        response = client.get("/")
        assert isinstance(response.json(), dict)
    
    def test_read_root_has_message_key(self, client):
        """Test that the response contains 'message' key"""
        response = client.get("/")
        data = response.json()
        assert "message" in data


class TestListCountries:
    """Test suite for the countries endpoint"""
    
    def test_list_countries_status_code(self, client):
        """Test that the countries endpoint returns status code 200"""
        response = client.get("/countries")
        assert response.status_code == 200
    
    def test_list_countries_response_content(self, client):
        """Test that the countries endpoint returns the expected countries list"""
        response = client.get("/countries")
        data = response.json()
        assert data == {"countries": COUNTRIES}
    
    def test_list_countries_has_correct_key(self, client):
        """Test that the response contains 'countries' key"""
        response = client.get("/countries")
        data = response.json()
        assert "countries" in data
    
    def test_list_countries_returns_list(self, client):
        """Test that countries value is a list"""
        response = client.get("/countries")
        data = response.json()
        assert isinstance(data["countries"], list)
    
    def test_list_countries_count(self, client):
        """Test that the correct number of countries is returned"""
        response = client.get("/countries")
        data = response.json()
        assert len(data["countries"]) == len(COUNTRIES)
        assert len(data["countries"]) == 11
    
    def test_list_countries_contains_expected_countries(self, client):
        """Test that the response contains specific expected countries"""
        response = client.get("/countries")
        data = response.json()
        countries = data["countries"]
        
        assert "Australia" in countries
        assert "Brazil" in countries
        assert "United States" in countries
        assert "India" in countries
    
    def test_list_countries_no_duplicates(self, client):
        """Test that there are no duplicate countries in the list"""
        response = client.get("/countries")
        data = response.json()
        countries = data["countries"]
        assert len(countries) == len(set(countries))


class TestAppMetadata:
    """Test suite for the FastAPI app metadata"""
    
    def test_app_title(self):
        """Test that the app has the correct title"""
        assert app.title == "Countries API"
    
    def test_app_version(self):
        """Test that the app has the correct version"""
        assert app.version == "1.0.0"
    
    def test_countries_constant_is_list(self):
        """Test that COUNTRIES is a list"""
        assert isinstance(COUNTRIES, list)
    
    def test_countries_constant_not_empty(self):
        """Test that COUNTRIES list is not empty"""
        assert len(COUNTRIES) > 0
