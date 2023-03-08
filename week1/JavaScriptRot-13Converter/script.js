const input = document.getElementById("valor")

function criptografar() {
  let valor = (input.value).toUpperCase()
  

  for (let i = 0; i < valor.length; i++) {
    let ascii = valor.charCodeAt(i)

    if (ascii >= 65 && ascii <= 90) {
      if (ascii >= 77 && ascii <= 90) {
        let rest = 90 - ascii
        ascii = 65 + rest
      } else {
        ascii += 13
      }
    }
    document.write(String.fromCharCode(ascii));
  }
}
