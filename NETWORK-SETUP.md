# Cardinal Otunga School App - Network Access Setup

## Access from Other Devices on Same Network

Follow these steps to allow other devices to access the app as `chibibyte.local` without port number:

### Step 1: Run Server on Port 80 (Requires Administrator)

**Option A: Using Batch File (Recommended)**
1. Right-click `run-server-port80.bat` in your project folder
2. Select "Run as administrator"
3. Click "Yes" to confirm
4. The server will start on port 80

**Option B: Using PowerShell as Administrator**
1. Press Windows Key + X
2. Select "Windows PowerShell (Admin)"
3. Navigate to: `cd C:\Users\USER\Desktop\cardinal-otunga-school-app`
4. Run: `python manage.py runserver 0.0.0.0:80`

### Step 2: Configure Hosts File on Other Devices

**For Other Windows Devices:**
1. Open Notepad as Administrator
2. Go to: `C:\Windows\System32\drivers\etc\hosts`
3. Add this line: `192.168.x.x  chibibyte.local` 
   - Replace `192.168.x.x` with your computer's IP address
4. Save and close

**For Finding Your Computer's IP:**
1. Open Command Prompt
2. Type: `ipconfig`
3. Look for "IPv4 Address" (e.g., 192.168.1.100)

**For Mac/Linux Devices:**
1. Open Terminal
2. Run: `sudo nano /etc/hosts`
3. Add: `192.168.x.x  chibibyte.local`
4. Press Ctrl+X, then Y, then Enter

### Step 3: Access from Other Devices

Once configured, other devices can access:
- `http://chibibyte.local/` (without port number!)
- `http://chibibyte.local/admin/` (admin panel)
- `http://chibibyte.local/api/` (API endpoints)

### Troubleshooting

**Port 80 Already in Use:**
- Type in Command Prompt: `netstat -ano | findstr :80`
- If something uses port 80, close it or use port 8000

**Can't Access from Other Devices:**
- Verify both computers on same WiFi/Network
- Check Windows Firewall allows port 80
- Confirm hosts file entries on client device
- Ping: `ping 192.168.x.x` to test connection

**Easy Alternative (Keep Using :8000):**
- Just use `python manage.py runserver 0.0.0.0:8000`
- Other devices access: `http://192.168.x.x:8000`
- Or add `192.168.x.x  chibibyte.local` to hosts on each device and use `http://chibibyte.local:8000`
