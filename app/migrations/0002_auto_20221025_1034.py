# Generated by Django 3.1 on 2022-10-25 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aap',
            name='Alanine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Arginine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Aspartic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Cystine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Glutamic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Glycine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Histidine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Isoleucine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Luecine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Lysine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Methionine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Phenylalanine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Proline',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Serine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Threonine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Tryptophan',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Tyrosine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='aap',
            name='Valine',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='A_Carotene',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='BCryptoxanthin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='B_Carotene',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='G_Carotene',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='Lutein',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='Lycopene',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='Total_Carotenoids',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='carotenoids',
            name='Zeaxanthin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Arachidic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Behenic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Butyric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Capric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Caproic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Caprylic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Eicosenoic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Elaidic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Erucic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Lauric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Lignoceric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Linoleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Linolenic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Mono_Unsaturated_Fatty_Acids',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Myristic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Myristoleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Oleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Palmitic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Palmitoleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Poly_Unsaturated_Fatty_Acids',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Saturated_Fatty_Acids',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='eof',
            name='Stearic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='A_Linolenic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Arachidic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Arachidonic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Behenic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Capric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Eicosadienoic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Eicosaenoic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Erucic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Lauric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Lignoceric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Linoleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Mono_UnSaturated_Fatty_Acids',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Myristic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Myristoleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Nervonic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Oleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Palmitic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Palmitoleic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Saturated_Fatty_Acids',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='Stearic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fap',
            name='poly_UnSaturated_Fatty_Acids',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='ERGCAL',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCPHA',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCPHB',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCPHD',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCPHG',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCTRA',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCTRB',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCTRD',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='TOCTRG',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='VITE',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='fsv',
            name='VITK1',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Aluminium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Arsenic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Cadmium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Calcium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Chromium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Cobalt',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Copper',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Iron',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Lead',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Lithium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Magnesium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Manganese',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Mercury',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Molebdeum',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Nickel',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Phosphorus',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Potassium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Selenium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Sodium',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='mte',
            name='Zinc',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Cis_Aconitic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Citric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Fumaric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Mallic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Oxalate_insoluble',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Oxalate_soluble',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Quinic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Succinic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='oa',
            name='Tartaric',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Ajugose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='B_Sitosterol',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Campesterol',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Phytate',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Raffinose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Stachyose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Stigmasterol',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Total_Saponin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='opps',
            name='Verbascose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Apigenin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Apigenin_6_C_gluoside',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Apigenin_7_O_neohesperidoside',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Caffeic_acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Chlorogenic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Cinamic_acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Daidzein',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Epicatechin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Ferulic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Gallic_acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Genistein',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Hesperdin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Hesperetin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Hydroxy_3_benzaldehyde',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Isoramnetin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Kaempferol',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Luteolin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Myricetin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Naringenin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='O_Coumaric_acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='P_Coumaric_acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Protocatechuic_acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Quercetin',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Quercetin_3_B_Dglucoside',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Quercetin_3_O_rutinoside',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Quercetin_3_β_galactoside',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Resvertrol',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='Vanillic_acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='pp',
            name='acid_3_4_Dihydroxy_benzoic',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='ash',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='carbohydrates',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='df_insoluble',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='df_soluble',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='energy',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='protein',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='totalfat',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='ppdf',
            name='water',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='Free_Sugars',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='Fructose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='Glucose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='Maltose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='Starch',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='Sucrose',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='Total_CHO',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='Ascorbic_Acid',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='B6',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='Biotin_B7',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='Folates_B9',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='Niacin_B3',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='Pantothenic_Acid_B5',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='Riboflavin_B2',
            field=models.FloatField(null = True),
        ),
        migrations.AlterField(
            model_name='wsv',
            name='Thiamine_B1',
            field=models.FloatField(null = True),
        ),
    ]
