from datetime import date

import connexion

app = connexion.App(__name__, specification_dir='./src/api/routes')
app.add_api('swagger.yml')

@app.route('/')
def get():
    return {
        'hello': 'cronologus',
        'now': date.today()
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
