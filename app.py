from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder='./templates',
            static_folder='./static',
            instance_relative_config=True,
            )


@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact_us.html')


@app.route('/partner', methods=['GET'])
def partner():
    return render_template('partner.html')


@app.route('/professionalServices', methods=['GET'])
def professional_services():
    return render_template('professional_services.html')


@app.route('/itIotSolution', methods=['GET'])
def it_iot_solution():
    return render_template('it_iot_solution.html')


@app.route('/odooErp', methods=['GET'])
def odoo_erp():
    return render_template('odoo_erp.html')


@app.route('/vms', methods=['GET'])
def vms():
    return render_template('vms.html')


@app.route('/cctvSystem', methods=['GET'])
def cctv_system():
    return render_template('cctv_system.html')


@app.route('/dataCenter', methods=['GET'])
def data_center():
    return render_template('data_center.html')


if __name__ == '__main__':
    app.run()
