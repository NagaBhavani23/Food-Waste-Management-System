# Real-Time Location Tracking Feature Documentation

## 📍 Overview
This document covers the real-time location tracking feature that enables NGOs/Receivers to track donor and receiver locations on a map when a food request is accepted.

## 🎯 Features Implemented

### 1. Donor Location Capture
- **Automatic GPS Capture**: Donors can capture their current location using the "Capture My Location" button in the donation form
- **Technology**: HTML5 Geolocation API (`navigator.geolocation.getCurrentPosition()`)
- **Data Stored**: 
  - Latitude (FloatField)
  - Longitude (FloatField)
  - Location Address (CharField - manually entered)

### 2. Receiver Location Capture
- **Automatic GPS Capture**: NGOs can capture their location when requesting food
- **Manual Address Entry**: Optionally enter a manual address
- **Data Stored**: Same as donor location (latitude, longitude, address)

### 3. Database Models
Updated models to include location tracking:

```python
class Donation(models.Model):
    # ... existing fields
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class FoodRequest(models.Model):
    # ... existing fields
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
```

### 4. Map Integration (Leaflet.js)
- **Map Library**: Leaflet.js (Open-source, no API key required)
- **Base Map**: OpenStreetMap tiles
- **Features**:
  - Donor location marker (🍽️ orange)
  - Receiver location marker (🏘️ blue)
  - Route line between locations
  - Auto-zoom to fit both markers
  - Distance display in kilometers

### 5. Distance Calculation
- **Algorithm**: Haversine Formula
- **Formula**: Calculates great-circle distance between two lat/long points
- **Return Value**: Distance in kilometers (rounded to 2 decimal places)
- **Location**: `tracking_views.py` - `haversine_distance()` function

## 🔧 Technical Implementation

### Backend Components

#### 1. **tracking_views.py** (New File)
Contains tracking-related views:
- `track_request(request, request_id)` - Display tracking map
- `save_location(request)` - AJAX endpoint to save GPS coordinates
- `get_location_data(request, request_id)` - AJAX endpoint to fetch location data
- `haversine_distance()` - Calculate distance between coordinates

#### 2. **views.py** (Updated)
- `add_donation()` - Updated to handle latitude/longitude
- `request_food()` - Updated to handle latitude/longitude
- Added imports for tracking functionality

#### 3. **forms.py** (Updated)
- `DonationForm` - Added latitude and longitude hidden fields
- `FoodRequestForm` - Added latitude and longitude hidden fields

#### 4. **urls.py** (Updated)
New URL patterns:
```python
path('track/<int:request_id>/', tracking_views.track_request, name='track_request')
path('api/save-location/', tracking_views.save_location, name='save_location')
path('api/location-data/<int:request_id>/', tracking_views.get_location_data, name='get_location_data')
```

### Frontend Components

#### 1. **add_donation.html** (Enhanced)
- Location capture button with status feedback
- Coordinates display
- Hidden input fields for latitude/longitude
- Geolocation permission handling

#### 2. **request.html** (Enhanced)
- Similar location capture UI for NGOs
- Coordinates display
- Error handling for geolocation issues

#### 3. **track_request.html** (New Template)
- Leaflet.js map integration
- Donor and receiver markers
- Route visualization
- Distance calculation display
- Status information cards
- Mobile-responsive design
- Location coordinates display
- Real-time refresh capability

#### 4. **dashboard.html** (Updated)
- Added "Track" button in NGO food requests table
- Shows tracking link only for approved/accepted requests
- Location status column

## 🗺️ How to Use

### For Donors (Adding Donations)
1. Go to Dashboard → Add New Donation
2. Fill in food details (name, quantity, location, description)
3. Click "📍 Capture My Location" button
4. Grant location permission when prompted
5. See coordinates confirmation
6. Click "Submit Donation"

### For Receivers (NGOs - Requesting Food)
1. Go to Dashboard → Request Food
2. Fill in request details (food type, quantity, location, notes)
3. Click "📍 Capture My Location" button
4. Grant location permission when prompted
5. See coordinates confirmation
6. Click "Submit Request"

