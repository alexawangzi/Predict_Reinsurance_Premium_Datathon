
TO_DROP = [#'DIVISION_NUM',
	'CT_STATUS',
	'UF_STATUS',
	'TAG',
	'REPORTCCY',
	'DIVISION_ID',
	'COVERAGE',
	'DEDUCTIBLES',
	'ORIGCCY',
	'MARKET',
	'MAIN_COUNTRY',
	#'MAIN_PRICING_CATEG',
	'MAIN_PRICING_SUBCATEG',
	'SUBSECTOR',
	'INCEPTION_MONTH',
	'INCEPTION',
	'EXPIRY',
	'PRICING_DATE']



SECTOR_PAIR = {'BS Construction':'BS CP', 'BS Property':'BS CP'}

GUARANTEE_PAIR = {'Property Damage':'PFF', 
                  'Fire Following Earthquake':'PFF',
                  'Fire':'PFF',
                  'Unspecified': 'EU',
                  'Earthquake-shake only': 'EU'}
    
BUSINESSUNIT_PAIR = {'BS Property': 'BS Property',
                             'BS Property (Power)': 'BS Property',
                             'BS Energy On-shore': 'BS Energy',
                             'BS Energy Mining': 'BS Energy'}
    
UWCENTER_PAIR = {'LATIN AMERICA': 'LAC',
                         'ASIA PACIFIC': 'LAC',
                         'CANADA': 'LAC'}
    
    
SUBSECTOR_PAIR = {'ONSHORE CO & CHEMICAL CO': 'HEAVY',
                          'HEALTHCARE': 'HEAVY',
                          'MINING COMPANY': 'HEAVY',
                          'OFFSHORE (E&P) COMPANY': 'HEAVY',
                          'CONSTRUCTION & ENGINEERING': 'HEAVY',
                          'CEDANTS FACULTATIVES SERVICES': 'HEAVY',
                          'HEAVY INDUSTRIES': 'HEAVY',
                          'UNSPECIFIED': 'HEAVY',
                          'HIGH TECH. INDUSTRIES': 'LIGHT_1',
                          'CONSUMER SERVICES': 'LIGHT_1',
                          'AGRICULTURAL/LIFE SCIENCES': 'LIGHT_1',
                          'POWER & UTILITY COMPANY': 'LIGHT_1',
                          'CONSUMER GOODS': 'LIGHT_1',
                          'OTHER INDUSTRIES': 'LIGHT_1',
                          'SECTOR UNSPECIFIED': 'LIGHT_1',
                          'AUTOMOTIVE & PARTS': 'LIGHT_1',
                          'OTHER SERVICES': 'LIGHT_1',
                          'TRANSPORTATION & LOGISTICS': 'LIGHT_2',
                           'CORPORATE PROPERTY & CASUALTY' :'LIGHT_2',
                           'ENVIRONMENTAL SERV. & IND.' :'LIGHT_2',
                           'TELECOMMUNICATIONS & MEDIA' :'LIGHT_2',
                           'ENERGY & NATURAL RESOURCES' :'LIGHT_2',
                           'FINANCIAL INSTITUTIONS' :'LIGHT_2',
                          'PROFESSIONAL SERVICES': 'LIGHT_2'}
    


NORTH_AMERICA = set(['Canada', 'United States of America', 'UNITED STATES', 'Puerto Rico'])
LATIN_AMERICA = set(['Antigua and Barbuda', 'Argentina', 'Bahamas', 'Barbados', 
                                                'Belize', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 
                                                'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 'El Salvador', 
                                                'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica',
                                                'Mexico', 'Netherlands Antilles', 'Nicaragua', 'Panama', 'Paraguay',
                                                'Peru', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 
                                                'Suriname', 'Trinidad and Tobago', 'Uruguay', 'Venezuela'])
WESTERN_EUROPE = set(['Austria', 'Belgium', 'Denmark', 'Finland', 'France', 'Germany', 
                                                 'Greece', 'Iceland', 'Ireland', 'Italy', 'Liechtenstein', 'Monaco',
                                                 'Luxembourg', 'Malta', 'Netherlands', 'Norway', 'Portugal', 
                                                 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'United Kingdom', 
                                                 'Bosnia and Herzegovina', 'Croatia', 'former Yugoslav Republic of Macedonia', 
                                                 'Slovenia', 'Yugoslavia'])
CENTRAL_AND_EASTERN_EUROPE = set(['Albania', 'Bulgaria', 'Czech Republic', 'Hungary', 'Poland', 
                                                             'Romania','the Slovak Republic', 'Estonia', 'Latvia', 'Lithuania',
                                                             'Armenia', 'Azerbaijan', 'Belarus', 'Georgia', 'Kazakhstan', 'Kyrgyz Repubic', 
                                                             'Republic of Moldova', 'Russian Federation', 'Russia', 'Tajikistan', 'Turkmenistan', 'Ukraine',
                                                             'Uzbekistan'])
AFRICA= set(['Algeria', 'Egypt', 'Libyan Arab Jamahiriya', 'Morocco', 'Tunisia',
                                         'Benin', 'Burkina Faso', 'Cape Verde', 'Ivory Coast', 'Gambia', 
                                         'Ghana', 'Guinea', 'Guinea-Bissau', 'Liberia', 'Mali', 'Mauritania', 
                                         'Niger', 'Nigeria', 'Senegal', 'Sierra Leone', 'Togo', 'Burundi', 'Cameroon', 
                                         'Central African Republic', 'Chad', 'Congo', 'Democratic Republic of the Congo', 
                                         'Equatorial Guinea', 'Gabon', 'Rwanda', 'Sao Tome and Principe', 'Comoros', 
                                         'Djibouti', 'Eritrea', 'Ethiopia', 'Kenya', 'Madagascar', 'Mauritius', 'Seychelles', 
                                         'Somalia', 'Sudan', 'United Republic of Tanzania', 'Tanzania', 'Uganda', 'Angola', 'Botswana', 
                                         'Lesotho', 'Malawi', 'Mozambique', 'Namibia', 'South Africa', 'Swaziland', 'Zambia', 
                                         'Zimbabwe'])
MIDDLE_EAST = set(['Bahrain', 'Cyprus', 'Iraq', 'Islamic Republic of Iran', 'Iran', 'Israel', 'Jordan', 
                                              'Kuwait', 'Lebanon', 'Oman', 'Qatar', 'Saudi Arabia', 'Syrian Arab Republic', 
                                              'United Arab Emirates', 'Yemen'])
MATURE_ASIA = set(['Australia','Hong Kong', 'Japan', 'New Zealand', 'Taiwan', 'Singapore', 'Republic of Korea', 'South Korea'   ])
EMERGING_ASIA = set(['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka', 
                                                'Brunei Darussalam', 'Brunei', 'Cambodia', 'China', 'Fiji', 'Indonesia', 'Kiribati', "Lao People's Democratic Republic", 
                                                'Laos','Macau', 'Malaysia', 'Mongolia', 'Myanmar', 'Papua New Guinea', 'Philippines', 'Samoa', 'Myanmar (Burma)',
                                                'Solomon Islands', 'Thailand', 'Tonga', 'Tuvalu', 'Vanuatu', 'Vietnam', ])


