from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',  
    'password': '098769543210',
    'database': 'Ranger_motion'
}

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employee_info")  
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/submit', methods=['POST'])
def create_user():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    salary = data.get('salary')

    if not name or salary is None:
        return jsonify({'error': 'Missing name or salary'}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employee_info (id ,name, salary) VALUES (%s , %s, %s)", (id ,name, salary))
        conn.commit()
        return jsonify({'message': 'Employee added successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



@app.route('/server_info', methods=['GET'])
def get_info():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM server_info")  
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/companies_info', methods=['GET'])
def get_companies():
    try:
        name = request.args.get('name')
        print('name',name)
        conn = mysql.connector.connect(**db_config) 
        cursor = conn.cursor(dictionary=True)
        # cursor.execute("SELECT * FROM companies")
        cursor.execute("SELECT * FROM companies WHERE name = %s",(name,))
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/companies_info', methods=['POST'])
def post_jobs():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    owner = data.get('owner')
    location = data.get('location')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO companies (id, name, owner, location) VALUES (%s , %s, %s, %s)", (id ,name, owner, location))
        conn.commit()
        return jsonify({'message': 'Student added successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

   
@app.route('/companies_info/<int:id>', methods=['PUT'])
def update_companies(id):
    data = request.get_json()
    name = data.get('name')
    owner = data.get('owner')
    location = data.get('location')

    # if not name or not salary:
    #     return jsonify({'error': 'Name and salary are required'}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE companies SET name = %s, owner = %s, location = %s WHERE id = %s",(name, owner, location, id))
        conn.commit()
        cursor.close()
        conn.close()

        if cursor.rowcount == 0:
            return jsonify({'message': 'No employee found with that ID'}), 404

        return jsonify({'message': 'Employee updated successfully'}), 200

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()   



@app.route('/companies_info/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM companies WHERE id = %s", (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({'message': 'No employee found with that ID'}), 404

        cursor.close()
        conn.close()
        return jsonify({'message': 'Employee deleted successfully'}), 200

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500



@app.route('/jobs/<role>', methods=['GET'])
def get_jobs(role):
    try:
        # role = request.args.get('role')
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM jobs WHERE role = %s", (role,))
        # cursor.execute("SELECT * FROM jobs")  

        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/edit_jobs', methods=['POST'])
def edit_jobs():
    data = request.get_json()
    id = data.get('id')
    role = data.get('role')
    qualifications = data.get('qualifications')
    salary = data.get('salary')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jobs (id ,role, qualifications, salary) VALUES (%s , %s, %s, %s)", (id ,role, qualifications, salary))
        conn.commit()
        return jsonify({'message': 'Employee added successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/edit_cars', methods=['POST'])
def edit_cars():
    data = request.get_json()
    id = data.get('id')
    BMW = data.get('BMW')
    Audi = data.get('Audi')
    honda = data.get('honda')
    hundai = data.get('hundai')
    maruti_suzuki = data.get('maruti_suzuki')
    kia = data.get('kia')
    MG = data.get('MG')
    Tesla = data.get('Tesla')
    Skoda = data.get('Skoda')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cars (id ,BMW ,Audi ,honda ,hundai ,maruti_suzuki ,kia ,MG ,Tesla ,Skoda ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id ,BMW ,Audi ,honda ,hundai ,maruti_suzuki ,kia ,MG ,Tesla ,Skoda))
        conn.commit()
        return jsonify({'message': 'Employee added successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



@app.route('/cars', methods=['GET'])
def get_cars():
    try:
        id = request.args.get('id')
        print('id',id)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        # cursor.execute("SELECT * FROM cars")
        cursor.execute("SELECT * FROM cars WHERE id = %s",(id,))  
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)





