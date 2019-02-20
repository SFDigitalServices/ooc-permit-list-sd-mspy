"""Tests for permit list"""
import json
from service.resources.permit_list import PermitList

def test_get_list_transform():
    """Test ELT for the Permit List"""
    permit_list_object = PermitList()
    permit_list = permit_list_object.get_list_transform(get_mock_sd_response())
    print(permit_list)
    expected_permit_list = get_expected_permit_list()
    assert expected_permit_list == permit_list

def test_get_legacy_list_transform():
    """Test ELT for the Permit List"""
    permit_list_object = PermitList()
    permit_list = permit_list_object.get_list_transform(get_mock_sd_response())
    legacy_permit_list = permit_list_object.get_legacy_list_transform(permit_list)
    expected_permit_list = get_expected_legacy_permit_list()
    assert expected_permit_list == legacy_permit_list

def get_expected_permit_list():
    """returns expected permit list from mock"""
    return json.loads("""[{"APPLICATION ID": "TESTblah", "DBA NAME": "",
        "ADDRESS": "California", "PARCEL": "no idea", "STATUS": "SUBMITTED", "REFERRING DEPARTMENT": "", "CULTIVATOR OR GROWER (INDOOR)": "SUBMITTED", "DISTRIBUTOR": "SUBMITTED", "RETAILER (MEDICINAL AND ADULT USE)": "SUBMITTED", "MANUFACTURER (NONVOLATILE)": "SUBMITTED"},
        {"APPLICATION ID": "TESTblah2", "DBA NAME": "Bestest Buddy Bud", "ADDRESS": "California", "PARCEL": "no idea", "STATUS": "SUBMITTED", "REFERRING DEPARTMENT": "", 
        "CULTIVATOR OR GROWER (INDOOR)": "SUBMITTED", "DISTRIBUTOR": "SUBMITTED", "MANUFACTURER (NONVOLATILE)": "SUBMITTED", 
        "RETAILER (MEDICINAL AND ADULT USE)": "SUBMITTED", "DELIVERY ONLY RETAILER (MEDICINAL AND ADULT USE)": "SUBMITTED", 
        "MEDICINAL RETAILER (MEDICINAL ONLY)": "SUBMITTED"}]""")

def get_expected_legacy_permit_list():
    """returns legacy expected permit list from mock"""
    return json.loads("""{"TESTblah": {"application_id": "TESTblah", "dba_name": "", 
    "address": "California", "parcel": "no idea", "activities": "retailer (medical and adult use)", "referring_dept": "", "status": "Submitted"}, "Bestest Buddy Bud TESTblah2": {"application_id": "TESTblah2", "dba_name": "Bestest Buddy Bud", 
    "address": "California", "parcel": "no idea", 
    "activities": "retailer (medical and adult use), delivery only retailer (medical and adult use), medicinal cannabis retailer (medical only)", 
    "referring_dept": "", "status": "Submitted"}}""")

