import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='art_gallery_db'
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galleries', methods=['GET', 'POST'])
def galleries():
    connection = get_db_connection()
    cursor = connection.cursor()
    message = None
    galleries = None

    if request.method == 'POST':
        if 'add' in request.form:
            cursor.execute(
                'INSERT INTO art_galleries (gallery_name, location, gallery_contact_no) VALUES (%s, %s, %s)',
                (request.form['gallery_name'], request.form['location'], request.form['gallery_contact_no'])
            )
            connection.commit()

        elif 'search' in request.form:
            cursor.execute('SELECT * FROM art_galleries WHERE gallery_id = %s', (request.form['gallery_id'],))
            galleries = cursor.fetchall()

            if not galleries:
                message = "No gallery found with the specified ID." 

        elif 'delete' in request.form:
            cursor.execute('DELETE FROM art_galleries WHERE gallery_id = %s', (request.form['gallery_id'],))
            connection.commit()

    cursor.execute('SELECT * FROM art_galleries')
    all_galleries = cursor.fetchall() 
    cursor.close()
    connection.close()
    return render_template('galleries.html', galleries=all_galleries, message=message, search_results=galleries) 

@app.route('/artists', methods=['GET', 'POST'])
def artists():
    connection = get_db_connection()
    cursor = connection.cursor()
    message = None 
    search_results = None  

    if request.method == 'POST':
        if 'add' in request.form:
            artist_name = request.form['artist_name']
            bio = request.form['bio']
            contact_no = request.form['artist_contact_no']
            cursor.execute('INSERT INTO artists (artist_name, bio, artist_contact_no) VALUES (%s, %s, %s)',
                           (artist_name, bio, contact_no))
            connection.commit()
        
        elif 'search' in request.form:
            artist_id = request.form['artist_id']
            cursor.execute('SELECT * FROM artists WHERE artist_id = %s', (artist_id,))
            search_results = cursor.fetchall()
            if not search_results:
                message = "No artist found with the given ID."

        elif 'delete' in request.form:
            artist_id = request.form['artist_id']
            cursor.execute('DELETE FROM artists WHERE artist_id = %s', (artist_id,))
            connection.commit()

    cursor.execute('SELECT * FROM artists')
    all_artists = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('artists.html', artists=all_artists, message=message, search_results=search_results)


@app.route('/artworks', methods=['GET', 'POST'])
def artworks():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    message = None
    search_results = None 

    if request.method == 'POST':
        if 'add' in request.form:
            title = request.form['title']
            artist_id = request.form['artist_id']
            year_created = request.form['year_created']
            medium = request.form['medium']
            price = request.form['price']
            gallery_id = request.form['gallery_id']
            cursor.execute('INSERT INTO artworks (title, artist_id, year_created, medium, price, gallery_id) VALUES (%s, %s, %s, %s, %s, %s)',
                           (title, artist_id, year_created, medium, price, gallery_id))
            connection.commit()

        elif 'search' in request.form:
            artwork_id = request.form['artwork_id']
            cursor.execute('SELECT * FROM artworks WHERE artwork_id = %s', (artwork_id,))
            search_results = cursor.fetchall()  
            if not search_results:
                message = "No artwork found with the provided ID."

        elif 'delete' in request.form:
            artwork_id = request.form['artwork_id']
            cursor.execute('DELETE FROM artworks WHERE artwork_id = %s', (artwork_id,))
            connection.commit()

    cursor.execute('SELECT * FROM artworks')
    all_artworks = cursor.fetchall() 
    cursor.close()
    connection.close()
    
    return render_template('artworks.html', artworks=all_artworks, message=message, search_results=search_results)


@app.route('/buyers', methods=['GET', 'POST'])
def buyers():
    connection = get_db_connection()
    cursor = connection.cursor()

    message = None
    search_results = None  

    if request.method == 'POST':
        if 'add' in request.form:
            buyer_name = request.form['buyer_name']
            contact_number = request.form['contact_number']
            address = request.form['address']
            cursor.execute('INSERT INTO buyers (buyer_name, contact_number, address) VALUES (%s, %s, %s)',
                           (buyer_name, contact_number, address))
            connection.commit()
        
        elif 'search' in request.form:
            buyer_id = request.form['buyer_id']
            cursor.execute('SELECT * FROM buyers WHERE buyer_id = %s', (buyer_id,))
            search_results = cursor.fetchone()
            if not search_results:
                message = "No buyer found with the given ID."

        elif 'delete' in request.form:
            buyer_id = request.form['buyer_id']
            cursor.execute('DELETE FROM buyers WHERE buyer_id = %s', (buyer_id,))
            connection.commit()

    cursor.execute('SELECT * FROM buyers')
    all_buyers = cursor.fetchall()  
    cursor.close()
    connection.close()
    return render_template('buyers.html', buyers=all_buyers, message=message, search_results=search_results)


