from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid numbers provided"}), 400

    if operation == "add":
        result = num1 + num2
        symbol = "+"
    elif operation == "subtract":
        result = num1 - num2
        symbol = "−"
    elif operation == "multiply":
        result = num1 * num2
        symbol = "×"
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = num1 / num2
        symbol = "÷"
    else:
        return jsonify({"error": "Unknown operation"}), 400

    # Format result: remove trailing zeros for clean display
    result_display = int(result) if result == int(result) else round(result, 8)

    return jsonify({
        "result": result_display,
        "expression": f"{num1:g} {symbol} {num2:g} = {result_display}"
    })

if __name__ == "__main__":
    app.run(debug=False)
