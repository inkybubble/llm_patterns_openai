# %%
horoscope_words_dict={
    "aries": 10,
    "taurus": 5,
    "others": 2
}

def tool_runner(tool_name, arguments):
    if tool_name=="get_horoscope_aries":
        print("WELCOME TO HOROSCOPE TOOL (ARIES VERSION) - nothing else called")
        print(f"--- Horoscope: {arguments["aries_horoscope"]}")
        num_words_received=len(arguments["aries_horoscope"].split())
        num_words_expected=horoscope_words_dict["aries"]
        if num_words_received!=num_words_expected:
            return {"result": f"Error: You provided me with the wrong number of words (Expected: {num_words_expected}, Received {num_words_received})"}
        else:
            return {"result": "horoscope tool (aries) was called successfully"}

    if tool_name=="get_horoscope_taurus":
        print("WELCOME TO HOROSCOPE TOOL (TAURUS VERSION) - nothing else called")
        print(f"--- Horoscope: {arguments["taurus_horoscope"]}")
        num_words_received=len(arguments["taurus_horoscope"].split())
        num_words_expected=horoscope_words_dict["taurus"]
        if num_words_received!=num_words_expected:
            return {"result": f"Error: You provided me with the wrong number of words (Expected: {num_words_expected}, Received {num_words_received})"}
        else:
            return {"result": "horoscope tool (taurus) was called successfully"}

    if tool_name=="get_horoscope_other_signs":
        print("WELCOME TO HOROSCOPE TOOL (OTHER SIGNS VERSION) - nothing else called")
        print(f"--- Horoscope: {arguments["name_sign"]}")
        print(f"--- Horoscope: {arguments["sign_horoscope"]}")
        num_words_received=len(arguments["sign_horoscope"].split())
        num_words_expected=horoscope_words_dict["others"]
        if num_words_received!=num_words_expected:
            return {"result": f"Error: You provided me with the wrong number of words (Expected: {num_words_expected}, Received {num_words_received})"}
        else:
            return {"result": "horoscope tool (other signs) was called successfully"}
