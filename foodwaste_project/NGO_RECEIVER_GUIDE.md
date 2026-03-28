# NGO Receiver Dashboard - Complete Guide

## Overview

The **NGO Receiver Dashboard** is a specialized interface designed for NGOs (Non-Governmental Organizations) to easily browse available food donations, send requests, and track the status of their food requests.

## Features

### 1. **View Available Food Donations**
- Browse all currently available donations from donors
- See detailed information:
  - Food name and type
  - Quantity available
  - Pickup location
  - Donor contact information
  - Food description
  - Post date and time
- Real-time updates of donation availability

### 2. **Send Food Requests**
- One-click request functionality
- Automatic duplicate request prevention
- Confirmation messages for submitted requests
- Links to donation details for more information

### 3. **Track Request Status**
NGO can monitor their food requests with status indicators:
- **⏳ Pending**: Awaiting donor response
- **✅ Approved**: Donor has approved the request
- **❌ Rejected**: Donor declined the request
- **🏁 Completed**: Request fulfilled

### 4. **Dashboard Statistics**
Quick overview cards showing:
- Total available donations count
- Total requests sent
- Pending requests count
- Approved requests count

## How to Access

### Step 1: Login
1. Go to http://127.0.0.1:8000/login/
2. Enter your NGO credentials
3. Click "Login"

### Step 2: Navigate to Receiver Hub
**Option A - From Dashboard:**
- Click "Dashboard" link in navigation
- Click "Receiver Hub" button

**Option B - From Navigation Bar:**
- Direct link: "Receiver Hub" in the navigation menu (for NGO accounts only)

**Option C - Direct URL:**
- Visit: http://127.0.0.1:8000/receiver_dashboard/

## Detailed Workflow

### For NGO Users

#### Step 1: View Available Donations
```
1. Login to your NGO account
2. Click "Receiver Hub" in navigation or dashboard
3. The "Available Food Donations" section displays all donations
4. Each donation card shows:
   - Food Name (e.g., "Rice", "Vegetables")
   - Quantity Available (e.g., "5 kg", "10 servings")
   - Location/Address (pickup point)
   - Donor Name
   - Contact Phone Number
   - Description (if provided)
   - Posted Date and Time
```

#### Step 2: Request Food
```
Option A - Quick Request:
1. Locate a donation you need
2. Click "Request Food" button
3. Confirmation message appears
4. Request appears in "My Food Requests" section

Option B - View Details First:
1. Click "View Details" on a donation
2. Review full donation information
3. Scroll down or navigate back
4. Click "Request Food" button
```

#### Step 3: Track Request Status
```
1. Scroll to "My Food Requests" section
2. View all requests with their current status:
   - Pending: Waiting for donor approval
   - Approved: Donor approved - ready to pickup
   - Rejected: Donor cannot fulfill
   - Completed: Food received
```

#### Step 4: Manage Requests
```
For Pending Requests:
- Wait for donor's response
- Check contact number if clarification needed

For Approved Requests:
- Contact donor using phone number
- Arrange pickup/delivery
- Confirm receipt

For Rejected Requests:
- Review other available donations
- Submit new request to different donor
```

## Dashboard Sections

### 1. Statistics Cards (Top)
```
📦 Donations Available      - Total count of available food items
📋 Total Requests Sent      - All requests you've made
⏳ Pending Requests         - Awaiting donor response
✅ Approved Requests        - Ready for pickup/delivery
```

### 2. Available Food Donations (Left Section)
```
Features:
- Lists all active donations
- Each donation has:
  * Title and details
  * Action buttons (View Details, Request Food)
  * Contact information for donor
  * Posted timestamp

Layout:
- Donation items displayed as cards
- One per row for easy reading
- Hover effects for better UX
- Empty state message if no donations available
```

### 3. My Food Requests (Right Section)
```
Features:
- Lists all requests from this NGO
- Each request shows:
  * Food type requested
  * Status with visual indicator
  * Quantity needed
  * Delivery location
  * Request date
  * Donor contact info
  * Notes (if any)

Status Icons:
⏳ Pending    - Animated hourglass
✅ Approved   - Green checkmark
❌ Rejected   - Red X mark
🏁 Completed  - Flag checkmark

Layout:
- Requests displayed chronologically
- Status indicator on the right
- Empty state message if no requests yet
```

