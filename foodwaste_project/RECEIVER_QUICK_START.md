# Quick Access Guide - NGO Receiver Dashboard

## 🚀 Quick Start

### Login as NGO
```
URL: http://127.0.0.1:8000/login/
Username: (your NGO username)
Password: (your NGO password)
```

### Access Receiver Dashboard
**After login, choose one:**

**Option 1 - Navigation Link**
```
Top Navigation Bar → "Receiver Hub"
(Only appears for NGO accounts)
```

**Option 2 - Dashboard Button**
```
Dashboard → Click "Receiver Hub" button
```

**Option 3 - Direct URL**
```
http://127.0.0.1:8000/receiver_dashboard/
```

---

## 📊 Dashboard Overview

### Four Main Sections

#### 1. **Statistics Cards** (Top)
```
📦 Donations Available     - Total count of active donations
📋 Total Requests Sent     - All requests from your NGO
⏳ Pending Requests        - Awaiting donor response
✅ Approved Requests       - Ready for pickup/delivery
```

#### 2. **Available Food Donations** (Left)
```
Shows all donations currently available:
- Food Name and Description
- Quantity Available
- Pickup Location
- Donor Name and Contact
- Posted Date/Time
- Action Buttons: [View Details] [Request Food]
```

#### 3. **My Food Requests** (Right)
```
Shows all your food requests:
- Food Type Requested
- Quantity Needed
- Delivery Location
- Request Status (with visual indicator)
- Request Date/Time
- Donor Contact Info
- Special Notes
```

#### 4. **Status Indicators**
```
⏳ Pending    - Yellow - Waiting for donor response
✅ Approved   - Green  - Donor approved, ready to pickup
❌ Rejected   - Red    - Donor unable to fulfill
🏁 Completed  - Blue   - Food received successfully
```

---

## 📝 How to Request Food

### Method 1: From Receiver Dashboard
```
1. Find a donation you need in "Available Food Donations"
2. Click "Request Food" button on that donation
3. Request created automatically
4. Success message appears
5. Request appears in "My Food Requests" section
6. Status shows as "⏳ Pending"
```

### Method 2: View Details First
```
1. Click "View Details" on a donation
2. Read full donation information
3. Scroll down and click "Request Food"
4. Same process as Method 1
```

---

## ✅ Track Request Status

### View Your Requests
```
1. In "My Food Requests" section
2. See all requests with their current status
3. Each request shows:
   - Food name
   - Status with icon
   - Quantity and location
   - Donor contact number
```

### Understand Status Changes

#### When Status is "⏳ Pending"
- Donor hasn't responded yet
- Wait for donor's approval/rejection
- You can contact donor at phone number shown

#### When Status is "✅ Approved"
- Donor approved your request!
- Contact donor to arrange pickup/delivery
- Use phone number shown in request
- Confirm time and location

#### When Status is "❌ Rejected"
- Donor cannot fulfill request
- Find another donation to request
- Try different donors
- Request food from another source

#### When Status is "🏁 Completed"
- Food has been delivered/picked up
- Transaction complete
- Can request from same donor again

---

## 🎯 Complete Workflow Example

### Scenario: Requesting Rice for Your NGO

```
STEP 1: Access Receiver Dashboard
  └─ URL: /receiver_dashboard/

STEP 2: See Available Donations
  ├─ Statistics show: 5 donations available
  └─ Donation List shows:
      - Rice (5kg) - Main Street
      - Vegetables (10kg) - Market Square
      - Bread (8 loaves) - Bakery Street

STEP 3: Request Rice
  └─ Click "Request Food" on Rice donation
      → Success: "Request sent for Rice!"

STEP 4: Check My Requests
  └─ "My Food Requests" section now shows:
      - Rice (5kg) | ⏳ Pending | Main Street

STEP 5: Wait for Approval
  ├─ Donor sees your request
  └─ Donor approves/rejects in their dashboard

STEP 6: Status Updates to "✅ Approved"
  └─ You see updated status in dashboard

STEP 7: Contact Donor
  ├─ Get donor's phone from request details
  └─ Call/WhatsApp to arrange pickup

STEP 8: Pickup/Delivery Arranged
  ├─ Confirm time and location
  └─ Complete the handover

STEP 9: Food Received
  ├─ Status marked as "🏁 Completed"
  └─ Request fulfilled!
```

---

## ⚙️ Important Features

### Duplicate Request Prevention
```
If you already requested a donation:
  ├─ Try requesting same donation again
  └─ System shows:
      "You already have a pending request for this donation!"
  
This prevents:
- Duplicate requests
- Confusion with multiple similar requests
- Unnecessary data
```

### One-Click Requesting
```
No forms to fill out!
  ├─ Food type: Pre-filled from donation
  ├─ Quantity: Pre-filled from donation
  ├─ Location: Pre-filled from donation
  └─ Just click "Request Food" button
```

### Real-Time Updates
```
Statistics update automatically
- Donations Available count
- Total Requests count
- Pending Requests count
- Approved Requests count
```

---

## 📱 Mobile Friendly

### Works on All Devices
```
✓ Smartphones (< 600px)
  ├─ Full functionality
  ├─ Touch-friendly buttons
  └─ Vertical card layout

✓ Tablets (600px - 1024px)
  ├─ Optimized 2-column layout
  └─ Large touch targets

✓ Desktops (> 1024px)
  ├─ Full side-by-side layout
  └─ All features visible
```

