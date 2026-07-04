# Phishing Simulation: Urgent EHR System Update 🎣🚨

This module provides a ready-to-use HTML email template designed for internal phishing simulations. Healthcare IT administrators can use this template to test staff awareness regarding deceptive emails.

## 🎯 Scenario Overview
*   **Target:** Medical and Administrative Staff.
*   **Vector:** A fake urgent notification requiring the user to "verify their account" due to an Electronic Health Record (EHR) system update.
*   **Goal:** Identify employees who click unverified links and enter credentials without checking the sender's actual email address.

## 📧 HTML Email Template (Copy & Paste)
Administrators can copy the HTML code below into their simulation tools (e.g., GoPhish) or email clients.

```html
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; color: #333;">
    <div style="border: 1px solid #ddd; padding: 20px; max-width: 600px; margin: auto;">
        <h2 style="color: #d9534f;">🚨 URGENT: Action Required for EHR System Update</h2>
        <p>Dear Staff Member,</p>
        <p>Our Electronic Health Record (EHR) system is undergoing a mandatory security upgrade tonight at 23:00.</p>
        <p>To ensure you do not lose access to patient records and scheduling tomorrow morning, you must verify your active session credentials immediately.</p>
        <div style="text-align: center; margin: 30px 0;">
            <a href="[http://fake-hospital-login-simulation.com](http://fake-hospital-login-simulation.com)" style="background-color: #0275d8; color: white; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 5px;">Verify My Account Now</a>
        </div>
        <p>Failure to verify will result in a temporary lock of your account, requiring manual IT unlock.</p>
        <p>Thank you,<br><strong>Hospital IT Security Department</strong></p>
    </div>
</body>
</html>