@app.route('/exhibitions', methods=['GET', 'POST'])
def exhibitions():
    connection = get_db_connection()
    cursor = connection.cursor()

    message = None
    search_results = None  
    if request.method == 'POST':
        if 'add' in request.form:
            exhibition_name = request.form['exhibition_name']
            gallery_id = request.form['gallery_id']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            artwork_id = request.form['artwork_id']
            cursor.execute('INSERT INTO exhibitions (exhibition_name, gallery_id, start_date, end_date, artwork_id) VALUES (%s, %s, %s, %s, %s)',
                           (exhibition_name, gallery_id, start_date, end_date, artwork_id))
            connection.commit()

        elif 'search' in request.form:
            exhibition_id = request.form['exhibition_id']
            cursor.execute('SELECT * FROM exhibitions WHERE exhibition_id = %s', (exhibition_id,))
            search_results = cursor.fetchall()
            if not search_results:
                message = "No exhibition found with the given ID."

        elif 'delete' in request.form:
            exhibition_id = request.form['exhibition_id']
            cursor.execute('DELETE FROM exhibitions WHERE exhibition_id = %s', (exhibition_id,))
            connection.commit()

    cursor.execute('SELECT * FROM exhibitions')
    all_exhibitions = cursor.fetchall()  
    cursor.close()
    connection.close()
    return render_template('exhibitions.html', exhibitions=all_exhibitions, message=message, search_results=search_results)


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    connection = get_db_connection()
    cursor = connection.cursor()

    message = None
    search_results = None  

    if request.method == 'POST':
        if 'add' in request.form:
            artwork_id = request.form['artwork_id']
            sale_date = request.form['sale_date']
            buyer_id = request.form['buyer_id']
            sale_price = request.form['sale_price']
            cursor.execute('INSERT INTO sales (artwork_id, sale_date, buyer_id, sale_price) VALUES (%s, %s, %s, %s)',
                           (artwork_id, sale_date, buyer_id, sale_price))
            connection.commit()
        
        elif 'search' in request.form:
            sale_id = request.form['sale_id']
            cursor.execute('SELECT * FROM sales WHERE sale_id = %s', (sale_id,))
            search_results = cursor.fetchall()
            if not search_results:
                message = "No sale found with the given ID."

        elif 'delete' in request.form:
            sale_id = request.form['sale_id']
            cursor.execute('DELETE FROM sales WHERE sale_id = %s', (sale_id,))
            connection.commit()

    cursor.execute('SELECT * FROM sales')
    all_sales = cursor.fetchall()      
    cursor.close()
    connection.close()
    return render_template('sales.html', sales=all_sales, message=message, search_results=search_results)


@app.route('/upcoming_exhibitions')
def upcoming_exhibitions():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM exhibitions WHERE start_date > NOW() ORDER BY start_date ASC')
    
    exhibitions = cursor.fetchall()
    cursor.close()
    connection.close()
  
    return render_template('upcoming_exhibitions.html', exhibitions=exhibitions)


@app.route('/search_artworks', methods=['GET', 'POST'])
def search_artworks():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = '''
        SELECT 
            artworks.artwork_id, artworks.title, artworks.year_created, artworks.medium, artworks.price, 
            artists.artist_id, artists.artist_name, artists.bio, artists.artist_contact_no, 
            galleries.gallery_id, galleries.gallery_name, galleries.location, galleries.gallery_contact_no, 
            buyers.buyer_id, buyers.buyer_name, buyers.contact_number, buyers.address, 
            exhibitions.exhibition_id, exhibitions.exhibition_name, exhibitions.start_date, exhibitions.end_date, 
            sales.sale_id, sales.sale_date, sales.sale_price
        FROM artworks
        LEFT JOIN artists ON artworks.artist_id = artists.artist_id
        LEFT JOIN art_galleries AS galleries ON artworks.gallery_id = galleries.gallery_id
        LEFT JOIN exhibitions ON artworks.artwork_id = exhibitions.artwork_id
        LEFT JOIN sales ON artworks.artwork_id = sales.artwork_id
        LEFT JOIN buyers ON sales.buyer_id = buyers.buyer_id
        WHERE 1=1
    '''

    params = []

    title = request.form.get('title')
    artist_id = request.form.get('artist_id')
    artist_name = request.form.get('artist_name')
    gallery_id = request.form.get('gallery_id')
    gallery_name = request.form.get('gallery_name')
    buyer_id = request.form.get('buyer_id')
    buyer_name = request.form.get('buyer_name')
    exhibition_id = request.form.get('exhibition_id')
    exhibition_name = request.form.get('exhibition_name')
    min_price = request.form.get('min_price')
    max_price = request.form.get('max_price')

    if title:
        query += " AND artworks.title ILIKE %s"
        params.append(f"%{title}%")
    if artist_id:
        query += " AND artworks.artist_id = %s"
        params.append(artist_id)
    if artist_name:
        query += " AND artists.artist_name ILIKE %s"
        params.append(f"%{artist_name}%")
    if gallery_id:
        query += " AND galleries.gallery_id = %s"
        params.append(gallery_id)
    if gallery_name:
        query += " AND galleries.gallery_name ILIKE %s"
        params.append(f"%{gallery_name}%")
    if buyer_id:
        query += " AND buyers.buyer_id = %s"
        params.append(buyer_id)
    if buyer_name:
        query += " AND buyers.buyer_name ILIKE %s"
        params.append(f"%{buyer_name}%")
    if exhibition_id:
        query += " AND exhibitions.exhibition_id = %s"
        params.append(exhibition_id)
    if exhibition_name:
        query += " AND exhibitions.exhibition_name ILIKE %s"
        params.append(f"%{exhibition_name}%")
    if min_price:
        query += " AND artworks.price >= %s"
        params.append(min_price)
    if max_price:
        query += " AND artworks.price <= %s"
        params.append(max_price)

    cursor.execute(query, params)
    artworks = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('search_artworks.html', artworks=artworks)



if __name__ == '__main__':
    app.run(debug=True)
