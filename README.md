# Bhardwaj Hospital Website

A modern, responsive website for Bhardwaj Hospital in Varanasi, Uttar Pradesh.

## Features

- ✅ Modern, responsive design that works on all devices
- ✅ Smooth animations and transitions
- ✅ Mobile-friendly navigation
- ✅ Service showcase
- ✅ Gallery section
- ✅ Patient testimonials
- ✅ Contact form with email integration
- ✅ Easy appointment booking system

## Getting Started

### Local Development

1. Clone or download this repository
2. Open `index.html` in your web browser
3. Or use a local server:
   ```bash
   python3 -m http.server 8000
   ```
   Then visit `http://localhost:8000`

## Deployment to Firebase

### Option 1: Automated Script

Run the deployment script:
```bash
./deploy.sh
```

The script will guide you through:
1. Firebase login (if needed)
2. Project selection/creation
3. Deployment

### Option 2: Manual Deployment

1. **Login to Firebase:**
   ```bash
   npx firebase login
   ```

2. **Initialize hosting (first time only):**
   ```bash
   npx firebase init hosting
   ```
   - Select existing project or create new one
   - Public directory: `.` (current directory)
   - Configure as single-page app: Yes

3. **Deploy:**
   ```bash
   npx firebase deploy --only hosting
   ```

4. **Your website will be live at:**
   - `https://<project-id>.web.app`
   - `https://<project-id>.firebaseapp.com`

## Sending Email Notification

After deployment, send an email to the hospital admin:

```bash
python3 send_email.py <website_url> <your_email> <your_password_or_app_password>
```

**Example:**
```bash
python3 send_email.py https://bhardwaj-hospital.web.app your-email@gmail.com your-app-password
```

### Gmail Setup

If using Gmail, you'll need an App Password:
1. Go to https://myaccount.google.com/apppasswords
2. Generate a new app password for "Mail"
3. Use this app password instead of your regular password

## Project Structure

```
bhardwaj-hospital-website/
├── index.html          # Main HTML file
├── styles.css          # Styles and responsive design
├── script.js           # JavaScript functionality
├── firebase.json       # Firebase hosting configuration
├── .firebaserc         # Firebase project configuration
├── deploy.sh           # Deployment automation script
├── send_email.py       # Email notification script
└── README.md           # This file
```

## Contact Information

**Bhardwaj Hospital**
- Email: bhardwajhos.vns@gmail.com
- Phone: +91-9140815001
- Address: Lahartara Bauliya, Varanasi, Uttar Pradesh

## Services Featured

- Anorectal Care (Piles, Fistula, Fissure, Pilonidal Sinus)
- Orthopaedic Surgery
- Neuro Surgery
- Urology
- Women Care
- Diabetes Care

## License

© 2025 Bhardwaj Hospital. All rights reserved.

