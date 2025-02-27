from amazon_photos import AmazonPhotos

# Initialize the AmazonPhotos object with your cookies
ap = AmazonPhotos(cookies={
    'ubid-main': 'your_ubid_main',
    'at-main': 'your_at_main',
    'session-id': 'your_session_id'
})

# Search for photos by year
year = 2023
photos = ap.query(f"timeYear:{year}")

# Download photos
for photo in photos:
    ap.download_photo(photo['id'], f'path/to/save/{photo["name"]}')
