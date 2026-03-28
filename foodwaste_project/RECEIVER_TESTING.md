# NGO Receiver Dashboard - Testing Guide

## Quick Test Scenario

### Prerequisites
- Django server running (`python manage.py runserver`)
- Admin account created (admin/admin123)
- At least one donation posted

---

## Test Workflow

### Step 1: Create Test Accounts

#### Create Donor Account
1. Go to: http://127.0.0.1:8000/register/
2. Fill form:
   - Account Type: **Donor**
   - Username: `donor_test`
   - Email: `donor@test.com`
   - Password: `test123test`
   - Confirm Password: `test123test`
   - Phone: `9876543210`
3. Click "Register"
4. You'll be redirected to login page

#### Create NGO Account  
1. Go to: http://127.0.0.1:8000/register/
2. Fill form:
   - Account Type: **NGO**
   - Username: `ngo_test`
   - Email: `ngo@test.com`
   - Password: `test123test`
   - Confirm Password: `test123test`
   - Organization Name: `Test NGO`
   - Registration Number: `NGO12345`
   - Phone: `9876543211`
   - Address: `123 Main Street`
   - City: `Test City`
3. Click "Register"
4. Redirected to login page

---

### Step 2: Create Test Donations

#### Login as Donor
1. Go to: http://127.0.0.1:8000/login/
2. Enter:
   - Username: `donor_test`
   - Password: `test123test`
3. Click "Login"

#### Post a Donation
1. Click "Donate Food" in dashboard
2. Fill form:
   - Food Name: `Rice`
   - Description: `5kg bag of white rice`
   - Quantity: `5 kg`
   - Location: `Main Street, Downtown`
   - Phone: `9876543210`
3. Click "Publish Donation"
4. Success message appears

#### Post More Donations
Repeat above steps with:
- Food: `Vegetables` | Qty: `10 kg` | Location: `Market Square`
- Food: `Bread` | Qty: `8 loaves` | Location: `Bakery Street`

#### Keep Logged In or Logout
- For now, we'll log out to test NGO

---

### Step 3: Test NGO Receiver Dashboard

#### Login as NGO
1. Go to: http://127.0.0.1:8000/login/
2. Enter:
   - Username: `ngo_test`
   - Password: `test123test`
3. Click "Login"

#### Navigate to Receiver Dashboard
**Option A - Via Dashboard:**
1. Click "Dashboard" in navigation
2. Click "Receiver Hub" button

**Option B - Via Navigation:**
1. Look for "Receiver Hub" link in nav bar (will appear after login as NGO)
2. Click it

**Option C - Direct URL:**
1. Visit: http://127.0.0.1:8000/receiver_dashboard/

#### View Page Contents
You should see:
```
✓ Dashboard Header ("NGO Receiver Dashboard")
✓ Statistics Cards (if donations exist)
  - 📦 Donations Available
  - 📋 Total Requests Sent
  - ⏳ Pending Requests
  - ✅ Approved Requests
✓ Available Food Donations section
  - Each donation as a card showing:
    * Food name
    * Quantity
    * Location
    * Donor name
    * Contact phone
    * Description
    * Posted date/time
    * Action buttons: "View Details", "Request Food"
✓ My Food Requests section
  - Shows all requests (initially empty)
```

---

### Step 4: Test Request Food Functionality

#### Send First Request
1. In "Available Food Donations" section
2. Find "Rice" donation
3. Click "Request Food" button
4. Success message: "Request sent for Rice! Waiting for donor approval."
5. Page may auto-refresh

#### Check Requests List
1. Scroll to "My Food Requests" section
2. You should see:
   - Food: Rice
   - Status: **⏳ Pending**
   - Quantity: 5 kg
   - Location: Main Street, Downtown
   - Donor Phone: 9876543210
   - Posted time: Recently

