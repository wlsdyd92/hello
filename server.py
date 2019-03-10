from flask import Flask, render_template

def get_app() :
    app = Flask(__name__)
    return app

@app.route('/')
def index():
    return render_template('index.html')

def main():
    app = get_app()
    app.run(debug=True, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()

    
