from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Table Utilisateurs
class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'
    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(50), unique=True, nullable=False)
    password    = db.Column(db.String(100), nullable=False)
    role        = db.Column(db.String(50), nullable=False)
    nom_complet = db.Column(db.String(100))
    statut      = db.Column(db.String(20), default='Actif')

# Table Clients
class Client(db.Model):
    __tablename__ = 'clients'
    id        = db.Column(db.Integer, primary_key=True)
    numero    = db.Column(db.String(20), unique=True)
    nom       = db.Column(db.String(100), nullable=False)
    adresse   = db.Column(db.String(200))
    telephone = db.Column(db.String(20))
    email     = db.Column(db.String(100))
    nif       = db.Column(db.String(50))
    rccm      = db.Column(db.String(50))

# Table Factures
class Facture(db.Model):
    __tablename__ = 'factures'
    id            = db.Column(db.Integer, primary_key=True)
    numero        = db.Column(db.String(30), unique=True, nullable=False)
    date          = db.Column(db.DateTime, default=datetime.now)
    nom_client    = db.Column(db.String(100), nullable=False)
    service       = db.Column(db.String(200), nullable=False)
    montant_ttc   = db.Column(db.Float, nullable=False)
    mode_paiement = db.Column(db.String(50))
    etat_paiement = db.Column(db.String(20), default='Non Payer')
    type_operation= db.Column(db.String(20), default='Recettes')
    categorie     = db.Column(db.String(20), default='Facture')
    section       = db.Column(db.String(50))
    cree_par      = db.Column(db.String(50))
    montant_paye  = db.Column(db.Float, default=0)
    reste_du      = db.Column(db.Float, default=0)

# Table Operations
class Operation(db.Model):
    __tablename__ = 'operations'
    id            = db.Column(db.Integer, primary_key=True)
    numero        = db.Column(db.String(30), unique=True, nullable=False)
    date          = db.Column(db.DateTime, default=datetime.now)
    nom_client    = db.Column(db.String(100))
    service       = db.Column(db.String(200))
    montant_ttc   = db.Column(db.Float)
    type_operation= db.Column(db.String(20))
    categorie     = db.Column(db.String(20))
    section       = db.Column(db.String(50))
    cree_par      = db.Column(db.String(50))

    # ================================================================
# MODÈLE PARAMETRES — à ajouter à la fin de database.py
# ================================================================

class Parametres(db.Model):
    __tablename__ = 'parametres'
    id                   = db.Column(db.Integer, primary_key=True)
    nom_entreprise       = db.Column(db.String(100), default='KS Production')
    slogan               = db.Column(db.String(200), default='Studio d\'Enregistrement & Sonorisation')
    adresse              = db.Column(db.String(200), default='Lomé, Togo')
    telephone            = db.Column(db.String(50),  default='+228 XX XX XX XX')
    email                = db.Column(db.String(100), default='contact@ksproduction.tg')
    site_web             = db.Column(db.String(100), default='')
    nif                  = db.Column(db.String(50),  default='')
    rccm                 = db.Column(db.String(50),  default='')
    couleur_principale   = db.Column(db.String(10),  default='#e94560')
    mentions_legales     = db.Column(db.Text, default='Paiement à réception de facture. Tout retard de paiement entraîne des pénalités.')
    coordonnees_bancaires= db.Column(db.Text, default='')
    logo_filename        = db.Column(db.String(200), default='')

# ================================================================
# MODÈLE LigneFacture — à ajouter à la fin de database.py
# ================================================================

class LigneFacture(db.Model):
    __tablename__ = 'lignes_facture'
    id             = db.Column(db.Integer, primary_key=True)
    facture_id     = db.Column(db.Integer, db.ForeignKey('factures.id'), nullable=False)
    service        = db.Column(db.String(200), nullable=False)
    prix_unitaire  = db.Column(db.Float, default=0)
    quantite       = db.Column(db.Integer, default=1)
    montant_ht     = db.Column(db.Float, default=0)
    montant_ttc    = db.Column(db.Float, default=0)

    facture = db.relationship('Facture', backref=db.backref('lignes', lazy=True))

