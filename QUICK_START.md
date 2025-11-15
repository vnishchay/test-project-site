# 🚀 Quick Start Guide - Bhardwaj Hospital Website

## What's Been Created

✅ Modern, responsive website with all hospital information
✅ Firebase hosting configuration ready
✅ Deployment scripts prepared
✅ Email notification script ready

## Next Steps to Deploy

### Step 1: Login to Firebase (First Time Only)

```bash
cd /home/nishv/projects/bhardwaj-hospital-website
npx firebase login
```

This will open a browser window for you to authenticate with your Google account.

### Step 2: Create/Select Firebase Project

**Option A: Create New Project**
```bash
npx firebase projects:create
# Follow the prompts to create a project like "bhardwaj-hospital-website"
```

**Option B: Use Existing Project**
```bash
npx firebase use <your-project-id>
```

Or update `.firebaserc` with your project ID:
```json
{
  "projects": {
    "default": "your-project-id"
  }
}
```

### Step 3: Deploy to Firebase

**Automated (Recommended):**
```bash
./deploy.sh
```

**Manual:**
```bash
npx firebase deploy --only hosting
```

### Step 4: Get Your Website URL

After deployment, you'll see URLs like:
- `https://<your-project-id>.web.app`
- `https://<your-project-id>.firebaseapp.com`

### Step 5: Send Email to Hospital Admin

After deployment, send the email notification:

```bash
python3 send_email.py <your-website-url> <your-email@gmail.com> <your-app-password>
```

**For Gmail App Password:**
1. Go to: https://myaccount.google.com/apppasswords
2. Generate an app password for "Mail"
3. Use that password (not your regular password)

**Example:**
```bash
python3 send_email.py https://bhardwaj-hospital-website.web.app your-email@gmail.com xxxx-xxxx-xxxx-xxxx
```

## Alternative: Manual Email

If you prefer to send the email manually, here's the template:

**To:** bhardwajhos.vns@gmail.com  
**Subject:** New Website for Bhardwaj Hospital – Live Now!

**Body:**

```
Dear Bhardwaj Hospital Administration,

We are pleased to inform you that a new, modern website for Bhardwaj Hospital has been created and is now live!

Website URL: [YOUR_WEBSITE_URL]

This stunning new website features:
• Modern, responsive design that works on all devices
• Comprehensive information about your services
• Easy appointment booking system
• Beautiful gallery showcase
• Patient testimonials
• Contact forms and information

PROPOSAL REQUEST:
We would be delighted to discuss this website further and explore:
• Customizations to match your specific needs
• Additional features and functionality
• SEO optimization for better visibility
• Ongoing maintenance and updates
• Digital marketing services

Please let us know a convenient time for a call or meeting to discuss how we can further support your hospital's digital presence.

Looking forward to hearing from you!

Best regards,
Website Development Team

---
Bhardwaj Hospital
Lahartara Bauliya, Varanasi, Uttar Pradesh
Email: bhardwajhos.vns@gmail.com
Phone: +91-9140815001
```

## Troubleshooting

### Firebase Login Issues
- Make sure you have a Google account
- Try: `npx firebase logout` then `npx firebase login` again

### Email Sending Issues
- For Gmail, use an App Password (not your regular password)
- Check that "Less secure app access" is enabled (older accounts)
- Make sure you have an internet connection

### Deployment Issues
- Check that `firebase.json` exists
- Ensure you're in the project directory
- Verify your project ID in `.firebaserc`

## Need Help?

All files are ready! Just follow the steps above to deploy and send the email.

