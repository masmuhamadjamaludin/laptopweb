# Program Laptop dengan request POST GET menggunakan Jinja
from flask import Flask,redirect,url_for,render_template,request, jsonify


app=Flask(__name__)
# Membuat route default dimana route ini secara otomatis akan dijalankan 
# pertama kali oleh server. Route ini memiliki 2 Methods yaitu GET dan POST dan akan 
# menjalankan fungsi home() ketika diakses dimana akan langsung  me-return halaman laptop.html
# yang diambil dari folder template menggunakan function render_template()
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('laptop.html')

#Disini kita menerima data dengan menggunakan request GET dimana dikirimkan oleh AJAX 
@app.route('/siap')
def siap():
    name = request.args.get('name')
    #Memberikan response ke client dalam bentuk json
    return jsonify({
        'name':name
    })

# Membuat route keranjang dimana route ini secara otomatis akan diakses 
# ketika dipanggil yaitu ketika menekan button submit dimana ketika action dari tag form
# adalah /keranjang dengan method post 
@app.route('/keranjang',methods=['POST'])
def keranjang():
    #Disini kita mendapatkan data dari client menggunakan method post 
    merk = request.form['merk']
    pro = request.form['pro']
    ukuran = request.form['ukuran']
    # Lalu me-return halaman keranjang.html yang diambil dari folder template menggunakan
    # function render_template() dengan keyword merk, pro, dan ukuran
    # yang nantinya akan kita letakkan menggunakan jinja pada keranjang.html
    return render_template('keranjang.html', merk=merk, pro=pro,ukuran=ukuran)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run('0.0.0.0',port=5000,debug=True)