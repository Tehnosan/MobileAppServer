from jwcrypto import jwk, jwt

key = None

def createToken(credentials):
    global key

    key = jwk.JWK.generate(kty='oct', size=256)

    token = jwt.JWT(header={"alg": "HS256"},
                    claims=credentials)
    token.make_signed_token(key)

    etoken = jwt.JWT(header={"alg": "A256KW", "enc": "A256CBC-HS512"},
                     claims=token.serialize())
    etoken.make_encrypted_token(key)

    return etoken.serialize()

def verify(token):
    print(token)
    ET = jwt.JWT(key=key, jwt=token)
    ST = jwt.JWT(key=key, jwt=ET.claims)

    return ST.claims