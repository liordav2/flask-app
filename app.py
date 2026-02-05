from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# HTML template for the home page
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .info {
            background: #e3f2fd;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        a {
            color: #1976d2;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 ברוכים הבאים לאפליקציית Flask</h1>
        <div class="info">
            <p><strong>האפליקציה פועלת בהצלחה!</strong></p>
            <p>נקודות קצה זמינות:</p>
            <ul>
                <li><a href="/">/</a> - דף הבית</li>
                <li><a href="/api/health">/api/health</a> - בדיקת תקינות</li>
                <li><a href="/api/info">/api/info</a> - מידע על האפליקציה</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running'
    })

@app.route('/api/info')
def info():
    return jsonify({
        'app_name': 'Flask Simple App',
        'version': '1.0.0',
        'description': 'A simple Flask application with Docker support'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
