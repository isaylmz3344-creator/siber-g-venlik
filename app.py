from flask import Flask, render_template_string

app = Flask(__name__)

# --- PREVENTER MOBILE ULTIMATE BY ISA ---
HTML_CODE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>PREVENTER MOBILE</title>
    <style>
        :root { --neon: #0f0; --bg: #000; --card: #0a0a0a; }
        * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--bg); color: var(--neon); font-family: sans-serif; margin: 0; padding: 0; overflow-x: hidden; }
        
        /* Auth Screen */
        #auth-screen { position: fixed; inset: 0; background: #000; z-index: 1000; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 20px; }
        .g-btn { background: #fff; color: #000; border: none; padding: 15px 30px; border-radius: 50px; font-weight: bold; display: flex; align-items: center; gap: 10px; font-size: 1rem; box-shadow: 0 0 20px rgba(255,255,255,0.2); }

        /* Mobile Navbar */
        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #050505; border-top: 1px solid #1a1a1a; display: flex; justify-content: space-around; padding: 10px 0; z-index: 100; }
        .nav-item { color: #555; text-decoration: none; font-size: 0.7rem; display: flex; flex-direction: column; align-items: center; border: none; background: none; }
        .nav-item.active { color: var(--neon); }

        /* Content Area */
        .page { display: none; padding: 20px; padding-bottom: 80px; min-height: 100vh; }
        .page.active { display: block; }
        .card { background: var(--card); border: 1px solid #1a1a1a; border-radius: 15px; padding: 20px; margin-bottom: 20px; }
        
        /* Chat UI - MOBİL İÇİN DÜZELTİLDİ */
        #chat-container { height: 300px; overflow-y: auto; background: #050505; border-radius: 10px; padding: 15px; display: flex; flex-direction: column; gap: 10px; border: 1px solid #111; }
        .msg { background: #111; padding: 10px; border-radius: 10px; font-size: 0.9rem; border-left: 3px solid var(--neon); width: fit-content; max-width: 85%; }
        .msg b { color: var(--neon); display: block; margin-bottom: 3px; }
        .input-group { display: flex; gap: 10px; margin-top: 15px; }
        input { flex: 1; background: #000; border: 1px solid #222; color: #fff; padding: 12px; border-radius: 10px; outline: none; }
        .send-btn { background: var(--neon); border: none; color: #000; padding: 10px 20px; border-radius: 10px; font-weight: bold; }

        /* Admin Badge */
        .admin-badge { background: red; color: #fff; font-size: 10px; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
        .isa-signature { text-align: center; font-size: 1.5rem; font-weight: 900; opacity: 0.1; letter-spacing: 10px; margin-top: 20px; }
    </style>
</head>
<body>

    <div id="auth-screen">
        <h1 style="font-size: 2.5rem; letter-spacing: 5px; margin-bottom: 10px;">🛡️ PREVENTER</h1>
        <p style="color: #444; margin-bottom: 30px;">MOBILE ACCESS</p>
        <button class="g-btn" onclick="handleLogin()">
            <img src="https://www.gstatic.com/images/branding/product/1x/gsa_512dp.png" width="18"> Sign in with Google
        </button>
    </div>

    <div id="home-page" class="page">
        <div class="card">
            <h2>Welcome, <span id="user-title">User</span> <span id="admin-tag"></span></h2>
            <p style="color: #555;">System is monitoring your connections.</p>
            <div id="admin-box" style="display:none; border: 1px dashed red; padding: 15px; border-radius: 10px;">
                <h4 style="color:red; margin:0;">👑 ISA ADMIN CONSOLE</h4>
                <p style="font-size: 0.8rem; margin: 10px 0;">Total Users: 1 | Global Status: Protected</p>
            </div>
        </div>
        <div class="isa-signature">BY ISA</div>
    </div>

    <div id="chat-page" class="page">
        <div class="card">
            <h3>GLOBAL CHAT</h3>
            <div id="chat-container">
                <div class="msg"><b>System</b> Welcome to encrypted mobile chat.</div>
            </div>
            <div class="input-group">
                <input type="text" id="chatInput" placeholder="Message...">
                <button class="send-btn" onclick="sendMessage()">SEND</button>
            </div>
        </div>
    </div>

    <div id="settings-page" class="page">
        <div class="card">
            <h3>SYSTEM SETTINGS</h3>
            <label>Interface Color</label>
            <input type="color" onchange="document.documentElement.style.setProperty('--neon', this.value)" style="width:100%; margin-top:10px;">
            <br><br>
            <button class="send-btn" style="width:100%; background: #222; color: #fff;" onclick="location.reload()">LOGOUT</button>
        </div>
    </div>

    <nav class="bottom-nav">
        <button class="nav-item active" onclick="showPage('home-page', this)">🏠<br>Home</button>
        <button class="nav-item" onclick="showPage('chat-page', this)">💬<br>Chat</button>
        <button class="nav-item" onclick="showPage('settings-page', this)">⚙️<br>Settings</button>
    </nav>

    <script>
        let currentUser = "Guest";

        function handleLogin() {
            let name = prompt("Google Account Name (Type 'isa' for Admin):");
            if (!name) return;
            currentUser = name;
            document.getElementById('auth-screen').style.display = 'none';
            document.getElementById('home-page').classList.add('active');
            document.getElementById('user-title').innerText = currentUser;

            if(currentUser.toLowerCase() === 'isa') {
                document.getElementById('admin-tag').innerHTML = '<span class="admin-badge">ADMIN</span>';
                document.getElementById('admin-box').style.display = 'block';
            }
        }

        function showPage(pageId, btn) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
            document.getElementById(pageId).classList.add('active');
            btn.classList.add('active');
        }

        function sendMessage() {
            let input = document.getElementById('chatInput');
            let container = document.getElementById('chat-container');
            if(input.value.trim() === "") return;

            let messageHtml = `<div class="msg"><b>${currentUser}</b>${input.value}</div>`;
            container.innerHTML += messageHtml;
            input.value = "";
            container.scrollTop = container.scrollHeight;
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