# ================================================================
# MODÈLE Service — à ajouter à la fin de database.py
# ================================================================

class Service(db.Model):
    __tablename__ = 'services'
    id      = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(50), nullable=False)
    libelle = db.Column(db.String(200), nullable=False)
    prix    = db.Column(db.Float, default=0)
    actif   = db.Column(db.Boolean, default=True)

    # ================================================================
# MODÈLE Paiement — à ajouter à la fin de database.py
# ================================================================

class Paiement(db.Model):
    __tablename__ = 'paiements'
    id             = db.Column(db.Integer, primary_key=True)
    numero         = db.Column(db.String(30), unique=True, nullable=False)
    date           = db.Column(db.DateTime, default=datetime.now)
    facture_id     = db.Column(db.Integer, db.ForeignKey('factures.id'), nullable=False)
    n_facture      = db.Column(db.String(30))
    nom_client     = db.Column(db.String(100))
    montant_facture= db.Column(db.Float, default=0)
    montant_paye   = db.Column(db.Float, default=0)
    reste_du       = db.Column(db.Float, default=0)
    mode_paiement  = db.Column(db.String(50))
    etat_facture   = db.Column(db.String(20))
    notes          = db.Column(db.Text, default='')
    cree_par       = db.Column(db.String(50))

    facture = db.relationship('Facture', backref=db.backref('paiements', lazy=True))


    # ================================================================
# MODÈLE Evenement — à ajouter dans database.py
# ================================================================

class Evenement(db.Model):
    __tablename__ = 'evenement'
    id          = db.Column(db.Integer, primary_key=True)
    titre       = db.Column(db.String(200), nullable=False)
    date        = db.Column(db.Date, default=datetime.utcnow)
    heure_debut = db.Column(db.String(10), nullable=True)   # "09:00"
    heure_fin   = db.Column(db.String(10), nullable=True)   # "17:00"
    nom_client  = db.Column(db.String(150), nullable=True)
    service     = db.Column(db.String(200), nullable=True)
    section     = db.Column(db.String(50),  nullable=True)
    lieu        = db.Column(db.String(200), nullable=True)
    notes       = db.Column(db.Text,        nullable=True)
    statut      = db.Column(db.String(30),  default='Confirmé')  # Confirmé, Tentative, Annulé
    cree_par    = db.Column(db.String(80),  nullable=True)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    facture_id = db.Column(db.Integer, db.ForeignKey('factures.id'), nullable=True)
    facture     = db.relationship('Facture', foreign_keys=[facture_id], lazy=True)
    

# ================================================================
# MODÈLES à ajouter dans database.py
# ================================================================

class Technicien(db.Model):
    __tablename__ = 'technicien'
    id          = db.Column(db.Integer, primary_key=True)
    nom         = db.Column(db.String(150), nullable=False)
    telephone   = db.Column(db.String(30),  nullable=True)
    email       = db.Column(db.String(150), nullable=True)
    specialite  = db.Column(db.String(100), nullable=True)  # Sonorisation, Studio, Régie...
    statut      = db.Column(db.String(30),  default='Disponible')  # Disponible, Inactif
    notes       = db.Column(db.Text,        nullable=True)
    date_ajout  = db.Column(db.DateTime,    default=datetime.utcnow)

# Table de liaison Evenement ↔ Technicien (many-to-many)
class EvenementTechnicien(db.Model):
    __tablename__ = 'evenement_technicien'
    id            = db.Column(db.Integer, primary_key=True)
    evenement_id  = db.Column(db.Integer, db.ForeignKey('evenement.id'), nullable=False)
    technicien_id = db.Column(db.Integer, db.ForeignKey('technicien.id'), nullable=False)
    role          = db.Column(db.String(100), nullable=True)  # Chef de son, Assistant...

