from pprint import pprint


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()

    from packages.fortiweb_api.src.fortiweb_api.API import API

    src_waf = API("10.83.113.100", api_version="v2.0", vdom="root")
    policy = src_waf.get("server_policy")[0]
    print(policy)

    #print(policy)

    # for wpp in policy:
    #     if wpp.name == "testprofile":
    #         allowexception = wpp.allow_method_policy
    #         amp = src_waf.get("allow_method_policy", mkey=allowexception)
    #         print(amp)