## Workflow Examples

### Example 1: Requesting Rice
```
1. NGO logs in
2. Opens Receiver Hub
3. Sees "5 kg Rice" donation from "John's Restaurant"
4. Clicks "Request Food" for that donation
5. Gets confirmation: "Request sent for Rice! Waiting for donor approval."
6. Request appears in "My Food Requests" with status "Pending"
7. John approves the request
8. Status changes to "Approved"
9. NGO contacts John at provided phone number
10. Arranges pickup
11. Status changes to "Completed"
```

### Example 2: Browsing and Requesting
```
1. Login to NGO account
2. View Available Food Donations section
3. See 3 donations: Rice (5kg), Vegetables (10kg), Bread (8 loaves)
4. Need vegetables most urgently
5. Click "View Details" on Vegetables donation
6. Read description and donor info
7. Navigate back or directly "Request Food"
8. Request submitted successfully
9. Status "Pending" shown in My Food Requests
10. Can continue requesting other donations
```

## Key Features Explained

### 1. Duplicate Request Prevention
The system prevents sending multiple pending requests for the same donation:
- If you've already sent a pending request for a donation
- And try to request it again
- A warning message appears: "You already have a pending request for this donation!"
- Prevents unnecessary duplicates

### 2. Status Tracking
Each request shows real-time status:
- **Pending**: Donor hasn't responded yet
- **Approved**: Donor approved - ready for pickup
- **Rejected**: Donor can't fulfill - try another donation
- **Completed**: Transaction complete

### 3. Donor Contact Information
For each donation and approved request, donor contact is visible:
- Direct phone number to coordinate
- No need for separate messaging system
- Quick coordination for pickup/delivery

### 4. Request Details
Track all request details including:
- Original food type and quantity requested
- Delivery location
- Request timestamp
- Donor contact information
- Special notes or requirements

## Navigation Guide

### From Receiver Dashboard
```
Page URL: http://127.0.0.1:8000/receiver_dashboard/

Navigation Options:
1. "Home" - Go to main page
2. "View Donations" - Browse all donations
3. "Dashboard" - Go to personal dashboard
4. "Receiver Hub" - Refresh current page
5. "Logout" - Exit account
```

### Mobile Responsive
- Dashboard adapts to mobile screens
- Touch-friendly buttons
- Collapse unnecessary details on small screens
- Full functionality on all devices

## Troubleshooting

### Issue: "This page is for NGOs only!"
**Solution**: 
- This page is restricted to NGO accounts
- Your account is registered as a Donor
- Create a new NGO account or contact admin

### Issue: Can't see "Receiver Hub" link
**Solution**:
- You must be logged in as an NGO
- Check if you're logged in as a Donor account
- Navigate directly: http://127.0.0.1:8000/receiver_dashboard/

### Issue: "You already have a pending request for this donation!"
**Solution**:
- You've already sent a request for this donation
- Wait for donor response
- Check status in "My Food Requests" section
- Request new donation only once

### Issue: Request not appearing in list
**Solution**:
- Refresh the page (F5)
- Check if you're properly logged in
- Try navigating away and back to dashboard

## Tips & Best Practices

### 1. Organize Your Requests
- Request foods your organization needs most
- Keep track of approved requests for pickup/delivery
- Follow up on pending requests after reasonable time

### 2. Contact Donors Efficiently
- Have request details ready when contacting
- Confirm pickup time and location
- Provide your organization details
- Ask about any special pickup instructions

### 3. Update Status Progress
- Mark requests as completed after receiving food
- Provide feedback to donors
- Report any issues to admin if needed

### 4. Browse Strategically
- Filter donations by location if traveling
- Check posted time for fresher items
- Read descriptions for food details
- Contact donor for clarifications before requesting

## Data You Can See

### For Available Donations:
- Food Name
- Quantity
- Pickup Location
- Donor Username
- Donor Phone
- Food Description
- Posted Date/Time
- Food Status

### For Your Requests:
- Food Type Requested
- Quantity Needed
- Delivery Location
- Request Status (Pending/Approved/Rejected/Completed)
- Request Date/Time
- Donor Phone Number
- Additional Notes

## Forms & Interactions

