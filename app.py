from flask import Flask

app = Flask(__name__)

@app.route('/factorial/<int:num>')
def factorial(num):
  if num < 0:
    return "No se puede calcular el factorial de un número negativo."
  
  result = 1
  for i in range(1, num+1):
    result *= i
  return str(result)

if __name__ == '__main__':
  app.run(debug=True)
