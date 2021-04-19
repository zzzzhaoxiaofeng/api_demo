



def test_ddt_login(client,bs64,login):
    client.url = "http://123.56.99.53:9000/event/api/login/"
    client.method = "POST"
    client.body_type = "url-encode"
    data = {"username": login[0], "password": bs64(login[1])}
    client.set_body(data)
    client.send()
    client.check_res_status_code_is_200()
    client.check_res_times_less_than(500)
    client.check_json_value_equal("/error_code", int(login[2]))


def test_ddt_add_event(client,add_event):
    client.url = "http://123.56.99.53:9000/event/api/add_event/"
    client.method = "POST"
    client.body_type = "url-encode"
    client.set_headers({"uid": "2", "key": "3c312df4f5a85216b50ddcc97b4d344031c02106"})

    client.set_body({"title": add_event[0], "limit": int(add_event[1]), "status": int(add_event[2]), "address": add_event[3],
                     "time": add_event[4], "price": int(add_event[5]), "type": add_event[6]})
    client.send()
    client.check_res_status_code_is_200()
    client.check_res_times_less_than(500)
    client.check_json_value_equal("/error_code", int(add_event[7]))