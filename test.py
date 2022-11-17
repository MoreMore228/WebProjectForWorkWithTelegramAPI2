from flask import Flask, render_template, request, redirect





app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def phone_number():
    if request.method == 'POST':
        phoneNumber = request.form['phonenumber']
        print(phoneNumber)
        return redirect('/code')
    
    return render_template('1.html')


@app.route('/code', methods=['POST', 'GET'])
def send_code():
    if request.method == 'POST':
        sendcode = request.form['title']

        print(sendcode)

        return redirect('/code/groopresend')
    
    return render_template('2.html')


@app.route('/code/groopresend', methods=['POST', 'GET'])
def groop_resend():
    if request.method == 'POST':
        input_canals_list = request.form['input_canals_list']
        search_text = request.form['search_text']
        output_canals_list = request.form['output_canals_list']

        print(input_canals_list, search_text, output_canals_list, sep='\n')

        return redirect('/code/groopresend/endpage')
    
    return render_template('3.html')


@app.route('/code/groopresend/endpage')
def end_page():
    return render_template('4.html')


if __name__ == "__main__":
    app.run(debug=True)






