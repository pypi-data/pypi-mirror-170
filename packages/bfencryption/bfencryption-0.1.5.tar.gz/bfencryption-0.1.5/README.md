# bfencryption

A encryption tool.

### Simple encryption 

Use 
`encrypt(<input>, <key>)`

to use the simple encryption. It returns the encrypted string.

Use
`decrypt(<encrypted input>, <key>)`

to decrypt a simple encrypted string. It returns the decrypted string.

### Safer encryption

This version is safer, but the encrypted string is very long.

You need to specify the security level. The higher the security level,

the longer the encrypted string, and it needs longer to decrypt.

##### Security levels

1 is the same as the simple encryption.

The higher you go, the longer it takes to decrypt it.

2 or 3 is good for the most use cases. 

<br/>

Use
`safe_encrypt(<input>, <key>, <security level>)`

to encrypt a string with a security level. It returns the encrypted string.

Use
`safe_decrypt(<encrypted input>, <key>, <security level>)`

to decrypt an encrypted string with a security level.

The security level has to be the same as the security level used in the encryption.

It returns the decrypted string.