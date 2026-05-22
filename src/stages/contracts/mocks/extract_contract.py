#pylint: disable=line-too-long
from datetime import datetime
from src.stages.contracts.extract_contract import ExtractContract

EXTRACT_CONTRACT_MOCKS = ExtractContract(
    raw_information_content = [
        {'name': 'Zabaglia, Niccola', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11630'},
        {'name': 'Zaccone, Fabian', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=34202'},
        {'name': 'Zadkine, Ossip', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3475'},
        {'name': 'Zaech, Bernhard', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=25135'},
        {'name': 'Zagar, Jacob', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=2298'},
        {'name': 'Zagroba, Idalia', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=23988'},
        {'name': 'Zaidenberg, A.', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=8232'},
        {'name': 'Zaidenberg, Arthur', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=34154'},
        {'name': 'Zaisinger, Matthäus', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=4910'},
        {'name': 'Zajac, Jack', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3450'},
        {'name': 'Zak, Eugène', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=1986'},
        {'name': 'Zakharov, Gurii Fillipovich', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3451'},
        {'name': 'Zakowortny, Igor', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=20099'},
        {'name': 'Zalce, Alfredo', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3452'},
        {'name': 'Zalopany, Michele', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=34309'},
        {'name': 'Zammiello, Craig', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=27191'},
        {'name': 'Zammitt, Norman', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=5846'},
        {'name': 'Zampieri, Domenico', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3941'},
        {'name': 'Zampieri, called Domenichino, Domenico', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3941'},
        {'name': 'Zanartú, Enrique Antunez', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3453'},
        {'name': 'Zanchi, Antonio', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=35173'},
        {'name': 'Zanetti, Anton Maria', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11133'},
        {'name': 'Zanetti Borzino, Leopoldina', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3455'},
        {'name': 'Zanetti I, Antonio Maria, conte', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3454'},
        {'name': 'Zanguidi, Jacopo', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=961'},
        {'name': 'Zanini, Giuseppe', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597'},
        {'name': 'Zanini-Viola, Giuseppe', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597'},
        {'name': 'Zanotti, Giampietro', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11631'},
        {'name': 'Zao Wou-Ki', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3427'},
        {'name': 'Zas-Zie', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ2.htm'},
        {'name': 'Zie-Zor', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ3.htm'},
        {'name': '<strong>next<br/>page</strong>', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ4.htm'}
        ],
    extraction_date = datetime.now()

)
