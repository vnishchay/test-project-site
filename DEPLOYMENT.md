# Bhardwaj Hospital Website - Deployment Guide

## Firebase Hosting Deployment

### Prerequisites
- Firebase CLI is installed (already done via npm)
- Google account with Firebase access

### Deployment Steps

1. **Login to Firebase** (first time only):
   ```bash
   npx firebase login
   ```

2. **Initialize Firebase Project** (if not done):
   ```bash
   npx firebase init hosting
   ```
   - Select "Create a new project" or use existing
   - Project ID: `bhardwaj-hospital-website` (or your choice)
   - Public directory: `.` (current directory)
   - Configure as single-page app: Yes
   - Set up automatic builds: No (for now)

3. **Deploy to Firebase**:
   ```bash
   npx firebase deploy --only hosting
   ```

4. **Your website will be live at**:
   - `https://bhardwaj-hospital-website.web.app`
   - `https://bhardwaj-hospital-website.firebaseapp.com`

### Updating the Site

Simply run:
```bash
npx firebase deploy --only hosting
```

## Website Features

- ✅ Modern, responsive design
- ✅ Mobile-friendly navigation
- ✅ Smooth scrolling animations
- ✅ Contact form with email integration
- ✅ Service showcase
- ✅ Gallery section
- ✅ Testimonials section

## Contact Email

Hospital Admin: bhardwajhos.vns@gmail.com
Phone: +91-9140815001

