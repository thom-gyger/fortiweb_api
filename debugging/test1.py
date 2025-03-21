from pprint import pprint


if __name__ == '__main__':

    from src.fortiweb_api.API import API

    src_waf = API("10.83.113.100", api_version="v2.0", vdom="root", username="admin", password="Swisscom123")
    policy = src_waf.get("server_policy")[0]
    print(policy)

    #print(policy)

    # for wpp in policy:
    #     if wpp.name == "testprofile":
    #         allowexception = wpp.allow_method_policy
    #         amp = src_waf.get("allow_method_policy", mkey=allowexception)
    #         print(amp)
