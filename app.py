from flask import Flask, request, render_template, redirect, url_for, abort, flash

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'

régions = [
   {'id' : 1 ,'nom_region':'FrancheComte'},
   {'id' : 2 ,'nom_region':'IleDeFrance'},
   {'id' : 3 ,'nom_region':'Bretagne'},
   {'id' : 4 ,'nom_region':'Occitanie'},
]

clubs = [
   {'id' : 1 ,'nom':'BelfortEchecs', 'nb_adherent':'67', 'date_creation':'1977-01-31', 'prix_cotisation':'100', 'region_id':1, 'image': 'BelfortEchecs.jpeg'},
   {'id' : 2 ,'nom':'EchiquierQuimpérois', 'nb_adherent':'36', 'date_creation':'1983-06-27', 'prix_cotisation':'90', 'region_id':3, 'image':'EchiquierQuimpérois.png'},
   {'id' : 3 ,'nom':'TremblayEnFrance', 'nb_adherent':'109', 'date_creation':'1982-03-05', 'prix_cotisation':'50', 'region_id':2, 'image': 'TremblayEnFrance.png'},
   {'id' : 4 ,'nom':'EchiquierLedonien', 'nb_adherent':'25', 'date_creation':'1966-06-12', 'prix_cotisation':'71', 'region_id':1, 'image':'EchiquierLedonien.png'},
   {'id' : 5 ,'nom':'EchiquierNimois' , 'nb_adherent':'85', 'date_creation':'1987-03-21', 'prix_cotisation':'120', 'region_id':4, 'image': 'EchiquierNimois.jpeg'},
   {'id' : 6 ,'nom':'LuteceEchecs', 'nb_adherent':'89', 'date_creation':'1957-08-05', 'prix_cotisation':'420', 'region_id':2, 'image': 'LuteceEchecs.png'},
   {'id' : 7 ,'nom':'UsamEchiquierBrestois', 'nb_adherent':'73', 'date_creation':'1964-06-25', 'prix_cotisation':'100', 'region_id':3, 'image': 'UsamEchiquierBrestois.jpg'},
   {'id' : 8 ,'nom':'EchecsClubMontpellier' , 'nb_adherent':'119', 'date_creation':'1981-04-15', 'prix_cotisation':'85', 'region_id':4, 'image': 'EchecsClubMontpellier.png'},
   {'id' : 9 ,'nom':'ClichyEchecs92', 'nb_adherent':'85', 'date_creation':'1961-10-07', 'prix_cotisation':'189', 'region_id':2, 'image': 'ClichyEchecs92.jpeg'},
   {'id' : 10 ,'nom':'RoiBlancMontbeliard', 'nb_adherent':'31', 'date_creation':'1950-02-10', 'prix_cotisation':'76', 'region_id':1,'image': 'RoiBlancMontbeliard.jpg'},
   {'id' : 11 ,'nom':'EchiquierToulousain', 'nb_adherent':'88', 'date_creation':'1978-03-18', 'prix_cotisation':'140', 'region_id':4, 'image': 'EchiquierToulousain.png'},
   {'id' : 12 ,'nom':'RennesPaulBert', 'nb_adherent':'89', 'date_creation':'1959-10-07', 'prix_cotisation':'115', 'region_id':3, 'image': 'RennesPaulBert.png'},
]

@app.route('/')
def show_accueil():
    return render_template('layout.html')

@app.route('/région/show')
def show_region():
    #print(régions)
    return render_template('région/show_region.html', régions=régions)

@app.route('/filtre')
def show_tout():
    return render_template('filtre.html')

@app.route('/région/add', methods=['GET'])
def add_region():
    return render_template('région/add_region.html')

@app.route('/région/add', methods=['POST'])
def valid_add_region():
    nom_region = request.form.get('nom_region', '')
    print(u'type ajouté , nom_region :', nom_region)
    message = u'type ajouté , nom_region :'+nom_region
    flash(message, 'alert-success')
    return redirect('/région/show')

@app.route('/région/delete', methods=['GET'])
def delete_région():
    id = request.args.get('id', '')
    print ("une région supprimé, id :",id)
    message=u'une région supprimé, id : ' + id
    flash(message, 'alert-warning')
    return redirect('/région/show')

