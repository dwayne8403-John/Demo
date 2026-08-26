import os
import webbrowser

# HTML கோடு
html_content = """
<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 300px;
            width: 100%;
        }
        h2 {
            color: #333;
            margin-bottom: 20px;
        }
        .btn-container {
            display: flex;
            justify-content: space-around;
        }
        button {
            padding: 10px 25px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .yes-btn {
            background-color: #4CAF50;
            color: white;
        }
        .no-btn {
            background-color: #f44336;
            color: white;
        }
    </style>
</head>
<body>

    <div class="card">
        <h2 id="message">ஹாய் எப்படி இருக்கீங்க?</h2>
        <div class="btn-container">
            <button class="yes-btn" onclick="response('Yes')">Yes</button>
            <button class="no-btn" onclick="response('No')">No</button>
        </div>
    </div>

    <script>
        function response(answer) {
            if (answer === 'Yes') {
                document.getElementById('message').innerText = "சூப்பர்! மகிழ்ச்சி! 😊";
            } else {
                document.getElementById('message').innerText = "அய்யோ, என்ன ஆச்சு? 🙁";
            }
        }
    </script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

file_path = os.path.abspath("index.html")
print(f"File saved at: {file_path}")

url = "file://" + file_path.replace("\\", "/")
webbrowser.open(url)
