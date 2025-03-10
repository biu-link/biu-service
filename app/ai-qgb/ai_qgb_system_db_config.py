from load_table_message_template import load_table_message_template
from load_product_setting import load_product_setting

db = 'mysql_prod'

load_table_message_template(db)

load_product_setting(db)