#### Send More Requests
1. Request "Vegetables" donation
2. Success message appears
3. Check "My Food Requests" - now shows 2 requests
4. Statistics update: "Total Requests: 2", "Pending Requests: 2"

#### Test Duplicate Prevention
1. Try requesting "Rice" again
2. You should get warning: "You already have a pending request for this donation!"
3. Request not created again

---

### Step 5: Test Status Indicators

#### Visual Status Checking
1. In "My Food Requests" section
2. Each request shows a status indicator:
   - ⏳ Pending (yellow background, hourglass icon)
   - ✅ Approved (green background, checkmark icon)
   - ❌ Rejected (red background, X icon)
   - 🏁 Completed (blue background, flag icon)

---

### Step 6: Test Admin Panel Status Updates

#### Login as Admin
1. Go to: http://127.0.0.1:8000/admin/
2. Login: `admin` / `admin123`

#### Find Food Requests
1. Click "Food requests" in admin panel
2. Click on a pending request (e.g., Rice request from ngo_test)
3. Change status dropdown from "Pending" to "Approved"
4. Click "Save"

#### Back as NGO - Check Updated Status
1. Stay logged in as admin or log back in as ngo_test
2. Go to receiver dashboard
3. Status should now show: **✅ Approved**
4. Status indicator changed from ⏳ to ✅
5. Check statistics

#### Test Other Status Changes
Repeat admin process for:
- Change one request to "Rejected"
  - Status shows: **❌ Rejected**
- Change another to "Completed"
  - Status shows: **🏁 Completed**

---

### Step 7: Test Responsive Design

#### Mobile View
1. In browser, press F12 (Dev Tools)
2. Click responsive design mode icon
3. Select "iPhone 12" or similar
4. Verify:
   - Navigation collapses properly
   - Cards stack vertically
   - Buttons remain clickable
   - Text is readable
   - No horizontal scroll

#### Tablet View
1. Select "iPad" in responsive mode
2. Verify layout adapts properly

#### Desktop View
1. Close dev tools
2. Maximize window
3. Verify full 2-column layout shows (if big enough)

---

### Step 8: Test Empty States

#### Clear All Requests
1. As admin, delete all food requests for the NGO
2. Go to receiver dashboard as NGO
3. "My Food Requests" should show:
   - "You haven't sent any food requests yet."
   - "Browse available donations and request food from donors!"

#### Clear All Donations
1. As admin, mark all donations as "expired"
2. Go to receiver dashboard
3. "Available Food Donations" should show:
   - "No donations available at the moment."
   - "Check back later for new donations!"

---

### Step 9: Test Navigation Links

#### From Receiver Dashboard
1. Click "Home" - should go to home page
2. Click "View Donations" - should show all donations
3. Click "Dashboard" - should go to personal dashboard
4. Click "Receiver Hub" in nav - should refresh current page
5. Click "Logout" - should logout and redirect home

#### From Other Pages
1. As logged in NGO, navigate to home
2. "Receiver Hub" link should appear in nav
3. Click it - should go to receiver dashboard

---

### Step 10: Test Edge Cases

#### Test with No Login
1. Logout
2. Try accessing: http://127.0.0.1:8000/receiver_dashboard/
3. You should be redirected to login page
4. URL changes to: /login/?next=/receiver_dashboard/
5. Login as NGO - should redirect to receiver_dashboard

#### Test as Donor
1. Login as donor_test
2. Try accessing: http://127.0.0.1:8000/receiver_dashboard/
3. Should show error: "This page is for NGOs only!"
4. Redirects to dashboard page

#### Test Search on View Donations
1. Go to "View Donations" page
2. Search for "Rice"
3. Only Rice donation appears
4. Search "UpdateMe" - no results
5. Click "View Details" on a donation
6. Full donation details show
7. "Request Food" button works if logged in as NGO

---

## Verification Checklist

