from flask import Flask, render_template, request
from flask_mysqldb import MySQL

 
app = Flask(__name__, template_folder = 'templates')

app.config['MYSQL_HOST'] = 'myazure134.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'Ibukun_33@myazure134'
app.config['MYSQL_PASSWORD'] = 'Forestgump_33'
app.config['MYSQL_DB'] = 'myazure134'

mysql = MySQL(app)

@app.route('/')
def index():
        cur = mysql.connection.cursor()


        show_database = """SELECT * FROM gender2"""
        cur.execute(show_database)
        data = cur.fetchall()
        
        
        mysql.connection.commit()
        cur.close()


                

        return render_template('index.html', value = data)

 
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)
