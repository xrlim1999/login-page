from website import create_app

# create the application
app = create_app()

if __name__ in "__main__":
    app.run(debug=True) # only set as True when in development phase