### Page Elements ✓
- [ ] Dashboard header displays correctly
- [ ] Statistics cards show correct numbers
- [ ] Available donations section displays all open donations
- [ ] Each donation card shows all required fields
- [ ] "View Details" button works
- [ ] "Request Food" button works
- [ ] "My Food Requests" section displays
- [ ] Request items show all information
- [ ] Status indicators display with correct colors
- [ ] Empty state messages appear when needed

### Functionality ✓
- [ ] Can request a donation with one click
- [ ] Duplicate requests are prevented
- [ ] Request appears in "My Food Requests" immediately
- [ ] Request status updates when admin changes it
- [ ] Success messages appear after actions
- [ ] Warning messages appear for invalid actions

### Navigation ✓
- [ ] "Receiver Hub" appears in nav for NGO users
- [ ] Navigation links work from dashboard
- [ ] Login required redirects work
- [ ] Donor access denial works
- [ ] All internal links function

### Responsive Design ✓
- [ ] Mobile layout works (< 768px)
- [ ] Tablet layout works (768px - 1024px)
- [ ] Desktop layout works (> 1024px)
- [ ] No horizontal scrolling
- [ ] Buttons clickable on all devices
- [ ] Text readable on all sizes

### User Experience ✓
- [ ] Page loads quickly
- [ ] Messages clear and helpful
- [ ] Visual hierarchy clear
- [ ] Status colors intuitive
- [ ] Hover effects working
- [ ] Forms validate properly

---

## Expected Test Results

### Scenario 1: NGO Browsing & Requesting
```
✓ Login as NGO
✓ Access Receiver Dashboard
✓ See 3 available donations
✓ Statistics show: 3 Available, 0 Requests, 0 Pending, 0 Approved
✓ Click "Request Food" for each
✓ Get 3 success messages
✓ Statistics show: 3 Available, 3 Requests, 3 Pending, 0 Approved
✓ See all 3 requests in "My Food Requests"
✓ All showing ⏳ Pending status
```

### Scenario 2: Admin Approves Request
```
✓ Admin login
✓ Change request status to "Approved"
✓ NGO refreshes dashboard
✓ Request now shows ✅ Approved
✓ Statistics update: 1 Pending, 1 Approved
```

### Scenario 3: Request Rejection
```
✓ Admin change status to "Rejected"
✓ NGO refreshes dashboard
✓ Request shows ❌ Rejected
✓ Statistics update
```

### Scenario 4: Complete Request
```
✓ Admin change status to "Completed"
✓ NGO refreshes dashboard
✓ Request shows 🏁 Completed
✓ Food received indicator visible
```

---

## Troubleshooting During Testing

### Issue: Can't see "Receiver Hub" in nav
**Solution**: Verify you're logged in as NGO account, not donor

### Issue: Request not appearing
**Solution**: 
1. Refresh page (F5)
2. Check browser console for errors
3. Verify you're logged in as NGO

### Issue: "This page is for NGOs only!" error
**Solution**: Your account is registered as Donor, not NGO. Create new account with NGO type

### Issue: Duplicate request allowed
**Solution**: Only one pending request per donation is allowed. Check status of existing request

### Issue: Page looking strange
**Solution**: 
1. Clear browser cache (Ctrl+Shift+Delete)
2. Hard refresh (Ctrl+F5)
3. Try different browser

---

## Performance Testing

### Load Time
- Page should load in < 2 seconds
- Static assets from cache < 500ms

### Database Queries
- No N+1 query problems
- Donations list loads efficiently
- Request status updates quickly

### Browser Compatibility
- Chrome/Chromium ✓
- Firefox ✓
- Safari ✓
- Edge ✓

---

## Final Sign-Off

After completing all tests above, the Receiver Dashboard is ready for:
- ✅ User acceptance testing
- ✅ Production deployment
- ✅ User training
- ✅ Full rollout to NGO users

---

**Test Date**: February 24, 2026
**Tested By**: [Your Name]
**Status**: Ready for Deployment ✅