### Testing on Mobile
```
1. Open http://127.0.0.1:8000/receiver_dashboard/
2. Press F12 to open DevTools
3. Click responsive design mode icon
4. Select device:
   - iPhone 12
   - iPad
   - Any resolution
5. All features should work perfectly
```

---

## 🔍 Filtering & Searching

### Find Specific Donations
```
Option 1: View Donations Page
  1. Click "View Donations" in navigation
  2. Use search box: "Rice" or "Location"
  3. Find what you need
  4. Click "Request Food"

Option 2: Receiver Dashboard
  1. Browse naturally through cards
  2. Click "View Details" for more info
  3. Then request if interested
```

---

## 📞 Contacting Donors

### Has Phone Number Visible
```
In each request, you can see:
  - Donor's phone number
  - From the original donation
  - Direct contact for coordination

Use for:
  ├─ Confirming donation details
  ├─ Arranging pickup time
  ├─ Discussing location/delivery
  └─ Building donor relationship
```

---

## ❓ Common Questions

### Q: How long does it take for donor to respond?
**A:** Depends on donor. Usually within 24 hours. Contact them using phone number if urgent.

### Q: Can I request multiple donations?
**A:** Yes! Request as many as you need. No limit on requests.

### Q: What if donor rejects my request?
**A:** Try requesting from another donor. Keep browsing available donations.

### Q: How do I know when status changes?
**A:** Refresh the page to see latest status. (Further updates: email/SMS may be added later)

### Q: Can I cancel a request?
**A:** Contact admin or try requesting different donation instead.

### Q: What if I don't get messages?
**A:** Check "My Food Requests" section - status shown there regardless.

### Q: Can donors see my organization info?
**A:** Yes, in their admin panel. They see your name and contact information.

### Q: Is my phone number visible to donors?
**A:** Yes, in your organization profile. You can verify in account settings.

---

## 🚨 Troubleshooting

### Issue: Can't see Receiver Hub link
```
Solution:
  1. Verify you're logged in as NGO (not Donor)
  2. Check account type during registration
  3. Create new NGO account if registered as Donor
  4. Try direct link: /receiver_dashboard/
```

### Issue: "This page is for NGOs only!"
```
Solution:
  ├─ Your account is registered as Donor
  └─ Create new account with "NGO" account type
```

### Issue: "You already have a pending request!"
```
Solution:
  ├─ You already requested this donation
  ├─ Wait for donor response
  ├─ Check status in "My Food Requests"
  └─ Request different donations
```

### Issue: Request not appearing
```
Solution:
  1. Refresh page (F5)
  2. Check if logged in
  3. Try scrolling down in "My Food Requests"
  4. Check browser console for errors
```

### Issue: Page looks wrong
```
Solution:
  1. Clear browser cache (Ctrl+Shift+Delete)
  2. Hard refresh (Ctrl+F5)
  3. Try different browser
  4. Check internet connection
```

---

## 📊 Understanding Statistics

### Donations Available Count
```
Shows: Number of active donations
  ├─ Status: Available
  ├─ Not claimed by others
  └─ Ready for request

Updates: Real-time (refresh page to see)
```

### Total Requests Sent
```
Shows: All requests you've ever sent
  ├─ Includes: Pending, Approved, Rejected, Completed
  └─ Total count: All time

Compare: Against "Available Donations" to understand coverage
```

### Pending Requests
```
Shows: Requests waiting for response
  ├─ Status: ⏳ Pending
  └─ Waiting for donor decision

Action: Contact donor if taking too long
```

### Approved Requests
```
Shows: Requests donor approved
  ├─ Status: ✅ Approved
  └─ Ready to arrange pickup/delivery

Action: Contact donor to finalize pickup
```

---

## 🎓 Best Practices

### Tips for Success

**1. Request Strategically**
```
- Request foods your org needs most
- Check quantity matches your need
- Verify location is accessible
- Read description for food details
```

**2. Act Fast**
```
- Good donations get claimed quickly
- Request soon after new post
- Follow up on approved requests quickly
- Arrange pickups promptly
```

**3. Communicate**
```
- Call donor at provided number
- Be professional and polite
- Confirm times and locations
- Provide feedback about experience
```

**4. Track Status**
```
- Check dashboard regularly
- Note approval dates
- Schedule pickups on time
- Update completed requests
```

**5. Build Relationships**
```
- Thank donors after receiving food
- Be reliable for pickups
- Provide feedback to donor
- Request from good donors again
```

---

## 📚 More Information

### Complete Documentation
- **NGO_RECEIVER_GUIDE.md** - Full detailed guide
- **IMPLEMENTATION_SUMMARY.md** - Technical details
- **RECEIVER_TESTING.md** - Testing procedures

### Getting Help
1. Check this quick guide ✓
2. Read full NGO_RECEIVER_GUIDE.md
3. Contact system administrator
4. Report bugs or issues

---

## ✨ Key Features Summary

```
✓ One-click food requesting
✓ Real-time status tracking
✓ View all available donations
✓ Prevent duplicate requests
✓ Donor contact information
✓ Request statistics
✓ Mobile responsive design
✓ Instant confirmations
✓ Organize by status
✓ Track request history
```

---

**Status**: ✅ Ready to Use
**Last Updated**: February 24, 2026
**Version**: 1.0

Happy requesting! 🎉
