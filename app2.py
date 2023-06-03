from flask import Flask,redirect,url_for,render_template,request,jsonify

app=Flask(__name__)
# Membuat route default dimana route ini secara otomatis akan dijalankan 
# pertama kali oleh server. Route ini memiliki 2 Methods yaitu GET dan POST dan akan 
# menjalankan fungsi home() ketika diakses
@app.route('/',methods=['GET','POST'])
def home():
    # Ketika function home() dijalankan akan terdapat conditional statement dimana
    # jike request method-nya adalah POST, maka kita akan mendapatkan data yang dikirimkan 
    # web browser
    if request.method=='POST':
        #Terdapat 3 Data request yang diterima akan ditampung ke dalam sebuah variabel
        #Yaitu merk, pro, ukuran (data ini dikirim melalui atribut name pada tag input)
        merk = request.form['merk']
        pro = request.form['pro']
        ukuran = request.form['ukuran']
        # Setelah melakukan proses penjumlahan, maka kita akan me-return ke sebuah halaman.
        # dengan redirect() kita dapat melakukan pengalihan dari satu page ke page yang lainnya (multipage)
        # url_for berfungsi untuk menghasilkan url dimana argument pertama berisikan functionnya 
        # lalu argument kedua adalah keyword yang akan kita lemparkan ke function itu.
        return redirect(url_for('keranjang', merk=merk, pro=pro,ukuran=ukuran))
    # Ketika function home() dijalankan, maka akan langsung me-return halaman laptop.html
    # yang diambil dari folder template menggunakan function render_template()
    return render_template('laptop.html')

# Membuat route keranjang dimana route ini secara otomatis akan diakses 
# ketika dipanggil, pada kasus ini akan diakses karena functionnya dipanggil oleh route('/') 
@app.route('/keranjang')
def keranjang():
# Data request yang diterima akan ditampung ke dalam sebuah variabel, data yang diterima ini
    # adalah result_given dimana ia merupakan keyword yang dilemparkan dari function calc()
    # Disini, kita menggunakan query string untuk meneruskan data ke web browser. 
    # Contohnya nanti pada url web browser: http://127.0.0.1:5000/keranjang?merk=asus,pro=intel,ukuran=12
    # untuk menghandle query string kita menggunakan request.args.get.
    merk = request.args.get('merk')
    pro = request.args.get('pro')
    ukuran = request.args.get('ukuran')
    result = request.args.get('result_given')
    # Lalu me-return halaman home.html yang diambil dari folder template menggunakan
    # function render_template() dengan keyword merk, pro, dan ukuran yang nantinya akan kita letakkan
    # menggunakan jinja pada keranjang.html
    return render_template('keranjang.html',merk=merk, pro=pro,ukuran=ukuran)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run('0.0.0.0',port=4000,debug=True)