import requests

ACCESS_TOKEN = "YOUR_LONG_LIVED_ACCESS_TOKEN"
IG_USER_ID = "YOUR_IG_BUSINESS_OR_CREATOR_ID"
BASE_URL = "https://graph.facebook.com/v21.0"

# Example 1: Get account insights
endpoint = f"{BASE_URL}/{IG_USER_ID}/insights"
params = {
    "metric": "impressions,reach,follower_count",
    "period": "day",
    "access_token": ACCESS_TOKEN
}
response = requests.get(endpoint, params=params)
print(response.json())

# Example 2: Check publishing limit
endpoint = f"{BASE_URL}/{IG_USER_ID}/content_publishing_limit"
params = {"access_token": ACCESS_TOKEN}
response = requests.get(endpoint, params=params)
print(response.json())


# Account Insights API
endpoint = f"{BASE_URL}/{IG_USER_ID}/insights"
params = {
    "metric": "impressions,reach,follower_count",
    "period": "day",
    "access_token": ACCESS_TOKEN
}
response = requests.get(endpoint, params=params)
print(response.json())

# Media Insights API
MEDIA_ID = "YOUR_MEDIA_ID"
endpoint = f"{BASE_URL}/{MEDIA_ID}/insights"
params = {
    "metric": "impressions,reach,engagement",
    "access_token": ACCESS_TOKEN
}
response = requests.get(endpoint, params=params)
print(response.json())

# Hashtag Search API
endpoint = f"{BASE_URL}/ig_hashtag_search"
params = {"user_id": IG_USER_ID, "q": "travel", "access_token": ACCESS_TOKEN}
response = requests.get(endpoint, params=params)
print(response.json())

# Get recent media for hashtag
HASHTAG_ID = "YOUR_HASHTAG_ID"
endpoint = f"{BASE_URL}/{HASHTAG_ID}/recent_media"
params = {"user_id": IG_USER_ID, "fields": "id,caption,like_count", "access_token": ACCESS_TOKEN}
response = requests.get(endpoint, params=params)
print(response.json())

# Business Discovery API
target_user = "dosa"
fields = "business_discovery.username({}){{followers_count,media_count}}".format(target_user)
endpoint = f"{BASE_URL}/{IG_USER_ID}"
params = {"fields": fields, "access_token": ACCESS_TOKEN}
response = requests.get(endpoint, params=params)
print(response.json())

# Content Publishing API
# Step 1: Create media container
endpoint = f"{BASE_URL}/{IG_USER_ID}/media"
params = {
    "image_url": "https://example.com/test.jpg",
    "caption": "Posted via API",
    "access_token": ACCESS_TOKEN
}
container = requests.post(endpoint, data=params).json()
print(container)

# Step 2: Publish container
creation_id = container.get("id")
endpoint = f"{BASE_URL}/{IG_USER_ID}/media_publish"
params = {"creation_id": creation_id, "access_token": ACCESS_TOKEN}
publish = requests.post(endpoint, data=params).json()
print(publish)

# Publishing Limit API
endpoint = f"{BASE_URL}/{IG_USER_ID}/content_publishing_limit"
params = {"access_token": ACCESS_TOKEN}
response = requests.get(endpoint, params=params)
print(response.json())