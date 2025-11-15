#!/bin/bash

# Bhardwaj Hospital Website - Firebase Deployment Script

echo "🏥 Bhardwaj Hospital Website - Firebase Deployment"
echo "=================================================="
echo ""

# Check if Firebase CLI is available
if ! command -v npx &> /dev/null; then
    echo "❌ Error: npx not found. Please install Node.js and npm."
    exit 1
fi

# Check if logged in to Firebase
echo "Checking Firebase authentication..."
if npx firebase projects:list &> /dev/null; then
    echo "✅ Already logged in to Firebase"
else
    echo "⚠️  Not logged in to Firebase"
    echo ""
    echo "Please run the following command to login:"
    echo "  npx firebase login"
    echo ""
    read -p "Press Enter after you've logged in, or Ctrl+C to cancel..."
fi

# List existing projects
echo ""
echo "Your Firebase projects:"
npx firebase projects:list

echo ""
read -p "Enter your Firebase project ID (or press Enter to create a new one): " PROJECT_ID

if [ -z "$PROJECT_ID" ]; then
    echo "Creating a new Firebase project..."
    echo "Please follow the prompts to create a new project."
    echo ""
    read -p "Press Enter to continue..."
    npx firebase projects:create
    read -p "Enter the project ID you just created: " PROJECT_ID
fi

# Update .firebaserc
if [ ! -z "$PROJECT_ID" ]; then
    echo "Setting project to: $PROJECT_ID"
    echo "{\"projects\": {\"default\": \"$PROJECT_ID\"}}" > .firebaserc
fi

# Initialize hosting if needed
if [ ! -f "firebase.json" ]; then
    echo "Initializing Firebase hosting..."
    npx firebase init hosting --project "$PROJECT_ID" --public . --yes
fi

# Deploy
echo ""
echo "🚀 Deploying to Firebase..."
echo ""
npx firebase deploy --only hosting --project "$PROJECT_ID"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Deployment successful!"
    echo ""
    echo "Your website is live at:"
    echo "  https://$PROJECT_ID.web.app"
    echo "  https://$PROJECT_ID.firebaseapp.com"
    echo ""
    echo "Next steps:"
    echo "1. Send an email to bhardwajhos.vns@gmail.com with the website link"
    echo "2. Include a proposal request for further discussion"
    echo ""
else
    echo ""
    echo "❌ Deployment failed. Please check the error messages above."
    exit 1
fi

