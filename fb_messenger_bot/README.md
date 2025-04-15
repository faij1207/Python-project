# Facebook Messenger Bot 🤖

A stealthy Facebook Messenger bot built using Selenium and Undetected ChromeDriver.

## 🚀 Features

- Logs in to Facebook stealthily
- Sends messages to multiple friends
- Avoids detection with human-like delays
- Uses `.env` file for sensitive credentials

## 🛠️ Setup

1. Clone the repository or copy files manually.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file with your credentials:

    ```ini
    FB_EMAIL=your_email_here
    FB_PASSWORD=your_password_here
    ```

4. Run the bot:

    ```bash
    python fb_bot.py
    ```

⚠️ **Warning**  
This is for educational purposes only. Use responsibly and respect Facebook's terms of service.

---

Once you’ve created those files, zip them up with your system’s file manager or use the following command:

```bash
zip -r fb_messenger_bot.zip fb_messenger_bot/
```

Then you can push it to GitHub with:

```bash
git init
git add .
git commit -m "Initial stealth Facebook Messenger bot"
git remote add origin https://github.com/YOUR_USERNAME/fb_messenger_bot.git
git push -u origin master
```