def get_mock_sd_response():
    """returns a mock response from screendoor"""
    return json.loads("""[{
        "id": 2187964,
        "sequential_id": 47,
        "project_id": 6360,
        "form_id": 5804,
        "initial_response_id": null,
        "pretty_id": "RydXhPnDZZ34",
        "submitted_at": "2019-01-22T23:48:06.685Z",
        "responses": {
            "uqqrsogr": "TESTblah",
            "rhakmnq6": "Buddy Bud",
            "9hm9uaua": "(123) 456-2234",
            "n5133tdk": null,
            "08l0rlqw": null,
            "q6ou2l7j": null,
            "tgbebquc": {
                "checked": [
                    "I ran a cannabis business that was previously shut down by federal authorities"
                ]
            },
            "xrttaasn": null,
            "u2wf93ww": null,
            "ja0ciw60": null,
            "o05kgf85": null,
            "r0df69hg": null,
            "jjswbsb5": null,
            "g2arrgkt": null,
            "se8hjyk9": null,
            "09d8gnzx": null,
            "hc0uyp4a": null,
            "lo1nx04d": null,
            "gs95ox9m": null,
            "6ma0d8qo": null,
            "fkpuv8fj": "1234534",
            "t00kheyd": "Bestest Buddy Bud",
            "60w4ep9y": null,
            "kbqz4189": {
                "city": "SF",
                "state": "California",
                "street": "420 Bud St",
                "country": "US",
                "zipcode": "94102"
            },
            "kby1cm3l": {
                "state": "California",
                "country": "US"
            },
            "83jot6nz": null,
            "6rk0z78i": null,
            "qvtkw5bs": "10-2",
            "6pxmfzgu": "1",
            "dwbppnt7": "na",
            "7h6geop6": "na",
            "eyhoauj6": null,
            "5okrxcom": null,
            "kvrgbqrl": "no idea",
            "icb0n2ae": null,
            "9u16p44i": {
                "checked": [
                    "No"
                ]
            },
            "2sxifp1f": null,
            "nabxbdpd": null,
            "3rbls8p4": null,
            "d578wxyj": {
                "checked": [
                    "No"
                ]
            },
            "zya7t8oq": null,
            "xq226tmz": null,
            "sa2zydz0": null,
            "9vl1pyuz": null,
            "kha0r0mz": null,
            "g56iehgs": null,
            "52k8jgnm": {
                "checked": [
                    "Own"
                ]
            },
            "996qknlk": null,
            "maxiy31h": null,
            "i7r363tl": null,
            "imkcygd1": null,
            "4w4580ih": null,
            "efckg74t": null,
            "n0prcwm1": null,
            "khuna9w8": null,
            "38p27qkg": "12345",
            "thoqrrt8": null,
            "gzq8jno5": "Retail",
            "vqrr0kms": "1",
            "71tw8jio": "Retail",
            "e9dp28ij": {
                "checked": [
                    "No"
                ]
            },
            "cbqd2wd2": null,
            "e75o089r": null,
            "umt9408s": null,
            "3hlo4we9": {
                "checked": [
                    "Non-profit"
                ]
            },
            "pgu6yasm": null,
            "ncgqqac8": null,
            "zhxaznpk": [
                {
                    "id": "AM32_i2XKrQ9jdtBV4aYu41G6MjZMziF",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "auywweg9": null,
            "3kir7v24": null,
            "dlf5bh94": null,
            "wj1tb99y": [
                {
                    "4e9aclly": null,
                    "4m3npp4g": "World",
                    "5o4d3rwh": null,
                    "5ubp7jpr": {
                        "city": "Lafayette",
                        "state": "California",
                        "street": "1233 Main St",
                        "country": "US",
                        "zipcode": "94549"
                    },
                    "ba6ndrs8": "100",
                    "c4umqxsj": "Me",
                    "e40uzviy": {
                        "cents": ""
                    },
                    "eqen8bu4": "hello@test.test",
                    "ftx0x558": "hello",
                    "g5gtndt1": "Bestest Buddy Bud",
                    "jg7lxezk": "(162) 676-54614",
                    "jo6ntur1": "",
                    "k9gpk4t7": {
                        "day": "22",
                        "year": "1984",
                        "month": "01"
                    },
                    "nd3yl1ji": "USA",
                    "ozmtluwe": {
                        "checked": [
                            "No"
                        ]
                    },
                    "zxwxahiv": null
                }
            ],
            "1thsvudu": true,
            "sv99tz3b": null,
            "e6t7r88q": null,
            "5v6jw6uo": {
                "checked": [
                    "No"
                ]
            },
            "2j58le1f": null,
            "72solxvr": null,
            "709fnemv": null,
            "6au0rjqk": null,
            "oiulv1ys": null,
            "jwzvxies": null,
            "1ob60i64": null,
            "t96cyy3o": null,
            "w6729h70": {
                "checked": [
                    "No"
                ]
            },
            "9e2srivj": null,
            "yse4clw9": null,
            "m63ebprg": null,
            "7uo5xofj": null,
            "2pn70w6i": null,
            "2padwkl7": null,
            "n067esa5": null,
            "u14mm1zj": null,
            "6jkymg77": {
                "checked": [
                    "No"
                ]
            },
            "mnoi8x7y": null,
            "cnnb8od5": null,
            "3i4snj9q": null,
            "w1nznx8c": null,
            "p5gsemmf": {
                "checked": [
                    "Yes"
                ]
            },
            "dd8a5g7g": {
                "checked": [
                    "cultivator or grower (indoor)",
                    "distributor",
                    "retailer (medicinal and adult use)",
                    "manufacturer (nonvolatile)"
                ]
            },
            "ujpoc5lf": null,
            "x9fv4frg": {
                "checked": [
                    "Allow onsite consumption of prepackaged cannabis products"
                ]
            },
            "as35515c": null,
            "mb0z9dh6": null,
            "p9q8hv7s": null,
            "sbbjw5u5": {
                "checked": [
                    "Testing: Type 8"
                ]
            },
            "s0szphc9": null,
            "bfp95f77": null,
            "94sg2b6u": true,
            "3kudziwl": true,
            "al4ch3m4": null,
            "dsfu4k6f": null
        },
        "rating_aggregates": {},
        "average_rating": null,
        "num_ratings": 0,
        "created_at": "2019-01-22T23:15:21.123Z",
        "updated_at": "2019-01-22T23:48:06.693Z",
        "status": "Submitted",
        "labels": [],
        "responder_language": "en",
        "responder": {
            "name": "TEST hello 2",
            "email": "hello@test.test"
        },
        "deleted_at": null,
        "submission_source": {
            "type": "embedded",
            "hostname": "test.test"
        }
    },
    {
        "id": 2188012,
        "sequential_id": 48,
        "project_id": 6360,
        "form_id": 5804,
        "initial_response_id": null,
        "pretty_id": "o8Ce6j902ZkE",
        "submitted_at": "2019-01-23T00:03:21.839Z",
        "responses": {
            "uqqrsogr": "TESTblah2",
            "rhakmnq6": "bestesty buddy bud bud",
            "9hm9uaua": "(162) 676-54614",
            "n5133tdk": null,
            "08l0rlqw": null,
            "q6ou2l7j": null,
            "tgbebquc": {
                "checked": [
                    "I ran a cannabis business that was previously shut down by federal authorities"
                ]
            },
            "xrttaasn": null,
            "u2wf93ww": null,
            "ja0ciw60": null,
            "o05kgf85": null,
            "r0df69hg": null,
            "jjswbsb5": null,
            "g2arrgkt": null,
            "se8hjyk9": null,
            "09d8gnzx": null,
            "hc0uyp4a": null,
            "lo1nx04d": null,
            "gs95ox9m": null,
            "6ma0d8qo": null,
            "fkpuv8fj": "1234567",
            "t00kheyd": "Bestest Buddy Bud Bud",
            "60w4ep9y": "Bestest Buddy Bud",
            "kbqz4189": {
                "city": "San Francisco",
                "state": "California",
                "street": "421 Bestest Bud St",
                "country": "US",
                "zipcode": "94103"
            },
            "kby1cm3l": {
                "state": "California",
                "country": "US"
            },
            "83jot6nz": null,
            "6rk0z78i": null,
            "qvtkw5bs": "8-4",
            "6pxmfzgu": "2",
            "dwbppnt7": "na",
            "7h6geop6": "nananana batman",
            "eyhoauj6": null,
            "5okrxcom": null,
            "kvrgbqrl": "no idea",
            "icb0n2ae": null,
            "9u16p44i": {
                "checked": [
                    "No"
                ]
            },
            "2sxifp1f": null,
            "nabxbdpd": null,
            "3rbls8p4": null,
            "d578wxyj": {
                "checked": [
                    "No"
                ]
            },
            "zya7t8oq": null,
            "xq226tmz": null,
            "sa2zydz0": null,
            "9vl1pyuz": null,
            "kha0r0mz": null,
            "g56iehgs": null,
            "52k8jgnm": {
                "checked": [
                    "Own"
                ]
            },
            "996qknlk": null,
            "maxiy31h": null,
            "i7r363tl": null,
            "imkcygd1": null,
            "4w4580ih": null,
            "efckg74t": null,
            "n0prcwm1": null,
            "khuna9w8": null,
            "38p27qkg": "23425",
            "thoqrrt8": null,
            "gzq8jno5": "Retail",
            "vqrr0kms": "1",
            "71tw8jio": "Retail",
            "e9dp28ij": {
                "checked": [
                    "No"
                ]
            },
            "cbqd2wd2": null,
            "e75o089r": null,
            "umt9408s": null,
            "3hlo4we9": {
                "checked": [
                    "Non-profit"
                ]
            },
            "pgu6yasm": null,
            "ncgqqac8": null,
            "zhxaznpk": [
                {
                    "id": "aytNYzpHV2Heyd-Buon9oilkBzXi3CDu",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "auywweg9": null,
            "3kir7v24": null,
            "dlf5bh94": null,
            "wj1tb99y": [
                {
                    "4e9aclly": null,
                    "4m3npp4g": "World",
                    "5o4d3rwh": null,
                    "5ubp7jpr": {
                        "city": "Lafayette",
                        "state": "California",
                        "street": "524 Main ST",
                        "country": "US",
                        "zipcode": "94549"
                    },
                    "ba6ndrs8": "100",
                    "c4umqxsj": "Me",
                    "e40uzviy": {
                        "cents": ""
                    },
                    "eqen8bu4": "hello@test.test",
                    "ftx0x558": "hello",
                    "g5gtndt1": "Bestest buddy bud",
                    "jg7lxezk": "(162) 676-54614",
                    "jo6ntur1": "",
                    "k9gpk4t7": {
                        "day": "22",
                        "year": "1984",
                        "month": "01"
                    },
                    "nd3yl1ji": "USS",
                    "ozmtluwe": {
                        "checked": [
                            "No"
                        ]
                    },
                    "zxwxahiv": null
                }
            ],
            "1thsvudu": true,
            "sv99tz3b": null,
            "e6t7r88q": null,
            "5v6jw6uo": {
                "checked": [
                    "No"
                ]
            },
            "2j58le1f": null,
            "72solxvr": null,
            "709fnemv": null,
            "6au0rjqk": null,
            "oiulv1ys": null,
            "jwzvxies": null,
            "1ob60i64": null,
            "t96cyy3o": null,
            "w6729h70": {
                "checked": [
                    "No"
                ]
            },
            "9e2srivj": null,
            "yse4clw9": null,
            "m63ebprg": null,
            "7uo5xofj": null,
            "2pn70w6i": null,
            "2padwkl7": null,
            "n067esa5": null,
            "u14mm1zj": null,
            "6jkymg77": {
                "checked": [
                    "No"
                ]
            },
            "mnoi8x7y": null,
            "cnnb8od5": null,
            "3i4snj9q": null,
            "w1nznx8c": null,
            "p5gsemmf": {
                "checked": [
                    "Yes"
                ]
            },
            "dd8a5g7g": {
                "checked": [
                    "cultivator or grower (indoor)",
                    "distributor",
                    "manufacturer (nonvolatile)",
                    "retailer (medicinal and adult use)",
                    "delivery only retailer (medicinal and adult use)", 
                    "medicinal retailer (medicinal only)"
                ]
            },
            "ujpoc5lf": null,
            "x9fv4frg": {
                "checked": [
                    "Allow onsite consumption of prepackaged cannabis products",
                    "Allow onsite consumption of cannabis products that your business will prepare"
                ]
            },
            "as35515c": null,
            "mb0z9dh6": null,
            "p9q8hv7s": null,
            "sbbjw5u5": {
                "checked": [
                    "Cultivation: Indoor (small) - Type 2A"
                ]
            },
            "s0szphc9": null,
            "bfp95f77": null,
            "94sg2b6u": true,
            "3kudziwl": true,
            "al4ch3m4": null,
            "dsfu4k6f": null
        },
        "rating_aggregates": {},
        "average_rating": null,
        "num_ratings": 0,
        "created_at": "2019-01-22T23:55:19.271Z",
        "updated_at": "2019-01-23T00:03:21.850Z",
        "status": "Submitted",
        "labels": [],
        "responder_language": "en",
        "responder": {
            "name": "TESThello3",
            "email": "hello@test.test"
        },
        "deleted_at": null,
        "submission_source": {
            "type": "embedded",
            "hostname": "test.test"
        }
    },
    {
        "id": 2188057,
        "sequential_id": 49,
        "project_id": 6360,
        "form_id": 5885,
        "initial_response_id": 2187964,
        "pretty_id": "apjHhphS4ElX",
        "submitted_at": "2019-01-23T00:35:42.640Z",
        "responses": {
            "mh89zaes": null,
            "1wl7ktd7": null,
            "ypfj1g15": null,
            "7zey7loz": null,
            "hjtp9ti9": null,
            "pazpghjk": null,
            "wapc1bnv": true,
            "vjpw5u74": [
                {
                    "id": "0bUL3Zi7AuhlC7yF5iZJ37tFsvJQ5LKY",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "usirtab3": [
                {
                    "id": "wWYvpO7Hor3b9x9rRZ844HtwGGXaRx3r",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "uat59lz9": [
                {
                    "id": "9YiEYFkAMyprsZlX4h4pIpylZEFOSSFh",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "q0msac4g": null,
            "7dyu9v99": null,
            "7ul7ixuw": [
                {
                    "id": "GcDlLH9mcf7rya3qgUz4Ao1UHdguutBt",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "af90k4af": null,
            "9r2l42ok": null,
            "zoe30bi9": null,
            "71w7fqfq": "NA",
            "vdc1b450": "NANANA batman",
            "xjljlo4v": "(123) 566-3214",
            "bpvt0ja7": "na@na.com",
            "hbezguaf": {
                "city": "na",
                "state": "Arkansas",
                "street": "na",
                "country": "US",
                "zipcode": "12345"
            },
            "defie5pc": null,
            "uf6ddhhc": null,
            "7yuqkcn0": null,
            "695wfpcs": {
                "checked": [
                    "Other (cultivator, distributor, manufacturer, delivery, testing)"
                ]
            },
            "hu8pywx4": null,
            "lmy4b1rf": true,
            "cr7ie3de": null,
            "byz83ebw": null,
            "xpgonjpu": null,
            "ey06tklh": null,
            "c281ul7m": null,
            "givjyong": null,
            "19m46b9d": null,
            "nqvhvev1": {
                "checked": [
                    "I have made no other commitments with my neighbors, other than the ones already mentioned"
                ]
            },
            "hz9l4f9v": null,
            "a39oi13b": null,
            "r67dkn4q": null,
            "m9zviapk": null,
            "umu8kpg3": {
                "checked": [
                    "No, I am not planning to have a compassion program"
                ]
            },
            "dcgia30y": null,
            "prrl2dfr": null,
            "iegpdhvq": null,
            "cigttw9x": null,
            "uf8xsqll": null,
            "462gzu10": null,
            "behgp5am": null,
            "iv2j3nrh": null,
            "s71266py": null,
            "2qlzez8q": null,
            "iczfn8n9": {
                "checked": [
                    "No"
                ]
            },
            "wlllj36h": null,
            "91poqnnz": null,
            "s4cz0j8d": {
                "checked": [
                    "Technical help, such as advice or mentoring"
                ],
                "other_checked": false
            },
            "612dov54": {
                "checked": [
                    "Buy inventory from equity businesses"
                ],
                "other_checked": false
            },
            "38nur70k": {
                "checked": [
                    "Donate services or technical help"
                ],
                "other_checked": false
            },
            "rwrgu6sc": null,
            "tngcf58b": null,
            "cytr5o6t": {
                "checked": [
                    "No"
                ]
            },
            "e9se69i7": null,
            "44r50u3i": null
        },
        "rating_aggregates": {},
        "average_rating": null,
        "num_ratings": 0,
        "created_at": "2019-01-23T00:34:11.526Z",
        "updated_at": "2019-01-23T00:35:42.649Z",
        "status": "Submitted",
        "labels": [],
        "responder_language": "en",
        "responder": {
            "name": "TEST hello 2",
            "email": "hello@test.test"
        },
        "deleted_at": null,
        "submission_source": {
            "type": "embedded",
            "hostname": "hello.test"
        }
    },
    {
        "id": 2188062,
        "sequential_id": 50,
        "project_id": 6360,
        "form_id": 5885,
        "initial_response_id": 2188012,
        "pretty_id": "jluacJ1bthG9",
        "submitted_at": "2019-01-23T00:41:15.149Z",
        "responses": {
            "mh89zaes": null,
            "1wl7ktd7": null,
            "ypfj1g15": null,
            "7zey7loz": null,
            "hjtp9ti9": null,
            "pazpghjk": null,
            "wapc1bnv": true,
            "vjpw5u74": [
                {
                    "id": "iop8CVw29nYImxosZb3PKTfrmYUSQoKQ",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "usirtab3": [
                {
                    "id": "hwaxJRF070FA6ArDNvxMiPLqp6vSWLw6",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "uat59lz9": [
                {
                    "id": "Efx4DdSTIq1nIEXXdOswkmbR-CG9gSG6",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "q0msac4g": null,
            "7dyu9v99": null,
            "7ul7ixuw": [
                {
                    "id": "HVYLn-G1sGIWYWJurHwBe56pPvMeiAE_",
                    "filename": "discovery-matrix.pdf"
                }
            ],
            "af90k4af": null,
            "9r2l42ok": null,
            "zoe30bi9": null,
            "71w7fqfq": "na",
            "vdc1b450": "nananana batman",
            "xjljlo4v": "0000000000",
            "bpvt0ja7": "test@test.com",
            "hbezguaf": {
                "city": "na",
                "state": "Alabama",
                "street": "na",
                "country": "US",
                "zipcode": "12345"
            },
            "defie5pc": null,
            "uf6ddhhc": null,
            "7yuqkcn0": null,
            "695wfpcs": {
                "checked": [
                    "Other (cultivator, distributor, manufacturer, delivery, testing)"
                ]
            },
            "hu8pywx4": null,
            "lmy4b1rf": true,
            "cr7ie3de": null,
            "byz83ebw": null,
            "xpgonjpu": null,
            "ey06tklh": null,
            "c281ul7m": null,
            "givjyong": null,
            "19m46b9d": null,
            "nqvhvev1": {
                "checked": [
                    "I have made no other commitments with my neighbors, other than the ones already mentioned"
                ]
            },
            "hz9l4f9v": null,
            "a39oi13b": null,
            "r67dkn4q": null,
            "m9zviapk": null,
            "umu8kpg3": {
                "checked": [
                    "No, I am not planning to have a compassion program"
                ]
            },
            "dcgia30y": null,
            "prrl2dfr": null,
            "iegpdhvq": null,
            "cigttw9x": null,
            "uf8xsqll": null,
            "462gzu10": null,
            "behgp5am": null,
            "iv2j3nrh": null,
            "s71266py": null,
            "2qlzez8q": null,
            "iczfn8n9": {
                "checked": [
                    "No"
                ]
            },
            "wlllj36h": null,
            "91poqnnz": null,
            "s4cz0j8d": {
                "checked": [
                    "Technical help, such as advice or mentoring"
                ],
                "other_checked": false
            },
            "612dov54": {
                "checked": [
                    "Buy inventory from equity businesses"
                ],
                "other_checked": false
            },
            "38nur70k": {
                "checked": [
                    "Provide paid employee time to help community organizations"
                ],
                "other_checked": false
            },
            "rwrgu6sc": null,
            "tngcf58b": null,
            "cytr5o6t": {
                "checked": [
                    "No"
                ]
            },
            "e9se69i7": null,
            "44r50u3i": null
        },
        "rating_aggregates": {},
        "average_rating": null,
        "num_ratings": 0,
        "created_at": "2019-01-23T00:39:45.517Z",
        "updated_at": "2019-01-23T00:41:15.174Z",
        "status": "Submitted",
        "labels": [],
        "responder_language": "en",
        "responder": {
            "name": "TESThello3",
            "email": "hello@test.test"
        },
        "deleted_at": null,
        "submission_source": {
            "type": "embedded",
            "hostname": "hello.test"
        }
    }]""")
