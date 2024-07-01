from waitress import serve
from ApiGreet.wsgi import application

if __name__ == '__main__':
  print("Starting Waitress server...")
  try:
      serve(application, host='127.0.0.1', port=8000)
  except Exception as e:
      print(f"Error starting server: {e}")
  else:
      print("Server started successfully.")