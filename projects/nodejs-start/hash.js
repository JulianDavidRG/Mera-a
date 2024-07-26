/*const crypto = require ("crypto")
const fs =require("fs")


const contenido = "lll"
const hash = crypto.createHash('sha512')
hash.update(contenido);
console.log(`${hash.digest('hex')}`);*/

const crypto = require ("crypto")
const hmac = crypto.createHmac("sha256", "gato");

hmac.update("persa");
console.log(hmac.digest("hex"));





