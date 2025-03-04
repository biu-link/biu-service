weight_fields = {
    'qtyLabel': '商品净重',
    'qtyDesc': 'Net Weight'
}

volume_fields = {
    'qtyLabel': '商品体积',
    'qtyDesc': 'Volume'
}

solid_volume_fields = {
    'qtyLabel': '商品体积',
    'qtyDesc': 'Volume'
}

area_fields = {
    'qtyLabel': '商品面积',
    'qtyDesc': 'Area'
}

qty_fields = {
    'qtyLabel': '商品数量',
    'qtyDesc': 'Quantity'
}

rate_parse_rules = [
    {  # Free
        'pattern': r'^Free$',
        'byAmount': True,
        'amountRate': 0.0,
        'amountRateString': 'Free',
    },
    {  # 25.9%
        'pattern': r'^(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 1,
        'amountRateDivide': 100,
    },
    {  # 9.9% on the value of the lead content
        'pattern': r'^(\d+(\.\d+)?)%\s*on the value of the lead content$',
        'byAmount': True,
        'amountRateMatchIndex': 1,
        'amountRateDivide': 100,
        'amountLabel': '所含铅的货值',
        'amountDesc': 'Value Of The Lead Content'
    },
    {  # 29.1¢/kg + 25.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(kg|t)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **weight_fields
    },
    {  # 9.9¢/pr. + 25.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(pr\.)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'pair',
        'qtyLabel': '商品数量',
        'qtyDesc': 'Quantity'
    },
    {  # 29.1¢/kg
        'pattern': r'^(\d+(\.\d+)?)¢/(kg|t)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **weight_fields
    },
    {  # 9.9¢/liter
        'pattern': r'^(\d+(\.\d+)?)¢/(liter)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **volume_fields
    },
    {  # 9.9¢/bbl
        'pattern': r'^(\d+(\.\d+)?)¢/\s*(bbl|doz\.|gross|head|liter|pf\.liter)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **qty_fields
    },
    {
        # 9.9¢/bbl + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/\s*(bbl|doz\.|gross|head|liter|pf\.liter|thousand|1,000 pins)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **qty_fields
    },
    {
        # 9.9¢/line/ gross + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/\s*(line/\s*gross)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'line/gross',
        **qty_fields
    },
    {  # 9.9¢/clean kg
        'pattern': r'^(\d+(\.\d+)?)¢/\s*clean kg$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        **qty_fields
    },
    {  # 9.9¢/kg on drained weight
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on drained weight)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '商品排水后净重',
        'qtyDesc': 'Drained Weight'
    },
    {  # 9.9¢/kg on drained weight + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on drained weight)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '商品排水后净重',
        'qtyDesc': 'Drained Weight'
    },
    {  # 9.9¢/kg of total sugars
        'pattern': r'^(\d+(\.\d+)?)¢/(kg of total sugars)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '总糖含量',
        'qtyDesc': 'Total Sugars'
    },
    {  # 9.9¢/kg of total sugars + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(kg of total sugars)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '总糖含量',
        'qtyDesc': 'Total Sugars'
    },
    {  # 9.9¢/kg on lead content
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on lead content)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '铅含量',
        'qtyDesc': 'Lead Content'
    },
    {  # 9.9¢/kg on tungsten content + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on tungsten content)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '钨含量',
        'qtyDesc': 'Tungsten Content'
    },
    {  # 9.9¢/kg on magnesium content + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on magnesium content)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '镁含量',
        'qtyDesc': 'Magnesium Content'
    },
    {  # 9.9¢/kg on molybdenum content
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on molybdenum content)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '钼含量',
        'qtyDesc': 'Molybdenum Content'
    },
    {  # 9.9¢/kg on molybdenum content + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on molybdenum content)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '钼含量',
        'qtyDesc': 'Molybdenum Content'
    },
    {  # 9.9¢/kg on contents and container
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on contents and container)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '商品重量(含容器)',
        'qtyDesc': 'Contents and Container'
    },
    {  # 9.9¢/kg on entire contents of container
        'pattern': r'^(\d+(\.\d+)?)¢/(kg on entire contents of container)$',
        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnit': 'kg',
        'qtyLabel': '商品总重量',
        'qtyDesc': 'Entire Contents of Container'
    },
    {  # $9.1/kg + 25.9%
        'pattern': r'^\$(\d+(\.\d+)?)/(kg|t)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 1,
        'qtyUnitMatchIndex': 3,
        **weight_fields
    },
    {  # $9.1/kg
        'pattern': r'^\$(\d+(\.\d+)?)/(kg|t)$',

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 1,
        'qtyUnitMatchIndex': 3,
        **weight_fields
    },
    {  # $9.9 each

        'pattern': r'^\$(\d+(\.\d+)?)\s*(each)$',

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 1,
        'qtyUnitMatchIndex': 3,
        **qty_fields
    },
    {  # 9.9¢ each

        'pattern': r'^(\d+(\.\d+)?)¢\s*(each)$',

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **qty_fields
    },
    {  # 9.9¢ each + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢\s*(each)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **qty_fields
    },
    {  # $9.1/m3
        'pattern': r'^\$(\d+(\.\d+)?)/(m3)$',

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 1,
        'qtyUnitMatchIndex': 3,
        **solid_volume_fields
    },
    {  # $9.1/m2
        'pattern': r'^\$(\d+(\.\d+)?)/(m2)$',

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 1,
        'qtyUnitMatchIndex': 3,
        **area_fields
    },
    {  # 9.9¢/m2 + 9.9%
        'pattern': r'^(\d+(\.\d+)?)¢/(m2)\s*\+\s*(\d+(\.\d+)?)%$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 1,
        'qtyUnitMatchIndex': 3,
        **area_fields
    },
    {  # $9.1/1000
        'pattern': r'^\$(\d+(\.\d+)?)/(1000)$',

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 1,
        'qtyUnit': '1000',
        **qty_fields
    },
    {  # 9.9¢/kg + 9.9% + 1.9¢/article
        'pattern': r'^(\d+(\.\d+)?)¢/(kg)\s*\+\s*(\d+(\.\d+)?)%\s*\+\s*(\d+(\.\d+)?)¢/(article)$',
        'byAmount': True,
        'amountRateMatchIndex': 4,
        'amountRateDivide': 100,

        'byQty': True,
        'qtyRateMatchIndex': 1,
        'qtyRateDivide': 100,
        'qtyUnitMatchIndex': 3,
        **weight_fields,

        'byQty2': True,
        'qtyRate2MatchIndex': 6,
        'qtyRate2Divide': 100,
        'qtyUnit2MatchIndex': 8,
        'qtyLabel2': '商品数量',
        'qtyDesc2': 'Quantity'

    },
    {  # other
        'pattern': r'(.+)',
        'isComplex': True,
        'tip': '该商品的税率为特殊规则或不明确，暂不支持税金计算。商品税率：{}'
    }
]
