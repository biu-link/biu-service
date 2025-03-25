# -*- coding: utf-8 -*-

ams_status = {
    "01": {
        "code": "01",
        "level": "info",
        "short_desc": "Port of discharge changed",
        "detail_cn": "当铁路承运人在提单的consist记录中更改卸货港时，会生成此通知。这通常是因为运输计划的变更或实际操作的需要。"
    },
    "02": {
        "code": "02",
        "level": "info",
        "short_desc": "Entry Advisory",
        "detail_cn": "当铁路承运人针对某提单的入境申报被提交时，无论是通过选择性申报还是手动申报，都会生成此通知。"
    },
    "03": {
        "code": "03",
        "level": "info",
        "short_desc": "Port of Entry Change",
        "detail_cn": "当铁路承运人更改入境口岸记录时生成，入境口岸与原始提单上的记录不同。"
    },
    "04": {
        "code": "04",
        "level": "info",
        "short_desc": "Add Second Notify Party",
        "detail_cn": "当铁路承运人在提单的consist记录中添加新的第二通知方SCAC代码时，会生成此通知。这通常发生在列车编组记录的修正期间。"
    },
    "11": {
        "code": "11",
        "level": "info",
        "short_desc": "Arrival of in-bond complete movement",
        "detail_cn": "当货物作为完整运输到达目的地时（无纸化或传统in-bond货物），由ACE M1参与者或CBP生成此通知。"
    },
    "12": {
        "code": "12",
        "level": "info",
        "short_desc": "Arrival of inbond  bill of lading",
        "detail_cn": "当货物通过提单到达目的地时（无纸化或传统in-bond货物），由ACE M1参与者或美国海关和边境保护局（CBP）生成此通知。"
    },
    "13": {
        "code": "13",
        "level": "info",
        "short_desc": "Arrival of inbond  container",
        "detail_cn": "当货物通过集装箱/封条到达目的地时（无纸化或传统in-bond货物），由ACE M1参与者或美国海关和边境保护局（CBP）生成此通知。"
    },
    "14": {
        "code": "14",
        "level": "info",
        "short_desc": "Delete entered quantity (transaction delete)",
        "detail_cn": "当CBP通过交易删除功能（transaction delete function）执行操作时，会生成此通知。此操作会从提单的已申报数量（ENT）中减去相应的数量。"
    },
    "15": {
        "code": "15",
        "level": "info",
        "short_desc": "Delete released quantity (transaction delete)",
        "detail_cn": "当CBP通过交易删除功能（transaction delete function）执行操作时，会生成此通知。此操作会从提单的已放行数量（REL）中减去相应的数量。"
    },
    "16": {
        "code": "16",
        "level": "info",
        "short_desc": "Delete entered/ released quantity (transaction delete)",
        "detail_cn": "当CBP通过交易删除功能（transaction delete function）执行操作时，会生成此通知。此操作会从提单的已申报数量（ENT）和已放行数量（REL）中减去相应的数量。"
    },
    "17": {
        "code": "17",
        "level": "info",
        "short_desc": "Overdue vessel arrival",
        "detail_cn": "当CBP或AMS参与者在预计到达日期（EDA）后两周内未收到船舶（运输工具）的到达信息时，会生成此通知。此通知的生成不会影响已申报数量（ENT）和已放行数量（REL）"
    },
    "18": {
        "code": "18",
        "level": "info",
        "short_desc": "Master inbond advisory",
        "detail_cn": "当在目的地港口针对正在途中的in-bond提单提交了入境申报时，会生成此通知。此通知表明该提单的货物正在途中，但尚未到达目的地港口。"
    },
    "19": {
        "code": "19",
        "level": "pass",
        "short_desc": "Actual conveyance arrival",
        "detail_cn": "当运输工具在AMS中被标记为已到达时，会生成此通知。这通常是在运输工具实际到达港口或指定地点后，由AMS系统自动更新状态时触发的。"
    },
    "1A": {
        "code": "1A",
        "level": "warning",
        "short_desc": "Entered:  Intensive examination required",
        "detail_cn": "当货物被标记为需要进行强化检查时，会生成此通知。此通知表明货物已被备案，正在等待CBP的检查，但尚未放行。"
    },
    "1B": {
        "code": "1B",
        "level": "pass",
        "short_desc": "Released:  Intensive examination completed",
        "detail_cn": "当CBP完成对货物的强化检查后，会生成此通知。此通知表明货物已经通过了CBP的详细检查，并且已被放行。"
    },
    "1C": {
        "code": "1C",
        "level": "pass",
        "short_desc": "Entered and released:  General examination",
        "detail_cn": "当CBP完成对货物的一般检查后，会生成此通知。此通知表明货物已经通过了CBP的一般检查，并且已被放行。"
    },
    "1F": {
        "code": "1F",
        "level": "pass",
        "short_desc": "Customs hold removed at port of inbond destination",
        "detail_cn": "当CBP在目的地港口解除对货物的扣留（hold）时，会生成此通知。表明货物的扣留状态已被解除，货物可以被放行给进口商或收货人。"
    },
    "1G": {
        "code": "1G",
        "level": "warning",
        "short_desc": "Customs hold placed at port of inbond destination",
        "detail_cn": "当CBP在目的地港口对货物实施扣留（hold）时，会生成此通知。表明货物在目的地港口被扣留，不能被放行给收货人，直到CBP解除扣留。"
    },
    "1H": {
        "code": "1H",
        "level": "warning",
        "short_desc": "Customs hold placed at port of discharge",
        "detail_cn": "当CBP在卸货港对货物实施扣留（hold）时，会生成此通知。表明货物在卸货港被扣留，不能被放行给收货人，直到CBP解除扣留。"
    },
    "1I": {
        "code": "1I",
        "level": "pass",
        "short_desc": "Customs hold removed at port of discharge",
        "detail_cn": "当CBP在卸货港解除对货物的扣留（hold）时，会生成此通知。表明货物在卸货港的扣留状态已被解除，货物可以被放行给进口商或收货人。"
    },
    "1J": {
        "code": "1J",
        "level": "pass",
        "short_desc": "Inbond movement authorized:  Bill of lading open",
        "detail_cn": "当CBP或AMS参与者输入IT、TE和IE提单数据时，会生成此通知。表明货物可以作为in-bond运输至目的地港口，提单状态保持开放。"
    },
    "1K": {
        "code": "1K",
        "level": "info",
        "short_desc": "Bill of lading late in 5 days",
        "detail_cn": "当由ACE M1参与者创建的IT、TE和IE的in-bond提单在运输期限到期前5天尚未到达目的地时，会生成此通知。"
    },
    "1L": {
        "code": "1L",
        "level": "info",
        "short_desc": "Bill of lading late",
        "detail_cn": "当由ACE M1参与者创建的IT、TE和IE的in-bond提单在运输期限到期时尚未到达目的地时，会生成此通知。"
    },
    "1M": {
        "code": "1M",
        "level": "info",
        "short_desc": "Bill of lading message transmission",
        "detail_cn": "当CBP或AMS参与者对提单进行操作时，会生成此通知。此通知是一个自由格式的消息，用于传达有关提单的特定信息。"
    },
    "1N": {
        "code": "1N",
        "level": "info",
        "short_desc": "Overage",
        "detail_cn": "当CBP或AMS参与者通过选择性处理或手动输入生成通知时，如果ENT或RE超过修正数量（AMEND），会生成此通知。此通知也可以是由于CBP对货物的实际数量进行验证时，实际数量大于提单上显示的数量而生成的。"
    },
    "1O": {
        "code": "1O",
        "level": "warning",
        "short_desc": "Shortage",
        "detail_cn": "当CBP进行货物的实际数量验证时，如果发现实际数量少于提单上显示的数量，会生成此通知。表明修正数量受到影响，需要承运人响应（A01）。"
    },
    "1P": {
        "code": "1P",
        "level": "warning",
        "short_desc": "Within case shortage, goods specifically manifested",
        "detail_cn": "当CBP进行货物的实际数量验证时，如果发现实际数量少于提单上显示的数量，会生成此通知。此通知表明修正数量受到影响，需要承运人响应（A01）。"
    },
    "1Q": {
        "code": "1Q",
        "level": "info",
        "short_desc": "Lay order extended",
        "detail_cn": "当CBP或AMS参与者输入G01消息代码2时，生成此通知。表明提单的延期请求已被处理，但每个提单只允许延期一次，且延期天数因港口而异。ENT数量和REL数量不受影响。"
    },
    "1R": {
        "code": "1R",
        "level": "info",
        "short_desc": "Pending eligible General Order",
        "detail_cn": "当CBP或AMS参与者在提单的lay order（存放期）到期前2天生成此通知时，表明提单上的ENT数量和REL数量少于修正数量（AMEND）。"
    },
    "1S": {
        "code": "1S",
        "level": "info",
        "short_desc": "Ordered to General Order",
        "detail_cn": "当CBP或AMS参与者在提单的lay order（存放期）到期时，发现提单上的ENT数量和REL数量与修正数量（AMEND）存在差异，并且这些差异在lay order到期时仍未解决，会生成此通知。"
    },
    "1T": {
        "code": "1T",
        "level": "info",
        "short_desc": "Seized",
        "detail_cn": "当CBP手动输入信息时，如果提单上的ENT数量或部分数量因违规被扣押，会生成此通知。表明扣押的数量金额已写入ENT和REL字段中。"
    },
    "1U": {
        "code": "1U",
        "level": "info",
        "short_desc": "Sent to General Order",
        "detail_cn": "当CBP或AMS参与者手动输入G01或G03记录时，如果提单上的ENT数量或部分数量被转移到General Order（GO）设施，会生成此通知。表明转移到GO的数量已写入ENT和REL字段中。"
    },
    "1V": {
        "code": "1V",
        "level": "info",
        "short_desc": "Lay order extension rejected",
        "detail_cn": "当CBP或AMS参与者输入G01消息代码2时，会生成此通知。表明提单持有人请求延期，但这是第二次或后续请求，或者港口没有延期。"
    },
    "1W": {
        "code": "1W",
        "level": "pass",
        "short_desc": "Within port transfer authorized:  Bill of lading remains open",
        "detail_cn": "当AMS参与者请求PTT（Permit to Transfer）、T01，或CBP手动发布PTT时，会生成此通知。表明ENT数量和REL数量不受影响，一般订单（General Order, GO）程序被绕过。"
    },
    "1X": {
        "code": "1X",
        "level": "warning",
        "short_desc": "Transfer for Exam",
        "detail_cn": "当CBP通过在线输入指定将货物转移到CES进行执法/合规检查时，会生成此通知。此类检查可能独立于货物选择性（Cargo Selectivity）或其他执法系统生成，且CES检查可能与申报者提供的入境信息无关。"
    },
    "1Y": {
        "code": "1Y",
        "level": "pass",
        "short_desc": "MVOC - NVOC BL Match",
        "detail_cn": "当CBP或AMS参与者输入相关数据时，如果NVO在B04记录中传输的SCAC和提单号与MVOC的记录相匹配，会生成此通知。表明提单匹配成功，NVO可以继续进行后续操作。"
    },
    "20": {
        "code": "20",
        "level": "info",
        "short_desc": "Delete Arrival of Inbond at Intermediate Port Complete Movement",
        "detail_cn": "当货物到达北部边境中间港口后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明所有与in-bond编号相关的提单中的所有到达记录都被删除，但已ENT数量和REL数量不受影响。"
    },
    "21": {
        "code": "21",
        "level": "info",
        "short_desc": "Delete Arrival of Inbond at Intermediate Port Bill of Lading",
        "detail_cn": "当货物到达北部边境中间港口后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明该行动不影响与in-bond编号相关的其他提单，ENT数量和REL数量不受影响。"
    },
    "22": {
        "code": "22",
        "level": "info",
        "short_desc": "Delete Arrival of Inbond at Intermediate Port Container",
        "detail_cn": "当货物通过集装箱-封条到达北部边境中间港口后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明从每个与集装箱相关的提单中删除了到达记录，但ENT数量和REL数量不受影响。"
    },
    "23": {
        "code": "23",
        "level": "info",
        "short_desc": "Delete Arrival of Inbond at Intermediate Port Complete Movement",
        "detail_cn": "当货物从北部边境中间港口出发后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明从所有与in-bond编号相关的提单中删除了所有出发记录，但ENT数量和REL数量不受影响。"
    },
    "24": {
        "code": "24",
        "level": "info",
        "short_desc": "Delete Departure of Inbond at Intermediate Port Bill of Lading",
        "detail_cn": "当货物通过提单从北部边境中间港口出发后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明该行动不影响与in-bond编号相关的其他提单，ENT数量和REL数量不受影响。"
    },
    "25": {
        "code": "25",
        "level": "info",
        "short_desc": "Delete Departure of Inbond at Intermediate Port Container",
        "detail_cn": "当货物通过集装箱-封条从北部边境港口出发后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明从每个与集装箱相关的提单中删除了出发记录，但ENT数量和REL数量不受影响。"
    },
    "26": {
        "code": "26",
        "level": "info",
        "short_desc": "Delete Transfer of Liability for Inbond",
        "detail_cn": "当货物的监管责任从一个担保承运人转移到另一个担保承运人后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明从所有与in-bond编号相关的提单中删除了转移的监管责任，但ENT数量和REL数量不受影响。"
    },
    "27": {
        "code": "27",
        "level": "info",
        "short_desc": "Delete Transfer of Liability for Bill of Lading",
        "detail_cn": "当货物通过提单从一个担保承运人转移到另一个担保承运人后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明该行动不影响与in-bond编号相关的其他提单，ENT数量和REL数量不受影响。"
    },
    "28": {
        "code": "28",
        "level": "info",
        "short_desc": "Delete Transfer of Liability for Container",
        "detail_cn": "当货物通过集装箱-封条从一个担保承运人转移到另一个担保承运人后采取行动时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明从所有与集装箱-封条相关的提单中删除了转移的监管责任，但ENT数量和REL数量不受影响。"
    },
    "2F": {
        "code": "2F",
        "level": "pass",
        "short_desc": "USDA miscellaneous hold removed at port of inbond destination",
        "detail_cn": "当货物到达保税目的地港口后（CBP或AMS参与者在无纸化或传统in-bond货物），手动发布USDA杂项扣留解除通知时，会生成此通知。表明提单状态从“HELD”恢复到之前的状，ENT数量和REL数量不受影响。"
    },
    "2G": {
        "code": "2G",
        "level": "warning",
        "short_desc": "USDA miscellaneous hold placed at port of inbond destination",
        "detail_cn": "当货物到达保税目的地港口后（CBP或AMS参与者在无纸化或传统in-bond货物），手动发布USDA杂项扣留通知时，会生成此通知。表明提单状态变为“HELD”，货物不能放行给收货人，直到CBP解除扣留。"
    },
    "2H": {
        "code": "2H",
        "level": "warning",
        "short_desc": "USDA miscellaneous hold placed at port of discharge",
        "detail_cn": "当货物到达卸货港后（CBP或AMS参与者在无纸化或传统in-bond货物），手动发布USDA杂项扣留通知时，会生成此通知。表明提单状态变为“HELD”，货物不能放行给收货人，直到CBP解除扣留。"
    },
    "2I": {
        "code": "2I",
        "level": "pass",
        "short_desc": "USDA miscellaneous hold removed at port of discharge",
        "detail_cn": "当CBP或AMS参与者在卸货港手动发布USDA杂项扣留解除通知时，会生成此通知。表明提单状态从“HELD”恢复到之前的状，ENT数量和REL数量不受影响。"
    },
    "2O": {
        "code": "2O",
        "level": "warning",
        "short_desc": "ISF Hold for no ISF on file",
        "detail_cn": "当CBP或AMS参与者在无纸化或传统in-bond货物到达卸货港后，发现提单没有有效的ISF记录时，会生成此通知。此通知表明提单状态变为“HELD”，货物不能放行给收货人，直到CBP解除扣留。"
    },
    "2P": {
        "code": "2P",
        "level": "warning",
        "short_desc": "ISF Hold for ISF Compiance Issue",
        "detail_cn": "当CBP或AMS参与者发现提单的ISF存在合规问题时，会生成此通知。此通知表明提单状态变为“HELD”，货物不能放行给收货人，直到CBP解除扣留。"
    },
    "2Q": {
        "code": "2Q",
        "level": "warning",
        "short_desc": "Do Not Load - No ISF",
        "detail_cn": "当CBP或AMS参与者在无纸化或传统in-bond货物到达卸货港后，发现提单没有有效的ISF记录时，会生成此通知。此通知表明提单状态变为“HELD”，货物不能放行给收货人，直到CBP解除扣留。"
    },
    "2R": {
        "code": "2R",
        "level": "warning",
        "short_desc": "Do Not Load - ISF Compliance",
        "detail_cn": "当CBP或AMS参与者发现提单的ISF存在合规问题时，会生成此通知。表明提单状态变为“HELD”，货物不能放行给收货人，直到CBP解除扣留。"
    },
    "2Z": {
        "code": "2Z",
        "level": "warning",
        "short_desc": "Master/House Container Mis-Match",
        "detail_cn": "主提单MBL与分提单HBL之间关于集装箱信息不符。"
    },
    "3F": {
        "code": "3F",
        "level": "pass",
        "short_desc": "Other Government Agency hold removed at port of inbond destination",
        "detail_cn": "当CBP或AMS参与者手动发布通知，解除在保税目的地港口生效的其他政府机构（OGA）的扣留时，会生成此通知。表明提单状态从“HELD”恢复到之前的状，ENT数量和REL数量不受影响。"
    },
    "3G": {
        "code": "3G",
        "level": "info",
        "short_desc": "Other Government Agency hold placed at port of inbond destination",
        "detail_cn": "当CBP或AMS参与者手动发布通知，解除在保税目的地港口生效的其他政府机构（OGA）的扣留时，会生成此通知。表明提单状态从“HELD”恢复到之前的状，ENT数量和REL数量不受影响。"
    },
    "3H": {
        "code": "3H",
        "level": "warning",
        "short_desc": "Other Government Agency hold placed at port of discharge",
        "detail_cn": "当CBP或AMS参与者在卸货港手动发布其他政府机构（OGA）的扣留通知时，会生成此通知。表明提单状态变为“HELD”，货物不能放行给收货人，直到CBP解除扣留。"
    },
    "3I": {
        "code": "3I",
        "level": "pass",
        "short_desc": "Other Government Agency hold removed at port of discharge",
        "detail_cn": "当CBP或AMS参与者手动发布通知，解除在卸货港生效的其他政府机构（OGA）的扣留时，会生成此通知。表明提单状态从“HELD”恢复到之前的状，ENT数量和REL数量不受影响。"
    },
    "3M": {
        "code": "3M",
        "level": "warning",
        "short_desc": "Unauthorized Attempt to use Bond",
        "detail_cn": "当CBP或AMS参与者发现未经授权的第三方尝试使用担保承运人的担保债券时，会生成此通知。表明担保债券的所有者需要采取行动，以确保只有授权的方可以使用该债券。"
    },
    "3P": {
        "code": "3P",
        "level": "warning",
        "short_desc": "Unauthorized Port of Origin for In-bond",
        "detail_cn": "当CBP或AMS参与者发现某方未经授权使用担保债券用于特定的保税起运港时，会生成此通知。表明担保债券的所有者需要采取行动，以确保只有授权的方可以使用该债券。"
    },
    "3Q": {
        "code": "3Q",
        "level": "warning",
        "short_desc": "Unauthorized Port of Destination for In-bond",
        "detail_cn": "当CBP或AMS参与者发现某方未经授权使用担保债券用于特定的保税目的地港口时，会生成此通知。表明担保债券的所有者需要采取行动，以确保只有授权的方可以使用该债券。"
    },
    "3R": {
        "code": "3R",
        "level": "warning",
        "short_desc": "Attempt to Use Bond Outside Specified Date Range",
        "detail_cn": "当CBP或AMS参与者发现某方未经授权使用担保债券用于特定的保税起运港或目的地港口时，会生成此通知。表明担保债券的所有者需要采取行动，以确保只有授权的方可以在指定的时间范围内使用该债券。"
    },
    "3U": {
        "code": "3U",
        "level": "pass",
        "short_desc": "Security Filing Removed",
        "detail_cn": "当CBP或AMS参与者删除了某个进口安全申报（ISF）时，会生成此通知。表明ISF已被删除，可能会影响货物的清关流程。"
    },
    "3W": {
        "code": "3W",
        "level": "info",
        "short_desc": "Request for In-bond Diversion Granted",
        "detail_cn": "当CBP或AMS参与者接受将in-bond货物改道至新目的地的请求时，会生成此通知。表明改道请求已被接受，货物将被运输至新的目的地。"
    },
    "3Z": {
        "code": "3Z",
        "level": "pass",
        "short_desc": "Security Filing on File",
        "detail_cn": "当CBP或AMS参与者接受了一个进口安全申报（ISF）时，会生成此通知。表明ISF已被接受，货物可以继续进行清关流程。"
    },
    "4A": {
        "code": "4A",
        "level": "info",
        "short_desc": "Override",
        "detail_cn": "当CBP或AMS参与者通过选择性处理生成此通知时，表明之前的1C或1B通知被覆盖，已放行数量（REL）从提单中减去。"
    },
    "4C": {
        "code": "4C",
        "level": "info",
        "short_desc": "Override",
        "detail_cn": "当CBP或AMS参与者通过选择性处理生成此通知时，表明之前的1A通知被覆盖，改为1C通知，REL数量被写入提单，而ENT数量不受影响。"
    },
    "4E": {
        "code": "4E",
        "level": "info",
        "short_desc": "Entry cancelled",
        "detail_cn": "当CBP或AMS参与者通过选择性处理生成此通知时，表明之前的报关单（Entry）被报关行撤回。此通知会从提单中减去ENT数量和REL数量，如果之前的报关单结果为1C或1A，随后又变成了1B；或者仅减去已申报数量（ENT），如果报关单结果为1A。"
    },
    "4O": {
        "code": "4O",
        "level": "pass",
        "short_desc": "ISF Hold Removed - 2O",
        "detail_cn": "当CBP或AMS参与者生成此通知时，表明之前因缺少ISF而被扣留的提单现在已解除扣留。此通知通常用于取消之前的2O通知。"
    },
    "4P": {
        "code": "4P",
        "level": "pass",
        "short_desc": "ISF Hold Removed - 2P",
        "detail_cn": "表示之前因申报问题而被暂停的货物，现在相关问题已经得到解决，CBP解除了对该货物的暂停放行措施。这通常表明申报信息已经更正或补充完整，货物可以继续进行正常的通关流程"
    },
    "4Q": {
        "code": "4Q",
        "level": "pass",
        "short_desc": "Do Not Load Removed - 2Q",
        "detail_cn": "表示之前因缺少进口安全申报（ISF）而被美国海关与边境保护局（CBP）禁止装运的货物，现在已经解决了缺少申报的问题，CBP解除了对该货物的禁止装运措施。这通常表明之前没有提交ISF申报，现在申报已经完成并且被接受，货物可以继续进行正常的装运流程"
    },
    "4R": {
        "code": "4R",
        "level": "pass",
        "short_desc": "Do Not Load Removed - 2R",
        "detail_cn": "表示之前因进口安全申报（ISF）合规问题而被美国海关与边境保护局（CBP）禁止装运的货物，现在已经解决了相关合规问题，CBP解除了对该货物的禁止装运措施。这通常表明之前提交的ISF申报信息存在不完整、不准确或其他问题，现在这些问题已经得到更正或补充完整，货物可以继续进行正常的装运流程"
    },
    "50": {
        "code": "50",
        "level": "info",
        "short_desc": "Export of inbond  complete movement",
        "detail_cn": "当货物作为完整运输从目的地港口出口时（无纸化或传统in-bond货物），会在所有与该保税编号相关的提单中写入入境（ENT）/放行（REL）数量。如果提单上存在任何禁止出口（HOLDS）措施，则不得出口。"
    },
    "51": {
        "code": "51",
        "level": "info",
        "short_desc": "Export of inbond  bill of lading",
        "detail_cn": "在所有提单中写入ENT/REL数量，但不影响与该保税编号相关的其他提单。如果提单存在任何限制（HOLDS），则不得出口"
    },
    "52": {
        "code": "52",
        "level": "info",
        "short_desc": "Export of inbond  container",
        "detail_cn": "当货物以集装箱形式从目的港出口时（无纸化或传统in-bond货物），在与该集装箱相关的每一份提单中写入该集装箱的ENT/REL数量。如果提单存在任何限制（HOLDS），则不得出口"
    },
    "53": {
        "code": "53",
        "level": "info",
        "short_desc": "Overdue export",
        "detail_cn": "当无纸化或传统TE（运输入境）或IE（运输出境）保税货物（in-bond）在到达目的港后30天内未从目的港出口，提单中的ENT/REL数量不受影响。"
    },
    "54": {
        "code": "54",
        "level": "info",
        "short_desc": "Carrier bill  delete",
        "detail_cn": "当AMS参与者通过修订（A01）传输删除提单时，会生成处置代码54，表示从舱单中删除提单。"
    },
    "55": {
        "code": "55",
        "level": "info",
        "short_desc": "Carrier bill  add",
        "detail_cn": "当AMS参与者通过修订（A01）传输向舱单中添加提单时，会生成处置代码55。需要注意的是，只有当“删除”和“添加”消息一起发送，并且该提单在AMS系统中有记录时，才会生成代码55。如果单独发送“添加”提单消息，则不会生成代码55"
    },
    "56": {
        "code": "56",
        "level": "info",
        "short_desc": "Carrier bill  change",
        "detail_cn": "当AMS参与者通过修订（A01）传输在不从舱单中删除提单的情况下，更改提单中的数量时，会生成处置代码56。这表示对提单数量进行了修改，但提单本身仍然保留在舱单中。"
    },
    "57": {
        "code": "57",
        "level": "info",
        "short_desc": "Change arrival of inbond  complete movement",
        "detail_cn": "当货物作为完整运输到达目的港（无纸化或传统in-bond货物），提单中的ENT/REL数量不受影响。"
    },
    "58": {
        "code": "58",
        "level": "info",
        "short_desc": "Change arrival of inbond  bill of lading",
        "detail_cn": "当货物以提单形式到达目的港（无纸化或传统in-bond货物），提单中的ENT/REL数量不受影响。"
    },
    "59": {
        "code": "59",
        "level": "info",
        "short_desc": "Change arrival of inbond  container",
        "detail_cn": "当货物以集装箱/封条形式到达目的港（无纸化或传统in-bond货物），提单中的ENT/REL数量不受影响。"
    },
    "5H": {
        "code": "5H",
        "level": "warning",
        "short_desc": "Entry Processing Hold",
        "detail_cn": "表示之前的入境申报已被选中进行文件差异检查。放行被拒绝，提单状态更改为“HELD”。如果之前的通知是1C或1B，则从提单中减去放行数量。"
    },
    "5I": {
        "code": "5I",
        "level": "pass",
        "short_desc": "Entry Processing Hold Removed",
        "detail_cn": "表示Entry处理HOLD已解除。作为选择性处理的结果而生成，如果CBP已经放行货物，并且没有其他生效的HOLDS，则货物可以被放行。"
    },
    "60": {
        "code": "60",
        "level": "info",
        "short_desc": "Change export of inbond  complete movement",
        "detail_cn": "当货物作为完整运输从目的港出口时（无纸化或传统in-bond货物），所有与保税编号相关的提单的新出口日期被写入，提单中的ENT/REL数量不受影响。"
    },
    "61": {
        "code": "61",
        "level": "info",
        "short_desc": "Change export of inbond  bill of lading",
        "detail_cn": "当货物以提单形式从目的港出口时（无纸化或传统in-bond货物），所有与保税编号相关的提单的新出口日期被写入，提单中的ENT/REL数量不受影响，且不影响与该保税编号相关的其他提单。"
    },
    "62": {
        "code": "62",
        "level": "info",
        "short_desc": "Change export of inbond  container",
        "detail_cn": "当货物以集装箱/封条形式从目的港出口时（无纸化或传统in-bond货物），所有与该集装箱相关的提单的新出口日期被写入。"
    },
    "63": {
        "code": "63",
        "level": "info",
        "short_desc": "Delete arrival of inbond  complete movement",
        "detail_cn": "当货物以集装箱/封条形式从目的港出口时（无纸化或传统in-bond货物），所有与该集装箱相关的提单的新出口日期被写入，提单中的ENT/REL数量不受影响。"
    },
    "64": {
        "code": "64",
        "level": "info",
        "short_desc": "Deleted arrival of inbond  bill of lading",
        "detail_cn": "当货物以集装箱/封条形式从目的港出口时（无纸化或传统in-bond货物），所有与该集装箱相关的提单的新出口日期被写入，提单中的ENT/REL数量不受影响。"
    },
    "65": {
        "code": "65",
        "level": "info",
        "short_desc": "Delete arrival of inbond  container",
        "detail_cn": "当货物以集装箱/封条形式从目的港出口时（无纸化或传统in-bond货物），所有与该集装箱相关的提单的新出口日期被写入，提单中的ENT/REL数量不受影响。"
    },
    "66": {
        "code": "66",
        "level": "info",
        "short_desc": "Delete export of inbond  complete movement",
        "detail_cn": "海关通过监管更新功能（supervisory update function）进行操作时，会从所有与保税编号（in-bond number）相关的提单中减去ENT/REL数量。"
    },
    "67": {
        "code": "67",
        "level": "info",
        "short_desc": "Delete export of inbond  bill of lading",
        "detail_cn": "当CBPAMS参与者通过交易删除功能（transaction delete function）执行操作时，会生成此通知，已申报数量（ENT）和已放行数量（REL）从提单中减去。"
    },
    "68": {
        "code": "68",
        "level": "info",
        "short_desc": "Delete export of inbond  container",
        "detail_cn": "当CBP或AMS参与者通过交易删除功能（transaction delete function）执行操作时，会生成此通知。已申报数量（ENT）和已放行数量（REL）从与集装箱相关的所有提单中减去。"
    },
    "69": {
        "code": "69",
        "level": "info",
        "short_desc": "24 hours quota  must arrive by container",
        "detail_cn": "表明提单的入境申报因24小时配额限制而受到影响。此通知通常用于提醒参与者，只有通过集装箱/封条（container/seal）方式到达的in-bond货物才符合24小时配额的要求。"
    },
    "6H": {
        "code": "6H",
        "level": "warning",
        "short_desc": "Do Not Load",
        "detail_cn": "指示货物不应被装载。此通知通常基于特定的合规问题或安全考虑而发出。"
    },
    "6I": {
        "code": "6I",
        "level": "pass",
        "short_desc": "Do Not Load Condition Released",
        "detail_cn": "表明之前因特定原因（如缺少ISF或ISF合规问题）而被禁止装载的货物现在可以重新装载。此通知通常用于取消之前的“Do Not Load”通知。"
    },
    "70": {
        "code": "70",
        "level": "info",
        "short_desc": "Penalty",
        "detail_cn": "表明已针对提单发出CF5955A罚款通知（Notice of Penalty），但此通知不涉及货物扣押，已申报数量（ENT）和已放行数量（REL）不受影响。"
    },
    "71": {
        "code": "71",
        "level": "warning",
        "short_desc": "Intensive hold for USDA placed at port of discharge",
        "detail_cn": "表明由于美国农业部（USDA）在卸货港（Port of Discharge）对货物实施了手动发布的强化扣留，导致货物的放行被拒绝。提单状态变更为“HELD”（被扣留），但入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "72": {
        "code": "72",
        "level": "warning",
        "short_desc": "Inspection/document review hold for USDA placed at port of discharge",
        "detail_cn": "表明由于美国农业部（USDA）在卸货港（Port of Discharge）对货物实施了手动发布的检查或文件审核扣留，导致货物的放行被拒绝。提单状态变更为“HELD”（被扣留），但入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "73": {
        "code": "73",
        "level": "warning",
        "short_desc": "Fumigation hold for USDA placed at port of discharge",
        "detail_cn": "表明由于美国农业部（USDA）在卸货港（Port of Discharge）对货物实施了手动发布的熏蒸扣留，导致货物的放行被拒绝。提单状态变更为“HELD”（被扣留），但入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "74": {
        "code": "74",
        "level": "pass",
        "short_desc": "Intensive hold for USDA removed at port of discharge",
        "detail_cn": "表明由于美国农业部（USDA）在卸货港（Port of Discharge）实施的强化扣留被手动解除，提单状态恢复到扣留前的状态，并且入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "75": {
        "code": "75",
        "level": "pass",
        "short_desc": "Inspection/document review hold for USDA removed at port of discharge",
        "detail_cn": "表明由于美国农业部（USDA）在卸货港（Port of Discharge）实施的检查或文件审核扣留被手动解除，提单状态恢复到扣留前的状态，并且入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "76": {
        "code": "76",
        "level": "pass",
        "short_desc": "Fumigation hold for USDA removed at port of discharge",
        "detail_cn": "表明由于美国农业部（USDA）在卸货港（Port of Discharge）实施的熏蒸扣留被手动解除，提单状态恢复到扣留前的状态，并且入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "77": {
        "code": "77",
        "level": "warning",
        "short_desc": "Intensive hold for USDA placed at port of inbond destination",
        "detail_cn": "表明由于美国农业部（USDA）在入境目的地港口（Port of In-Bond Destination）对货物实施了手动发布的强化扣留，导致货物的放行被拒绝。提单状态变更为“HELD”（被扣留），但入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "78": {
        "code": "78",
        "level": "warning",
        "short_desc": "Inspection/document review hold for USDA placed at port of in﷓bond destination",
        "detail_cn": "表明由于美国农业部（USDA）在入境目的地港口（Port of In-Bond Destination）对货物实施了手动发布的检查或文件审核扣留，导致货物的放行被拒绝。提单状态变更为“HELD”（被扣留），但入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "79": {
        "code": "79",
        "level": "warning",
        "short_desc": "Fumigation hold for USDA placed at port of inbond destination",
        "detail_cn": "表明由于美国农业部（USDA）在入境目的地港口（Port of In-Bond Destination）对货物实施了手动发布的熏蒸扣留，导致货物的放行被拒绝。提单状态变更为“HELD”（被扣留），但入境/放行（ENT/REL）的数量字段未受影响。"
    },
    "7H": {
        "code": "7H",
        "level": "warning",
        "short_desc": "NII Exam Ordered",
        "detail_cn": "表明已对货物下达了非侵入性检查（Non Intrusive Inspection, NII）的命令，通常是X射线检查，货物已被扣留。此通知通常用于告知承运人，货物需要进行进一步的检查，直到检查完成并获得CBP的放行消息，货物才能继续运输或放行。"
    },
    "7I": {
        "code": "7I",
        "level": "pass",
        "short_desc": "NII Exam Completed",
        "detail_cn": "表明非侵入性检查（NII）已完成，货物的扣留状态（7H）被取消。此通知通常用于告知承运人，货物可以继续进行清关流程。"
    },
    "80": {
        "code": "80",
        "level": "pass",
        "short_desc": "Intensive hold for USDA removed at port of inbond destination",
        "detail_cn": "解除在保税目的地港口生效的USDA强化扣留时，会生成此通知。此通知表明提单状态从“HELD”恢复到之前的状，已申报数量（ENT）和已放行数量（REL）不受影响。"
    },
    "81": {
        "code": "81",
        "level": "pass",
        "short_desc": "Inspection/document review hold for USDA removed at port of in﷓bond destination",
        "detail_cn": "解除在保税目的地港口生效的USDA检验/文件审查扣留时，会生成此通知。表明提单状态从“HELD”恢复到之前的状，已申报数量（ENT）和已放行数量（REL）不受影响。"
    },
    "82": {
        "code": "82",
        "level": "pass",
        "short_desc": "Fumigation hold for USDA removed at port of inbond destination",
        "detail_cn": "解除在保税目的地港口生效的USDA熏蒸扣留时，会生成此通知。表明提单状态从“HELD”恢复到之前的状，已申报数量（ENT）和已放行数量（REL）不受影响\n"
    },
    "83": {
        "code": "83",
        "level": "info",
        "short_desc": "PTT cancelled",
        "detail_cn": "当CBP或AMS参与者通过交易删除功能（transaction delete function）执行操作时，会生成此通知。表明ENT数量和REL数量不受影响。"
    },
    "84": {
        "code": "84",
        "level": "pass",
        "short_desc": "Transfer for exam cancelled",
        "detail_cn": "该状态表示之前请求的货物转移进行检查或检验的操作已被取消。取消的原因可能包括：\n\n- 不再需要进行检查。\n- 货物已通过其他检验流程完成放行。\n- 行政或程序上的变更。\n- 货物已被重新定向或通过其他流程处理。\n\n当此状态生效时，货物将不再被转移到指定的检查地点，清关流程可能会在没有进一步检查的情况下继续进行。"
    },
    "85": {
        "code": "85",
        "level": "info",
        "short_desc": "Arrive inbond at intermediate port",
        "detail_cn": "当货物作为完整运输到达北部边境中间港口时（通常是无纸化或传统in-bond货物），会生成此通知。表明所有与in-bond编号相关的提单已到达，但ENT数量和REL数量不受影响。"
    },
    "86": {
        "code": "86",
        "level": "info",
        "short_desc": "Arrive bill of lading at intermediate port",
        "detail_cn": "当货物通过提单到达北部边境中间港口时（无纸化或传统in-bond货物），会生成此通知。表明与in-bond编号相关的提单已到达，但不影响其他与该in-bond编号相关的提单，ENT数量和REL数量不受影响"
    },
    "87": {
        "code": "87",
        "level": "info",
        "short_desc": "Arrive container at intermediate port",
        "detail_cn": "当货物通过集装箱/封条到达北部边境中间港口时（无纸化或传统in-bond货物），会生成此通知。表明与集装箱相关的每个提单已到达，但ENT数量和REL数量不受影响。"
    },
    "88": {
        "code": "88",
        "level": "info",
        "short_desc": "Depart inbond from intermediate port",
        "detail_cn": "当货物作为完整运输从北部边境中间港口出发时（无纸化或传统in-bond货物），会生成此通知。表明所有与in-bond编号相关的提单已出发，但ENT数量和REL数量不受影响。"
    },
    "89": {
        "code": "89",
        "level": "info",
        "short_desc": "Depart bill of lading from intermediate port",
        "detail_cn": "当货物通过提单从北部边境中间港口出发时（无纸化或传统in-bond货物），会生成此通知。表明与in-bond编号相关的提单已出发，但不影响其他与该in-bond编号相关的提单，ENT数量和REL数量不受影响\n"
    },
    "90": {
        "code": "90",
        "level": "info",
        "short_desc": "Depart container from intermediate port",
        "detail_cn": "当货物通过集装箱/封条从北部边境中间港口出发时（无纸化或传统in-bond货物），会生成此通知。表明与集装箱相关的每个提单已出发，ENT数量和REL数量不受影响。"
    },
    "91": {
        "code": "91",
        "level": "info",
        "short_desc": "Transfer of liability for inbond",
        "detail_cn": "当货物的监管责任从一个担保承运人转移到另一个担保承运人时(CBP或AMS参与者在无纸化或传统in-bond货物)，会生成此通知。表明与in-bond编号相关的所有提单的监管责任已转移，ENT数量和REL数量不受影响\n"
    },
    "92": {
        "code": "92",
        "level": "info",
        "short_desc": "Transfer of liability for bill of lading",
        "detail_cn": "当货物的监管责任从一个担保承运人转移到另一个担保承运人时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明与in-bond编号相关的提单的监管责任已转移，但不影响其他与该in-bond编号相关的提单，ENT数量和REL数量不受影响"
    },
    "93": {
        "code": "93",
        "level": "info",
        "short_desc": "Transfer of liability for container",
        "detail_cn": "当货物的监管责任从一个担保承运人转移到另一个担保承运人时（CBP或AMS参与者在无纸化或传统in-bond货物），会生成此通知。表明与集装箱/封条相关的所有提单的监管责任已转移，但ENT数量和REL数量不受影响。"
    },
    "94": {
        "code": "94",
        "level": "info",
        "short_desc": "Broker download",
        "detail_cn": "当CBP或AMS参与者生成此通知时，表明与提单相关的输入信息的副本已通过电子方式提供给ABI入境申报人，如提单数据中所标识的。此通知通常用于告知相关方，电子数据已成功传输并可供处理。"
    },
    "95": {
        "code": "95",
        "level": "info",
        "short_desc": "In-bond deleted",
        "detail_cn": "当CBP或AMS参与者通过在线功能删除由CBP在线创建的in-bond时，会生成此通知。表明与该in-bond相关的所有非自动化的提单也被删除。"
    },
    "96": {
        "code": "96",
        "level": "info",
        "short_desc": "Manifest Consist",
        "detail_cn": "当CBP或AMS参与者在ABI NS Application中使用记录标识符30时，表明与提单相关的Consist数据正在传输。此通知用于告知相关方，Consist数据已成功传输到ABI NS Application集中。"
    },
    "97": {
        "code": "97",
        "level": "warning",
        "short_desc": "Conveyance Hold",
        "detail_cn": "当CBP通过在线输入生成此通知时，表明整个运输工具（包括装载和空的集装箱/设备）被海关扣留。此通知仅传输给申报人。"
    },
    "98": {
        "code": "98",
        "level": "pass",
        "short_desc": "Release Conveyance",
        "detail_cn": "当CBP通过在线输入生成此通知时，表明某个级别的扣留（level hold）已被解除。此通知仅传输给申报人（filer）。"
    },
    "99": {
        "code": "99",
        "level": "info",
        "short_desc": "Train Consist Deleted",
        "detail_cn": "当CBP或AMS参与者在ABI NS Application中使用记录标识符30时，表明与特定列车相关的提单不再关联。此通知用于告知相关方，提单已从特定列车的记录中删除。"
    },
    "A1": {
        "code": "A1",
        "level": "warning",
        "short_desc": "FDA PN ADVISORY",
        "detail_cn": "表示FDA的提前通知（Prior Notice, PN）数据已被FDA接收，并且提交的AMS提单中包含了R02或X4记录中引用的提单号。从物流和物料处理的角度来看，收到A1通知表示一个潜在的放行或移动授权障碍已被满足。然而，A1并不是放行或移动授权的保证，仍然可能分配扣留，但它确实表明FDA BTA（进口食品提前通知）货物的PN申报已经完成。"
    },
    "A2": {
        "code": "A2",
        "level": "info",
        "short_desc": "WARNING – PN DATA REQUIRED, MOVEMENT AUTHORIZED",
        "detail_cn": "表示FDA的提前通知（Prior Notice, PN）数据被要求，但当前CBP与FDA之间的接口不可用（FDA应用系统故障或离线）。此通知仅在系统覆盖模式下由CBP发送。"
    },
    "A3": {
        "code": "A3",
        "level": "info",
        "short_desc": "PN DATA MISSING, MOVEMENT DENIED",
        "detail_cn": "表示FDA（食品和药物管理局）的提前通知（Prior Notice, PN）数据未提供或存在重大缺陷，如FDA BTA PN应用所确定的。此通知在FDA BTA PN计划的实施阶段3和阶段4中发出。"
    },
    "AI": {
        "code": "AI",
        "level": "info",
        "short_desc": "Submit Amendment",
        "detail_cn": "表示用户提交了修正（Amendment）请求，特别是在FDA BTA PN（提前通知）计划中"
    },
    "AR": {
        "code": "AR",
        "level": "info",
        "short_desc": "Archived",
        "detail_cn": "当提单被归档并移至离线存储时，会生成此通知。此通知用于告知相关方，提单记录已不再在线可查，而是被归档并存储在离线系统中。"
    },
    "BC": {
        "code": "BC",
        "level": "warning",
        "short_desc": "Goods Not Authorized for Zone",
        "detail_cn": "当货物原本计划进入某个区域（如自由贸易区或保税区），但最终无法进入时，会生成此通知。此通知用于告知承运人，货物将不会进入预期的区域，需要进行额外的清关安排。"
    },
    "BD": {
        "code": "BD",
        "level": "info",
        "short_desc": "Goods Accepted/No Qty Verification",
        "detail_cn": "当货物被区运营者（Zone Operator）接受，并且将由区进行处理时，会生成此通知。此通知用于告知承运人，货物已被区运营者接受，并将按照相关程序进行处理。"
    },
    "BE": {
        "code": "BE",
        "level": "info",
        "short_desc": "Goods Arrived",
        "detail_cn": "当货物到达指定的区域（如自由贸易区或保税区）时，会生成此通知。此通知用于告知承运人，货物已成功到达指定区域，并且相关的PTT（Permit to Transfer）操作被视为完成。"
    },
    "BG": {
        "code": "BG",
        "level": "info",
        "short_desc": "Admission Advisory",
        "detail_cn": "当货物被放置在自由贸易区（FTZ）的准入名单上时，会生成此通知。此通知用于告知承运人，货物已被区运营者接受，并将由区进行处理。"
    },
    "BH": {
        "code": "BH",
        "level": "warning",
        "short_desc": "Admission is Deleted",
        "detail_cn": "表明之前的准入申报（admission filing）已被删除。此通知用于告知承运人，之前的准入申报已不再有效，需要进行相应的调整。"
    },
    "F0": {
        "code": "F0",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在起源港口的入境申请进行了拒绝，并添加了相应的扣留。此通知用于告知承运人，货物在起源港口的入境申请被拒绝，需要进行相应的调整。"
    },
    "F1": {
        "code": "F1",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在保税目的地港口的入境申请进行了拒绝，并添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的入境申请被拒绝，需要进行相应的调整。"
    },
    "F2": {
        "code": "F2",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在起源港口的入境申请拒绝的扣留已被解除。此通知用于告知承运人，货物在起源港口的入境申请拒绝的扣留已不再有效，货物可以继续运输。"
    },
    "F3": {
        "code": "F3",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在保税目的地港口的入境申请拒绝的扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的入境申请拒绝的扣留已不再有效，货物可以继续运输。"
    },
    "F4": {
        "code": "F4",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在起源港口的封条检查（Seal Check）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的封条检查扣留已生效，需要进行相应的调整。"
    },
    "F5": {
        "code": "F5",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action – Seal Check Hold at In-bond Destination",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在保税目的地港口的封条检查（Seal Check）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的封条检查扣留已生效，需要进行相应的调整。"
    },
    "F6": {
        "code": "F6",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在起源港口的封条检查（Seal Check）扣留已被解除。此通知用于告知承运人，货物在起源港口的封条检查扣留已不再有效，货物可以继续运输。"
    },
    "F7": {
        "code": "F7",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明AMS(Agricultural Marketing Service,农业市场服务局)对货物在保税目的地港口的封条检查（Seal Check）扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的封条检查扣留已不再有效，货物可以继续运输。"
    },
    "F8": {
        "code": "F8",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明APHIS(Animal Plant Health Inspection Services,动植物卫生检验局)对货物在起源港口的封条检查（Seal Check）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的封条检查扣留已生效，需要进行相应的调整。"
    },
    "F9": {
        "code": "F9",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明APHIS(Animal Plant Health Inspection Services,动植物卫生检验局)对货物在保税目的地港口的封条检查（Seal Check）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的封条检查扣留已生效，需要进行相应的调整。"
    },
    "FA": {
        "code": "FA",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明APHIS(Animal Plant Health Inspection Services,动植物卫生检验局)对货物在起源港口的封条检查（Seal Check）扣留已被解除。此通知用于告知承运人，货物在起源港口的封条检查扣留已不再有效，货物可以继续运输。"
    },
    "FB": {
        "code": "FB",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明APHIS(Animal Plant Health Inspection Services,动植物卫生检验局)对货物在保税目的地港口的封条检查（Seal Check）扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的封条检查扣留已不再有效，货物可以继续运输。"
    },
    "FC": {
        "code": "FC",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在起源港口的PGA（Partner Government Agency）文档要求添加了相应的扣留。此通知用于告知承运人，货物在起源港口的PGA文档要求扣留已生效，需要进行相应的调整。"
    },
    "FD": {
        "code": "FD",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action – PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在保税目的地港口的PGA（Partner Government Agency）文档要求添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的PGA文档要求扣留已生效，需要进行相应的调整。"
    },
    "FE": {
        "code": "FE",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在起源港口的PGA（Partner Government Agency）文档要求扣留已被解除。此通知用于告知承运人，货物在起源港口的PGA文档要求扣留已不再有效，货物可以继续运输。"
    },
    "FF": {
        "code": "FF",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在保税目的地港口的PGA（Partner Government Agency）文档要求扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的PGA文档要求扣留已不再有效，货物可以继续运输。"
    },
    "FG": {
        "code": "FG",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在起源港口的PGA（Partner Government Agency）文档要求添加了相应的扣留。此通知用于告知承运人，货物在起源港口的PGA文档要求扣留已生效，需要进行相应的调整。"
    },
    "FH": {
        "code": "FH",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在保税目的地港口的PGA（Partner Government Agency）文档要求添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的PGA文档要求扣留已生效，需要进行相应的调整。"
    },
    "FI": {
        "code": "FI",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在起源港口的PGA（Partner Government Agency）文档要求扣留已被解除。此通知用于告知承运人，货物在起源港口的PGA文档要求扣留已不再有效，货物可以继续运输。"
    },
    "FJ": {
        "code": "FJ",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在保税目的地港口的PGA（Partner Government Agency）文档要求扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的PGA文档要求扣留已不再有效，货物可以继续运输。"
    },
    "FK": {
        "code": "FK",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FL": {
        "code": "FL",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action – Inspection Hold at In-bond Destination",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FM": {
        "code": "FM",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "FN": {
        "code": "FN",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明农业市场服务局（Agricultural Marketing Service, AMS）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "FO": {
        "code": "FO",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FP": {
        "code": "FP",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FQ": {
        "code": "FQ",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "FR": {
        "code": "FR",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明动植物卫生检验局（Animal Plant Health Inspection Services, APHIS）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "FS": {
        "code": "FS",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明环境保护局（Environmental Protection Agency, EPA）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FT": {
        "code": "FT",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明环境保护局（Environmental Protection Agency, EPA）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FU": {
        "code": "FU",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明环境保护局（Environmental Protection Agency, EPA）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "FV": {
        "code": "FV",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明环境保护局（Environmental Protection Agency, EPA）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "FX": {
        "code": "FX",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明食品和药物管理局（Food and Drug Administration, FDA）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FY": {
        "code": "FY",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明食品和药物管理局（Food and Drug Administration, FDA）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整。"
    },
    "FZ": {
        "code": "FZ",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明食品和药物管理局（Food and Drug Administration, FDA）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "G0": {
        "code": "G0",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明食品和药物管理局（Food and Drug Administration, FDA）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "G1": {
        "code": "G1",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明食品检验服务局（Food Safety Inspection Service, FSIS）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整。"
    },
    "G2": {
        "code": "G2",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明食品检验服务局（Food Safety Inspection Service, FSIS）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整\n。"
    },
    "G3": {
        "code": "G3",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明食品检验服务局（Food Safety Inspection Service, FSIS）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输\n。"
    },
    "G4": {
        "code": "G4",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明食品检验服务局（Food Safety Inspection Service, FSIS）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输"
    },
    "G5": {
        "code": "G5",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明鱼类和野生动物服务局（Fish and Wildlife Service, FWS）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整"
    },
    "G6": {
        "code": "G6",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明鱼类和野生动物服务局（Fish and Wildlife Service, FWS）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整。"
    },
    "G7": {
        "code": "G7",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明鱼类和野生动物服务局（Fish and Wildlife Service, FWS）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "G8": {
        "code": "G8",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明鱼类和野生动物服务局（Fish and Wildlife Service, FWS）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "G9": {
        "code": "G9",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明国家公路交通安全管理局（National Highway Transportation Safety Administration, NHTSA）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整。"
    },
    "GA": {
        "code": "GA",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明国家公路交通安全管理局（National Highway Transportation Safety Administration, NHTSA）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整"
    },
    "GB": {
        "code": "GB",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明国家公路交通安全管理局（National Highway Transportation Safety Administration, NHTSA）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "GC": {
        "code": "GC",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明国家公路交通安全管理局（National Highway Transportation Safety Administration, NHTSA）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "GD": {
        "code": "GD",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明财政部海外资产控制办公室（Office of Foreign Assets Control, OFAC）对货物在起源港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在起源港口的检查扣留已生效，需要进行相应的调整。"
    },
    "GE": {
        "code": "GE",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明财政部海外资产控制办公室（Office of Foreign Assets Control, OFAC）对货物在保税目的地港口的检查（Inspection）添加了相应的扣留。此通知用于告知承运人，货物在保税目的地港口的检查扣留已生效，需要进行相应的调整。"
    },
    "GF": {
        "code": "GF",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明财政部海外资产控制办公室（Office of Foreign Assets Control, OFAC）对货物在起源港口的检查扣留已被解除。此通知用于告知承运人，货物在起源港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "GG": {
        "code": "GG",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明财政部海外资产控制办公室（Office of Foreign Assets Control, OFAC）对货物在保税目的地港口的检查扣留已被解除。此通知用于告知承运人，货物在保税目的地港口的检查扣留已不再有效，货物可以继续运输。"
    },
    "GH": {
        "code": "GH",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明酒精和烟草税与贸易局（Alcohol and Tobacco Tax and Trade Bureau, TTB）对货物在起源港口的检查（Inspection）添加了相应的扣留。"
    },
    "GI": {
        "code": "GI",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明美国酒精和烟草税务和贸易局（TTB）在保税目的地港口对货物进行检查而实施的扣押行动。当出现这种情况时，货物在保税目的地港口被扣留，无法释放给收货人，直到TTB完成检查并解除扣押"
    },
    "GJ": {
        "code": "GJ",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在原产地港口或出口港口的检查暂停措施"
    },
    "GK": {
        "code": "GK",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在保税目的地港口的检查暂停措施"
    },
    "GL": {
        "code": "GL",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "美国海岸警卫队（United States Coast Guard, USCG）和预先归类程序（Pre-Arrival Processing System, PGA）所采取的执法行动，具体是指在货物原发港口（Port of Origin），由于某些合规性问题或其他原因，USCG决定对特定货物实施检查扣留（Inspection Hold）"
    },
    "GM": {
        "code": "GM",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "美国海岸警卫队（United States Coast Guard, USCG）和预先归类程序（Pre-Arrival Processing System, PGA）所采取的执法行动，具体是指在货物保税目的地港口（In-Bond Destination），由于某些合规性问题或其他原因，USCG决定对特定货物实施检查扣留（Inspection Hold）"
    },
    "GN": {
        "code": "GN",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "解除美国海岸警卫队在原发港口的检查扣留，表明需要采取一系列步骤来确保货物符合USCG的要求，并获得正式的放行通知。这种情况通常发生在货物已经到达美国并在入境目的地港口等待进一步处理时。"
    },
    "GO": {
        "code": "GO",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "解除美国海岸警卫队在保税目的地港口的检查扣留，表明需要采取一系列步骤来确保货物符合USCG的要求，并获得正式的放行通知。这种情况通常发生在货物已经到达美国并在入境目的地港口等待进一步处理时。"
    },
    "GP": {
        "code": "GP",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "在原发港口添加动植物卫生检验服务的拒绝入境扣留，表明需要根据美国农业部动植物卫生检验局（Animal and Plant Health Inspection Service, APHIS）的要求，对特定货物实施检查和扣留。这种情况通常发生在APHIS认为某些货物不符合其进口标准或存在潜在风险时。"
    },
    "GQ": {
        "code": "GQ",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国农业部动植物卫生检验局（APHIS）在入境口岸的保税目的地港口对货物进行扣留，以拒绝其入境。这表明相关货物在到达保税目的地港口时，由于不符合APHIS的检疫要求或其他相关规定，被要求停止进一步的运输或处理，并可能面临退回原出口国或进行销毁等措施"
    },
    "GR": {
        "code": "GR",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国农业部动植物卫生检验局（APHIS）在原产地港口对货物的扣留，该扣留原本是为了拒绝货物入境。这通常发生在货物经过检查后，被发现符合了所有相关的动植物检疫要求，因此可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "GS": {
        "code": "GS",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国农业部动植物卫生检验局（APHIS）在保税目的地港口对货物的拒绝入境扣留。这通常发生在货物经过进一步检查或采取了必要的补救措施后，被认定符合了APHIS的入境要求，从而可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场"
    },
    "GT": {
        "code": "GT",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国环保署（EPA）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合EPA的相关环保标准或规定。例如，某些机动车、发动机或设备可能因未达到美国的排放标准而被扣留。"
    },
    "GU": {
        "code": "GU",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国环保署（EPA）在保税目的地港口对货物实施扣留，以拒绝其入境"
    },
    "GV": {
        "code": "GV",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国环保署（EPA）在原产地港口对货物的拒绝入境扣留。通常情况下，只有当货物经过重新检查或采取了必要的补救措施后，被认定符合了EPA的入境要求，才能取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "GX": {
        "code": "GX",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国环保署（EPA）在保税目的地港口对货物的拒绝入境扣留。通常情况下，只有当货物经过重新检查或采取了必要的补救措施后，被认定符合了EPA的入境要求，才能取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "GY": {
        "code": "GY",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国食品药品监督管理局（FDA）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合FDA的相关标准或规定，例如食品安全、药品质量等方面的问题。"
    },
    "GZ": {
        "code": "GZ",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国食品药品监督管理局（FDA）在保税目的地港口对货物实施扣留，以拒绝其入境。"
    },
    "H0": {
        "code": "H0",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国食品药品监督管理局（FDA）在原产地港口对货物的拒绝入境扣留"
    },
    "H1": {
        "code": "H1",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国食品药品监督管理局（FDA）在保税目的地港口对货物的拒绝入境扣留。"
    },
    "H2": {
        "code": "H2",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国农业部食品安全检验局（FSIS）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合FSIS的相关标准或规定，例如肉类、禽类或蛋制品等食品的安全和卫生标准。"
    },
    "H3": {
        "code": "H3",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国农业部食品安全检验局（FSIS）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合FSIS的相关标准或规定，例如肉类、禽类或蛋制品等食品的安全和卫生标准。"
    },
    "H4": {
        "code": "H4",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国农业部食品安全检验局（FSIS）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了FSIS的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "H5": {
        "code": "H5",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国农业部食品安全检验局（FSIS）在保税目的地港口对货物的拒绝入境扣留。通常情况下，只有当货物经过重新检查或采取了必要的补救措施后，被认定符合了FSIS的入境要求，才能取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "H6": {
        "code": "H6",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国鱼类和野生动物服务局（FWS）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合FWS的相关标准或规定，例如涉及濒危物种或野生动物保护等方面的问题。"
    },
    "H7": {
        "code": "H7",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国鱼类和野生动物服务局（FWS）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合FWS的相关标准或规定，例如涉及濒危物种或野生动物保护等方面的问题"
    },
    "H8": {
        "code": "H8",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国鱼类和野生动物服务局（FWS）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了FWS的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场"
    },
    "H9": {
        "code": "H9",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国鱼类和野生动物服务局（FWS）在保税目的地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了FWS的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HA": {
        "code": "HA",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国国家公路交通安全管理局（NHTSA）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合NHTSA的相关标准或规定，例如机动车安全标准等。"
    },
    "HB": {
        "code": "HB",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国国家公路交通安全管理局（NHTSA）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合NHTSA的相关标准或规定，例如机动车安全标准等。"
    },
    "HC": {
        "code": "HC",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国国家公路交通安全管理局（NHTSA）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了NHTSA的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HD": {
        "code": "HD",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国国家公路交通安全管理局（NHTSA）在保税目的地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了NHTSA的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HE": {
        "code": "HE",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国财政部外国资产控制办公室（OFAC）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物涉及违反美国的制裁或禁运规定等情况。"
    },
    "HF": {
        "code": "HF",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国财政部外国资产控制办公室（OFAC）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物涉及违反美国的制裁或禁运规定等情况。"
    },
    "HG": {
        "code": "HG",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国财政部外国资产控制办公室（OFAC）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了OFAC的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HH": {
        "code": "HH",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国财政部外国资产控制办公室（OFAC）在保税目的地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了OFAC的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HI": {
        "code": "HI",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国酒精和烟草税务和贸易局（TTB）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合TTB的相关标准或规定，例如涉及酒精和烟草产品的税务和贸易要求等。"
    },
    "HJ": {
        "code": "HJ",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国酒精和烟草税务和贸易局（TTB）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合TTB的相关标准或规定，例如涉及酒精和烟草产品的税务和贸易要求等。"
    },
    "HK": {
        "code": "HK",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了TTB的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HL": {
        "code": "HL",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在保税目的地港口对货物的拒绝入境扣留"
    },
    "HM": {
        "code": "HM",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国海岸警卫队（USCG）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物或船舶不符合USCG的相关标准或规定，例如船舶安全、环保标准等。"
    },
    "HN": {
        "code": "HN",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action – Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国海岸警卫队（USCG）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物或船舶不符合USCG的相关标准或规定，例如船舶安全、环保标准等。"
    },
    "HO": {
        "code": "HO",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "解除美国海岸警卫队（USCG）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了USCG的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HP": {
        "code": "HP",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国海岸警卫队（USCG）在保税目的地港口对货物的拒绝入境扣留。"
    },
    "HQ": {
        "code": "HQ",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在原产地港口对货物实施扣留，以进行检查。通常与货物的物理装载和运输方式相关。"
    },
    "HR": {
        "code": "HR",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在保税目的地港口对货物实施扣留，以进行检查。通常与货物的物理装载和运输方式相关。"
    },
    "HS": {
        "code": "HS",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在原产地港口对货物的检查扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CDC的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。通常与货物的物理装载和运输方式相关。"
    },
    "HT": {
        "code": "HT",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在保税目的地港口对货物的检查扣留。通常与货物的物理装载和运输方式相关。"
    },
    "HU": {
        "code": "HU",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在原产地港口对货物实施扣留，以进行检查。"
    },
    "HV": {
        "code": "HV",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在保税目的地港口对货物实施扣留，以进行检查。"
    },
    "HX": {
        "code": "HX",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "解除美国消费品安全委员会（CPSC）在原产地港口对货物的检查扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CPSC的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "HY": {
        "code": "HY",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "解除美国消费品安全委员会（CPSC）在保税目的地港口对货物的检查扣留"
    },
    "HZ": {
        "code": "HZ",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明美国药品执法局（DEA）在原产地港口对货物实施扣留，以进行检查。"
    },
    "I0": {
        "code": "I0",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "表明美国药品执法局（DEA）在保税目的地港口对货物实施扣留，以进行检查。"
    },
    "I1": {
        "code": "I1",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "解除美国药品执法局（DEA）在原产地港口对货物的检查扣留。"
    },
    "I2": {
        "code": "I2",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "解除美国药品执法局（DEA）在保税目的地港口对货物的检查扣留。"
    },
    "I3": {
        "code": "I3",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "表明美国海关和边境保护局（CBP）在原产地港口对货物实施扣留，以进行检查。"
    },
    "I4": {
        "code": "I4",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "美国海关和边境保护局（CBP）在保税目的地港口对货物实施扣留，以进行检查。"
    },
    "I5": {
        "code": "I5",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Inspection Hold",
        "detail_cn": "解除美国海关和边境保护局（CBP）在原产地港口对货物的检查扣留。"
    },
    "I6": {
        "code": "I6",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Inspection Hold at In-bond Destination",
        "detail_cn": "解除美国海关和边境保护局（CBP）在保税目的地港口对货物的检查扣留。"
    },
    "I7": {
        "code": "I7",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国农业市场服务局（AMS）在原产地港口对货物实施扣留，要求进行纠正措施。"
    },
    "I8": {
        "code": "I8",
        "level": "warning",
        "short_desc": "AMS PGA Enforcement Action – Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国农业市场服务局（AMS）在保税目的地港口对货物实施扣留，要求进行纠正措施。"
    },
    "I9": {
        "code": "I9",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国农业市场服务局（AMS）在原产地港口对货物的纠正措施扣留。"
    },
    "IA": {
        "code": "IA",
        "level": "pass",
        "short_desc": "Remove AMS PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国农业市场服务局（AMS）在保税目的地港口对货物的纠正措施扣留"
    },
    "IB": {
        "code": "IB",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国动植物卫生检验局（APHIS）在原产地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IC": {
        "code": "IC",
        "level": "warning",
        "short_desc": "APHIS PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国动植物卫生检验局（APHIS）在保税目的地港口对货物实施扣留，要求进行纠正措施。"
    },
    "ID": {
        "code": "ID",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国动植物卫生检验局（APHIS）在原产地港口对货物的纠正措施扣留。"
    },
    "IE": {
        "code": "IE",
        "level": "pass",
        "short_desc": "Remove APHIS PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国动植物卫生检验局（APHIS）在保税目的地港口对货物的纠正措施扣留。"
    },
    "IF": {
        "code": "IF",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国环保署（EPA）在原产地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IG": {
        "code": "IG",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国环保署（EPA）在保税目的地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IH": {
        "code": "IH",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国环保署（EPA）在原产地港口对货物的纠正措施扣留。"
    },
    "II": {
        "code": "II",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国环保署（EPA）在保税目的地港口对货物的纠正措施扣留。"
    },
    "IJ": {
        "code": "IJ",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国食品药品监督管理局（FDA）在原产地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IK": {
        "code": "IK",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国食品药品监督管理局（FDA）在保税目的地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IL": {
        "code": "IL",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国食品药品监督管理局（FDA）在原产地港口对货物的纠正措施扣留。"
    },
    "IM": {
        "code": "IM",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国食品药品监督管理局（FDA）在保税目的地港口对货物的纠正措施扣留。"
    },
    "IN": {
        "code": "IN",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国食品安全检验局（FSIS）在原产地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IO": {
        "code": "IO",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国食品安全检验局（FSIS）在保税目的地港口对货物实施扣留，要求进行纠正措施。表明美国食品安全检验局（FSIS）在保税目的地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IP": {
        "code": "IP",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国食品安全检验局（FSIS）在原产地港口对货物的纠正措施扣留。"
    },
    "IQ": {
        "code": "IQ",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国食品安全检验局（FSIS）在保税目的地港口对货物的纠正措施扣留。"
    },
    "IR": {
        "code": "IR",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国鱼类和野生动物服务局（FWS）在原产地港口对货物实施扣留，要求进行纠正措施。"
    },
    "IS": {
        "code": "IS",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国鱼类和野生动物服务局（FWS）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物不符合FWS的相关标准或规定，例如涉及濒危物种或野生动物保护等方面的问题"
    },
    "IT": {
        "code": "IT",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国鱼类和野生动物服务局（FWS）在原产地港口对货物的检查扣留。"
    },
    "IU": {
        "code": "IU",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国鱼类和野生动物服务局（FWS）在保税目的地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了FWS的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "IV": {
        "code": "IV",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国国家公路交通安全管理局（NHTSA）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物不符合NHTSA的相关标准或规定，例如机动车安全标准等。"
    },
    "IX": {
        "code": "IX",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国国家公路交通安全管理局（NHTSA）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物不符合NHTSA的相关标准或规定，例如机动车安全标准等。"
    },
    "IY": {
        "code": "IY",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国国家公路交通安全管理局（NHTSA）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了NHTSA的入境要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "IZ": {
        "code": "IZ",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国国家公路交通安全管理局（NHTSA）在保税目的地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了NHTSA的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "J0": {
        "code": "J0",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国财政部外国资产控制办公室（OFAC）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关交易涉及违反美国的制裁或禁运规定等情况。"
    },
    "J1": {
        "code": "J1",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国财政部外国资产控制办公室（OFAC）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关交易涉及违反美国的制裁或禁运规定等情况。"
    },
    "J2": {
        "code": "J2",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国财政部外国资产控制办公室（OFAC）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了OFAC的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "J3": {
        "code": "J3",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国财政部外国资产控制办公室（OFAC）在保税目的地港口对货物的纠正措施扣留。这通常是因为货物经过重新检查或采取了必要的补救措施后，被认定符合了OFAC的要求。"
    },
    "J4": {
        "code": "J4",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国酒精和烟草税务和贸易局（TTB）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物不符合TTB的相关标准或规定，例如涉及酒精和烟草产品的税务和贸易要求等"
    },
    "J5": {
        "code": "J5",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国酒精和烟草税务和贸易局（TTB）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物不符合TTB的相关标准或规定，例如涉及酒精和烟草产品的税务和贸易要求等。"
    },
    "J6": {
        "code": "J6",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了TTB的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "J7": {
        "code": "J7",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在保税目的地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了TTB的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "J8": {
        "code": "J8",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国海岸警卫队（USCG）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关船舶不符合USCG的相关标准或规定，例如船舶安全、环保标准等。"
    },
    "J9": {
        "code": "J9",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国海岸警卫队（USCG）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关船舶不符合USCG的相关标准或规定，例如船舶安全、环保标准等。"
    },
    "JA": {
        "code": "JA",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "解除美国海岸警卫队（USCG）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了USCG的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "JB": {
        "code": "JB",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国海岸警卫队（USCG）在保税目的地港口对货物的纠正措施扣留。这通常是因为货物经过重新检查或采取了必要的补救措施后，被认定符合了USCG的要求。"
    },
    "JC": {
        "code": "JC",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关运输工具不符合CDC的相关标准或规定，例如涉及传染病的传播风险等。JC主要用于标记涉及多个承运人或运输方式的货物运输，"
    },
    "JD": {
        "code": "JD",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关运输工具不符合CDC的相关标准或规定，例如涉及传染病的传播风险等。主要用于标记涉及多个承运人或运输方式的货物运输，"
    },
    "JE": {
        "code": "JE",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Corrective Action Hold ",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CDC的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "JF": {
        "code": "JF",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在保税目的地港口对货物的纠正措施扣留。这通常是因为货物经过重新检查或采取了必要的补救措施后，被认定符合了CDC的要求。"
    },
    "JG": {
        "code": "JG",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物不符合CPSC的相关标准或规定，例如涉及产品安全、标签要求等方面的问题。"
    },
    "JH": {
        "code": "JH",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物不符合CPSC的相关标准或规定，例如产品安全、标签要求等方面的问题。"
    },
    "JI": {
        "code": "JI",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Corrective Action Hold ",
        "detail_cn": "解除美国消费品安全委员会（CPSC）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CPSC的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "JJ": {
        "code": "JJ",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国消费品安全委员会（CPSC）在保税目的地港口对货物的纠正措施扣留。这通常是因为货物经过重新检查或采取了必要的补救措施后，被认定符合了CPSC的要求"
    },
    "JK": {
        "code": "JK",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国药品执法局（DEA）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关交易涉及违反美国的药品法规或禁运规定等情况。"
    },
    "JL": {
        "code": "JL",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国药品执法局（DEA）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关交易涉及违反美国的药品法规或禁运规定等情况。"
    },
    "JM": {
        "code": "JM",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Corrective Action Hold ",
        "detail_cn": "解除美国药品执法局（DEA）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了DEA的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "JN": {
        "code": "JN",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国药品执法局（DEA）在保税目的地港口对货物的纠正措施扣留。这通常是因为货物经过重新检查或采取了必要的补救措施后，被认定符合了DEA的要求。"
    },
    "JO": {
        "code": "JO",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Corrective Action Hold",
        "detail_cn": "表明美国海关和边境保护局（CBP）在原产地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关交易涉及违反美国的海关法规或其他参与政府机构（PGA）的规定。"
    },
    "JP": {
        "code": "JP",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "表明美国海关和边境保护局（CBP）在保税目的地港口对货物实施扣留，要求进行纠正措施。这通常是因为货物或相关交易涉及违反美国的海关法规或其他参与政府机构（PGA）的规定。"
    },
    "JQ": {
        "code": "JQ",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Corrective Action Hold ",
        "detail_cn": "解除美国海关和边境保护局（CBP）在原产地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CBP及其他参与政府机构（PGA）的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "JR": {
        "code": "JR",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Corrective Action Hold at In-bond Destination",
        "detail_cn": "解除美国海关和边境保护局（CBP）在保税目的地港口对货物的纠正措施扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CBP及其他参与政府机构（PGA）的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "JS": {
        "code": "JS",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物或相关运输工具不符合CDC的相关标准或规定，例如涉及传染病的传播风险等。\nCDC在管理可能传播严重传染病的旅客方面，使用两种联邦公共卫生工具：“禁止登机名单”（Do Not Board list）和“公共卫生观察名单”（Public Health Lookout）。这些工具旨在减少在旅行期间传播传染病的风险。"
    },
    "JT": {
        "code": "JT",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物或相关运输工具不符合CDC的相关标准或规定，例如涉及传染病的传播风险等。"
    },
    "JU": {
        "code": "JU",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Denied Entry Hold ",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CDC的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "JV": {
        "code": "JV",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Denied Entry Hold In-bond Destination",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在保税目的地港口对货物的拒绝入境扣留。这通常是因为货物经过重新检查或采取了必要的补救措施后，被认定符合了CDC的要求"
    },
    "JX": {
        "code": "JX",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合CPSC的相关标准或规定，例如涉及产品安全、标签要求等方面的问题。\n当CPSC对货物实施扣留时，会向备案进口商（Importer of Record）或指定的报关行（Assigned Customs Broker）发出抽样/扣留通知以及样品收据（Form 163，Form 352），直至CPSC测试/评估完成，被扣留的产品仍由美国海关与边境保护局监管。CPSC有权决定受管制消费品和某些进口危险物质的可接受性，自CPSC发出抽样和扣留通知之日起，产品最多可被扣留60天，另外，CPSC可自行决定延长扣留期限。"
    },
    "JY": {
        "code": "JY",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物不符合CPSC的相关标准或规定，例如涉及产品安全、标签要求等方面的问题。\n当CPSC对货物实施扣留时，会向备案进口商（Importer of Record）或指定的报关行（Assigned Customs Broker）发出抽样/扣留通知以及样品收据（Form 163，Form 352），直至CPSC测试/评估完成，被扣留的产品仍由美国海关与边境保护局监管。CPSC有权决定受管制消费品和某些进口危险物质的可接受性，自CPSC发出抽样和扣留通知之日起，产品最多可被扣留60天，另外，CPSC可自行决定延长扣留期限。"
    },
    "JZ": {
        "code": "JZ",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Denied Entry Hold ",
        "detail_cn": "解除美国消费品安全委员会（CPSC）在原产地港口对货物的拒绝入境扣留。当货物经过重新检查或采取了必要的补救措施后，被认定符合了CPSC的要求，就可以取消之前的扣留决定，允许货物继续进行运输或进入美国市场。"
    },
    "K0": {
        "code": "K0",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Corrective Action Hold  Denied Entry Hold",
        "detail_cn": "解除美国消费品安全委员会（CPSC）在保税目的地港口对货物的拒绝入境扣留。这通常是因为货物经过重新检查或采取了必要的补救措施后，被认定符合了CPSC的要求。"
    },
    "K1": {
        "code": "K1",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国药品执法局（DEA）在原产地港口对货物实施扣留，以拒绝其入境。这通常是因为货物或相关交易涉及违反美国的药品法规或禁运规定等情况。"
    },
    "K2": {
        "code": "K2",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国药品执法局（DEA）在保税目的地港口对货物实施扣留，以拒绝其入境。这通常是因为货物或相关交易涉及违反美国的药品法规或禁运规定。"
    },
    "K3": {
        "code": "K3",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Denied Entry Hold ",
        "detail_cn": "解除美国药品执法局（DEA）在原产地港口对货物实施的拒绝入境扣留。"
    },
    "K4": {
        "code": "K4",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Denied Entry Hold In-bond Destination",
        "detail_cn": "解除美国药品执法局（DEA）在保税目的地港口对货物实施的拒绝入境扣留。"
    },
    "K5": {
        "code": "K5",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Denied Entry Hold",
        "detail_cn": "表明美国海关和边境保护局（CBP）在原产地港口对货物实施扣留，以拒绝其入境。这种扣留通常是因为货物不符合参与政府机构（PGA）的要求，例如产品安全、标签合规性或其他法规问题。"
    },
    "K6": {
        "code": "K6",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "表明美国海关和边境保护局（CBP）在保税目的地港口对货物实施扣留，以拒绝其入境。这种扣留通常是因为货物不符合参与政府机构（PGA）的要求，例如产品安全、标签合规性或其他法规问题。"
    },
    "K7": {
        "code": "K7",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Denied Entry Hold ",
        "detail_cn": "解除美国海关和边境保护局（CBP）在原产地港口对货物实施的拒绝入境扣留。"
    },
    "K8": {
        "code": "K8",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Denied Entry Hold at In-bond Destination",
        "detail_cn": "解除美国海关和边境保护局（CBP）在保税目的地港口对货物实施的拒绝入境扣留。"
    },
    "K9": {
        "code": "K9",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国环保署（EPA）在原产地港口对货物实施扣留，要求进行封条检查。"
    },
    "KA": {
        "code": "KA",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国环保署（EPA）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "KB": {
        "code": "KB",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国环保署（EPA）在原产地港口对货物实施的封条检查扣留。"
    },
    "KC": {
        "code": "KC",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国环保署（EPA）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "KD": {
        "code": "KD",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国食品药品监督管理局（FDA）在原产地港口对货物实施封条检查的扣留。"
    },
    "KE": {
        "code": "KE",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国食品药品监督管理局（FDA）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "KF": {
        "code": "KF",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国食品药品监督管理局（FDA）在原产地港口对货物实施的封条检查扣留。"
    },
    "KG": {
        "code": "KG",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国食品药品监督管理局（FDA）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "KH": {
        "code": "KH",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国食品安全检验局（FSIS）在原产地港口对货物实施封条检查的扣留。"
    },
    "KI": {
        "code": "KI",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国食品安全检验局（FSIS）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "KJ": {
        "code": "KJ",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国食品安全检验局（FSIS）在原产地港口对货物实施的封条检查扣留。"
    },
    "KK": {
        "code": "KK",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国食品安全检验局（FSIS）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "KL": {
        "code": "KL",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国鱼类和野生动物服务局（FWS）在原产地港口对货物实施封条检查的扣留。"
    },
    "KM": {
        "code": "KM",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国鱼类和野生动物服务局（FWS）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "KN": {
        "code": "KN",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国鱼类和野生动物服务局（FWS）在原产地港口对货物实施的检查扣留。"
    },
    "KO": {
        "code": "KO",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国鱼类和野生动物服务局（FWS）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "KP": {
        "code": "KP",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国国家公路交通安全管理局（NHTSA）在原产地港口对货物实施封条检查的扣留。"
    },
    "KQ": {
        "code": "KQ",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国国家公路交通安全管理局（NHTSA）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "KR": {
        "code": "KR",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国国家公路交通安全管理局（NHTSA）在原产地港口对货物实施的封条检查扣留。"
    },
    "KS": {
        "code": "KS",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国国家公路交通安全管理局（NHTSA）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "KT": {
        "code": "KT",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国财政部外国资产控制办公室（OFAC）在原产地港口对货物实施封条检查的扣留。"
    },
    "KU": {
        "code": "KU",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国财政部外国资产控制办公室（OFAC）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "KV": {
        "code": "KV",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国财政部外国资产控制办公室（OFAC）在原产地港口对货物实施的封条检查扣留。"
    },
    "KX": {
        "code": "KX",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国财政部外国资产控制办公室（OFAC）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "KY": {
        "code": "KY",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国酒精和烟草税务和贸易局（TTB）在原产地港口对货物实施封条检查的扣留。"
    },
    "KZ": {
        "code": "KZ",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国酒精和烟草税务和贸易局（TTB）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "L0": {
        "code": "L0",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在原产地港口对货物实施的封条检查扣留。"
    },
    "L1": {
        "code": "L1",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国酒精和烟草税务和贸易局（TTB）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "L2": {
        "code": "L2",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国海岸警卫队（USCG）在原产地港口对货物实施封条检查的扣留。"
    },
    "L3": {
        "code": "L3",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国海岸警卫队（USCG）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "L4": {
        "code": "L4",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国海岸警卫队（USCG）在原产地港口对货物实施的封条检查扣留。"
    },
    "L5": {
        "code": "L5",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国海岸警卫队（USCG）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "L6": {
        "code": "L6",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在原产地港口对货物实施封条检查的扣留，L6用于标识申报文件的技术处理状态，通常表示货物的申报文件已经通过了初步的技术检查，但还需要进一步的审核或补充信息"
    },
    "L7": {
        "code": "L7",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国疾病控制与预防中心（CDC）在保税目的地港口对货物实施封条检查的扣留，通常与货物的申报文件的技术处理状态相关。"
    },
    "L8": {
        "code": "L8",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在原产地港口对货物实施的封条检查扣留，通常与货物的申报文件的技术处理状态相关。"
    },
    "L9": {
        "code": "L9",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除美国疾病控制与预防中心（CDC）在保税目的地港口对货物实施的封条检查扣留。通常与货物的申报文件的技术处理状态相关。"
    },
    "LA": {
        "code": "LA",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在原产地港口对货物实施封条检查的扣留。"
    },
    "LB": {
        "code": "LB",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明美国消费品安全委员会（CPSC）在保税目的地港口对货物实施封条检查的扣留。"
    },
    "LC": {
        "code": "LC",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Seal Check Hold ",
        "detail_cn": "解除美国消费品安全委员会（CPSC）在原产地港口对货物实施的封条检查扣留。"
    },
    "LD": {
        "code": "LD",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除消费品安全委员会在入境目的地港口的封条检查扣留，需要采取一系列步骤来确保货物符合美国消费品安全委员会（CPSC）的要求，并获得正式的放行通知。这种情况通常发生在CPSC认为某些货物存在潜在的安全风险，需要进行封条检查以确认其安全性时。"
    },
    "LE": {
        "code": "LE",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明在原发港口添加药物执法局的封条检查扣留，意味着需要根据美国药物执法局（Drug Enforcement Administration, DEA）的要求，对特定货物实施封条检查和扣留。这种情况通常发生在DEA认为某些货物存在潜在的毒品或相关化学品走私风险时。"
    },
    "LF": {
        "code": "LF",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加药物执法局的封条检查扣留，意味着需要根据美国药物执法局（Drug Enforcement Administration, DEA）的要求，在货物到达入境目的地后，对特定货物实施封条检查和扣留。这种情况通常发生在DEA认为某些货物存在潜在的毒品或相关化学品走私风险时。"
    },
    "LG": {
        "code": "LG",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Seal Check Hold ",
        "detail_cn": "解除药物执法局在原发港口的封条检查扣留，意味着需要采取一系列步骤来确保货物符合美国药物执法局（DEA）的要求，并获得正式的放行通知。这种情况通常发生在DEA认为某些货物存在潜在的毒品或相关化学品走私风险，实施了封条检查并扣留后，现在决定解除这一扣留。"
    },
    "LH": {
        "code": "LH",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "解除药物执法局在入境目的地港口的封条检查扣留，意味着需要采取一系列步骤来确保货物符合美国药物执法局（DEA）的要求，并获得正式的放行通知。这种情况通常发生在DEA认为某些货物存在潜在的毒品或相关化学品走私风险，实施了封条检查并扣留后，现在决定解除这一扣留。"
    },
    "LI": {
        "code": "LI",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Seal Check Hold",
        "detail_cn": "表明在原发港口添加美国海关与边境保护局（CBP）的预先指导行动（Pre-Arrival Guidance Action, PGA）封条检查扣留，意味着需要根据CBP的要求，在货物出发前对特定货物实施封条检查和扣留。这种情况通常发生在CBP认为某些货物存在潜在的安全风险，需要进行额外检查以确保其符合所有入境要求。"
    },
    "LJ": {
        "code": "LJ",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加美国海关与边境保护局（CBP）的预先指导行动（Pre-Arrival Guidance Action, PGA）封条检查扣留，意味着需要根据CBP的要求，在货物到达入境目的地后，对特定货物实施封条检查和扣留。这种情况通常发生在CBP认为某些货物存在潜在的安全风险，需要进行额外检查以确保其符合所有入境要求。"
    },
    "LK": {
        "code": "LK",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Seal Check Hold ",
        "detail_cn": "表明移除美国海关和边境保护局（CBP）在原产地港口对货物实施的封条检查扣留。"
    },
    "LL": {
        "code": "LL",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  Seal Check Hold at In-bond Destination",
        "detail_cn": "表明移除美国海关和边境保护局（CBP）在保税目的地港口对货物实施的封条检查扣留。"
    },
    "LM": {
        "code": "LM",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明美国环保署（EPA）在原产地港口对货物实施的扣留，要求提供参与政府机构（PGA）所需的文件。"
    },
    "LN": {
        "code": "LN",
        "level": "warning",
        "short_desc": "EPA PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明美国环保署（EPA）在保税目的地港口对货物实施的扣留，要求提供参与政府机构（PGA）所需的文件。"
    },
    "LO": {
        "code": "LO",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除环境保护局在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国环境保护局（EPA）的要求，并获得正式的放行通知。这种情况通常发生在EPA认为某些货物存在潜在的环境风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "LP": {
        "code": "LP",
        "level": "pass",
        "short_desc": "Remove EPA PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除环境保护局在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国环境保护局（EPA）的要求，并获得正式的放行通知。这种情况通常发生在EPA认为某些货物存在潜在的环境风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "LQ": {
        "code": "LQ",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加食品安全检验服务（FSIS）的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国农业部食品安全检验服务局（Food Safety and Inspection Service, FSIS）的要求，在货物出发前确保所有必要的文件和信息都符合FSIS的规定。这种情况通常发生在FSIS认为某些食品或相关产品存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "LR": {
        "code": "LR",
        "level": "warning",
        "short_desc": "FSIS PGA Enforcement Action -  PGA Documentation Required Hold At In-Bond Destination",
        "detail_cn": "表明在入境目的地港口添加食品安全检验服务（FSIS）的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国农业部食品安全检验服务局（Food Safety and Inspection Service, FSIS）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合FSIS的规定。这种情况通常发生在FSIS认为某些食品或相关产品存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "LS": {
        "code": "LS",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除食品安全检验服务在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国农业部食品安全检验服务局（Food Safety and Inspection Service, FSIS）的要求，并获得正式的放行通知。这种情况通常发生在FSIS认为某些食品或相关产品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "LT": {
        "code": "LT",
        "level": "pass",
        "short_desc": "Remove FSIS PGA Enforcement Action -  PGA Documentation Required Hold At In-Bond Destination",
        "detail_cn": "解除食品安全检验服务在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国农业部食品安全检验服务局（Food Safety and Inspection Service, FSIS）的要求，并获得正式的放行通知。这种情况通常发生在FSIS认为某些食品或相关产品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "LU": {
        "code": "LU",
        "level": "warning",
        "short_desc": "FDA  PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加食品药品监督管理局（FDA）的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国食品药品监督管理局（Food and Drug Administration, FDA）的要求，在货物出发前确保所有必要的文件和信息都符合FDA的规定。这种情况通常发生在FDA认为某些食品、药品或相关产品存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "LV": {
        "code": "LV",
        "level": "warning",
        "short_desc": "FDA PGA Enforcement Action -  PGA Documentation Required Hold At In-Bond Destination",
        "detail_cn": "表明在入境目的地港口添加食品药品监督管理局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国食品药品监督管理局（Food and Drug Administration, FDA）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合FDA的规定。这种情况通常发生在FDA认为某些食品、药品或相关产品存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "LX": {
        "code": "LX",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除食品药品监督管理局在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留），意味着需要采取一系列步骤来确保货物符合美国食品药品监督管理局（FDA）的要求，并获得正式的放行通知。这种情况通常发生在FDA认为某些食品、药品或相关产品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "LY": {
        "code": "LY",
        "level": "pass",
        "short_desc": "Remove FDA PGA Enforcement Action -  PGA Documentation Required Hold At In-Bond Destination",
        "detail_cn": "解除食品药品监督管理局在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国食品药品监督管理局（FDA）的要求，并获得正式的放行通知。这种情况通常发生在FDA认为某些食品、药品或相关产品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "LZ": {
        "code": "LZ",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加鱼类和野生动物服务局（Fish and Wildlife Service, FWS）的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国鱼类和野生动物服务局（FWS）的要求，在货物出发前确保所有必要的文件和信息都符合FWS的规定。这种情况通常发生在FWS认为某些涉及野生动植物及其制品的货物存在潜在的法律或保护风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "M0": {
        "code": "M0",
        "level": "warning",
        "short_desc": "FWS PGA Enforcement Action -  PGA Documentation  Hold ",
        "detail_cn": "表明在入境目的地港口添加鱼类和野生动物服务局（Fish and Wildlife Service, FWS）的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国鱼类和野生动物服务局（FWS）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合FWS的规定。这种情况通常发生在FWS认为某些涉及野生动植物及其制品的货物存在潜在的法律或保护风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "M1": {
        "code": "M1",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除鱼类和野生动物服务局在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国鱼类和野生动物服务局（Fish and Wildlife Service, FWS）的要求，并获得正式的放行通知。这种情况通常发生在FWS认为某些涉及野生动植物及其制品的货物存在潜在的法律或保护风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "M2": {
        "code": "M2",
        "level": "pass",
        "short_desc": "Remove FWS PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除鱼类和野生动物服务局在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国鱼类和野生动物服务局（Fish and Wildlife Service, FWS）的要求，并获得正式的放行通知。这种情况通常发生在FWS认为某些涉及野生动植物及其制品的货物存在潜在的法律或保护风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "M3": {
        "code": "M3",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加国家公路交通安全管理局（NHTSA）的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国国家公路交通安全管理局（National Highway Traffic Safety Administration, NHTSA）的要求，在货物出发前确保所有必要的文件和信息都符合NHTSA的规定。这种情况通常发生在NHTSA认为某些涉及机动车及其零部件的产品存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "M4": {
        "code": "M4",
        "level": "warning",
        "short_desc": "NHTSA PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加国家公路交通安全管理局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国国家公路交通安全管理局（National Highway Traffic Safety Administration, NHTSA）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合NHTSA的规定。这种情况通常发生在NHTSA认为某些涉及机动车及其零部件的产品存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "M5": {
        "code": "M5",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除国家公路交通安全管理局在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国国家公路交通安全管理局（National Highway Traffic Safety Administration, NHTSA）的要求，并获得正式的放行通知。这种情况通常发生在NHTSA认为某些涉及机动车及其零部件的产品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "M6": {
        "code": "M6",
        "level": "pass",
        "short_desc": "Remove NHTSA PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除国家公路交通安全管理局在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国国家公路交通安全管理局（National Highway Traffic Safety Administration, NHTSA）的要求，并获得正式的放行通知。这种情况通常发生在NHTSA认为某些涉及机动车及其零部件的产品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "M7": {
        "code": "M7",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加外国资产控制办公室的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国财政部外国资产控制办公室（Office of Foreign Assets Control, OFAC）的要求，在货物出发前确保所有必要的文件和信息都符合OFAC的规定。这种情况通常发生在OFAC认为某些货物涉及受制裁国家、实体或个人，存在潜在的法律风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "M8": {
        "code": "M8",
        "level": "warning",
        "short_desc": "OFAC PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加外国资产控制办公室的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国财政部外国资产控制办公室（Office of Foreign Assets Control, OFAC）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合OFAC的规定。这种情况通常发生在OFAC认为某些货物涉及受制裁国家、实体或个人，存在潜在的法律风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "M9": {
        "code": "M9",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除外国资产控制办公室在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国财政部外国资产控制办公室（Office of Foreign Assets Control, OFAC）的要求，并获得正式的放行通知。这种情况通常发生在OFAC认为某些涉及受制裁国家、实体或个人的货物存在潜在的法律风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MA": {
        "code": "MA",
        "level": "pass",
        "short_desc": "Remove OFAC PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除外国资产控制办公室在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国财政部外国资产控制办公室（Office of Foreign Assets Control, OFAC）的要求，并获得正式的放行通知。这种情况通常发生在OFAC认为某些涉及受制裁国家、实体或个人的货物存在潜在的法律风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MB": {
        "code": "MB",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加酒精和烟草税及贸易局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国酒精和烟草税及贸易局（Alcohol and Tobacco Tax and Trade Bureau, TTB）的要求，在货物出发前确保所有必要的文件和信息都符合TTB的规定。这种情况通常发生在TTB认为某些涉及酒精、烟草及其制品的货物存在潜在的法律或安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MC": {
        "code": "MC",
        "level": "warning",
        "short_desc": "TTB PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加酒精和烟草税及贸易局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国酒精和烟草税及贸易局（Alcohol and Tobacco Tax and Trade Bureau, TTB）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合TTB的规定。这种情况通常发生在TTB认为某些涉及酒精、烟草及其制品的货物存在潜在的法律或安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MD": {
        "code": "MD",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除酒精和烟草税及贸易局在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国酒精和烟草税及贸易局（Alcohol and Tobacco Tax and Trade Bureau, TTB）的要求，并获得正式的放行通知。这种情况通常发生在TTB认为某些涉及酒精、烟草及其制品的货物存在潜在的法律或安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "ME": {
        "code": "ME",
        "level": "pass",
        "short_desc": "Remove TTB PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除酒精和烟草税及贸易局在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国酒精和烟草税及贸易局（Alcohol and Tobacco Tax and Trade Bureau, TTB）的要求，并获得正式的放行通知。这种情况通常发生在TTB认为某些涉及酒精、烟草及其制品的货物存在潜在的法律或安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MF": {
        "code": "MF",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加美国海岸警卫队的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国海岸警卫队（U.S. Coast Guard, USCG）的要求，在货物出发前确保所有必要的文件和信息都符合USCG的规定。这种情况通常发生在USCG认为某些涉及船舶、海上安全、危险品运输等货物存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MG": {
        "code": "MG",
        "level": "warning",
        "short_desc": "USCG PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加美国海岸警卫队的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国海岸警卫队（U.S. Coast Guard, USCG）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合USCG的规定。这种情况通常发生在USCG认为某些涉及船舶、海上安全、危险品运输等货物存在潜在的安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MH": {
        "code": "MH",
        "level": "pass",
        "short_desc": "Remove USCG PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "解除美国海岸警卫队在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国海岸警卫队（U.S. Coast Guard, USCG）的要求，并获得正式的放行通知。这种情况通常发生在USCG认为某些涉及船舶、海上安全、危险品运输等货物存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MI": {
        "code": "MI",
        "level": "info",
        "short_desc": "Submit Batch",
        "detail_cn": "提示用户进行EFT(Electronic Funds Transfer）电子资金转账相关批处理操作。"
    },
    "MJ": {
        "code": "MJ",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加疾病控制与预防中心的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国疾病控制与预防中心（Centers for Disease Control and Prevention, CDC）的要求，在货物出发前确保所有必要的文件和信息都符合CDC的规定。这种情况通常发生在CDC认为某些涉及公共卫生风险的货物存在潜在的安全或健康风险，例如可能携带病原体的生物材料、医疗废物或其他受监管的产品，需要进行额外检查或确认以确保其符合所有入境要求。\n\n详细操作指南"
    },
    "MK": {
        "code": "MK",
        "level": "warning",
        "short_desc": "CDC PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加疾病控制与预防中心的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国疾病控制与预防中心（Centers for Disease Control and Prevention, CDC）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合CDC的规定。这种情况通常发生在CDC认为某些涉及公共卫生风险的货物存在潜在的安全或健康风险，例如可能携带病原体的生物材料、医疗废物或其他受监管的产品，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "ML": {
        "code": "ML",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  PGA Documentation Required Hold ",
        "detail_cn": "解除疾病控制与预防中心在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国疾病控制与预防中心（Centers for Disease Control and Prevention, CDC）的要求，并获得正式的放行通知。这种情况通常发生在CDC认为某些涉及公共卫生风险的货物存在潜在的安全或健康风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MM": {
        "code": "MM",
        "level": "pass",
        "short_desc": "Remove CDC PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除疾病控制与预防中心在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国疾病控制与预防中心（Centers for Disease Control and Prevention, CDC）的要求，并获得正式的放行通知。这种情况通常发生在CDC认为某些涉及公共卫生风险的货物存在潜在的安全或健康风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MN": {
        "code": "MN",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加消费品安全委员会的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国消费品安全委员会（Consumer Product Safety Commission, CPSC）的要求，在货物出发前确保所有必要的文件和信息都符合CPSC的规定。这种情况通常发生在CPSC认为某些涉及消费品存在潜在的安全风险，例如玩具、家具、电器等产品不符合安全标准，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MO": {
        "code": "MO",
        "level": "warning",
        "short_desc": "CPSC PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加消费品安全委员会的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国消费品安全委员会（Consumer Product Safety Commission, CPSC）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合CPSC的规定。这种情况通常发生在CPSC认为某些涉及消费品存在潜在的安全风险，例如玩具、家具、电器等产品不符合安全标准，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MP": {
        "code": "MP",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  PGA Documentation Required Hold ",
        "detail_cn": "解除消费品安全委员会在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国消费品安全委员会（Consumer Product Safety Commission, CPSC）的要求，并获得正式的放行通知。这种情况通常发生在CPSC认为某些涉及消费品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MQ": {
        "code": "MQ",
        "level": "pass",
        "short_desc": "Remove CPSC PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除消费品安全委员会在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国消费品安全委员会（Consumer Product Safety Commission, CPSC）的要求，并获得正式的放行通知。这种情况通常发生在CPSC认为某些涉及消费品存在潜在的安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MR": {
        "code": "MR",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加药物执法局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国药物执法局（Drug Enforcement Administration, DEA）的要求，在货物出发前确保所有必要的文件和信息都符合DEA的规定。这种情况通常发生在DEA认为某些涉及受控物质、药品或化学品的货物存在潜在的法律或安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MS": {
        "code": "MS",
        "level": "warning",
        "short_desc": "DEA PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加药物执法局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国药物执法局（Drug Enforcement Administration, DEA）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合DEA的规定。这种情况通常发生在DEA认为某些涉及受控物质、药品或化学品的货物存在潜在的法律或安全风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MT": {
        "code": "MT",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  PGA Documentation Required Hold ",
        "detail_cn": "解除药物执法局在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国药物执法局（Drug Enforcement Administration, DEA）的要求，并获得正式的放行通知。这种情况通常发生在DEA认为某些涉及受控物质、药品或化学品的货物存在潜在的法律或安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MU": {
        "code": "MU",
        "level": "pass",
        "short_desc": "Remove DEA PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除药物执法局在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国药物执法局（Drug Enforcement Administration, DEA）的要求，并获得正式的放行通知。这种情况通常发生在DEA认为某些涉及受控物质、药品或化学品的货物存在潜在的法律或安全风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MV": {
        "code": "MV",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  PGA Documentation Required Hold",
        "detail_cn": "表明在原发港口添加美国海关与边境保护局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国海关与边境保护局（U.S. Customs and Border Protection, CBP）的要求，在货物出发前确保所有必要的文件和信息都符合CBP的规定。这种情况通常发生在CBP认为某些货物存在潜在的法律、安全或合规风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MX": {
        "code": "MX",
        "level": "warning",
        "short_desc": "CBP PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加美国海关与边境保护局的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要根据美国海关与边境保护局（U.S. Customs and Border Protection, CBP）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合CBP的规定。这种情况通常发生在CBP认为某些货物存在潜在的法律、安全或合规风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "MY": {
        "code": "MY",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  PGA Documentation Required Hold ",
        "detail_cn": "解除美国海关与边境保护局在原发港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国海关与边境保护局（U.S. Customs and Border Protection, CBP）的要求，并获得正式的放行通知。这种情况通常发生在CBP认为某些货物存在潜在的法律、安全或合规风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "MZ": {
        "code": "MZ",
        "level": "pass",
        "short_desc": "Remove CBP PGA Enforcement Action -  PGA Documentation Required Hold at In-bond Destination",
        "detail_cn": "解除美国海关与边境保护局在入境目的地港口的预先指导行动（Pre-Arrival Guidance Action, PGA）文件要求扣留，意味着需要采取一系列步骤来确保货物符合美国海关与边境保护局（U.S. Customs and Border Protection, CBP）的要求，并获得正式的放行通知。这种情况通常发生在CBP认为某些货物存在潜在的法律、安全或合规风险，实施了PGA文件检查并扣留后，现在决定解除这一扣留。"
    },
    "N1": {
        "code": "N1",
        "level": "warning",
        "short_desc": "APHIS Fumigation Hold",
        "detail_cn": "表明在原发港口添加动植物卫生检验局熏蒸要求的预先指导行动扣留，意味着需要根据美国农业部动植物卫生检验局（Animal and Plant Health Inspection Service, APHIS）的要求，在货物出发前确保所有必要的文件和信息都符合APHIS的规定，并且货物已经按照规定进行了熏蒸处理。这种情况通常发生在APHIS认为某些涉及动植物产品或相关物品存在潜在的病虫害风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "N2": {
        "code": "N2",
        "level": "warning",
        "short_desc": "APHIS Fumigation Hold at In-bond Destination",
        "detail_cn": "表明在入境目的地港口添加动植物卫生检验局熏蒸要求的预先指导行动扣留，意味着需要根据美国农业部动植物卫生检验局（Animal and Plant Health Inspection Service, APHIS）的要求，在货物到达入境目的地后，确保所有必要的文件和信息都符合APHIS的规定，并且货物已经按照规定进行了熏蒸处理。这种情况通常发生在APHIS认为某些涉及动植物产品或相关物品存在潜在的病虫害风险，需要进行额外检查或确认以确保其符合所有入境要求。"
    },
    "N3": {
        "code": "N3",
        "level": "pass",
        "short_desc": "Remove APHIS Fumigation Hold",
        "detail_cn": "解除动植物卫生检验局在原发港口的熏蒸要求扣留，意味着需要采取一系列步骤来确保货物符合美国农业部动植物卫生检验局（Animal and Plant Health Inspection Service, APHIS）的要求，并获得正式的放行通知。这种情况通常发生在APHIS认为某些涉及动植物产品或相关物品存在潜在的病虫害风险，实施了熏蒸要求并扣留后，现在决定解除这一扣留。"
    },
    "N4": {
        "code": "N4",
        "level": "pass",
        "short_desc": "Remove APHIS Fumigation Hold at In-bond Destination",
        "detail_cn": "解除动植物卫生检验局在入境目的地港口的熏蒸要求扣留，意味着需要采取一系列步骤来确保货物符合美国农业部动植物卫生检验局（Animal and Plant Health Inspection Service, APHIS）的要求，并获得正式的放行通知。这种情况通常发生在APHIS认为某些涉及动植物产品或相关物品存在潜在的病虫害风险，实施了熏蒸要求并扣留后，现在决定解除这一扣留。"
    },
    "S1": {
        "code": "S1",
        "level": "pass",
        "short_desc": "AMS Bill Matched to Importer Security Filing",
        "detail_cn": "表明CBP已经成功地将进口商的安全申报（Importer Security Filing, ISF）信息与系统中已有的提单信息进行了匹配。这是一个重要的步骤，确保货物在入境前符合所有必要的安全要求。"
    },
    "S2": {
        "code": "S2",
        "level": "warning",
        "short_desc": "AMS Bill not Matched to Import Security Filing ?C Cancel in 30 days",
        "detail_cn": "表明CBP发现提交的进口安全申报（ISF）信息未能与系统中已有的提单信息成功匹配。这通常是一个严重的问题，因为它意味着货物信息不一致或存在错误，可能会导致ISF在30天后自动取消。"
    },
    "S3": {
        "code": "S3",
        "level": "warning",
        "short_desc": "AMS Bill not Matched to Import Security Filing ?C Cancel in 25 days",
        "detail_cn": "表明CBP发现提交的进口安全申报（ISF）信息未能与系统中已有的提单信息成功匹配。这通常是一个严重的问题，因为它意味着货物信息不一致或存在错误，可能会导致ISF在25天后自动取消。"
    },
    "S4": {
        "code": "S4",
        "level": "warning",
        "short_desc": "AMS Bill not Matched to Import Security Filing ?C Cancel in 10 days",
        "detail_cn": "表明CBP发现提交的进口安全申报（ISF）信息未能与系统中已有的提单信息成功匹配。这通常是一个严重的问题，因为它意味着货物信息不一致或存在错误，可能会导致ISF在10天后自动取消。"
    },
    "S5": {
        "code": "S5",
        "level": "warning",
        "short_desc": "AMS Bill not Matched to Import Security Filing ?C Cancelled",
        "detail_cn": "表明CBP的自动舱单系统（Automated Manifest System, AMS）中记录的提单信息与进口安全申报（Importer Security Filing, ISF）中的提单信息不匹配。具体来说，ISF中的提单可能被系统识别为另一种类型的提单，这可能导致一系列问题，包括但不限于清关延误、罚款或货物扣留。"
    },
    "S6": {
        "code": "S6",
        "level": "warning",
        "short_desc": "No Bill Match (Wrong Type)",
        "detail_cn": "表明CBP的AMS系统中记录的提单信息与进口安全申报（ISF）中的提单信息不匹配。具体来说，ISF中的提单可能被系统识别为另一种类型的提单，这可能导致一系列问题，包括但不限于清关延误、罚款或货物扣留。"
    },
    "S7": {
        "code": "S7",
        "level": "info",
        "short_desc": "Duplicate ISF By Another Filer",
        "detail_cn": "表明另一申报人已提交了具有相同提单号和记录进口商的ISF）发生时，这意味着针对同一货物，已经有另一个申报人使用相同的提单号和记录进口商信息向美国海关和边境保护局（U.S. Customs and Border Protection, CBP）提交了进口安全申报（Importer Security Filing, ISF）。"
    },
    "SA": {
        "code": "SA",
        "level": "warning",
        "short_desc": "No Bill Match (Wrong Type)",
        "detail_cn": "在提交ISF后5天，生成于ISF提单在自动舱单系统（AMS）中被记录为不同的提单类型时发生时，意味着美国海关和边境保护局（U.S. Customs and Border Protection, CBP）的AMS系统中记录的提单信息与进口安全申报（Importer Security Filing, ISF）中的提单信息不匹配。具体来说，ISF中的提单可能在提交后的5天内被系统识别为另一种类型的提单，这可能导致一系列问题，包括但不限于清关延误、罚款或货物扣留。"
    },
    "SB": {
        "code": "SB",
        "level": "warning",
        "short_desc": "No Bill Match (Wrong Type)",
        "detail_cn": "在提交ISF后20天，生成于ISF提单在自动舱单系统（AMS）中被记录为不同的提单类型时发生时，这意味着美国海关和边境保护局（U.S. Customs and Border Protection, CBP）的AMS系统中记录的提单信息与进口安全申报（Importer Security Filing, ISF）中的提单信息不匹配。具体来说，在ISF提交后的第20天，CBP发现ISF中的提单被系统识别为另一种类型的提单，这可能导致一系列问题，包括但不限于清关延误、罚款或货物扣留。"
    },
    "SC": {
        "code": "SC",
        "level": "warning",
        "short_desc": "No Bill Match (Wrong Type)",
        "detail_cn": "在提交ISF后30天，生成于ISF提单在自动舱单系统（AMS）中被记录为不同的提单类型时发生时，这意味着美国海关和边境保护局（U.S. Customs and Border Protection, CBP）的AMS系统中记录的提单信息与进口安全申报（Importer Security Filing, ISF）中的提单信息不匹配。具体来说，在ISF提交后的第20天，CBP发现ISF中的提单被系统识别为另一种类型的提单，这可能导致一系列问题，包括但不限于清关延误、罚款或货物扣留。"
    },
    "SR": {
        "code": "SR",
        "level": "info",
        "short_desc": "Shell record",
        "detail_cn": "海关条目处理生成的咨询通知：告知AMS参与者，针对尚未传输的AMS提单已经提交了一个条目：不是放行）发生时，这意味着美国海关和边境保护局（U.S. Customs and Border Protection, CBP）系统中存在一个与自动舱单系统（Automated Manifest System, AMS）中的提单不匹配的情况。具体来说，有一个海关条目（Customs Entry）被提交给CBP，但对应的AMS提单尚未传输到CBP系统中。"
    },
    "TI": {
        "code": "TI",
        "level": "info",
        "short_desc": "Submit PTT",
        "detail_cn": "提示用户进行PTT文件操作"
    },
    "W1": {
        "code": "W1",
        "level": "warning",
        "short_desc": "Error Reply",
        "detail_cn": "表明CBP的自动舱单系统（AMS）在处理提交的文件时发现了问题，并因此拒绝了该申报。这种情况下，通常会伴随一个或多个具体的错误代码或条件，帮助识别问题所在。"
    },
    "W2": {
        "code": "W2",
        "level": "pass",
        "short_desc": "AMS Filing -  Accepted",
        "detail_cn": "表明CB的自动舱单系统（AMS）成功处理了提交的文件，并确认所有信息符合要求。这表明货物运输的相关数据已成功上传到CBP系统中，没有发现任何问题或错误。"
    },
    "WA": {
        "code": "WA",
        "level": "info",
        "short_desc": "Vessel Arrived",
        "detail_cn": "船舶到达目的港，Port of Destination"
    },
    "WV": {
        "code": "WV",
        "level": "info",
        "short_desc": "Vessel Arrived",
        "detail_cn": "船舶到达通知"
    }
}
