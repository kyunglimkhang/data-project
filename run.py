from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)