from app import app

def test_data():
    response = app.test_client().get('/')
    expected = b"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Ingenieria Software CI</title>
  </head>
  <body>
    <h1>Flask is working!!</h1>
  </body>
</html>"""
    assert response.data.strip() == expected.strip()

