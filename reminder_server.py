from g_mail import gmail
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# 处理POST请求的路由
@app.route('/reminder', methods=['POST'])
def reminder():
    serverpass = None
    data = request.form.to_dict()
    clientpass = data.pop('password', None)
    # if need password
    if serverpass is not None:
        if serverpass != clientpass:
            return jsonify({"status": "error", "message": "Wrong password"}), 401
    
    to = data.pop('to')
    if not to:
        return jsonify({"status": "error", "message": "No email provided"}), 400

    error = data.pop('Error', None)
    cost_time = data.pop('CostTime', 'N/A')
    result = data.pop('result', 'N/A')
    file_path = data.pop('FilePath', 'N/A')
    
    if error:
        subject = "Task Failed"
        body = f"<h3>Task Status: Failed</h3>"
    else:
        subject = "Task Completed"
        body = f"<h3>Task Status: Completed</h3>"

    if error:
        subject = "[GMAIL reminder] Task Failed"
        body = f"""
        <h3>Task Status: Failed</h3>
        <p>Error: {error}</p>
        <p>Cost Time: {cost_time}</p>
        <p>File Path: {file_path}</p>
        """
    else:
        subject = "[GMAIL reminder] Task Completed"
        body = f"""
        <h3>Task Status: Completed</h3>
        <p>Result: {result}</p>
        <p>Cost Time: {cost_time}</p>
        <p>File Path: {file_path}</p>
        """

    for key, value in data.items():
        body += f"<p>{key}: {value}</p>"

    gmail()(to=to,
        subject=subject,
        message=body,
        mode="html",
        attachment=file_path,
        from_who="GMAIL reminder")
    
    return jsonify({"status": "success", "message": "Email sent successfully"}), 200

# 启动服务器
if __name__ == '__main__':
    app.run(threaded=True, debug=False, port=5000, host='0.0.0.0')
