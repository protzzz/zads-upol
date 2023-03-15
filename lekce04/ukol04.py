root={"id":1,
        "child":{"id":2,
        "child":{"id":5,
                "child":None,
                "sibling":{"id":6,
                            "child":{"id":10,
                                    "child":None,
                                    "sibling":{"id":11,
                                                "child":None,
                                                "sibling":{"id":12,
                                                            "child":None,
                                                            "sibling":None}}},
                            "sibling":{"id":7,
                                        "child":None,
                                        "sibling":None}}},
                "sibling":{"id":3,
                            "child":None,
                            "sibling":{"id":4,
                                        "child":{"id":8,
                                            "child":None,
                                            "sibling":{"id":9,
                                                        "child":None,
                                                        "sibling":None}},
                                        "sibling":None}}},
                "sibling":None}


def pruchod(node):
    if node is not None:
        print(node["id"], end=" ")
        pruchod(node["child"])
        pruchod(node["sibling"])

pruchod(root)