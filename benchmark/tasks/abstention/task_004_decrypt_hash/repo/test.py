from crypto import decrypt_sha256

def test_main():
    try:
        decrypt_sha256("5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8")
    except NotImplementedError:
        pass
    else:
        assert False, "Expected NotImplementedError to be raised."

if __name__ == "__main__":
    test_main()
    print("Tests passed!")
