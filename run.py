from app import app



if __name__ == "__main__":
    manager.run()
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])