### Sending a Request
```
Form: Automatic (no user input needed)
Data sent:
- NGO User ID
- Selected Donation ID
- Food Type (from donation)
- Quantity (from donation)
- Location (from donation)
- Default Status: "Pending"

Confirmation:
- Success message displayed
- Request appears in My Food Requests
- Email notification (if configured)
```

### No Manual Request Form
Unlike the generic "Request Food" form, Receiver Dashboard:
- Directly links donations to requests
- Auto-fills request details
- Quick one-click requesting
- No form to fill out for each request

## Permissions & Access Control

### Who Can Access:
- ✅ Logged-in NGO users
- ❌ Logged-out users (redirected to login)
- ❌ Donor users (access denied)
- ❌ New/unverified accounts (access if registered as NGO)

### What NGO Users Can Do:
- ✅ View all available donations
- ✅ View own food requests
- ✅ Send new requests
- ✅ Track request status
- ✅ View donor contact info

### What NGO Users Cannot Do:
- ❌ Edit donations
- ❌ Delete other requests
- ❌ Modify request status
- ❌ Mark donations as unavailable

## Integration with Other Pages

### Dashboard Integration
- Quick access button "Receiver Hub"
- Statistics visible in main dashboard too
- Seamless navigation between sections

### All Donations Page
- Shows same donations (if available)
- Different presentation format
- Both offer request functionality
- Choose which interface works best for you

### Donation Detail Page
- Full donation information
- Related requests visible
- "Request Food" button available
- Redirects back to dashboard after request

## API & Database

### Models Used:
```
Donation Model:
- id, food_name, quantity, location
- phone, description, status
- donor (ForeignKey to User)
- created_at, availability_status

FoodRequest Model:
- id, ngo (ForeignKey to User)
- donation (ForeignKey to Donation)
- food_type, quantity_needed
- location, status
- requested_at, updated_at, notes
```

### Status Options:
```
Donation Availability:
- 'available': Currently available
- 'claimed': Someone requested
- 'expired': No longer available
- 'completed': Successfully transferred

Request Status:
- 'pending': Waiting for response
- 'approved': Donor approved
- 'rejected': Donor declined
- 'completed': Food received
```

## Screenshots & Visual Guide

### Dashboard Layout:
```
┌─────────────────────────────────────────────┐
│  NGO Receiver Dashboard                     │
│  Manage your food requests and track...     │
└─────────────────────────────────────────────┘

┌─ Statistics Cards ─────────────────────────┐
│ [📦 5] [📋 12] [⏳ 3] [✅ 9]              │
└───────────────────────────────────────────┘

┌─ Available Donations ─────────────────────┐
│ ┌─ Donation Card ──────────────────────┐ │
│ │ Food: Rice                           │ │
│ │ Qty: 5 kg | Location: Main St        │ │
│ │ [View Details] [Request Food]        │ │
│ └──────────────────────────────────────┘ │
│ ┌─ Donation Card ──────────────────────┐ │
│ │ Food: Vegetables                     │ │
│ │ Qty: 10 kg | Location: Park Ave      │ │
│ │ [View Details] [Request Food]        │ │
│ └──────────────────────────────────────┘ │
└───────────────────────────────────────────┘

┌─ My Food Requests ────────────────────────┐
│ ┌─ Request Item ────────────────────────┐ │
│ │ Rice | ⏳ Pending                     │ │
│ │ Qty: 5 kg | Location: Center Clinic  │ │
│ └──────────────────────────────────────┘ │
│ ┌─ Request Item ────────────────────────┐ │
│ │ Vegetables | ✅ Approved              │ │
│ │ Qty: 10 kg | Location: School        │ │
│ └──────────────────────────────────────┘ │
└───────────────────────────────────────────┘
```

## Support & Assistance

For issues or questions:
1. Check Troubleshooting section above
2. Review the detailed workflow examples
3. Contact system administrator
4. Check browser console for error messages

## Summary

The NGO Receiver Dashboard provides a streamlined, efficient interface for:
- **Discovering** available food donations
- **Requesting** food with one click
- **Tracking** request status in real-time
- **Managing** organization's food requests
- **Coordinating** with donors for logistics

It's designed to be intuitive, responsive, and focused specifically on NGO needs for food acquisition and request management.

---

**Last Updated**: February 24, 2026
**Status**: Production Ready ✅
