from app import app
from flask import render_template
from models import DB

if __name__ == "__main__":
    a=DB()
    # a.create_table()
    a.insert_table("ravi","2020-4-5",9000)
    a.fetch()
    a.update_table(4000,'2019-5-18','alex')
    a.delete('ravi')
    row=a.fetch()
    app.run(debug=True) 