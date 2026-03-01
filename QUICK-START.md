# 🚀 Cardinal Otunga School App - Quick Start Guide

## One-Click Automatic Setup

Everything is automated! Just choose one option below:

---

## Option 1: Batch File (Easiest for Windows)

### Quick Start
1. **Open File Explorer**
2. **Navigate to**: `C:\Users\USER\Desktop\cardinal-otunga-school-app\`
3. **Right-click** on `setup-and-run.bat`
4. **Select**: "Run as administrator"
5. **Click**: "Yes" when prompted
6. **Done!** ✅ Open browser: `http://chibibyte.local/`

That's it! The script automatically:
- ✅ Adds `chibibyte.local` to your hosts file
- ✅ Starts the server on port 80
- ✅ Provides network access instructions

---

## Option 2: PowerShell (Alternative)

### Quick Start
1. **Press**: `Windows Key + X`
2. **Select**: "Windows PowerShell (Admin)"
3. **Run**: 
   ```powershell
   cd C:\Users\USER\Desktop\cardinal-otunga-school-app
   .\setup-and-run.ps1
   ```
4. **Done!** ✅ Open browser: `http://chibibyte.local/`

---

## Option 3: Manual Command Line

If you prefer manual control:

```bash
# Run as Administrator in Command Prompt
cd C:\Users\USER\Desktop\cardinal-otunga-school-app
python manage.py runserver 0.0.0.0:80
```

---

## Access Your App

### From Your Computer
```
http://chibibyte.local/
```

### From Other Devices on Same Network

**Step 1: Find Your Computer's IP**
- Open Command Prompt
- Run: `ipconfig`
- Look for "IPv4 Address" (e.g., `192.168.1.100`)

**Step 2: Configure Other Devices**

**Windows Device:**
1. Open Notepad as Administrator
2. Edit: `C:\Windows\System32\drivers\etc\hosts`
3. Add line: `192.168.1.100  chibibyte.local` (use YOUR IP)
4. Save

**Mac/Linux Device:**
1. Open Terminal
2. Run: `sudo nano /etc/hosts`
3. Add line: `192.168.1.100  chibibyte.local` (use YOUR IP)
4. Save: `Ctrl+X` → `Y` → `Enter`

**Step 3: Access from Other Device**
```
http://chibibyte.local/
```

---

## Available URLs

Once running:

| URL | Purpose |
|-----|---------|
| `http://chibibyte.local/` | Main homepage |
| `http://chibibyte.local/admin/` | Admin panel |
| `http://chibibyte.local/api/` | REST API endpoints |
| `http://chibibyte.local/api/students/` | Student list API |
| `http://chibibyte.local/api/grades/` | Grades API |

---

## Troubleshooting

### "Port 80 already in use"
- Something else is using port 80
- In Command Prompt: `netstat -ano | findstr :80`
- Close the conflicting application

### "Access Denied" when running script
- Right-click the file
- Select "Run as administrator"
- Click "Yes" to confirm

### Can't access from other devices
- Verify both devices on same WiFi
- Check Windows Firewall (allow port 80)
- Verify hosts file entries on client device
- Test connection: `ping 192.168.x.x`

### Still showing :8000?
- Close all browser tabs with the app
- Hard refresh: **Ctrl + Shift + R** (Windows)
- Or: **Cmd + Shift + R** (Mac)

---

## Quick Reference

| File | What It Does |
|------|-------------|
| `setup-and-run.bat` | 🟢 Recommended: One-click setup + server |
| `setup-and-run.ps1` | PowerShell version of above |
| `run-server-port80.bat` | Just start server (assumes hosts already set) |
| `NETWORK-SETUP.md` | Detailed network configuration guide |

---

## Support

For issues or questions:
- Check `NETWORK-SETUP.md` for detailed instructions
- Verify Django is running: Check terminal output for "Starting development server"
- Make sure Python packages are installed: `pip install -r requirements.txt`

---

**Your app is ready! 🎉 Just run `setup-and-run.bat` and enjoy!**