@app.route('/région/edit', methods=['GET'])
def edit_region():
    id = request.args.get('id', '')
    nom_region = request.args.get('nom_region', '')     # comment passé plusieurs paramètres (clé primaire composés)
    id=int(id)
    région = régions[id-1]
    return render_template('région/edit_region.html', région=région)

@app.route('/région/edit', methods=['POST'])
def valid_edit_region():
    nom_region = request.form['nom_region']
    id = request.form.get('id', '')
    print(u'une région modifiée, id: ',id, " nom_region :", nom_region)
    message=u'une région modifiée, id: ' + id + " nom_region : " + nom_region
    flash(message, 'alert-success')
    return redirect('/région/show')

@app.route('/club/show')
def show_club():
    # print(articles)
    return render_template('club/show_club.html', clubs=clubs)

@app.route('/club/add', methods=['GET'])
def add_club():
    return render_template('club/add_club.html', régions=régions)

@app.route('/club/add', methods=['POST'])
def valid_add_club():
    nom = request.form.get('nom', '')
    région_id = request.form.get('region_id', '')
    nb_adherent = request.form.get('nb_adherent', '')
    date_creation = request.form.get('date_creation', '')
    prix_cotisation = request.form.get('prix_cotisation', '')
    image = request.form.get('image', '')
    print(u'article ajouté , nom: ', nom, ' - region_id :', région_id, ' - nb_adherent:', nb_adherent,' - date_creation:', date_creation, ' - prix_cotisation:', prix_cotisation, ' - image:', image)
    message = u'article ajouté , nom:' + nom + '- region_id :' + région_id + ' - nb_adherent:' + nb_adherent + ' - date_creation:' + date_creation + ' - prix_cotisation:' + prix_cotisation + ' - image:' + image
    flash(message, 'alert-success')
    return redirect('/club/show')

@app.route('/club/delete', methods=['GET'])
def delete_club():
    id = request.args.get('id', '')
    message=u'un club supprimé, id : ' + id
    flash(message, 'alert-warning')
    return redirect('/club/show')

@app.route('/club/edit', methods=['GET'])
def edit_club():
    id = request.args.get('id', '')
    id = int(id)
    club = clubs[id-1]
    return render_template('club/edit_club.html', club=club, régions=régions)

@app.route('/club/edit', methods=['POST'])
def valid_edit_club():
    nom = request.form.get('nom', '')
    id = request.form.get('id', '')
    région_id = request.form.get('region_id', '')
    nb_adherent = request.form.get('nb_adherent', '')
    date_creation = request.form.get('date_creation', '')
    prix_cotisation = request.form.get('prix_cotisation', '')
    image = request.form.get('image', '')
    print(u'article ajouté , nom: ', nom, ' - region_id :', région_id, ' - nb_adherent:', nb_adherent,' - date_creation:', date_creation, ' - prix_cotisation:', prix_cotisation, ' - image:', image)
    message = u'article ajouté , nom:' + nom + '- region_id :' + région_id + ' - nb_adherent:' + nb_adherent + ' - date_creation:' + date_creation + ' - prix_cotisation:' + prix_cotisation + ' - image:' + image
    flash(message, 'alert-success')
    return redirect('/club/show')

@app.route('/filtre', methods=['GET'])
def filtre():
    filter_word = request.args.get('filter word', None)
    filter_value_min = request.args.get('filter_value min', None)
    filter_value_max = request.args.get('filter value max', None)
    filter_items = request.args.getlist('filter items', None)
    if filter_word and filter_word != "":
        message = 'filtre sur le mot : ' + filter_word
        flash(message, 'alert-success')
    if filter_value_min or filter_value_max:
        if filter_value_min. isdecimal() and filter_value_max.isdecimal():
            if int(filter_value_min) < int(filter_value_max):
                message = u'filtre sur la colonne avec un numérique entre : ' + filter_value_min + " et "+ filter_value_max
                flash(message,'alert-success')
            else:
                message=u'min <max!'
                flash(message, 'alert-warning')
        else:
            message=u'min et max doivent être des numériques'
            flash(message, 'alert-warning')
    if filter_items and filter_items != [] :
        message=u'case à cocher selectionnée : '
        for case in filter_items:
            message +=' id: '+case+ '  '
            flash(message, 'alert-success')
    return render_template('/filtre.html', clubs=clubs, régions=régions)

if __name__ == '__main__':
    app.run()
