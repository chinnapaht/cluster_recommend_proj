from flask import Flask , render_template , request
import pickle
import numpy as np
import pandas as pd



model = pickle.load(open('km.pkl','rb'))
pca= pickle.load(open('pca.pkl','rb'))
scaler= pickle.load(open('scaler.pkl','rb'))

app = Flask(__name__)

df = pd.read_csv("df_clus")


@app.route('/')
def first():
    return render_template('home.html')


@app.route('/cluster' , methods = ['POST'])

def home():
    try :
        d1 = int(request.form['a'])
        if d1 == 100000 :
            d1 = int(request.form['a_input'])

        d2 = int(request.form['b'])
        if d2 == 100000 :
            d2 = int(request.form['b_input'])

        d3 = int(request.form['c'])
        if d3 == 100000 :
            d3 = int(request.form['c_input'])

        d4 = int(request.form['d'])
        if d4 == 100000 :
            d4 = int(request.form['d_input'])

        d5 = int(request.form['e'])
        if d5 == 100000 :
            d5 = int(request.form['e_input'])

        d6 = int(request.form['f'])
        if d6 == 100000 :
            d6 = int(request.form['f_input'])

        d7 = int(request.form['g'])
        if d7 == 100000 :
            d7 = int(request.form['g_input'])

        d8 = int(request.form['h'])
        if d8 == 100000 :
            d8 = int(request.form['h_input'])

        d9 = int(request.form['i'])
        if d9 == 100000 :
            d9 = int(request.form['i_input'])

        gen = request.form['genre']
        
    except ValueError :
        return render_template('input_error.html')
    except :
        return render_template('request_error.html')


    arr = np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9]])
    
    arr = scaler.transform(arr)

    X_prin = pca.transform(arr)

    pred = model.predict(X_prin)


    data = df[df["clus"]== pred[0]] 
    data = data.sort_values(by='pop', ascending=False)
    data_genre = data[data["genre"] == gen]
    data_genre_title = data_genre.title
    data_genre_artist = data_genre.artist
    data_title = data[:10].title
    data_artist = data[:10].artist


    top_cluster = [data_title.iloc[i] + "  by  " +  data_artist.iloc[i] for i in range(0,10)]
    

    y = [data_genre_title.iloc[i] + "  by  " +  data_genre_artist.iloc[i] for i in range(len(data_genre_artist))]
    z = set(y) - set(top_cluster)

    if len(z) > 10  :
        song = list(z)
        song_genre = [song[i] for i in range(10)]
        
    else: 
        song = list(z)
        song_genre = [i for i in z]


    return render_template("final.html" , song1 = top_cluster ,song2 =song_genre , d1=d1 ,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,d7=d7,d8=d8,d9=d9,genre =gen , pred = pred[0])


if __name__ == "__main__" :
    app.run(debug = True)