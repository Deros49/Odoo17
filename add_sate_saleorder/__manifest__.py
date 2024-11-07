{
    'name': 'Add_sate_sale_order',
    'version': '1.0',
    'summary': 'Ajouter un état sur le champ state de la commande de vente',
    'description': 'Ce module ajoute un état sur le champ state dans le modèle sale.order.',
    'author': 'Votre Nom ou Société',
    'depends': ['sale'],  # Assurez-vous que le module dépend de "sale"
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
