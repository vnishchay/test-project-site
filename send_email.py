#!/usr/bin/env python3
"""
Email script to send notification to Bhardwaj Hospital admin
with the website link and proposal request.
"""

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(website_url, sender_email, sender_password, recipient_email="bhardwajhos.vns@gmail.com"):
    """
    Send email to hospital admin with website link and proposal request.
    
    Args:
        website_url: The Firebase hosting URL
        sender_email: Email address to send from
        sender_password: Password/app password for sender email
        recipient_email: Hospital admin email (default: bhardwajhos.vns@gmail.com)
    """
    
    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'New Website for Bhardwaj Hospital – Live Now!'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # Create email content
    text = f"""
Dear Bhardwaj Hospital Administration,

We are pleased to inform you that a new, modern website for Bhardwaj Hospital has been created and is now live!

Website URL: {website_url}

This stunning new website features:
• Modern, responsive design that works on all devices
• Comprehensive information about your services
• Easy appointment booking system
• Beautiful gallery showcase
• Patient testimonials
• Contact forms and information

We believe this website will significantly enhance your online presence and help attract more patients to your hospital.

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
"""
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: #457B9D; color: white; padding: 20px; text-align: center; border-radius: 5px 5px 0 0; }}
        .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 5px 5px; }}
        .button {{ display: inline-block; padding: 12px 30px; background: #457B9D; color: white; text-decoration: none; border-radius: 5px; margin: 20px 0; }}
        .website-link {{ font-size: 18px; font-weight: bold; color: #457B9D; }}
        .footer {{ margin-top: 30px; padding-top: 20px; border-top: 2px solid #ddd; color: #666; font-size: 14px; }}
        ul {{ list-style-type: none; padding-left: 0; }}
        li:before {{ content: "✓ "; color: #457B9D; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏥 New Website for Bhardwaj Hospital</h1>
        </div>
        <div class="content">
            <p>Dear Bhardwaj Hospital Administration,</p>
            
            <p>We are pleased to inform you that a new, modern website for <strong>Bhardwaj Hospital</strong> has been created and is now live!</p>
            
            <p style="text-align: center;">
                <a href="{website_url}" class="website-link">{website_url}</a>
            </p>
            
            <p style="text-align: center;">
                <a href="{website_url}" class="button">Visit Website</a>
            </p>
            
            <h3>This stunning new website features:</h3>
            <ul>
                <li>Modern, responsive design that works on all devices</li>
                <li>Comprehensive information about your services</li>
                <li>Easy appointment booking system</li>
                <li>Beautiful gallery showcase</li>
                <li>Patient testimonials</li>
                <li>Contact forms and information</li>
            </ul>
            
            <p>We believe this website will significantly enhance your online presence and help attract more patients to your hospital.</p>
            
            <h3>📋 PROPOSAL REQUEST:</h3>
            <p>We would be delighted to discuss this website further and explore:</p>
            <ul>
                <li>Customizations to match your specific needs</li>
                <li>Additional features and functionality</li>
                <li>SEO optimization for better visibility</li>
                <li>Ongoing maintenance and updates</li>
                <li>Digital marketing services</li>
            </ul>
            
            <p>Please let us know a convenient time for a call or meeting to discuss how we can further support your hospital's digital presence.</p>
            
            <p>Looking forward to hearing from you!</p>
            
            <p>Best regards,<br>
            <strong>Website Development Team</strong></p>
            
            <div class="footer">
                <p><strong>Bhardwaj Hospital</strong><br>
                Lahartara Bauliya, Varanasi, Uttar Pradesh<br>
                Email: bhardwajhos.vns@gmail.com<br>
                Phone: +91-9140815001</p>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    # Add parts
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    msg.attach(part1)
    msg.attach(part2)
    
    try:
        # Send email using Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        print("✅ Email sent successfully to", recipient_email)
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        print("\nNote: If using Gmail, you may need to:")
        print("1. Enable 'Less secure app access' OR")
        print("2. Generate an App Password: https://myaccount.google.com/apppasswords")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 send_email.py <website_url> <sender_email> <sender_password>")
        print("\nExample:")
        print("  python3 send_email.py https://bhardwaj-hospital.web.app your-email@gmail.com your-app-password")
        print("\nNote: For Gmail, use an App Password instead of your regular password.")
        print("Generate one at: https://myaccount.google.com/apppasswords")
        sys.exit(1)
    
    website_url = sys.argv[1]
    sender_email = sys.argv[2]
    sender_password = sys.argv[3]
    
    send_email(website_url, sender_email, sender_password)

