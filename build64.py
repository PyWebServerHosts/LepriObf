import base64 as __imp__

def __a__(b: str) -> str:
    __b__ = __imp__.b64encode(b.encode()).decode()
    __c__ = f'''
(lambda __d__: __d__(__d__, [98,97,115,101,54,52], b'{__b__}'))(
    lambda __e__, __f__, __g__: exec(
        __import__(''.join([chr(__h__) for __h__ in __f__]))
        .b64decode(__g__).decode()
    )
)
'''
    return __c__.strip()

if __name__ == "__main__":
    __i__ = input("Enter your Python code to obfuscate:\n>>> ")
    print("\nObfuscated Code:\n")
    print(__a__(__i__))
    