### For Tracking
1. After food request is approved/accepted
2. Open Dashboard → My Food Requests
3. Click "🗺️ Track" button for the request
4. View interactive map with:
   - Donor location (🍽️ orange marker)
   - Receiver location (🏘️ blue marker)
   - Route between locations
   - Distance in kilometers
5. Click "📍 Capture My Location" to update position
6. Click "🔄 Refresh Map" to get latest data

## 🔐 Security Features

- **Login Required**: All tracking views require user authentication
- **Authorization Checks**: Only donor or receiver can view tracking data
- **CSRF Protection**: All AJAX requests include CSRF token
- **Data Validation**: Latitude/longitude validation on backend

## 📱 Browser Compatibility

### Geolocation Support
- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Requires HTTPS (except localhost)
- Requires user permission

### Leaflet.js Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Responsive design included

## 📊 Data Flow

```
Donor Submits Donation
    ↓
Captures Location (GPS coords saved to DB)
    ↓
Receiver Views and Claims Donation
    ↓
Captures Their Location (GPS coords saved to DB)
    ↓
Request Approved → Tracking Enabled
    ↓
View Track Button Appears in Dashboard
    ↓
Click Track → See Both Locations on Map
    ↓
Distance Calculated (Haversine Formula)
    ↓
Route Drawn Between Locations
```

## 🔄 Real-Time Updates

The tracking page includes:
- Auto-refresh every 30 seconds for approved requests
- Manual refresh button
- Live status updates
- Both users can update their location anytime

## 📈 Optional Advanced Features (Implemented)

✅ Distance calculation using Haversine formula
✅ Real-time location updates using AJAX
✅ Mobile-responsive map design
✅ Status tracking system
✅ Location coordinates storage

### Future Enhancements
- 🚚 Delivery agent live tracking
- 🔔 Notification when delivery is near
- ⏱️ Estimated delivery time based on distance
- 📝 Delivery proof with photos
- 🚫 Geofencing alerts

## 🛠️ API Endpoints

### Save Location (POST)
```
Endpoint: /api/save-location/
Parameters:
  - latitude: float
  - longitude: float
  - type: 'donation' or 'request'
  - id: integer (donation_id or request_id)

Response: {
  "status": "success|error",
  "message": "string"
}
```

### Get Location Data (GET)
```
Endpoint: /api/location-data/<request_id>/
Response: {
  "donor": {
    "name": "string",
    "location": "string",
    "latitude": float,
    "longitude": float
  },
  "receiver": {
    "name": "string",
    "location": "string",
    "latitude": float,
    "longitude": float
  },
  "distance": float,
  "status": "string"
}
```

## 🐛 Troubleshooting

### Location Not Capturing
- Check browser geolocation permissions
- Ensure HTTPS (or localhost for development)
- Check browser console for errors

### Map Not Loading
- Check internet connection
- Verify Leaflet CDN is accessible
- Clear browser cache

### Distance Shows "Locations not set"
- One or both parties haven't captured location yet
- Click "Capture My Location" button
- Both locations must be captured for distance display

## 📝 Database Migrations

Migrations automatically created:
```
foodwaste_project/foodapp/migrations/0003_donation_latitude_...
```

To apply:
```bash
python manage.py migrate
```

## 📦 Dependencies

- **Leaflet.js**: 1.9.4 (CDN)
- **OpenStreetMap**: Free tile layer (no API key needed)
- **Python**: math module (Haversine calculation)
- **Django**: Built-in geolocation via HTML5 API

## 🎨 UI/UX Features

- Color-coded status badges
- Emoji icons for easy identification
- Responsive grid layouts
- Status cards with distance display
- Toast-style notifications
- Mobile-friendly interface
- Smooth transitions and hover effects

## 📞 Support

For issues or questions about location tracking:
1. Check browser console for JavaScript errors
2. Verify database migrations applied
3. Ensure location permissions granted
4. Check network tab for API failures
5. Review server logs for backend errors

---

**Last Updated**: February 25, 2026
**Version**: 1.0
**Status**: Production Ready ✅
